"""Gated trading CLI - the surface Claude Code drives on the user's subscription.

Every write goes through src.trading.service.place_order, which (fork change,
Task 3b) routes alpaca-paper-trade through the mandate gate: mandate, long-only,
symbol allowlist, kill switch, daily caps, audit ledger. Reads are plain.

Function names below are matched against the real service.py API (confirmed by
reading agent/src/trading/service.py):
    check_connection(profile_id=...)      -- NOT check_status
    get_account(profile_id=...)           -- NOT get_account_snapshot
    get_positions(profile_id=...)
    get_open_orders(profile_id=...)
    get_quote(symbol, profile_id=...)
    place_order(symbol=..., profile_id=..., side=..., quantity=..., session_id=...)
    cancel_order(order_id, profile_id=..., symbol=..., session_id=...)
profile_by_id() resolves an explicit profile_id straight from the built-in
profile registry -- no ~/.vibe-trading/trading-connections.json selection file
is required when profile_id is passed explicitly, which this CLI always does.

Usage (from any directory - the script moves itself into the VT root):
    python ..\\ops\\trade_cli.py status | account | positions | orders
    python ..\\ops\\trade_cli.py quote SYM
    python ..\\ops\\trade_cli.py bars SYM [period] [limit]   (periods: 1m 5m 15m 1h 1d)
    python ..\\ops\\trade_cli.py buy SYM QTY  |  sell SYM QTY
    python ..\\ops\\trade_cli.py cancel ORDER_ID [SYM]
    python ..\\ops\\trade_cli.py halt [REASON...]  |  resume
    python ..\\ops\\trade_cli.py audit [N]
"""
import json
import os
import sys
from pathlib import Path

# the agent package resolves imports relative to the VT root, so run from there
# whatever the caller's cwd (sessions call this by absolute path, no cd)
os.chdir(Path(__file__).resolve().parent.parent / "Vibe-Trading")
sys.path.insert(0, "agent")

PROFILE = "alpaca-paper-trade"
RATE_LIMIT_N = 30          # orders per window
RATE_LIMIT_WINDOW = 60.0   # seconds
PRICE_BAND_PCT = 10.0      # limit price may not be >10% through the quote


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _blocked(code: str, **detail):
    return {"status": "blocked", "code": code, **detail}


def _preflight(service, symbol: str, side: str, qty: float, rest: list[str]):
    """NautilusTrader-inspired pre-trade guards. Returns a denial dict or None."""
    import time
    from pathlib import Path

    # RATE_LIMIT: sliding window persisted across CLI invocations.
    window_file = Path(__file__).parent / "logs" / "order_rate.json"
    now = time.time()
    try:
        stamps = [t for t in json.loads(window_file.read_text()) if now - t < RATE_LIMIT_WINDOW]
    except Exception:  # noqa: BLE001
        stamps = []
    if len(stamps) >= RATE_LIMIT_N:
        return _blocked("RATE_LIMIT", detail=f"{len(stamps)} orders in {RATE_LIMIT_WINDOW:.0f}s "
                                             f"(max {RATE_LIMIT_N}) - runaway-loop brake")
    stamps.append(now)
    try:
        window_file.write_text(json.dumps(stamps))
    except OSError:
        pass

    # PRICE_BAND: fat-finger collar on limit prices vs current quote.
    limit_px = None
    if "--limit" in rest:
        try:
            limit_px = float(rest[rest.index("--limit") + 1])
        except (IndexError, ValueError):
            return _blocked("BAD_REQUEST", detail="--limit needs a numeric price")
    if limit_px is not None:
        q = (service.get_quote(symbol, profile_id=PROFILE) or {}).get("quote") or {}
        bid, ask = _num(q.get("bid")), _num(q.get("ask"))
        # Prefer the natural side; fall back to the other; DENY rather than guess
        # with no reference at all (Nautilus MARKET_PRICE_UNAVAILABLE doctrine -
        # a skipped check placed a $480 AAPL limit on a zero-ask Saturday quote).
        candidates = [ask, bid] if side == "buy" else [bid, ask]
        ref = next((c for c in candidates if c and c > 0), None)
        if ref is None:
            return _blocked("MARKET_PRICE_UNAVAILABLE",
                            detail=f"no usable quote for {symbol} to sanity-check the limit price "
                                   f"against - refusing to place a blind limit order")
        through = ((limit_px - ref) / ref * 100) if side == "buy" else ((ref - limit_px) / ref * 100)
        if through > PRICE_BAND_PCT:
            return _blocked("PRICE_BAND", detail=f"{side} limit {limit_px} is {through:.1f}% through "
                                                 f"quote ref {ref} (band {PRICE_BAND_PCT}%) - fat-finger guard")

    # OVERSELL_GUARD: available = held - leaves of resting sells (never double-sell
    # shares already promised to a resting target).
    if side == "sell":
        held = 0.0
        for row in (service.get_positions(profile_id=PROFILE) or {}).get("positions") or []:
            if str(row.get("symbol", "")).upper() == symbol:
                held += _num(row.get("exact_quantity") or row.get("quantity")) or 0.0
        resting = 0.0
        payload = service.get_open_orders(profile_id=PROFILE) or {}
        for o in payload.get("orders") or payload.get("open_orders") or []:
            if (str(o.get("symbol", "")).upper() == symbol
                    and str(o.get("side", "")).lower() == "sell"):
                leaves = _num(o.get("leaves_quantity"))
                if leaves is None:
                    leaves = (_num(o.get("quantity")) or 0.0) - (_num(o.get("filled_quantity")) or 0.0)
                resting += max(leaves, 0.0)
        available = held - resting
        if qty > available + 1e-9:
            return _blocked("OVERSELL_GUARD",
                            detail=f"sell {qty} {symbol} exceeds available {available:g} "
                                   f"(held {held:g} minus {resting:g} promised to resting sells) - "
                                   f"cancel the resting order first if this exit should replace it")
    return None


def run(cmd: str, args: list[str]):
    if cmd in ("--help", "-h", "help") or "--help" in args or "-h" in args:
        print(__doc__)
        return 0

    from src.live.audit import audit_ledger_path
    from src.live.halt import clear_halt, halt_flag_set, trip_halt
    from src.trading import service

    if cmd == "status":
        out = {"halted": halt_flag_set(), "connector": service.check_connection(profile_id=PROFILE)}
    elif cmd == "account":
        out = service.get_account(profile_id=PROFILE)
    elif cmd == "positions":
        out = service.get_positions(profile_id=PROFILE)
    elif cmd == "orders":
        out = service.get_open_orders(profile_id=PROFILE)
    elif cmd == "quote":
        out = service.get_quote(args[0], profile_id=PROFILE)
    elif cmd == "bars":
        # bars SYM [period] [limit] - e.g. "bars AAPL 5m 78" (a day of 5-min bars)
        # or "bars AAPL 1d 20" (a month of dailies). Read-only research data.
        period = args[1] if len(args) > 1 else "5m"
        limit = int(args[2]) if len(args) > 2 else 78
        out = service.get_history(args[0], profile_id=PROFILE, period=period, limit=limit)
    elif cmd in ("buy", "sell"):
        # buy|sell SYM QTY [--limit PRICE] [--gtc]
        # A GTC limit order rests at the broker and fills the instant price
        # touches the level - the zero-latency way to sell highs / buy dips.
        #
        # Pre-flight guards (patterns adopted from NautilusTrader's RiskEngine):
        #   OVERSELL_GUARD - available = held qty minus leaves of resting sells;
        #     a sell beyond that could double-sell via the resting-target +
        #     watcher-stop pair (their overselling invariant, risk mod.rs).
        #   PRICE_BAND    - fat-finger collar: a limit priced >10% through the
        #     current quote is a typo, not a strategy.
        #   RATE_LIMIT    - sliding-window submit throttle (30/60s): catches
        #     runaway loops before the broker does.
        # Codes are stable leading tokens; the rest of the envelope is diagnostic.
        kwargs = {}
        rest = args[2:]
        qty = float(args[1])
        guard = _preflight(service, args[0].upper(), cmd, qty, rest)
        if guard is not None:
            print(json.dumps(guard, indent=2))
            return 1
        if "--limit" in rest:
            kwargs["order_type"] = "limit"
            kwargs["limit_price"] = float(rest[rest.index("--limit") + 1])
        if "--gtc" in rest:
            # Alpaca rejects GTC on fractional quantities (fractional = day only).
            # A rejected submission also wedges the gate's pending-action recovery,
            # so downgrade loudly instead of letting it fail at the broker.
            if qty != int(qty):
                print(json.dumps({"warning": "fractional qty cannot rest GTC at Alpaca - "
                                             "placed as DAY limit; re-rest it each day or use whole shares"}))
            else:
                kwargs["time_in_force"] = "gtc"
        out = service.place_order(
            symbol=args[0], side=cmd, quantity=float(args[1]),
            profile_id=PROFILE, session_id="claude-code", **kwargs,
        )
    elif cmd == "cancel":
        out = service.cancel_order(
            args[0], profile_id=PROFILE,
            symbol=args[1] if len(args) > 1 else None, session_id="claude-code",
        )
    elif cmd == "halt":
        trip_halt(by="cli", reason=" ".join(args) or "manual halt via trade_cli")
        out = {"halted": True}
    elif cmd == "resume":
        clear_halt()
        out = {"halted": halt_flag_set()}
    elif cmd == "audit":
        n = int(args[0]) if args else 10
        path = audit_ledger_path()
        lines = path.read_text(encoding="utf-8").splitlines()[-n:] if path.is_file() else []
        print("\n".join(lines) or "(audit ledger empty)")
        return 0
    else:
        print(__doc__)
        return 2
    print(json.dumps(out, indent=2, default=str))
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    args = sys.argv[2:]
    try:
        return run(cmd, args)
    except Exception as exc:  # noqa: BLE001 - surface a clean envelope, never a traceback
        print(json.dumps({"status": "error", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
