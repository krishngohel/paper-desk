"""Rotate the narrative journal so sessions stop paying to re-read history.

Every session reads the tail of `journal/YYYY-MM.md`. That file grows a few KB
per session forever, so the per-session context cost climbs every day even when
nothing else changes (272 KB / 95 entries by 2026-08-31 - roughly 68k tokens of
standing context). Rotation moves older entries into `journal/archive/` and
leaves a slim active file behind.

NOTHING IS DELETED. Archived entries stay in git and remain the training
record; they simply stop being loaded into every session's context. The
dashboard and ops console only ever render the newest 10-14 entries, so neither
loses anything (verified against build_dashboard._entries and console._journal_entries).

Run: <venv python> ops\\rotate_journal.py [--keep N] [--month YYYY-MM] [--dry-run]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOURNAL = ROOT / "journal"
ARCHIVE = JOURNAL / "archive"
KEEP_DEFAULT = 12          # comfortably more than the SOP's "last 10 entries"


def _arg(flag: str, default: str | None = None) -> str | None:
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default


def rotate(month: str, keep: int, dry: bool) -> int:
    src = JOURNAL / f"{month}.md"
    if not src.exists():
        print(f"no such journal: {src}")
        return 1

    text = src.read_text(encoding="utf-8")
    # Split into (file header, [entries]) - entries start at a "## " line.
    parts = re.split(r"^(?=## )", text, flags=re.M)
    header = parts[0] if parts and not parts[0].startswith("## ") else ""
    entries = [p for p in parts if p.startswith("## ")]

    if len(entries) <= keep:
        print(f"{src.name}: {len(entries)} entries <= keep {keep} - nothing to rotate")
        return 0

    old, recent = entries[:-keep], entries[-keep:]
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    existing = sorted(ARCHIVE.glob(f"{month}-part*.md"))
    dest = ARCHIVE / f"{month}-part{len(existing) + 1}.md"

    first = old[0].splitlines()[0].removeprefix("## ").strip()
    last = old[-1].splitlines()[0].removeprefix("## ").strip()
    archive_text = (f"# Archived session journal — {month} (part {len(existing) + 1})\n"
                    f"Entries {first!r} through {last!r}.\n"
                    f"Archived to keep the active journal small; this is still the "
                    f"permanent training record.\n\n" + "".join(old))

    kept_header = header.rstrip() or f"# Session journal — {month}"
    archived_names = ", ".join(p.name for p in existing + [dest])
    new_text = (f"{kept_header}\n\n"
                f"> Older entries live in `journal/archive/` ({archived_names}). "
                f"Read them only when you need history older than this file.\n\n"
                + "".join(recent))

    print(f"{src.name}: {len(entries)} entries -> keeping {len(recent)}, "
          f"archiving {len(old)} to {dest.relative_to(ROOT)}")
    print(f"  size {len(text):,} B -> {len(new_text):,} B "
          f"({100 * (1 - len(new_text) / len(text)):.0f}% smaller)")
    if dry:
        print("  (dry run - nothing written)")
        return 0

    dest.write_text(archive_text, encoding="utf-8")
    src.write_text(new_text, encoding="utf-8")
    return 0


def main() -> int:
    month = _arg("--month") or sorted(p.stem for p in JOURNAL.glob("2*.md"))[-1]
    keep = int(_arg("--keep", str(KEEP_DEFAULT)))
    return rotate(month, keep, "--dry-run" in sys.argv)


if __name__ == "__main__":
    raise SystemExit(main())
