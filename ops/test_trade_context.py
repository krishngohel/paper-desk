"""Exit replay: rules only add earlier exits, arm on the bar that reaches the
threshold, and fill a gap-through at the open."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from trade_context import exit_replay  # noqa: E402


def bar(o, h, l, c):
    return {"o": o, "h": h, "l": l, "c": c}


def test_never_armed_keeps_actual_exit():
    path = [bar(100, 100.4, 99, 99.5), bar(99.5, 99.6, 97, 97)]
    r = exit_replay(path, entry=100, atr=2, actual_ret=-3.0)
    assert all(v == -3.0 for v in r.values())


def test_gave_back_trade_is_saved_at_breakeven():
    # +1.5 ATR, then collapses to a -4% actual exit.
    path = [bar(100, 103, 99.8, 102.5), bar(102.5, 102.6, 99, 99.2), bar(99.2, 99.3, 96, 96)]
    r = exit_replay(path, entry=100, atr=2, actual_ret=-4.0)
    assert r["breakeven_after_1atr"] == 0.0
    assert r["breakeven_after_0.5atr"] == 0.0
    # peak 103, trail 1 ATR -> stop 101, hit on bar 2
    assert r["trail_1atr_after_1atr"] == 1.0
    # half sold at +2%, half at -4%
    assert r["half_off_at_1atr"] == -1.0


def test_arming_bar_is_not_also_the_stop_bar():
    # One bar both reaches +1 ATR and trades below entry: ambiguous order, so the
    # stop is only live from the next bar.
    path = [bar(100, 102.5, 99, 101), bar(101, 101.5, 100.5, 101.2)]
    r = exit_replay(path, entry=100, atr=2, actual_ret=1.2)
    assert r["breakeven_after_1atr"] == 1.2


def test_gap_through_fills_at_open():
    path = [bar(100, 102.2, 100, 102), bar(98, 98.5, 97, 97.5)]
    r = exit_replay(path, entry=100, atr=2, actual_ret=-2.5)
    assert r["breakeven_after_1atr"] == -2.0


def test_winner_cut_short_by_trailing_stop():
    path = [bar(100, 104, 100, 103.5), bar(103.5, 103.6, 101.5, 102), bar(102, 110, 102, 110)]
    r = exit_replay(path, entry=100, atr=2, actual_ret=10.0)
    assert r["trail_1atr_after_1atr"] == 2.0
    assert r["breakeven_after_1atr"] == 10.0
