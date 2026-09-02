"""Backtest harness: settle strategy questions on history instead of on money.

Built 2026-09-02 to answer one question the live desk was paying ~$300/day to
learn: does buying a CONFIRMED reclaim beat resting a blind dip-buy limit
(playbook 7a)? Live trading produces ~3 trades/day; this produces thousands in
seconds, at zero cost for being wrong.

HONESTY RULES - a backtest that flatters itself is worse than none:

  * No look-ahead. A setup at bar i may read bars[0..i] only. Entries and exits
    resolve on bars strictly AFTER i. The engine slices the history for the
    strategy so peeking is impossible by construction, not by discipline.
  * Pessimistic intrabar ordering. If a bar's range covers BOTH the stop and the
    target, we assume the STOP filled first. Bars carry no tick sequence, so the
    only safe assumption is the adverse one; otherwise every wide bar becomes a
    fake win.
  * Gaps fill at the open, not the level. A stop at 100 on a bar that opens at 95
    fills at 95. Assuming 100 is the single most common way backtests lie.
  * Costs are charged. Entry and exit each pay half the spread, plus optional
    slippage. Default 10bp round trip, near the measured spread on the liquid
    names this desk trades.
  * Both mechanisms see IDENTICAL setups. The A/B differs only in how entry is
    attempted, so any P&L difference is attributable to the mechanism alone.

Run:
    <venv python> ops\\backtest.py --symbols AAPL,MSFT,... --days 400
    <venv python> ops\\backtest.py --universe scan --days 400      (uses universe_scan.json)
"""

from __future__ import annotations

import json
import statistics
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ops"))
from bt_data import load_bars  # noqa: E402

OUT = ROOT / "journal" / "backtest_results.json"

# --- cost model -------------------------------------------------------------
MECHANISMS = ("anticipatory_limit", "confirmation_trigger", "confirmation_fairstop")
ROUND_TRIP_BP = 10.0      # 10 basis points total (5bp each side) - liquid names
SLIPPAGE_BP = 2.0         # extra adverse fill on market-ish executions


# --- indicators (self-contained; no network, no import side effects) --------
def atr(bars: list[dict], n: int = 14) -> float | None:
    if len(bars) < n + 1:
        return None
    trs = []
    for i in range(len(bars) - n, len(bars)):
        h, l, pc = bars[i]["h"], bars[i]["l"], bars[i - 1]["c"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    return sum(trs) / len(trs) if trs else None


def swing_lows(bars: list[dict], wing: int = 2) -> list[float]:
    """Pivot lows: a bar lower than `wing` bars on each side."""
    out = []
    for i in range(wing, len(bars) - wing):
        lo = bars[i]["l"]
        if all(lo <= bars[j]["l"] for j in range(i - wing, i + wing + 1)):
            out.append(lo)
    return out


def touches_near(bars: list[dict], level: float, tol: float) -> int:
    """How many bars traded within `tol` of the level - i.e. how tested it is."""
    return sum(1 for b in bars if b["l"] <= level + tol and b["l"] >= level - tol)


# --- trade record -----------------------------------------------------------
@dataclass
class BTTrade:
    symbol: str
    mechanism: str
    setup_bar: str
    level: float
    stop: float
    target: float
    entry_ts: str | None = None
    entry_price: float | None = None
    exit_ts: str | None = None
    exit_price: float | None = None
    exit_reason: str | None = None
    pnl_pct: float | None = None
    bars_held: int = 0
    filled: bool = False
    support_touches: int = 0


# --- the strategy under test ------------------------------------------------
def find_setup(hist: list[dict], min_touches: int = 2) -> dict | None:
    """The desk's actual idea: buy a tested support level in a name that is not
    in freefall. Reads ONLY `hist` (bars up to and including the decision bar).
    Returns level/stop/target, or None when no setup exists.
    """
    if len(hist) < 30:
        return None
    a = atr(hist, 14)
    if not a or a <= 0:
        return None
    last = hist[-1]["c"]
    lows = swing_lows(hist[-40:], wing=2)
    if not lows:
        return None
    # nearest pivot low BELOW price - the level we would want to buy
    below = [x for x in lows if x < last]
    if not below:
        return None
    level = max(below)
    if last <= 0 or level <= 0:
        return None
    # skip levels absurdly far away (not actionable) or already breached
    dist = (last - level) / last
    if dist > 0.08 or dist < 0.002:
        return None
    touches = touches_near(hist[-40:], level, tol=0.35 * a)
    if touches < min_touches:
        return None
    return {"level": level, "stop": level - 0.5 * a, "target": level + 1.5 * a,
            "atr": a, "touches": touches}


# --- fill simulation --------------------------------------------------------
def _cost(price: float, bp: float) -> float:
    return price * (bp / 10_000.0)


def simulate(bars: list[dict], i: int, setup: dict, mechanism: str,
             symbol: str, max_hold: int = 10) -> BTTrade:
    """Resolve one setup forward from bar i using bars[i+1:] only.

    anticipatory_limit : a buy-limit resting AT the level. Fills the first time a
                         later bar trades down through it.
    confirmation_trigger: wait for price to trade DOWN to the level, then buy only
                         if a subsequent bar RECLAIMS it (trades back above
                         level + 0.25*ATR). Enters on evidence, not on hope.
    """
    t = BTTrade(symbol=symbol, mechanism=mechanism, setup_bar=bars[i]["t"],
                level=setup["level"], stop=setup["stop"], target=setup["target"],
                support_touches=setup["touches"])
    fwd = bars[i + 1: i + 1 + max_hold + 1]
    if not fwd:
        return t

    trigger = setup["level"] + 0.25 * setup["atr"]
    touched = False
    entry_k: int | None = None

    for k, b in enumerate(fwd):
        if not t.filled:
            if mechanism == "anticipatory_limit":
                if b["l"] <= t.level:
                    # gap-through fills at the open, never at the level
                    px = min(t.level, b["o"])
                    t.filled, t.entry_ts, entry_k = True, b["t"], k
                    t.entry_price = px + _cost(px, ROUND_TRIP_BP / 2)
                else:
                    continue
            else:  # confirmation_trigger / confirmation_fairstop
                if not touched:
                    if b["l"] <= t.level:
                        touched = True
                    continue  # cannot enter on the same bar that first tests it
                if b["h"] >= trigger:
                    px = max(trigger, b["o"])
                    t.filled, t.entry_ts, entry_k = True, b["t"], k
                    t.entry_price = px + _cost(px, ROUND_TRIP_BP / 2 + SLIPPAGE_BP)
                    if mechanism == "confirmation_fairstop":
                        # Geometry-neutral control: entering higher with the SAME
                        # absolute stop silently hands the limit a better R:R, so
                        # this variant re-anchors stop/target to the actual fill.
                        # Now the ONLY difference between arms is entry timing.
                        t.stop = t.entry_price - 0.5 * setup["atr"]
                        t.target = t.entry_price + 1.5 * setup["atr"]
                else:
                    continue
            # entry resolved on this bar; exits are checked from the NEXT bar so
            # we never claim an exit we could not have reached after filling
            continue

        # --- position is open: check exits, stop first (pessimistic) ---
        if b["o"] <= t.stop:                       # gapped below the stop
            t.exit_price, t.exit_reason = b["o"] - _cost(b["o"], ROUND_TRIP_BP / 2), "stop_gap"
        elif b["l"] <= t.stop:
            t.exit_price, t.exit_reason = t.stop - _cost(t.stop, ROUND_TRIP_BP / 2), "stop"
        elif b["o"] >= t.target:                   # gapped above the target
            t.exit_price, t.exit_reason = b["o"] - _cost(b["o"], ROUND_TRIP_BP / 2), "target_gap"
        elif b["h"] >= t.target:
            t.exit_price, t.exit_reason = t.target - _cost(t.target, ROUND_TRIP_BP / 2), "target"
        if t.exit_reason:
            t.exit_ts, t.bars_held = b["t"], k
            break

    if t.filled and not t.exit_reason:
        # Only time-stop if at least one bar existed AFTER the entry bar. A fill on
        # the final available bar is UNRESOLVED - inventing an exit at that same
        # bar's close would manufacture a trade out of the edge of the data.
        if entry_k is not None and entry_k < len(fwd) - 1:
            last = fwd[-1]
            t.exit_price = last["c"] - _cost(last["c"], ROUND_TRIP_BP / 2)
            t.exit_ts, t.exit_reason, t.bars_held = last["t"], "time_stop", len(fwd) - 1
        else:
            t.exit_reason = "unresolved"       # pnl stays None -> excluded from stats
    if t.filled and t.exit_price and t.entry_price:
        t.pnl_pct = 100.0 * (t.exit_price / t.entry_price - 1.0)
    return t


# --- runner -----------------------------------------------------------------
def run(symbols: list[str], days: int, timeframe: str = "1Day",
        max_hold: int = 10) -> dict:
    trades: list[BTTrade] = []
    used, skipped = [], []
    for sym in symbols:
        bars = load_bars(sym, timeframe, days)
        if len(bars) < 60:
            skipped.append(sym)
            continue
        used.append(sym)
        # leave max_hold bars of runway so every setup can actually resolve
        for i in range(40, len(bars) - max_hold - 1):
            setup = find_setup(bars[: i + 1])
            if not setup:
                continue
            for mech in MECHANISMS:
                trades.append(simulate(bars, i, setup, mech, sym, max_hold))
    return summarize(trades, used, skipped, days, timeframe, max_hold)


def _stats(ts: list[BTTrade]) -> dict:
    filled = [t for t in ts if t.filled and t.pnl_pct is not None]
    if not filled:
        return {"setups": len(ts), "filled": 0, "fill_rate_pct": 0.0}
    wins = [t for t in filled if t.pnl_pct > 0]
    losses = [t for t in filled if t.pnl_pct <= 0]
    pnls = [t.pnl_pct for t in filled]
    return {
        "setups": len(ts),
        "filled": len(filled),
        "fill_rate_pct": round(100.0 * len(filled) / len(ts), 1),
        "win_rate_pct": round(100.0 * len(wins) / len(filled), 1),
        "expectancy_pct": round(statistics.fmean(pnls), 4),
        "total_pct": round(sum(pnls), 2),
        "avg_win_pct": round(statistics.fmean([t.pnl_pct for t in wins]), 3) if wins else None,
        "avg_loss_pct": round(statistics.fmean([t.pnl_pct for t in losses]), 3) if losses else None,
        "median_pct": round(statistics.median(pnls), 4),
        "avg_bars_held": round(statistics.fmean([t.bars_held for t in filled]), 2),
        "exit_reasons": {r: sum(1 for t in filled if t.exit_reason == r)
                         for r in sorted({t.exit_reason for t in filled})},
    }


def summarize(trades: list[BTTrade], used: list[str], skipped: list[str],
              days: int, timeframe: str, max_hold: int) -> dict:
    by_mech = {}
    for mech in MECHANISMS:
        by_mech[mech] = _stats([t for t in trades if t.mechanism == mech])
    return {
        "config": {"symbols": used, "skipped": skipped, "days": days,
                   "timeframe": timeframe, "max_hold_bars": max_hold,
                   "round_trip_bp": ROUND_TRIP_BP, "slippage_bp": SLIPPAGE_BP,
                   "intrabar_rule": "stop assumed to fill before target",
                   "gap_rule": "fills at the open when it gaps through a level"},
        "by_mechanism": by_mech,
        "n_setups": len(trades) // len(MECHANISMS),
    }


def main() -> int:
    argv = sys.argv[1:]
    days, tf, hold = 400, "1Day", 10
    symbols: list[str] = []
    for i, a in enumerate(argv):
        if a == "--days":
            days = int(argv[i + 1])
        elif a == "--timeframe":
            tf = argv[i + 1]
        elif a == "--hold":
            hold = int(argv[i + 1])
        elif a == "--symbols":
            symbols = [s.strip().upper() for s in argv[i + 1].split(",") if s.strip()]
        elif a == "--universe" and argv[i + 1] == "scan":
            scan = json.loads((ROOT / "journal" / "universe_scan.json").read_text(encoding="utf-8"))
            symbols = [r["symbol"] for r in (scan.get("shortlist") or [])]
    if not symbols:
        print("usage: backtest.py --symbols A,B,C | --universe scan  [--days N] [--hold N]")
        return 2

    res = run(symbols, days, tf, hold)
    OUT.write_text(json.dumps(res, indent=1), encoding="utf-8")
    c, m = res["config"], res["by_mechanism"]
    print(f"\nBACKTEST  {len(c['symbols'])} symbols, {c['days']}d {c['timeframe']}, "
          f"hold<={c['max_hold_bars']} bars, costs {c['round_trip_bp']}bp round trip")
    print(f"  {res['n_setups']} setups, each tested BOTH ways (identical setups)\n")
    hdr = f"  {'mechanism':22s} {'setups':>7s} {'filled':>7s} {'fill%':>6s} {'win%':>6s} {'expectancy':>11s} {'total%':>9s}"
    print(hdr)
    for name, s in m.items():
        if not s.get("filled"):
            print(f"  {name:22s} {s['setups']:>7d} {0:>7d}       -      -           -         -")
            continue
        print(f"  {name:22s} {s['setups']:>7d} {s['filled']:>7d} {s['fill_rate_pct']:>6.1f} "
              f"{s['win_rate_pct']:>6.1f} {s['expectancy_pct']:>10.4f}% {s['total_pct']:>8.1f}%")
    print(f"\n  -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
