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

Usage (from VT root, venv active):
    python ..\\ops\\trade_cli.py status | account | positions | orders
    python ..\\ops\\trade_cli.py quote SYM
    python ..\\ops\\trade_cli.py bars SYM [period] [limit]   (periods: 1m 5m 15m 1h 1d)
    python ..\\ops\\trade_cli.py buy SYM QTY  |  sell SYM QTY
    python ..\\ops\\trade_cli.py cancel ORDER_ID [SYM]
    python ..\\ops\\trade_cli.py halt [REASON...]  |  resume
    python ..\\ops\\trade_cli.py audit [N]
"""
import json
import sys

sys.path.insert(0, "agent")

PROFILE = "alpaca-paper-trade"


def run(cmd: str, args: list[str]):
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
        kwargs = {}
        rest = args[2:]
        qty = float(args[1])
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
