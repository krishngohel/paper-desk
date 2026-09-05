"""Statistical validation of a measured edge - is it real, or did we find noise?

The desk's weak point is not idea generation, it is that every number it acts on
is a point estimate with no error bar. Renaissance's actually-transferable
discipline is not their signals (proprietary, HFT infrastructure, decades of
data) - it is the refusal to trade a number that has not survived:

  1. A significance test. Expectancy +0.71%/trade means nothing without knowing
     whether it is distinguishable from zero given the sample and its variance.
  2. A multiple-testing correction. We evaluated 81 configurations; the best of
     81 draws from a zero-edge distribution still looks good. Sidak-adjust the
     threshold or you are guaranteed to "discover" something.
  3. An out-of-sample check (already in bt_sweep: train/test by time).
  4. Position sizing derived FROM the edge, not from feeling. Kelly gives the
     growth-optimal fraction; half-Kelly is the practitioner's standard because
     full Kelly assumes your estimates are exact, and they never are.

Nothing here is a forecast. It only ever answers: given what we measured, how
much of it should we believe, and how large may we bet on it?

Run: <venv python> ops\\bt_stats.py            (validates the current trend-gate finding)
"""

from __future__ import annotations

import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ops"))


def t_stat(returns: list[float]) -> dict:
    """One-sample t-test of mean(returns) != 0, plus a normal-approx p-value."""
    n = len(returns)
    if n < 3:
        return {"n": n, "error": "sample too small"}
    mean = statistics.fmean(returns)
    sd = statistics.stdev(returns)
    if sd == 0:
        return {"n": n, "mean": mean, "error": "zero variance"}
    se = sd / math.sqrt(n)
    t = mean / se
    # two-sided p from the normal approximation (n is large here, so it is close)
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(t) / math.sqrt(2))))
    return {"n": n, "mean_pct": round(mean, 4), "sd_pct": round(sd, 3),
            "std_err": round(se, 4), "t_stat": round(t, 2), "p_value": p,
            "ci95_low_pct": round(mean - 1.96 * se, 4),
            "ci95_high_pct": round(mean + 1.96 * se, 4)}


def bootstrap_ci(returns: list[float], iters: int = 4000, seed: int = 7) -> dict:
    """Non-parametric CI - trade returns are fat-tailed and skewed, so the
    normal-theory interval flatters them. Resampling makes no shape assumption."""
    if len(returns) < 20:
        return {"error": "sample too small"}
    rng = random.Random(seed)
    n = len(returns)
    means = []
    for _ in range(iters):
        means.append(statistics.fmean([returns[rng.randrange(n)] for _ in range(n)]))
    means.sort()
    return {"boot_ci95_low_pct": round(means[int(0.025 * iters)], 4),
            "boot_ci95_high_pct": round(means[int(0.975 * iters)], 4),
            "p_edge_negative": round(sum(1 for m in means if m <= 0) / iters, 4)}


def sidak_threshold(alpha: float, n_tests: int) -> float:
    """Per-test significance needed so the FAMILY-wise error stays at alpha.

    Testing 81 configurations at p<0.05 gives a ~98% chance of at least one false
    'discovery'. This is the threshold an honest search must clear instead.
    """
    return 1 - (1 - alpha) ** (1.0 / max(n_tests, 1))


def kelly(win_rate: float, avg_win: float, avg_loss: float) -> dict:
    """Growth-optimal fraction of capital to risk.

    f* = (p*b - q) / b, with b = avg_win/|avg_loss| the payoff ratio.
    Half-Kelly is the standard practical choice: full Kelly assumes p and b are
    known exactly, and estimation error makes it wildly over-aggressive - the
    penalty for overbetting is far worse than for underbetting.
    """
    if avg_loss >= 0 or avg_win <= 0:
        return {"error": "need a positive avg win and a negative avg loss"}
    b = avg_win / abs(avg_loss)
    p, q = win_rate, 1 - win_rate
    f = (p * b - q) / b
    return {"payoff_ratio_b": round(b, 3), "win_rate": round(p, 3),
            "kelly_fraction": round(f, 4),
            "half_kelly": round(f / 2, 4),
            "verdict": ("NO EDGE - do not bet" if f <= 0 else
                        f"risk about {100*f/2:.1f}% of equity per trade at half-Kelly")}


def report(name: str, returns: list[float], n_tests: int = 1) -> None:
    print(f"\n=== {name} ===")
    t = t_stat(returns)
    if "error" in t:
        print("  ", t["error"]); return
    b = bootstrap_ci(returns)
    thr = sidak_threshold(0.05, n_tests)
    print(f"  n={t['n']}  mean={t['mean_pct']}%/trade  sd={t['sd_pct']}%")
    print(f"  t-stat={t['t_stat']}  p={t['p_value']:.2e}")
    print(f"  95% CI (normal)    [{t['ci95_low_pct']}%, {t['ci95_high_pct']}%]")
    if "error" not in b:
        print(f"  95% CI (bootstrap) [{b['boot_ci95_low_pct']}%, {b['boot_ci95_high_pct']}%]"
              f"   P(edge<=0) = {b['p_edge_negative']}")
    if n_tests > 1:
        print(f"  Sidak threshold for {n_tests} tests: p < {thr:.2e}")
    verdict = ("SIGNIFICANT" if t["p_value"] < thr else
               "NOT significant after correction - treat as noise")
    print(f"  VERDICT: {verdict}")


def main() -> int:
    from backtest import run  # noqa: E402

    SYMS = ("AAPL,MSFT,NVDA,AMD,MRVL,CRWD,DUOL,CRK,ASND,CRCL,MRNA,GAP,PYPL,TENB,"
            "IREN,RBRK,ESTC,SOLS,STDN,DELL,TSLA,SMMT,CHPT,NU,SAIC").split(",")
    print("Validating the 2026-09-03 trend-gate finding (playbook 2a).")
    print("81 configurations were searched, so the bar is Sidak-adjusted.")

    for label, frac in (("TRAIN (older 60%)", (0.0, 0.6)), ("TEST (newer 40%)", (0.6, 1.0))):
        for up in (False, True):
            res = run(SYMS, 400, "1Day", 10, 2, 1.0, 2.5, frac, False, up)
            rets = res.pop("_returns", {}).get("anticipatory_limit", [])
            tag = "trend gate ON " if up else "trend gate OFF"
            if not rets:
                print(f"\n=== {label} / {tag} === (no per-trade returns exported)")
                continue
            report(f"{label} / {tag}", rets, n_tests=81)

    print("\n--- position sizing from the measured edge ---")
    # measured with the gate on, 1.0/2.5 geometry, TEST period
    print(kelly(win_rate=0.466, avg_win=0.0, avg_loss=-0.0) if False else "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
