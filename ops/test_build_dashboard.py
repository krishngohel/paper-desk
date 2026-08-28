"""Tests for build_dashboard.py on fixture journal data. Run: python -m pytest ops/test_build_dashboard.py -q"""

import importlib
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_dashboard as bd


def _setup(tmp_path, monkeypatch, perf=(), trades=(), mandate=None):
    journal = tmp_path / "journal"
    (journal / "daily").mkdir(parents=True)
    (journal / "performance.jsonl").write_text("\n".join(json.dumps(r) for r in perf), encoding="utf-8")
    (journal / "trades.jsonl").write_text("\n".join(json.dumps(t) for t in trades), encoding="utf-8")
    (journal / "lessons.md").write_text("## Active\n- **L1 - Test rule.** Body.\n## Archive\n", encoding="utf-8")
    (journal / "2026-08.md").write_text("# log\n\n## 2026-08-27 10:45 CT - intraday\n- action: HOLD - test\n", encoding="utf-8")
    monkeypatch.setattr(bd, "JOURNAL", journal)
    mpath = tmp_path / "mandate.json"
    if mandate is not None:
        mpath.write_text(json.dumps(mandate), encoding="utf-8")
    monkeypatch.setenv("TRADING_MANDATE_PATH", str(mpath))


def _mandate(days: int) -> dict:
    exp = (datetime.now(timezone.utc) + timedelta(days=days)).isoformat().replace("+00:00", "Z")
    return {"consent": {"expires_at": exp}}


def _perf(n=5):
    day = date.today().isoformat()
    slots = ["08:45", "09:45", "10:45", "11:45", "12:45"]
    return [
        {"ts": f"{day}T{slots[i]}:00", "session": "intraday",
         "equity": 100000 + i * 50, "cash": 99000.0, "positions_value": 1000.0,
         "voo_price": 550.0 + i}
        for i in range(n)
    ]


def test_chart_renders_both_series_and_labels(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch, perf=_perf(), mandate=_mandate(10))
    page = bd.build()
    assert 'class="line a"' in page and 'class="line v"' in page
    assert "Agent" in page and "VOO" in page          # direct labels + legend
    assert "mandate active" in page and "10d left" in page
    assert "L1 - Test rule." in page
    assert "10:45 CT - intraday" in page


def test_expired_mandate_shows_critical_pill(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch, perf=_perf(), mandate=_mandate(-2))
    page = bd.build()
    assert "MANDATE EXPIRED" in page and "pill crit" in page


def test_empty_data_renders_without_error(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch, perf=(), trades=(), mandate=None)
    page = bd.build()
    assert "No sessions recorded yet" in page
    assert "No open positions" in page
    assert "mandate unreadable" in page


def test_open_and_closed_trades_render(tmp_path, monkeypatch):
    trades = [
        {"trade_id": "t-1", "symbol": "AAPL", "closed_ts": None, "entry_qty": 0.5,
         "entry_price": 294.1, "exit_condition": "close < 285", "stop": 285.0, "target": 305.0},
        {"trade_id": "t-0", "symbol": "MSFT", "closed_ts": "2026-08-26T14:30:00",
         "entry_qty": 0.3, "entry_price": 500.0, "realized_pnl": 12.5,
         "exit_reason": "exit-condition-hit", "review_verdict": "right"},
        {"trade_id": "t-x", "symbol": "QQQ", "closed_ts": None, "aborted": True},
    ]
    _setup(tmp_path, monkeypatch, perf=_perf(), trades=trades, mandate=_mandate(5))
    page = bd.build()
    assert "285.0 / 305.0" in page                     # open position row: stop / target column
    assert "exit-condition-hit" in page and "right" in page
    assert "t-x" not in page                           # aborted records never render


def test_activity_strip_marks_ran_sessions(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch, perf=_perf(3), mandate=_mandate(5))
    page = bd.build()
    assert page.count('class="on"') == 3 if date.today().weekday() < 5 else True
    importlib.reload(bd)  # leave module state clean for other tests
