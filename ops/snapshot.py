"""Lightweight account snapshot: append a performance point, rebuild the dashboard, commit.

No LLM decisions here - pure data plumbing for dashboard freshness (pre-market and
after-hours slots). The scheduled wrapper has Claude publish the rebuilt page.

Run: <venv python> C:\\Users\\awsom\\Documents\\Projects\\trading-agent\\ops\\snapshot.py
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VT = ROOT / "Vibe-Trading"

os.chdir(VT)  # the agent package resolves imports relative to this cwd
sys.path.insert(0, "agent")

from src.trading import service  # noqa: E402

PROFILE = "alpaca-paper-trade"


def _num(value) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main() -> int:
    account = service.get_account(profile_id=PROFILE)
    acct = account.get("account") or {}
    equity = _num(acct.get("equity"))
    cash = _num(acct.get("cash"))
    if equity is None:
        print(json.dumps({"status": "error", "error": "equity unreadable", "raw": account}, default=str))
        return 1

    positions = service.get_positions(profile_id=PROFILE)
    pos_rows = positions.get("positions") or []
    pos_value = 0.0
    for row in pos_rows:
        pos_value += _num(row.get("market_value")) or 0.0
    # Per-position live detail (shares, avg cost, current, unrealized P&L) for
    # the dashboard and for sessions - refreshed every snapshot/watcher cycle.
    (ROOT / "journal" / "positions_live.json").write_text(
        json.dumps({"ts": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), "positions": pos_rows}, default=str),
        encoding="utf-8",
    )

    quote = service.get_quote("VOO", profile_id=PROFILE)
    q = quote.get("quote") or {}
    bid, ask = _num(q.get("bid")), _num(q.get("ask"))
    # After-hours quotes can be garbage (zero ask, absurd spread) - record null over noise.
    voo = None
    if bid and ask and bid > 0 and ask > 0 and abs(ask - bid) / ask < 0.02:
        voo = round((bid + ask) / 2, 2)

    line = {
        "ts": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "session": "snapshot",
        "equity": equity,
        "cash": cash,
        "positions_value": round(pos_value, 2),
        "voo_price": voo,
    }
    perf = ROOT / "journal" / "performance.jsonl"
    with perf.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(line) + "\n")

    # Refresh the whole-market candidate scan alongside every freshness cycle.
    subprocess.run([sys.executable, str(ROOT / "ops" / "screen.py")], capture_output=True, timeout=60, check=False)
    subprocess.run([sys.executable, str(ROOT / "ops" / "build_dashboard.py"), "--deploy"], check=True)
    subprocess.run(["git", "-C", str(ROOT), "add", "journal", "ops/dashboard.html"], check=True)
    subprocess.run(
        ["git", "-C", str(ROOT), "commit", "-m", "journal: snapshot " + line["ts"][:16]],
        check=False,  # nothing-to-commit is fine
    )
    print(json.dumps({"status": "ok", **line}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
