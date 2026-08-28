"""Session mutex. Slot sessions must never overlap each other or the continuous
loop (journal/git collisions). Rules:
  - `acquire` (slot caller): exit 1 if a fresh lock exists, else take it.
  - `acquire continuous` (the day loop): take/refresh the lock unconditionally -
    the loop owns the day and refreshes before every cycle.
  - `release`: drop it.
Stale locks (>20 min - a crashed process) are broken automatically, which is
also the fallback path: if the continuous loop dies, the 15-min slot grid
starts winning the lock again within 20 minutes.
"""
import json
import os
import sys
import time
from pathlib import Path

LOCK = Path(__file__).parent / "logs" / "session.lock"
STALE = 1200  # 20 min


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "acquire"
    caller = sys.argv[2] if len(sys.argv) > 2 else "slot"
    if cmd == "acquire":
        if caller != "continuous" and LOCK.exists():
            try:
                age = time.time() - json.loads(LOCK.read_text())["ts"]
            except Exception:  # noqa: BLE001
                age = STALE + 1
            if age < STALE:
                print(f"locked ({int(age)}s old) - slot skipped")
                return 1
            print("stale lock broken")
        LOCK.write_text(json.dumps({"ts": time.time(), "pid": os.getpid(), "owner": caller}))
        return 0
    if cmd == "release":
        LOCK.unlink(missing_ok=True)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
