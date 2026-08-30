"""Market-hours watcher: enforce numeric stops, catch anomalies, wake sessions.

Runs from market open until 15:05 CT, polling every 45s. It is deliberately
dumb: it only enforces numbers the LLM sessions already committed to in
journal/trades.jsonl (stop / target / time_stop fields) and wakes a full LLM
session when judgment is needed. Every order goes through the same gated
service path as everything else - the watcher has no special powers.

Division of labor:
  - Sell-at-target: normally a resting GTC limit order at the broker (zero
    latency); the watcher only market-sells a target breach as a FALLBACK when
    no resting order exists.
  - Stop-loss: the connector cannot rest stop orders broker-side, so the
    watcher enforces stops: cancel the symbol's resting orders, then market
    sell.
  - Anomaly (holding moves >2% since last check, or a position with no ledger
    stop): spawn one 'triggered' LLM session (rate-limited to 1 per 10 min).
  - Freshness: appends a performance point + redeploys the dashboard every
    ~15 min so the site stays near-live during market hours.

Run: <venv python> ops\\watcher.py [--once]   (--once = single iteration, for tests)
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VT = ROOT / "Vibe-Trading"
LOG = ROOT / "ops" / "logs" / "watcher.log"
STATE = ROOT / "ops" / "logs" / "watcher_state.json"

os.chdir(VT)
sys.path.insert(0, "agent")

from src.live.halt import halt_flag_set  # noqa: E402
from src.live.paths import live_root  # noqa: E402
from src.trading import service  # noqa: E402

# ---------------------------------------------------------------------------
# Tick stream: to-the-second prices without REST polling. A daemon thread runs
# alpaca-py's websocket stream for every symbol we hold, stalk, or have armed
# triggers on; handlers drop the latest trade price into PRICES. The main loop
# then evaluates every POLL_SECONDS using streamed prices, falling back to REST
# quotes (at a gentler cadence) if the stream is down. Orders still go through
# the gated service path - the stream has no execution powers of its own.
# ---------------------------------------------------------------------------
import threading

PRICES: dict[str, tuple[float, float]] = {}   # symbol -> (price, epoch_ts)
_STREAM_SYMBOLS: set[str] = set()
_STREAM_ALIVE = {"ok": False}


def _stream_thread() -> None:
    from src.trading.connectors.alpaca import sdk as _sdk

    cfg = _sdk.load_config()
    while True:
        try:
            from alpaca.data.live import StockDataStream

            stream = StockDataStream(cfg.api_key, cfg.secret_key)

            async def _on_trade(data):  # noqa: ANN001
                try:
                    PRICES[str(data.symbol).upper()] = (float(data.price), time.time())
                except Exception:  # noqa: BLE001
                    pass

            symbols = sorted(_STREAM_SYMBOLS) or ["SPY"]
            stream.subscribe_trades(_on_trade, *symbols)
            _STREAM_ALIVE["ok"] = True
            _STREAM_ALIVE["symbols"] = set(symbols)
            log(f"stream connected: {symbols}")
            stream.run()  # blocks until closed
        except Exception as exc:  # noqa: BLE001
            log(f"stream error: {str(exc)[:150]} - reconnecting in 10s")
        _STREAM_ALIVE["ok"] = False
        time.sleep(10)


def ensure_stream(symbols: set[str]) -> None:
    """(Re)start the stream thread; restart it when the symbol set changes."""
    global _STREAM_SYMBOLS
    if symbols != _STREAM_SYMBOLS:
        _STREAM_SYMBOLS = set(symbols)
        # Simplest robust resubscribe: kill by letting the old thread's run()
        # error out on next reconnect; start a fresh thread now.
        threading.Thread(target=_stream_thread, daemon=True).start()


def live_price(symbol: str, max_age: float = 5.0) -> float | None:
    """Streamed last trade if fresh, else None (caller falls back to REST)."""
    px = PRICES.get(symbol.upper())
    if px and time.time() - px[1] <= max_age:
        return px[0]
    return None


def load_triggers() -> list[dict]:
    out = []
    if TRIGGERS.is_file():
        for line in TRIGGERS.read_text(encoding="utf-8").splitlines():
            try:
                trg = json.loads(line)
            except ValueError:
                continue
            if not trg.get("consumed") and not trg.get("cancelled"):
                out.append(trg)
    return out


def consume_trigger(trigger_id: str, note: str) -> None:
    lines = TRIGGERS.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        try:
            trg = json.loads(line)
        except ValueError:
            continue
        if trg.get("trigger_id") == trigger_id:
            trg["consumed"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            trg["consumed_note"] = note
            lines[i] = json.dumps(trg)
            break
    TRIGGERS.write_text("\n".join(lines) + "\n", encoding="utf-8")

PROFILE = "alpaca-paper-trade"
POLL_SECONDS = 2           # evaluation cadence; prices come from the tick stream
REST_POLL_SECONDS = 15     # fallback cadence when the stream is down

# Death floor: percentage drawdown from the account's HIGH-WATER MARK. If
# equity ever falls DEATH_DD_PCT below the best equity ever seen, the
# experiment ends - flatten everything, cancel everything, trip the kill
# switch (halt.py doctrine explicitly allows an external watchdog to write
# the sentinel). Only the operator can resurrect by removing the HALT file.
# Trailing HWM means profits RAISE the floor: gains are protected, not spent.
# PAPER_DEATH_FLOOR (absolute $) overrides the percentage math - tests only.
DEATH_DD_PCT = float(os.environ.get("PAPER_DEATH_DD_PCT", "0.05"))
DEATH_FLOOR_OVERRIDE = float(os.environ["PAPER_DEATH_FLOOR"]) if os.environ.get("PAPER_DEATH_FLOOR") else None
HWM_SEED = 100_000.0       # starting paper capital; HWM never sits below this
DEATH_CHECK_SECONDS = 15
TRIGGERS = ROOT / "journal" / "triggers.jsonl"
CLOSE_HHMM = 1505          # stop looping at 15:05 CT
SPAWN_COOLDOWN = 600       # one triggered session per 10 min
FRESHNESS_EVERY = 900      # performance point + deploy every 15 min
ANOMALY_MOVE = 0.02        # 2% move on a holding since last check


def log(msg: str) -> None:
    line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
    print(line)
    try:
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_state(state: dict) -> None:
    try:
        STATE.write_text(json.dumps(state), encoding="utf-8")
    except OSError:
        pass


def open_records() -> list[dict]:
    path = ROOT / "journal" / "trades.jsonl"
    out = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("closed_ts") is None and not rec.get("aborted") and not rec.get("pending_entry"):
                out.append(rec)
    return out


def close_record(trade_id: str, exit_price: float | None, order_id: str | None, reason: str) -> None:
    """Rewrite the ledger line for trade_id with the exit half filled in."""
    path = ROOT / "journal" / "trades.jsonl"
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("trade_id") == trade_id:
            rec["closed_ts"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            rec["exit_order_id"] = order_id
            rec["exit_price"] = exit_price
            rec["exit_reason"] = reason
            entry_notional = _num(rec.get("entry_notional"))
            qty = _num(rec.get("entry_qty"))
            if exit_price is not None and entry_notional and qty:
                rec["realized_pnl"] = round(exit_price * qty - entry_notional, 2)
                rec["realized_pnl_pct"] = round((exit_price * qty / entry_notional - 1) * 100, 3)
            rec["closed_by"] = "watcher"
            lines[i] = json.dumps(rec)
            break
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def journal_note(text: str) -> None:
    month = ROOT / "journal" / (datetime.now().strftime("%Y-%m") + ".md")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with month.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {stamp} CT - watcher\n{text}\n")


def good_quote(symbol: str) -> tuple[float, float] | None:
    """(bid, ask) with sanity checks; None on bad/afterhours-garbage quotes."""
    try:
        q = service.get_quote(symbol, profile_id=PROFILE).get("quote") or {}
    except Exception:  # noqa: BLE001
        return None
    bid, ask = _num(q.get("bid")), _num(q.get("ask"))
    if bid and ask and bid > 0 and ask > 0 and abs(ask - bid) / ask < 0.02:
        return bid, ask
    return None


def cancel_symbol_orders(symbol: str) -> None:
    try:
        payload = service.get_open_orders(profile_id=PROFILE) or {}
        orders = payload.get("orders") or payload.get("open_orders") or []
    except Exception:  # noqa: BLE001
        return
    for o in orders:
        if str(o.get("symbol", "")).upper() == symbol.upper():
            oid = o.get("order_id") or o.get("id")
            if oid:
                try:
                    service.cancel_order(str(oid), profile_id=PROFILE, symbol=symbol, session_id="watcher")
                    log(f"cancelled resting order {oid} on {symbol}")
                except Exception as exc:  # noqa: BLE001
                    log(f"cancel failed on {symbol}: {exc}")


def market_sell(symbol: str, qty: float, why: str) -> dict:
    out = service.place_order(symbol=symbol, side="sell", quantity=qty,
                              profile_id=PROFILE, session_id="watcher")
    log(f"SELL {qty} {symbol} ({why}): {json.dumps(out, default=str)[:300]}")
    return out


def sell_succeeded(out: dict) -> bool:
    """Only a broker-accepted order counts. A gate deny/error/timeout does NOT
    close a ledger record - closing on failure was the day-one false-close bug."""
    return isinstance(out, dict) and out.get("status") == "ok"


def exit_blocked(rec: dict, state: dict, out: dict) -> None:
    """A triggered exit could not execute. Back off this trade and summon judgment
    instead of hammering the gate every 45s and spamming the journal."""
    trade_id = rec.get("trade_id", "?")
    fails = state.setdefault("exit_fails", {})
    fails[trade_id] = fails.get(trade_id, 0) + 1
    state.setdefault("exit_backoff", {})[trade_id] = time.time() + 900  # 15 min
    save_state(state)
    reason = str((out or {}).get("reason", "unknown"))[:200]
    log(f"exit BLOCKED for {trade_id} (attempt {fails[trade_id]}): {reason} - backing off 15 min")
    if fails[trade_id] <= 2 or fails[trade_id] % 4 == 0:
        journal_note(f"EXIT BLOCKED on {rec.get('symbol')} ({trade_id}): gate/broker refused the "
                     f"triggered exit - {reason}. Backing off 15 min. Ledger record kept OPEN.")
    spawn_session(f"triggered exit for {trade_id} ({rec.get('symbol')}) is BLOCKED: {reason} - "
                  f"investigate and resolve (position still held)", state)


def _backed_off(rec: dict, state: dict) -> bool:
    until = state.get("exit_backoff", {}).get(rec.get("trade_id", ""), 0)
    return time.time() < until


def spawn_session(reason: str, state: dict) -> None:
    now = time.time()
    if now - state.get("last_spawn", 0) < SPAWN_COOLDOWN:
        return
    state["last_spawn"] = now
    save_state(state)
    try:
        (ROOT / "ops" / "logs" / "trigger_reason.txt").write_text(reason, encoding="utf-8")
        # Fire via the registered task so the child gets a clean Task Scheduler
        # environment (a shell-inherited env can point claude at the wrong config
        # home and silently drop the project's permission allowlist).
        subprocess.run(["schtasks", "/Run", "/TN", "TradingAgent-triggered"],
                       capture_output=True, timeout=30, check=False)
        log(f"spawned triggered session: {reason}")
    except Exception as exc:  # noqa: BLE001
        log(f"spawn failed: {exc}")


def freshness(state: dict) -> None:
    now = time.time()
    if now - state.get("last_fresh", 0) < FRESHNESS_EVERY:
        return
    state["last_fresh"] = now
    save_state(state)
    try:
        # Non-blocking: a 2-min snapshot+deploy must never pause stop enforcement.
        subprocess.Popen([sys.executable, str(ROOT / "ops" / "snapshot.py")],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log("freshness snapshot launched (background)")
    except Exception as exc:  # noqa: BLE001
        log(f"freshness failed: {exc}")


def _trip_death_halt(reason: str) -> None:
    halt_path = live_root() / "HALT"
    halt_path.parent.mkdir(parents=True, exist_ok=True)
    halt_path.write_text(json.dumps({
        "tripped_at": datetime.now().isoformat(),
        "by": "watcher-death-floor",
        "reason": reason,
    }), encoding="utf-8")


def death_check(state: dict) -> bool:
    """Equity floor enforcement. Returns True when the floor was breached and
    the account has been flattened + halted (the watcher then only watches)."""
    now = time.time()
    if now - state.get("last_death_check", 0) < DEATH_CHECK_SECONDS:
        return False
    state["last_death_check"] = now
    try:
        acct = (service.get_account(profile_id=PROFILE) or {}).get("account") or {}
        eq = _num(acct.get("equity"))
    except Exception as exc:  # noqa: BLE001
        log(f"death_check: account unreadable ({exc}) - fail-open on read, floor still enforced next tick")
        return False
    if eq is None:
        return False
    hwm = max(_num(state.get("hwm")) or HWM_SEED, HWM_SEED)
    if eq > hwm:
        hwm = eq
        state["hwm"] = hwm
        save_state(state)
        log(f"new high-water mark ${hwm:,.2f} - death floor rises to ${hwm * (1 - DEATH_DD_PCT):,.2f}")
    state.setdefault("hwm", hwm)
    floor = DEATH_FLOOR_OVERRIDE if DEATH_FLOOR_OVERRIDE is not None else hwm * (1 - DEATH_DD_PCT)
    if eq >= floor:
        return False

    reason = (f"equity ${eq:,.2f} fell below the death floor ${floor:,.2f} "
              f"({DEATH_DD_PCT:.0%} drawdown from high-water mark ${hwm:,.2f})")
    log(f"DEATH FLOOR BREACHED: {reason} - flattening everything and tripping the kill switch")
    # 1) flatten every position (cancel its resting orders first so sells clear the gate)
    try:
        positions = (service.get_positions(profile_id=PROFILE) or {}).get("positions") or []
    except Exception:  # noqa: BLE001
        positions = []
    for p in positions:
        sym = str(p.get("symbol", "")).upper()
        qty = _num(p.get("exact_quantity") or p.get("quantity"))
        if sym and qty:
            cancel_symbol_orders(sym)
            market_sell(sym, qty, f"death floor breached: {reason} - flatten all")
    # 2) cancel every remaining resting order (staged buys included)
    try:
        payload = service.get_open_orders(profile_id=PROFILE) or {}
        for o in (payload.get("orders") or payload.get("open_orders") or []):
            sym = str(o.get("symbol", "")).upper()
            if sym:
                cancel_symbol_orders(sym)
    except Exception:  # noqa: BLE001
        pass
    # 3) trip the kill switch (out-of-band sentinel; blocks ALL further orders)
    _trip_death_halt(reason)
    journal_note(f"DEATH FLOOR: {reason}. All positions flattened, all resting orders cancelled, "
                 f"kill switch tripped by the watcher. The experiment is OVER pending operator review - "
                 f"no session can trade until the operator clears the halt.")
    spawn_session("DEATH FLOOR BREACHED - the kill switch is tripped; write the post-mortem: "
                  "what sequence of decisions spent the cushion, and what would have prevented it", state)
    return True


def tick(state: dict) -> None:
    if halt_flag_set():
        log("halted - watching only, no actions")
        return
    if death_check(state):
        return

    records = open_records()
    try:
        positions = {str(p.get("symbol", "")).upper(): p
                     for p in (service.get_positions(profile_id=PROFILE).get("positions") or [])}
    except Exception as exc:  # noqa: BLE001
        log(f"positions unreadable, skipping tick: {exc}")
        return

    last_marks = state.setdefault("marks", {})
    for rec in records:
        symbol = str(rec.get("symbol", "")).upper()
        pos = positions.get(symbol)
        if not pos:
            continue  # sessions reconcile ledger-vs-book; not the watcher's call
        qty = _num(pos.get("exact_quantity") or pos.get("quantity"))
        quote = good_quote(symbol)
        if not quote or not qty:
            continue
        bid, _ask = quote

        stop = _num(rec.get("stop"))
        target = _num(rec.get("target"))

        if stop is None:
            spawn_session(f"open trade {rec.get('trade_id')} ({symbol}) has no numeric stop in the ledger - set one", state)
        elif bid <= stop and not _backed_off(rec, state):
            cancel_symbol_orders(symbol)
            out = market_sell(symbol, qty, f"stop {stop} breached at bid {bid}")
            if sell_succeeded(out):
                oid = (out.get("order") or {}).get("order_id") if isinstance(out.get("order"), dict) else out.get("order_id")
                close_record(rec["trade_id"], bid, str(oid) if oid else None, "exit-condition-hit")
                state.get("exit_fails", {}).pop(rec["trade_id"], None)
                journal_note(f"STOP enforced on {symbol}: bid {bid} <= stop {stop}. Sold {qty} (order {oid}). "
                             f"Ledger {rec['trade_id']} closed. Verbatim envelope in watcher.log.")
            else:
                exit_blocked(rec, state, out)
            continue

        if target is not None and bid >= target:
            # Normally a resting GTC limit handles this; fallback if none exists.
            try:
                payload = service.get_open_orders(profile_id=PROFILE) or {}
                orders = payload.get("orders") or payload.get("open_orders") or []
            except Exception:  # noqa: BLE001
                orders = []
            has_resting_sell = any(str(o.get("symbol", "")).upper() == symbol
                                   and str(o.get("side", "")).lower() == "sell" for o in orders)
            if not has_resting_sell and not _backed_off(rec, state):
                out = market_sell(symbol, qty, f"target {target} reached at bid {bid}, no resting limit")
                if sell_succeeded(out):
                    oid = (out.get("order") or {}).get("order_id") if isinstance(out.get("order"), dict) else out.get("order_id")
                    close_record(rec["trade_id"], bid, str(oid) if oid else None, "exit-condition-hit")
                    state.get("exit_fails", {}).pop(rec["trade_id"], None)
                    journal_note(f"TARGET fallback on {symbol}: bid {bid} >= target {target} with no resting sell. "
                                 f"Sold {qty} (order {oid}). Ledger {rec['trade_id']} closed.")
                else:
                    exit_blocked(rec, state, out)
                continue

        # OUO-lite bracket sync (NautilusTrader pattern: protective legs must track
        # the actual position). If resting sell qty drifts from held qty (partial
        # fill on an entry rung or a partial target fill), wake a session to
        # resize the brackets rather than auto-amending blind.
        try:
            _op = service.get_open_orders(profile_id=PROFILE) or {}
            resting_sells = sum(
                (_num(o.get("leaves_quantity")) or
                 ((_num(o.get("quantity")) or 0) - (_num(o.get("filled_quantity")) or 0)))
                for o in (_op.get("orders") or _op.get("open_orders") or [])
                if str(o.get("symbol", "")).upper() == symbol
                and str(o.get("side", "")).lower() == "sell"
            )
            if resting_sells > 0 and abs(resting_sells - qty) > 1e-6:
                spawn_session(f"{symbol} bracket drift: {resting_sells:g} sh promised to resting "
                              f"sells vs {qty:g} held - resize brackets to the position", state)
        except Exception:  # noqa: BLE001
            pass

        prev = _num(last_marks.get(symbol))
        if prev and abs(bid - prev) / prev >= ANOMALY_MOVE:
            spawn_session(f"{symbol} moved {((bid - prev) / prev) * 100:+.1f}% since last check "
                          f"({prev} -> {bid}) - reassess position and levels", state)
        last_marks[symbol] = bid

    save_state(state)
    freshness(state)


CACHE: dict = {"records": [], "qty": {}, "ts": 0.0}


def fire_trigger(trg: dict, px: float, state: dict) -> None:
    """Execute an armed trigger within ~a second of its price printing.
    NautilusTrader emulator pattern: held locally, transformed to a market order
    on trigger, and sent through the SAME gated path as every other order."""
    symbol = str(trg.get("symbol", "")).upper()
    qty = _num(trg.get("qty"))
    if str(trg.get("side", "buy")).lower() != "buy" or not qty or qty <= 0:
        consume_trigger(trg["trigger_id"], "invalid: only long buy triggers are supported")
        return
    out = service.place_order(symbol=symbol, side="buy", quantity=qty,
                              profile_id=PROFILE, session_id="watcher-trigger")
    ok = isinstance(out, dict) and out.get("status") == "ok"
    log(f"TRIGGER {trg['trigger_id']} {symbol} @ {px}: {'FILLED-PATH' if ok else 'REFUSED'} "
        f"{json.dumps(out, default=str)[:200]}")
    consume_trigger(trg["trigger_id"], f"fired at {px}: {'ok' if ok else 'refused'}")
    if ok:
        oid = out.get("order_id")
        rec = {"trade_id": f"t-{datetime.now().strftime('%Y-%m-%d')}-trg-{trg['trigger_id'][-6:]}",
               "symbol": symbol, "opened_ts": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
               "entry_order_id": str(oid), "entry_qty": qty, "entry_price": px,
               "entry_notional": round(px * qty, 2),
               "thesis": trg.get("thesis", ""), "lesson_refs": trg.get("lesson_refs", []),
               "exit_condition": trg.get("exit_condition", ""),
               "setup_grade": trg.get("setup_grade"), "probe": trg.get("probe", False),
               "stop": trg.get("stop"), "target": trg.get("target"),
               "time_stop": trg.get("time_stop"), "target_order_id": None,
               "closed_ts": None, "exit_order_id": None, "exit_price": None,
               "exit_reason": None, "realized_pnl": None, "realized_pnl_pct": None,
               "holding_days": None, "voo_pnl_pct_same_window": None,
               "review_verdict": None, "review_notes": None,
               "sizing_rationale": trg.get("sizing_rationale", ""),
               "entered_by": "watcher-trigger"}
        with (ROOT / "journal" / "trades.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec) + "\n")
        journal_note(f"ARMED TRIGGER FIRED: {trg['trigger_id']} bought {qty} {symbol} at ~{px} "
                     f"(trigger: {trg.get('condition')} {trg.get('trigger_price')}). "
                     f"Ledger {rec['trade_id']} opened with stop {trg.get('stop')} / target {trg.get('target')}.")
        spawn_session(f"armed trigger {trg['trigger_id']} fired: bought {qty} {symbol} ~{px} - "
                      f"rest the target bracket and verify the fill", state)
    else:
        journal_note(f"ARMED TRIGGER {trg['trigger_id']} on {symbol} fired at {px} but the order "
                     f"was refused: {json.dumps(out, default=str)[:200]}")


def fast_eval(state: dict) -> None:
    """Sub-second-reaction pass on streamed prices: stops and armed triggers.
    Uses only cached book state (refreshed by the slow tick) + live ticks."""
    if halt_flag_set():
        return
    # Stops on streamed prices.
    for rec in CACHE["records"]:
        symbol = str(rec.get("symbol", "")).upper()
        qty = CACHE["qty"].get(symbol)
        stop = _num(rec.get("stop"))
        px = live_price(symbol)
        if not qty or stop is None or px is None or _backed_off(rec, state):
            continue
        if px <= stop:
            cancel_symbol_orders(symbol)
            out = market_sell(symbol, qty, f"STREAM stop {stop} breached at {px}")
            if sell_succeeded(out):
                oid = out.get("order_id")
                close_record(rec["trade_id"], px, str(oid) if oid else None, "exit-condition-hit")
                journal_note(f"STOP enforced (stream, ~1s) on {symbol}: {px} <= {stop}. "
                             f"Sold {qty} (order {oid}). Ledger {rec['trade_id']} closed.")
                CACHE["records"] = [r for r in CACHE["records"] if r.get("trade_id") != rec["trade_id"]]
            else:
                exit_blocked(rec, state, out)
    # Armed triggers on streamed prices.
    now_iso = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    for trg in load_triggers():
        if str(trg.get("expires", "9999")) < now_iso:
            continue  # slow tick reaps expired ones
        symbol = str(trg.get("symbol", "")).upper()
        px = live_price(symbol)
        tp = _num(trg.get("trigger_price"))
        cond = str(trg.get("condition", ">="))
        if px is None or tp is None:
            continue
        if (cond == ">=" and px >= tp) or (cond == "<=" and px <= tp):
            fire_trigger(trg, px, state)


def main() -> int:
    once = "--once" in sys.argv
    log(f"watcher start (once={once}, stream+fast-eval mode)")
    state = load_state()
    last_slow = 0.0
    while True:
        try:
            now = time.time()
            if now - last_slow >= REST_POLL_SECONDS:
                tick(state)
                # Refresh the fast-eval cache and the stream subscription set.
                records = open_records()
                CACHE["records"] = records
                try:
                    CACHE["qty"] = {
                        str(p.get("symbol", "")).upper():
                            _num(p.get("exact_quantity") or p.get("quantity"))
                        for p in (service.get_positions(profile_id=PROFILE).get("positions") or [])
                    }
                except Exception:  # noqa: BLE001
                    pass
                symbols = {str(r.get("symbol", "")).upper() for r in records}
                symbols |= {str(t.get("symbol", "")).upper() for t in load_triggers()}
                symbols.add("SPY")
                ensure_stream(symbols)
                last_slow = now
            else:
                fast_eval(state)
        except Exception as exc:  # noqa: BLE001 - the watcher must survive anything
            log(f"tick error: {exc}")
        if once:
            return 0
        dt = datetime.now()
        if dt.hour * 100 + dt.minute >= CLOSE_HHMM:
            log("market closed - watcher exiting")
            return 0
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    raise SystemExit(main())
