"""Correctness tests for the backtest fill engine.

A backtest is only worth running if its fills are honest, so every rule that
could flatter results is pinned here with synthetic bars whose right answer is
computed by hand. If one of these breaks, the harness is lying and its output
must not be trusted.

Run: <venv python> -m pytest ops/test_backtest.py -q
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from backtest import (ROUND_TRIP_BP, SLIPPAGE_BP, BTTrade, atr, find_setup,  # noqa: E402
                      simulate, swing_lows, touches_near)


def bar(t, o, h, l, c, v=1_000_000):
    return {"t": t, "o": o, "h": h, "l": l, "c": c, "v": v}


def setup(level=100.0, a=2.0):
    """stop = level - 0.5*ATR, target = level + 1.5*ATR (engine's convention)."""
    return {"level": level, "stop": level - 0.5 * a, "target": level + 1.5 * a,
            "atr": a, "touches": 3}


# --- anticipatory limit -----------------------------------------------------
def test_limit_does_not_fill_when_price_stays_above():
    bars = [bar("d0", 105, 106, 104, 105), bar("d1", 105, 107, 101, 106),
            bar("d2", 106, 108, 102, 107)]
    t = simulate(bars, 0, setup(), "anticipatory_limit", "X")
    assert not t.filled, "limit must not fill when the low never reaches the level"


def test_limit_fills_at_level_when_traded_through():
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 103, 104, 99, 103),      # low 99 < level 100 -> fill
            bar("d2", 103, 104, 102, 103)]
    t = simulate(bars, 0, setup(), "anticipatory_limit", "X")
    assert t.filled and t.entry_ts == "d1"
    # open (103) is above the level, so we fill AT the level, plus half-spread
    expected = 100.0 + 100.0 * (ROUND_TRIP_BP / 2 / 10_000)
    assert abs(t.entry_price - expected) < 1e-9, t.entry_price


def test_limit_gap_through_fills_at_open_not_level():
    """The classic backtest lie: a gap-down must not fill at the limit price."""
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 95, 96, 94, 95),         # gapped straight through 100
            bar("d2", 95, 96, 94, 95)]
    t = simulate(bars, 0, setup(), "anticipatory_limit", "X")
    assert t.filled
    expected = 95.0 + 95.0 * (ROUND_TRIP_BP / 2 / 10_000)
    assert abs(t.entry_price - expected) < 1e-9, "gap must fill at the open (95), not 100"


# --- exits ------------------------------------------------------------------
def test_stop_assumed_before_target_when_bar_covers_both():
    """Bars carry no tick order; covering both must resolve as the LOSS."""
    s = setup()                                  # stop 99, target 103
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 103, 104, 99.5, 100),      # fills the limit at 100
            bar("d2", 100, 104, 98, 101)]        # spans stop 99 AND target 103
    t = simulate(bars, 0, s, "anticipatory_limit", "X")
    assert t.filled
    assert t.exit_reason == "stop", f"expected pessimistic stop, got {t.exit_reason}"


def test_stop_gap_fills_at_open():
    s = setup()                                  # stop 99
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 103, 104, 99.5, 100),      # entry at 100
            bar("d2", 90, 91, 89, 90)]           # opened far below the stop
    t = simulate(bars, 0, s, "anticipatory_limit", "X")
    assert t.exit_reason == "stop_gap"
    expected = 90.0 - 90.0 * (ROUND_TRIP_BP / 2 / 10_000)
    assert abs(t.exit_price - expected) < 1e-9, "gapped stop must fill at 90, not 99"


def test_target_fill_and_positive_pnl():
    s = setup()                                  # target 103
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 103, 104, 99.5, 100),      # entry at 100
            bar("d2", 100.5, 103.5, 100.2, 103)] # reaches target, never the stop
    t = simulate(bars, 0, s, "anticipatory_limit", "X")
    assert t.exit_reason == "target"
    assert t.pnl_pct > 0


def test_time_stop_when_neither_level_is_reached():
    s = setup()
    bars = [bar("d0", 105, 106, 104, 105), bar("d1", 103, 104, 99.5, 100)]
    bars += [bar(f"d{i}", 100.5, 101, 100.1, 100.6) for i in range(2, 8)]
    t = simulate(bars, 0, s, "anticipatory_limit", "X", max_hold=5)
    assert t.exit_reason == "time_stop"


def test_exit_never_checked_on_the_entry_bar():
    """Filling and stopping out on the SAME bar would assume an order sequence we
    cannot observe; the engine must wait for the next bar."""
    s = setup()
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 103, 104, 98, 99)]         # spans entry AND the stop
    t = simulate(bars, 0, s, "anticipatory_limit", "X")
    assert t.filled and t.entry_ts == "d1"
    assert t.exit_reason == "unresolved", "no bar after entry -> unresolved, never a fabricated exit"
    assert t.pnl_pct is None, "unresolved trades must not contribute P&L"


# --- confirmation trigger ---------------------------------------------------
def test_confirmation_needs_a_touch_first():
    """Price never comes down to the level -> no touch -> no entry, even if it
    trades above the trigger the whole time."""
    bars = [bar("d0", 105, 106, 104, 105), bar("d1", 106, 108, 105, 107),
            bar("d2", 107, 109, 106, 108)]
    t = simulate(bars, 0, setup(), "confirmation_trigger", "X")
    assert not t.filled


def test_confirmation_does_not_fill_on_the_touch_bar():
    """A bar that dips to the level and closes strong is one bar of information;
    entering on it would be the same blind dip-buy we are trying to replace."""
    s = setup()                                  # level 100, trigger 100.5
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 103, 104, 99, 103),        # touches AND exceeds the trigger
            bar("d2", 103, 103.2, 102, 103)]
    t = simulate(bars, 0, s, "confirmation_trigger", "X")
    assert t.entry_ts != "d1", "must not enter on the bar that first tests the level"


def test_confirmation_fills_on_reclaim_after_touch():
    s = setup()                                  # level 100, trigger 100.5
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 101, 101.5, 99, 99.5),     # touch (low 99)
            bar("d2", 99.8, 102, 99.7, 101.5),   # reclaims above 100.5
            bar("d3", 101.5, 102, 101, 101.6)]
    t = simulate(bars, 0, s, "confirmation_trigger", "X")
    assert t.filled and t.entry_ts == "d2"
    # fills at the trigger (open 99.8 is below it), plus half-spread AND slippage
    base = 100.5
    expected = base + base * ((ROUND_TRIP_BP / 2 + SLIPPAGE_BP) / 10_000)
    assert abs(t.entry_price - expected) < 1e-9, t.entry_price


def test_confirmation_pays_more_than_limit_for_the_same_setup():
    """The mechanism's cost is real and must show up: you buy higher, later, and
    pay slippage. If this ever fails, the A/B is rigged in its favour."""
    s = setup()
    bars = [bar("d0", 105, 106, 104, 105),
            bar("d1", 101, 101.5, 99, 99.5),
            bar("d2", 99.8, 102, 99.7, 101.5),
            bar("d3", 101.5, 102, 101, 101.6)]
    lim = simulate(bars, 0, s, "anticipatory_limit", "X")
    conf = simulate(bars, 0, s, "confirmation_trigger", "X")
    assert lim.filled and conf.filled
    assert conf.entry_price > lim.entry_price


# --- no look-ahead ----------------------------------------------------------
def test_find_setup_cannot_see_the_future():
    """Identical history + wildly different futures must yield the same setup."""
    hist = [bar(f"d{i}", 100 + (i % 3), 101 + (i % 3), 99 + (i % 3), 100 + (i % 3))
            for i in range(60)]
    a = find_setup(list(hist))
    moon = hist + [bar("z", 500, 600, 499, 590)]
    crash = hist + [bar("z", 5, 6, 4, 5)]
    # the decision bar is the last of `hist` in every case
    assert find_setup(moon[:len(hist)]) == a
    assert find_setup(crash[:len(hist)]) == a


def test_simulate_only_reads_bars_after_the_setup_bar():
    """Mutating history BEFORE the setup index must not change the outcome."""
    s = setup()
    fut = [bar("d1", 103, 104, 99.5, 100), bar("d2", 100.5, 103.5, 100.2, 103)]
    a = simulate([bar("d0", 105, 106, 104, 105)] + fut, 0, s, "anticipatory_limit", "X")
    b = simulate([bar("d0", 999, 999, 999, 999)] + fut, 0, s, "anticipatory_limit", "X")
    assert (a.entry_price, a.exit_price, a.exit_reason) == (b.entry_price, b.exit_price, b.exit_reason)


# --- indicators -------------------------------------------------------------
def test_atr_matches_hand_computation():
    bars = [bar("d0", 10, 11, 9, 10), bar("d1", 10, 12, 10, 11), bar("d2", 11, 13, 11, 12)]
    # TR(d1)=max(2, |12-10|, |10-10|)=2 ; TR(d2)=max(2, |13-11|, |11-11|)=2
    assert abs(atr(bars, 2) - 2.0) < 1e-9


def test_swing_low_detection():
    lows = [10, 9, 8, 9, 10]  # pivot at index 2
    bars = [bar(f"d{i}", l, l + 1, l, l) for i, l in enumerate(lows)]
    assert 8 in swing_lows(bars, wing=2)


def test_touches_counts_only_near_bars():
    bars = [bar("a", 10, 10, 9.95, 10), bar("b", 10, 10, 20, 10), bar("c", 10, 10, 10.02, 10)]
    assert touches_near(bars, 10.0, tol=0.1) == 2
