"""Momentum-with-instant-reversal-exit backtest.

The operator's spec, 2026-09-09: "any downward motion don't buy; if it's going
up buy; as soon as the direction changes at all, sell for profit; do that for as
many positions as viable per day."

That is a trend-following entry with a very tight trailing exit. It is a real
strategy family, so it gets measured rather than argued about. The open question
is whether an exit that tight survives paying the spread on every shake-out.

Entry (all must hold on the decision bar, using only bars up to it):
  * the last UP_BARS closes are strictly rising  ("it's going up")
  * close is above the short EMA and the short EMA is above the long one
    ("not any downward motion")
Exit, tested at three strictnesses of "direction changed":
  * first_down_close : any close below the prior close
  * break_prior_low  : any trade below the prior bar's low  (tightest)
  * two_down_closes  : two consecutive lower closes         (loosest)
Plus a hard stop under the entry bar's low, and flat-by-close for intraday runs.

Same honesty rules as the other harnesses: no look-ahead, exits resolve only on
bars AFTER entry, gaps fill at the open, costs charged both ways.

Run: <venv python> ops\\bt_momentum.py --symbols A,B,C --days 30 --timeframe 5Min
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ops"))
from bt_data import load_bars  # noqa: E402
from bt_stats import sidak_threshold, t_stat  # noqa: E402

ROUND_TRIP_BP = 10.0
SLIPPAGE_BP = 2.0
OUT = ROOT / "journal" / "backtest_momentum.json"


def _cost(px: float, bp: float) -> float:
    return px * (bp / 10_000.0)


def _ema(vals, n):
    if len(vals) < n:
        return None
    k, e = 2 / (n + 1), vals[0]
    for v in vals[1:]:
        e = v * k + e * (1 - k)
    return e


def simulate(bars, i, exit_rule, up_bars, max_hold):
    """Enter at the open of bar i+1 after bar i qualifies; exit on reversal."""
    if i + 2 >= len(bars):
        return None
    e = bars[i + 1]
    entry = e["o"] + _cost(e["o"], ROUND_TRIP_BP / 2 + SLIPPAGE_BP)
    stop = min(bars[i]["l"], e["l"])            # under the launch bars
    prev = e
    downs = 0
    for b in bars[i + 2: i + 2 + max_hold]:
        # hard stop first (pessimistic: assume the adverse touch came first)
        if b["o"] <= stop:
            px = b["o"] - _cost(b["o"], ROUND_TRIP_BP / 2)
            return {"pnl_pct": 100 * (px / entry - 1), "reason": "stop_gap"}
        if b["l"] <= stop:
            px = stop - _cost(stop, ROUND_TRIP_BP / 2)
            return {"pnl_pct": 100 * (px / entry - 1), "reason": "stop"}

        reversed_ = False
        if exit_rule == "break_prior_low":
            reversed_ = b["l"] < prev["l"]
        elif exit_rule == "first_down_close":
            reversed_ = b["c"] < prev["c"]
        else:  # two_down_closes
            downs = downs + 1 if b["c"] < prev["c"] else 0
            reversed_ = downs >= 2
        if reversed_:
            # sell into the reversal: assume the close of the reversing bar
            px = b["c"] - _cost(b["c"], ROUND_TRIP_BP / 2)
            return {"pnl_pct": 100 * (px / entry - 1), "reason": exit_rule}
        prev = b
    last = bars[min(i + 1 + max_hold, len(bars) - 1)]
    px = last["c"] - _cost(last["c"], ROUND_TRIP_BP / 2)
    return {"pnl_pct": 100 * (px / entry - 1), "reason": "time"}


def run(bars, exit_rule, up_bars=3, max_hold=40, ema_s=9, ema_l=21):
    out = []
    closes = [b["c"] for b in bars]
    for i in range(ema_l + 2, len(bars) - 2):
        w = closes[: i + 1]
        es, el = _ema(w[-60:], ema_s), _ema(w[-120:], ema_l)
        if es is None or el is None:
            continue
        # "if it's going up" - strictly rising closes AND stacked EMAs
        if not all(closes[i - k] > closes[i - k - 1] for k in range(up_bars)):
            continue
        if not (closes[i] > es > el):
            continue
        r = simulate(bars, i, exit_rule, up_bars, max_hold)
        if r:
            out.append(r)
    return out


def main() -> int:
    argv = sys.argv[1:]
    days, tf, symbols = 30, "5Min", []
    for i, a in enumerate(argv):
        if a == "--days":
            days = int(argv[i + 1])
        elif a == "--timeframe":
            tf = argv[i + 1]
        elif a == "--symbols":
            symbols = [s.strip().upper() for s in argv[i + 1].split(",") if s.strip()]
    if not symbols:
        print("usage: bt_momentum.py --symbols A,B,C [--days N] [--timeframe 5Min|1Day]")
        return 2

    loaded = {s: load_bars(s, tf, days) for s in symbols}
    loaded = {s: b for s, b in loaded.items() if len(b) > 150}
    print(f'MOMENTUM + INSTANT REVERSAL EXIT - "buy strength, sell the moment it turns"')
    print(f"  {len(loaded)} symbols, {days}d of {tf} bars, costs {ROUND_TRIP_BP}bp round trip\n")
    print(f"  {'exit rule':18s} {'up-bars':>8s} {'n':>6s} {'win%':>6s} {'NET/trade':>11s} "
          f"{'t':>7s} {'avg win':>9s} {'avg loss':>9s}")

    results, configs = [], 0
    for rule in ("break_prior_low", "first_down_close", "two_down_closes"):
        for up_bars in (2, 3):
            configs += 1
            trades = []
            for s, bars in loaded.items():
                trades += run(bars, rule, up_bars)
            rets = [t["pnl_pct"] for t in trades]
            if len(rets) < 30:
                continue
            st = t_stat(rets)
            wins = [r for r in rets if r > 0]
            losses = [r for r in rets if r <= 0]
            aw = sum(wins) / len(wins) if wins else 0
            al = sum(losses) / len(losses) if losses else 0
            results.append({"rule": rule, "up_bars": up_bars, "n": len(rets),
                            "win_pct": round(100 * len(wins) / len(rets), 1),
                            "mean_pct": st["mean_pct"], "t": st["t_stat"],
                            "p": st["p_value"], "avg_win": round(aw, 3),
                            "avg_loss": round(al, 3)})
            print(f"  {rule:18s} {up_bars:>8d} {len(rets):>6d} "
                  f"{100*len(wins)/len(rets):>5.1f}% {st['mean_pct']:>10.4f}% "
                  f"{st['t_stat']:>7.2f} {aw:>8.3f}% {al:>8.3f}%")

    if results:
        best = max(results, key=lambda r: r["mean_pct"])
        thr = sidak_threshold(0.05, configs)
        print(f"\nBEST: {best['rule']}, {best['up_bars']} up-bars")
        print(f"  n={best['n']} win={best['win_pct']}% net={best['mean_pct']}%/trade t={best['t']}")
        print(f"  avg win {best['avg_win']}% vs avg loss {best['avg_loss']}%")
        print(f"  p={best['p']:.2e} vs Sidak bar for {configs} configs p<{thr:.2e}")
        ok = best["p"] < thr and best["mean_pct"] > 0
        print(f"  VERDICT: {'SIGNIFICANT EDGE' if ok else 'no significant edge'}")
        OUT.write_text(json.dumps(results, indent=1), encoding="utf-8")
        print(f"\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
