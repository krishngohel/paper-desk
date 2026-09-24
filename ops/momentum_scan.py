"""Find today's playbook §6a momentum-continuation candidates.

§6a is the only archetype on this desk with a measured, significance-tested edge
(+1.96%/trade, p=0.0043, n=287). This turns it into a list a session can act on
instead of a rule it has to hand-check symbol by symbol.

Screens for exactly the tested entry:
  * the last 3 daily closes STRICTLY rising
  * close > EMA9 > EMA21
  * no liquidity floor (operator rule 2026-09-24: nothing is screened out) -
    dollar volume is reported; the per-symbol spread test (§7b, ta.py) judges it

Output: journal/momentum_candidates.json, and a table on stdout. Research only -
places no orders, and never decides size.

Run: <venv python> ops\\momentum_scan.py [--universe scan | --symbols A,B,C]
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ops"))
from bt_data import load_bars  # noqa: E402

OUT = ROOT / "journal" / "momentum_candidates.json"


def ema(vals: list[float], n: int) -> float | None:
    if len(vals) < n:
        return None
    k, e = 2 / (n + 1), vals[0]
    for v in vals[1:]:
        e = v * k + e * (1 - k)
    return e


def evaluate(symbol: str) -> dict | None:
    bars = load_bars(symbol, "1Day", 120)
    if len(bars) < 30:
        return None
    closes = [b["c"] for b in bars]
    e9, e21 = ema(closes[-40:], 9), ema(closes[-60:], 21)
    if e9 is None or e21 is None:
        return None
    last = closes[-1]
    rising = all(closes[-1 - k] > closes[-2 - k] for k in range(3))
    stacked = last > e9 > e21
    dv = bars[-1]["c"] * bars[-1]["v"] / 1e6
    launch_low = min(bars[-1]["l"], bars[-2]["l"])
    return {
        "symbol": symbol,
        "close": round(last, 2),
        "ema9": round(e9, 2),
        "ema21": round(e21, 2),
        "three_rising_closes": rising,
        "stacked_emas": stacked,
        "qualifies": bool(rising and stacked),
        "dollar_volume_m": round(dv, 1),
        "pct_up_3d": round(100 * (last / closes[-4] - 1), 2) if len(closes) > 4 else None,
        "suggested_stop": round(launch_low, 2),
        "risk_per_share": round(last - launch_low, 2),
        "risk_pct": round(100 * (last - launch_low) / last, 2) if last else None,
    }


def main() -> int:
    argv = sys.argv[1:]
    symbols: list[str] = []
    if "--symbols" in argv:
        symbols = [s.strip().upper() for s in argv[argv.index("--symbols") + 1].split(",") if s.strip()]
    else:
        try:
            scan = json.loads((ROOT / "journal" / "universe_scan.json").read_text(encoding="utf-8"))
            symbols = [r["symbol"] for r in (scan.get("shortlist") or [])]
            symbols += [r["symbol"] for r in (scan.get("explore", {}).get("all") or [])]
        except Exception:  # noqa: BLE001
            pass
        symbols = list(dict.fromkeys(symbols))
    if not symbols:
        print("no symbols (need journal/universe_scan.json or --symbols)")
        return 2

    rows = [r for r in (evaluate(s) for s in symbols) if r]
    hits = [r for r in rows if r["qualifies"]]
    hits.sort(key=lambda r: r["pct_up_3d"] or 0, reverse=True)

    print(f"MOMENTUM CANDIDATES (playbook §6a) - screened {len(rows)} of {len(symbols)} symbols")
    print(f"  entry: 3 rising closes + close>EMA9>EMA21 | exit: TWO consecutive lower closes\n")
    if not hits:
        print("  none qualify today - that is a normal outcome, roughly 1 trade / 2 days / 14 names")
    else:
        print(f"  {'sym':7s} {'close':>9s} {'EMA9':>9s} {'EMA21':>9s} {'3d%':>7s} "
              f"{'stop':>9s} {'risk%':>7s} {'$vol M':>8s}")
        for r in hits:
            print(f"  {r['symbol']:7s} {r['close']:>9.2f} {r['ema9']:>9.2f} {r['ema21']:>9.2f} "
                  f"{r['pct_up_3d']:>6.2f}% {r['suggested_stop']:>9.2f} {r['risk_pct']:>6.2f}% "
                  f"{r['dollar_volume_m']:>8.1f}")

    OUT.write_text(json.dumps({"ts": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                               "screened": len(rows), "candidates": hits,
                               "all": rows}, indent=1), encoding="utf-8")
    print(f"\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
