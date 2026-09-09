"""Opening-range breakout backtest - the canonical day-trading setup.

The support-bounce strategy in backtest.py is mean reversion, and it has no
measurable intraday edge (best config +0.016%/trade, t=0.82, p=0.41 - zero).
That condemns THAT strategy intraday, not day trading itself. ORB is the
opposite archetype and the classic day-trade: mark the first N minutes of the
session, buy the break above that high, stop under the range, be flat by close.

Same honesty rules as backtest.py: no look-ahead (the range is fixed before any
entry is allowed), pessimistic intrabar ordering (stop assumed first when a bar
spans both), gaps fill at the open, and costs are charged both ways.

Run: <venv python> ops\\bt_orb.py --symbols A,B,C --days 30
"""

from __future__ import annotations

import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ops"))
from bt_data import load_bars  # noqa: E402
from bt_stats import sidak_threshold, t_stat  # noqa: E402

ROUND_TRIP_BP = 10.0
SLIPPAGE_BP = 2.0
OUT = ROOT / "journal" / "backtest_orb.json"


def _cost(px: float, bp: float) -> float:
    return px * (bp / 10_000.0)


def by_session(bars: list[dict]) -> dict[str, list[dict]]:
    days: dict[str, list[dict]] = defaultdict(list)
    for b in bars:
        days[b["t"][:10]].append(b)
    return days


def run_symbol(bars: list[dict], or_bars: int, target_r: float,
               stop_mode: str, require_trend: bool) -> list[dict]:
    """One trade per session at most: the first break of the opening-range high.

    stop_mode 'range' puts the stop at the opening-range LOW (classic ORB, wide);
    'half' puts it at the range midpoint (tighter, more stop-outs, better R).
    """
    out = []
    # trend context uses only bars BEFORE the session being traded
    closes_by_day = {d: s[-1]["c"] for d, s in by_session(bars).items()}
    days = sorted(by_session(bars).items())
    prior_closes: list[float] = []

    for di, (day, session) in enumerate(days):
        if len(session) < or_bars + 6:
            prior_closes.append(closes_by_day[day])
            continue
        if require_trend and len(prior_closes) >= 21:
            k = 2 / 22
            e = prior_closes[0]
            for v in prior_closes[1:]:
                e = v * k + e * (1 - k)
            if session[0]["o"] <= e:        # opened below its own 21-day EMA
                prior_closes.append(closes_by_day[day])
                continue

        opening = session[:or_bars]
        or_high = max(b["h"] for b in opening)
        or_low = min(b["l"] for b in opening)
        rng = or_high - or_low
        if rng <= 0:
            prior_closes.append(closes_by_day[day])
            continue
        stop = or_low if stop_mode == "range" else or_high - rng / 2
        risk = or_high - stop
        if risk <= 0:
            prior_closes.append(closes_by_day[day])
            continue
        target = or_high + target_r * risk

        entry = exit_px = exit_reason = None
        for b in session[or_bars:]:
            if entry is None:
                if b["h"] >= or_high:                       # break above the range
                    px = max(or_high, b["o"])               # gap-up fills at the open
                    entry = px + _cost(px, ROUND_TRIP_BP / 2 + SLIPPAGE_BP)
                continue
            if b["o"] <= stop:
                exit_px, exit_reason = b["o"] - _cost(b["o"], ROUND_TRIP_BP / 2), "stop_gap"
            elif b["l"] <= stop:                            # stop checked first
                exit_px, exit_reason = stop - _cost(stop, ROUND_TRIP_BP / 2), "stop"
            elif b["o"] >= target:
                exit_px, exit_reason = b["o"] - _cost(b["o"], ROUND_TRIP_BP / 2), "target_gap"
            elif b["h"] >= target:
                exit_px, exit_reason = target - _cost(target, ROUND_TRIP_BP / 2), "target"
            if exit_reason:
                break
        if entry is not None and exit_reason is None:        # day trade: flat at the close
            c = session[-1]["c"]
            exit_px, exit_reason = c - _cost(c, ROUND_TRIP_BP / 2), "close"
        if entry is not None and exit_px is not None:
            out.append({"day": day, "pnl_pct": 100 * (exit_px / entry - 1),
                        "exit_reason": exit_reason})
        prior_closes.append(closes_by_day[day])
    return out


def main() -> int:
    argv = sys.argv[1:]
    days, symbols = 30, []
    for i, a in enumerate(argv):
        if a == "--days":
            days = int(argv[i + 1])
        elif a == "--symbols":
            symbols = [s.strip().upper() for s in argv[i + 1].split(",") if s.strip()]
    if not symbols:
        print("usage: bt_orb.py --symbols A,B,C [--days N]")
        return 2

    loaded = {s: load_bars(s, "5Min", days) for s in symbols}
    loaded = {s: b for s, b in loaded.items() if len(b) > 200}
    print(f"OPENING-RANGE BREAKOUT - {len(loaded)} symbols, {days}d of 5-min bars, "
          f"costs {ROUND_TRIP_BP}bp round trip\n")
    print(f"  {'ORmin':>6s} {'stop':>6s} {'targ':>5s} {'trend':>6s} {'n':>5s} {'win%':>6s} "
          f"{'NET/trade':>11s} {'t':>6s} {'total%':>8s}")

    results, configs = [], 0
    for or_bars in (3, 6):                      # 15-min and 30-min opening range
        for stop_mode in ("range", "half"):
            for target_r in (1.0, 2.0):
                for trend in (False, True):
                    configs += 1
                    trades = []
                    for s, bars in loaded.items():
                        trades += run_symbol(bars, or_bars, target_r, stop_mode, trend)
                    rets = [t["pnl_pct"] for t in trades]
                    if len(rets) < 30:
                        continue
                    st = t_stat(rets)
                    wins = sum(1 for r in rets if r > 0)
                    results.append({"or_min": or_bars * 5, "stop": stop_mode,
                                    "target_r": target_r, "trend": trend,
                                    "n": len(rets), "win_pct": round(100 * wins / len(rets), 1),
                                    "mean_pct": st["mean_pct"], "t": st["t_stat"],
                                    "p": st["p_value"], "total_pct": round(sum(rets), 1)})
                    print(f"  {or_bars*5:>6d} {stop_mode:>6s} {target_r:>5.1f} "
                          f"{('ON' if trend else 'off'):>6s} {len(rets):>5d} "
                          f"{100*wins/len(rets):>5.1f}% {st['mean_pct']:>10.4f}% "
                          f"{st['t_stat']:>6.2f} {sum(rets):>7.1f}%")

    if results:
        best = max(results, key=lambda r: r["mean_pct"])
        thr = sidak_threshold(0.05, configs)
        print(f"\nBEST: {best['or_min']}-min range, stop={best['stop']}, "
              f"target={best['target_r']}R, trend gate {'ON' if best['trend'] else 'off'}")
        print(f"  n={best['n']}  win={best['win_pct']}%  net={best['mean_pct']}%/trade  t={best['t']}")
        print(f"  p={best['p']:.2e} vs Sidak bar for {configs} configs p<{thr:.2e}")
        print(f"  VERDICT: {'SIGNIFICANT EDGE' if best['p'] < thr and best['mean_pct'] > 0 else 'no significant edge'}")
        OUT.write_text(json.dumps(results, indent=1), encoding="utf-8")
        print(f"\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
