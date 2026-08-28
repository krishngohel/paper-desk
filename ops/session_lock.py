"""Session mutex: at 15-min cadence, sessions must never overlap (journal/git
collisions). acquire exits 1 when a fresh lock exists - the slot is skipped by
design; effective cadence adapts to session duration. Stale locks (>20 min,
a crashed session) are broken automatically."""
import json
import os
import sys
import time
from pathlib import Path

LOCK = Path(__file__).parent / "logs" / "session.lock"
STALE = 1200  # 20 min


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "acquire"
    if cmd == "acquire":
        if LOCK.exists():
            try:
                age = time.time() - json.loads(LOCK.read_text())["ts"]
            except Exception:  # noqa: BLE001
                age = STALE + 1
            if age < STALE:
                print(f"locked ({int(age)}s old) - slot skipped")
                return 1
            print("stale lock broken")
        LOCK.write_text(json.dumps({"ts": time.time(), "pid": os.getpid()}))
        return 0
    if cmd == "release":
        LOCK.unlink(missing_ok=True)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
