"""Parameter sweep with an honest train/test split.

The live desk's problem as of 2026-09-03 is geometry, not effort: avg win $132
against avg loss $122 at a 25% win rate is losing math. This searches the
stop/target/level-quality space for a configuration whose edge SURVIVES on data
it was not fitted to.

Anti-overfitting protocol, which is the whole point of the file:
  1. Split each symbol's history in time: first 60% = TRAIN, last 40% = TEST.
  2. Rank every configuration on TRAIN only.
  3. Take the TRAIN winner and report its TEST result.
  4. Report the full TEST table too, so a config that only wins in-sample is
     visible as such rather than quietly adopted.
A parameter set that looks brilliant in TRAIN and mediocre in TEST is noise, and
adopting it would be worse than changing nothing.

Run: <venv python> ops\\bt_sweep.py --symbols A,B,C --days 400
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ops"))
from backtest import MECHANISMS, run  # noqa: E402

OUT = ROOT / "journal" / "backtest_sweep.json"

TOUCHES = (1, 2, 3)
STOPS = (0.5, 1.0, 1.5)
TARGETS = (1.5, 2.5, 4.0)
MIN_FILLS = 60          # ignore configurations too rare to trust


def score(symbols, days, hold, frac):
    rows = []
    for mt in TOUCHES:
        for st in STOPS:
            for tg in TARGETS:
                if tg <= st:
                    continue          # never accept worse than 1:1 to target
                res = run(symbols, days, "1Day", hold, mt, st, tg, frac)
                for mech, s in res["by_mechanism"].items():
                    if s.get("filled", 0) < MIN_FILLS:
                        continue
                    rows.append({
                        "touches": mt, "stop_atr": st, "target_atr": tg,
                        "mechanism": mech, "filled": s["filled"],
                        "win_pct": s["win_rate_pct"],
                        "expectancy_pct": s["expectancy_pct"],
                        "avg_win": s["avg_win_pct"], "avg_loss": s["avg_loss_pct"],
                        "total_pct": s["total_pct"],
                    })
    return rows


def main() -> int:
    argv = sys.argv[1:]
    days, hold, symbols = 400, 10, []
    for i, a in enumerate(argv):
        if a == "--days":
            days = int(argv[i + 1])
        elif a == "--hold":
            hold = int(argv[i + 1])
        elif a == "--symbols":
            symbols = [s.strip().upper() for s in argv[i + 1].split(",") if s.strip()]
    if not symbols:
        print("usage: bt_sweep.py --symbols A,B,C [--days N] [--hold N]")
        return 2

    print(f"sweeping {len(TOUCHES)*len(STOPS)*len(TARGETS)} configs x {len(MECHANISMS)} "
          f"mechanisms over {len(symbols)} symbols...\n")
    train = score(symbols, days, hold, (0.0, 0.6))
    test = score(symbols, days, hold, (0.6, 1.0))

    train.sort(key=lambda r: r["expectancy_pct"], reverse=True)
    tkey = {(r["touches"], r["stop_atr"], r["target_atr"], r["mechanism"]): r for r in test}

    print("TOP 8 BY TRAIN EXPECTANCY  (train = oldest 60% of bars)")
    hdr = f"  {'tch':>3s} {'stop':>5s} {'targ':>5s} {'mechanism':22s} {'n':>5s} {'win%':>6s} {'TRAIN exp':>10s} {'TEST exp':>10s} {'held up?'}"
    print(hdr)
    for r in train[:8]:
        k = (r["touches"], r["stop_atr"], r["target_atr"], r["mechanism"])
        te = tkey.get(k)
        te_s = f"{te['expectancy_pct']:>9.4f}%" if te else "     n/a  "
        ok = "" if not te else ("YES" if te["expectancy_pct"] > 0 else "no - noise")
        print(f"  {r['touches']:>3d} {r['stop_atr']:>5.2f} {r['target_atr']:>5.2f} "
              f"{r['mechanism']:22s} {r['filled']:>5d} {r['win_pct']:>6.1f} "
              f"{r['expectancy_pct']:>9.4f}% {te_s} {ok}")

    best = train[0]
    bk = (best["touches"], best["stop_atr"], best["target_atr"], best["mechanism"])
    bt = tkey.get(bk)
    print(f"\nTRAIN winner: touches>={best['touches']}, stop {best['stop_atr']}xATR, "
          f"target {best['target_atr']}xATR, {best['mechanism']}")
    if bt:
        print(f"  TRAIN: n={best['filled']} win={best['win_pct']}% exp={best['expectancy_pct']}% "
              f"avgW={best['avg_win']}% avgL={best['avg_loss']}%")
        print(f"  TEST : n={bt['filled']} win={bt['win_pct']}% exp={bt['expectancy_pct']}% "
              f"avgW={bt['avg_win']}% avgL={bt['avg_loss']}%")
        print("  VERDICT:", "edge survived out of sample" if bt["expectancy_pct"] > 0
              else "did NOT survive - treat as overfit, do not adopt")
    else:
        print("  no out-of-sample sample - cannot validate")

    test.sort(key=lambda r: r["expectancy_pct"], reverse=True)
    print("\nTOP 5 BY TEST EXPECTANCY (for comparison - not selected on)")
    for r in test[:5]:
        print(f"  {r['touches']:>3d} {r['stop_atr']:>5.2f} {r['target_atr']:>5.2f} "
              f"{r['mechanism']:22s} n={r['filled']:>4d} win={r['win_pct']:>5.1f}% "
              f"exp={r['expectancy_pct']:>8.4f}% avgW={r['avg_win']}% avgL={r['avg_loss']}%")

    OUT.write_text(json.dumps({"train": train, "test": test}, indent=1), encoding="utf-8")
    print(f"\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
