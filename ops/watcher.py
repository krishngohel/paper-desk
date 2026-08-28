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
from src.trading import service  # noqa: E402

PROFILE = "alpaca-paper-trade"
POLL_SECONDS = 45
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
        orders = service.get_open_orders(profile_id=PROFILE).get("orders") or []
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
        subprocess.Popen(["cmd.exe", "/c", str(ROOT / "ops" / "run_session.cmd"), "triggered"],
                         cwd=ROOT, creationflags=0x08000000)  # CREATE_NO_WINDOW
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
        subprocess.run([sys.executable, str(ROOT / "ops" / "snapshot.py")],
                       capture_output=True, timeout=240, check=False)
        log("freshness snapshot + deploy done")
    except Exception as exc:  # noqa: BLE001
        log(f"freshness failed: {exc}")


def tick(state: dict) -> None:
    if halt_flag_set():
        log("halted - watching only, no actions")
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
                orders = service.get_open_orders(profile_id=PROFILE).get("orders") or []
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

        prev = _num(last_marks.get(symbol))
        if prev and abs(bid - prev) / prev >= ANOMALY_MOVE:
            spawn_session(f"{symbol} moved {((bid - prev) / prev) * 100:+.1f}% since last check "
                          f"({prev} -> {bid}) - reassess position and levels", state)
        last_marks[symbol] = bid

    save_state(state)
    freshness(state)


def main() -> int:
    once = "--once" in sys.argv
    log(f"watcher start (once={once})")
    state = load_state()
    while True:
        try:
            tick(state)
        except Exception as exc:  # noqa: BLE001 - the watcher must survive anything
            log(f"tick error: {exc}")
        if once:
            return 0
        now = datetime.now()
        if now.hour * 100 + now.minute >= CLOSE_HHMM:
            log("market closed - watcher exiting")
            return 0
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    raise SystemExit(main())
