"""Distill journal/trades.jsonl into journal/stats.json - the hard numbers every
session and review reasons from. No vibes: expectancy, win rate, and P&L broken
down by setup grade, probe status, symbol, and holding time. Recomputed by every
weekly review and available to any session.

Run: <venv python> ops\compute_stats.py [--show]
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "journal" / "trades.jsonl"
OUT = ROOT / "journal" / "stats.json"


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def bucket_stats(trades: list[dict]) -> dict:
    pnls = [_f(t.get("realized_pnl")) for t in trades]
    pnls = [p for p in pnls if p is not None]
    if not pnls:
        return {"n": len(trades), "closed": 0}
    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p <= 0]
    return {
        "n": len(trades), "closed": len(pnls),
        "win_rate_pct": round(100 * len(wins) / len(pnls), 1),
        "total_pnl": round(sum(pnls), 2),
        "avg_win": round(sum(wins) / len(wins), 2) if wins else None,
        "avg_loss": round(sum(losses) / len(losses), 2) if losses else None,
        "expectancy_per_trade": round(sum(pnls) / len(pnls), 2),
        "largest_win": round(max(pnls), 2), "largest_loss": round(min(pnls), 2),
    }


def main() -> int:
    trades = []
    if LEDGER.is_file():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            try:
                t = json.loads(line)
            except ValueError:
                continue
            if not t.get("aborted") and not t.get("pending_entry"):
                trades.append(t)
    closed = [t for t in trades if t.get("closed_ts")]

    by_grade = defaultdict(list)
    for t in closed:
        by_grade[str(t.get("setup_grade") or "ungraded")].append(t)
    by_symbol = defaultdict(list)
    for t in closed:
        by_symbol[str(t.get("symbol"))].append(t)

    verdicts = defaultdict(int)
    for t in closed:
        verdicts[str(t.get("review_verdict") or "unscored")] += 1

    stats = {
        "computed_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "overall": bucket_stats(closed),
        "open_positions": sum(1 for t in trades if not t.get("closed_ts")),
        "by_grade": {g: bucket_stats(ts) for g, ts in sorted(by_grade.items())},
        "by_probe": {"probe": bucket_stats([t for t in closed if t.get("probe")]),
                     "full_size": bucket_stats([t for t in closed if not t.get("probe")])},
        "by_symbol": {s: bucket_stats(ts) for s, ts in sorted(by_symbol.items())},
        "review_verdicts": dict(verdicts),
        "by_exit_reason": {r: bucket_stats([t for t in closed if t.get("exit_reason") == r])
                           for r in sorted({str(t.get("exit_reason")) for t in closed})},
    }
    OUT.write_text(json.dumps(stats, indent=1), encoding="utf-8")
    print(f"stats over {len(closed)} closed / {len(trades)} total trades -> {OUT}")
    if "--show" in sys.argv:
        print(json.dumps(stats["overall"], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
