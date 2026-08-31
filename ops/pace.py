"""Sleep out the remainder of a minimum interval between session starts.

The continuous relay used to sleep a flat 5 seconds between legs, so sessions
ran effectively back-to-back: on 2026-08-31 it started 12 full research legs in
40 minutes and exhausted a 5-hour usage window, twice. This enforces a floor on
the START-to-START interval instead: a leg that takes 4 minutes is followed by
~11 minutes of quiet; a leg that overruns the floor is followed immediately.

The watcher is what makes this safe - it streams live ticks and enforces stops
and armed triggers in about a second, independent of sessions. Sessions think;
the watcher reacts. Slowing the thinking cadence does not slow the reflexes.

Run: <venv python> ops\\pace.py <start_epoch> [floor_seconds]
"""

from __future__ import annotations

import sys
import time

DEFAULT_FLOOR = 900  # 15 minutes between leg starts


def main() -> int:
    try:
        start = float(sys.argv[1])
    except (IndexError, ValueError):
        print("pace: no valid start epoch given, not sleeping")
        return 0
    floor = float(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_FLOOR
    elapsed = time.time() - start
    remaining = floor - elapsed
    if remaining <= 0:
        print(f"pace: leg took {elapsed:.0f}s >= floor {floor:.0f}s - next leg starts now")
        return 0
    print(f"pace: leg took {elapsed:.0f}s, sleeping {remaining:.0f}s to hold the "
          f"{floor / 60:.0f}-min floor between leg starts")
    time.sleep(remaining)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
