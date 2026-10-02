"""The watcher defers a stop breach to a stop resting at the broker, then falls
back to its own cancel-and-sell if the position is still held after the grace."""
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
_cwd = os.getcwd()
import watcher as w  # noqa: E402  (import chdirs into Vibe-Trading)
os.chdir(_cwd)

REC = {"trade_id": "t-1", "symbol": "TXG", "stop": 64.73, "target": None}


class _Service:
    def __init__(self, orders):
        self.orders = orders

    def get_positions(self, profile_id=None):
        return {"positions": [{"symbol": "TXG", "quantity": 15}]}

    def get_open_orders(self, profile_id=None):
        return {"open_orders": self.orders}


@pytest.fixture
def harness(monkeypatch):
    calls = {"cancel": 0, "sell": 0}
    clock = {"now": 1_000_000.0}
    monkeypatch.setattr(w.time, "time", lambda: clock["now"])
    for name, fn in {
        "halt_flag_set": lambda: False, "death_check": lambda state: False,
        "unwedge_gate_if_phantom": lambda: False, "open_records": lambda: [dict(REC)],
        "pending_records": lambda: [], "good_quote": lambda sym: (60.0, 60.1),
        "save_state": lambda state: None, "freshness": lambda state: None,
        "spawn_session": lambda reason, state: None, "journal_note": lambda text: None,
        "close_record": lambda *a, **k: None, "log": lambda msg: None,
        "cancel_symbol_orders": lambda sym: calls.__setitem__("cancel", calls["cancel"] + 1),
        "market_sell": lambda sym, qty, why: calls.__setitem__("sell", calls["sell"] + 1) or {"status": "ok"},
        "sell_succeeded": lambda out: True,
    }.items():
        monkeypatch.setattr(w, name, fn)
    return calls, clock


def test_breach_waits_for_a_resting_broker_stop(monkeypatch, harness):
    calls, clock = harness
    monkeypatch.setattr(w, "service", _Service([
        {"symbol": "TXG", "side": "sell", "order_type": "stop", "stop_price": 64.73}]))
    state = {"last_gate_check": clock["now"]}
    w.tick(state)
    clock["now"] += 10
    w.tick(state)
    assert calls == {"cancel": 0, "sell": 0}


def test_still_held_after_grace_falls_back_to_the_watcher_sell(monkeypatch, harness):
    calls, clock = harness
    monkeypatch.setattr(w, "service", _Service([
        {"symbol": "TXG", "side": "sell", "order_type": "oco", "stop_price": 64.73}]))
    state = {"last_gate_check": clock["now"]}
    w.tick(state)
    clock["now"] += w.BROKER_STOP_GRACE + 1
    w.tick(state)
    assert calls == {"cancel": 1, "sell": 1}


def test_no_broker_stop_sells_immediately_as_before(monkeypatch, harness):
    calls, clock = harness
    monkeypatch.setattr(w, "service", _Service([
        {"symbol": "TXG", "side": "sell", "order_type": "limit", "limit_price": 99}]))
    w.tick({"last_gate_check": clock["now"]})
    assert calls == {"cancel": 1, "sell": 1}


def test_recovery_above_the_stop_resets_the_grace(monkeypatch, harness):
    calls, clock = harness
    monkeypatch.setattr(w, "service", _Service([
        {"symbol": "TXG", "side": "sell", "order_type": "stop", "stop_price": 64.73}]))
    state = {"last_gate_check": clock["now"]}
    w.tick(state)                                   # breach starts the window
    monkeypatch.setattr(w, "good_quote", lambda sym: (70.0, 70.1))
    clock["now"] += 5
    w.tick(state)                                   # recovered: window cleared
    monkeypatch.setattr(w, "good_quote", lambda sym: (60.0, 60.1))
    clock["now"] += 3600
    w.tick(state)                                   # new breach, fresh grace
    assert calls == {"cancel": 0, "sell": 0}
