"""Has today's post-close review run yet? Lets several launchers race for the
review safely: the continuous loop chains one when it ends, and the scheduled
daily/weekly review tasks are fallbacks that skip if it already ran.

Before 2026-09-23 the review ran only from a scheduled task at a fixed local
time. The laptop's time zone has been flipping between CT and ET, which moved
the task an hour early, into the trading loop's session lock, and it was
silently skipped (no review 09-21 or 09-22; six closed trades went unscored).

  review_due.py          exit 0 = due (no successful review today, CT date), 1 = done
  review_due.py --mark   record that today's review completed
  review_due.py --ct     print the current Central-time HHMM (the loop's clock;
                         immune to the system zone)
"""
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

STAMP = Path(__file__).parent / "logs" / "last_review.txt"


def ct_now() -> datetime:
    """US Central without tzdata (Windows Python ships no IANA database):
    CDT from the 2nd Sunday of March 2:00 to the 1st Sunday of November 2:00."""
    utc = datetime.now(timezone.utc)
    y = utc.year
    mar1 = datetime(y, 3, 1, tzinfo=timezone.utc)
    nov1 = datetime(y, 11, 1, tzinfo=timezone.utc)
    dst_start = mar1 + timedelta(days=(6 - mar1.weekday()) % 7 + 7, hours=8)  # 2:00 CST = 08:00Z
    dst_end = nov1 + timedelta(days=(6 - nov1.weekday()) % 7, hours=7)         # 2:00 CDT = 07:00Z
    offset = -5 if dst_start <= utc < dst_end else -6
    return utc.astimezone(timezone(timedelta(hours=offset)))


def main() -> int:
    today = ct_now().strftime("%Y-%m-%d")
    if "--ct" in sys.argv:
        print(ct_now().strftime("%H%M"))
        return 0
    if "--mark" in sys.argv:
        STAMP.parent.mkdir(exist_ok=True)
        STAMP.write_text(today, encoding="utf-8")
        return 0
    try:
        done = STAMP.read_text(encoding="utf-8").strip() == today
    except OSError:
        done = False
    print(f"review {'already ran' if done else 'due'} for {today}")
    return 1 if done else 0


if __name__ == "__main__":
    raise SystemExit(main())
