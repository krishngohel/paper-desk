"""Local live ops console - mission control for the trading agents.

Serves http://localhost:8321 : a live view of the thought process (journal +
session stdout), the agent map (relay / watcher / stream / snapshots / broker,
with real liveness), the book, armed triggers, and research state.

Data paths: journal files polled every request (cheap reads); broker truth
(positions/orders) refreshed by a background thread every 20s through the same
gated read-only service layer everything else uses. Read-only: this console
can NOT place, cancel, or modify anything.

Run: <venv python> ops\\console.py    (Ctrl+C to stop)
"""

from __future__ import annotations

import json
import os
import re
import secrets
import sys
import threading
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
VT = ROOT / "Vibe-Trading"
JOURNAL = ROOT / "journal"
LOGS = ROOT / "ops" / "logs"
PORT = 8321

os.chdir(VT)
sys.path.insert(0, "agent")
from src.live.halt import halt_flag_set  # noqa: E402
from src.trading import service  # noqa: E402

PROFILE = "alpaca-paper-trade"
BROKER: dict = {"positions": [], "orders": [], "equity": None, "cash": None, "ts": None}


def _broker_refresher() -> None:
    while True:
        try:
            acct = (service.get_account(profile_id=PROFILE) or {}).get("account") or {}
            BROKER["equity"] = acct.get("equity")
            BROKER["cash"] = acct.get("cash")
            BROKER["last_equity"] = acct.get("last_equity")
            BROKER["positions"] = (service.get_positions(profile_id=PROFILE) or {}).get("positions") or []
            op = service.get_open_orders(profile_id=PROFILE) or {}
            BROKER["orders"] = op.get("orders") or op.get("open_orders") or []
            BROKER["ts"] = datetime.now().strftime("%H:%M:%S")
            BROKER["error"] = None
        except Exception as exc:  # noqa: BLE001
            BROKER["error"] = str(exc)[:150]
        time.sleep(20)


def _tail(path: Path, n: int = 40) -> list[str]:
    try:
        return path.read_text(encoding="utf-8", errors="replace").splitlines()[-n:]
    except OSError:
        return []


def _jsonl(path: Path, n: int = 200) -> list[dict]:
    out = []
    for line in _tail(path, n):
        try:
            out.append(json.loads(line))
        except ValueError:
            continue
    return out


def _journal_entries(n: int = 14) -> list[dict]:
    out = []
    files = sorted(JOURNAL.glob("2*.md"), reverse=True)[:2]
    for f in files:
        parts = re.split(r"^## ", f.read_text(encoding="utf-8", errors="replace"), flags=re.M)
        for chunk in parts[1:]:
            lines = chunk.strip().splitlines()
            if lines:
                out.append({"head": lines[0].strip(), "body": "\n".join(lines[1:40])})
    out = out[-n:]
    out.reverse()
    return out


def _log_age(path: Path) -> float | None:
    try:
        return time.time() - path.stat().st_mtime
    except OSError:
        return None


def _agents() -> dict:
    lock = {}
    try:
        lock = json.loads((LOGS / "session.lock").read_text())
        lock["age"] = round(time.time() - lock.get("ts", 0))
    except Exception:  # noqa: BLE001
        lock = None
    hwm = None
    try:
        hwm = json.loads((LOGS / "watcher_state.json").read_text()).get("hwm")
    except Exception:  # noqa: BLE001
        pass
    # Liveness comes from the heartbeat file (touched every loop, ~2s), NOT the
    # log: watcher.log is silent for ~15 min at a time when nothing happens, so
    # log mtime made a healthy watcher read as dead. Falls back to the log for
    # a watcher started before heartbeats existed.
    watcher_age = _log_age(LOGS / "watcher.heartbeat")
    if watcher_age is None:
        watcher_age = _log_age(LOGS / "watcher.log")
    stream_line = next((ln for ln in reversed(_tail(LOGS / "watcher.log", 200))
                        if "stream connected" in ln or "stream error" in ln), "")
    sess_lines = _tail(LOGS / "sessions.log", 400)
    last_session = next((ln for ln in reversed(sess_lines) if ln.startswith("====")), "")
    perf = _jsonl(JOURNAL / "performance.jsonl", 5)
    return {
        "halted": halt_flag_set(),
        "hwm": hwm,
        "session_lock": lock,
        "last_session_header": last_session,
        "watcher_alive": watcher_age is not None and watcher_age < 90,
        "watcher_log_age_s": round(watcher_age) if watcher_age is not None else None,
        "stream_status": stream_line[-160:],
        "last_snapshot": perf[-1] if perf else None,
        "broker_ts": BROKER.get("ts"),
        "broker_error": BROKER.get("error"),
    }


def state() -> dict:
    scan = {}
    try:
        scan = json.loads((JOURNAL / "universe_scan.json").read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        pass
    stats = {}
    try:
        stats = json.loads((JOURNAL / "stats.json").read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        pass
    watchlist = ""
    try:
        watchlist = (JOURNAL / "watchlist.md").read_text(encoding="utf-8", errors="replace")
    except OSError:
        pass
    return {
        "now": datetime.now().strftime("%H:%M:%S"),
        "agents": _agents(),
        "broker": {"equity": BROKER["equity"], "cash": BROKER["cash"],
                   "last_equity": BROKER.get("last_equity"),
                   "positions": BROKER["positions"], "orders": BROKER["orders"]},
        "trades": _jsonl(JOURNAL / "trades.jsonl", 60),
        "triggers": _jsonl(JOURNAL / "triggers.jsonl", 40),
        "performance": _jsonl(JOURNAL / "performance.jsonl", 300),
        "journal": _journal_entries(),
        "watcher_log": _tail(LOGS / "watcher.log", 25),
        "sessions_log": _tail(LOGS / "sessions.log", 30),
        "scan": (scan.get("shortlist") or [])[:24],
        "scan_ts": scan.get("ts"),
        "stats": stats.get("overall"),
        "watchlist_md": watchlist,
    }


def _token() -> str:
    """Shared secret for REMOTE viewers (a tunnel makes this console public).

    Local requests are exempt, but note the test cannot be the peer address:
    cloudflared/ngrok run on this machine, so tunnelled requests also arrive
    from 127.0.0.1. A forwarding header is the reliable tell that a request
    came in from outside.
    """
    env = os.environ.get("PAPERDESK_TOKEN")
    if env:
        return env
    path = LOGS / "console_token.txt"
    try:
        return path.read_text(encoding="utf-8").strip()
    except OSError:
        tok = secrets.token_urlsafe(18)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(tok, encoding="utf-8")
        return tok


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # noqa: ANN002, D102
        pass

    def _authorized(self) -> bool:
        remote = bool(self.headers.get("X-Forwarded-For")
                      or self.headers.get("Cf-Connecting-Ip"))
        if not remote:
            return True
        tok = _token()
        qs = parse_qs(urlparse(self.path).query)
        if (qs.get("t") or [""])[0] == tok:
            return True
        cookie = self.headers.get("Cookie") or ""
        return f"pd={tok}" in cookie

    def do_GET(self):  # noqa: N802, D102
        if not self._authorized():
            self.send_response(403)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Paper Desk console: add ?t=<token> to the URL.\n"
                             b"Token is in ops/logs/console_token.txt on the trading machine.")
            return
        if self.path.startswith("/api/state"):
            body = json.dumps(state(), default=str).encode("utf-8")
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("cache-control", "no-store")
        else:
            try:
                body = (ROOT / "ops" / "console.html").read_bytes()
            except OSError:
                body = b"console.html missing"
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=utf-8")
            qs = parse_qs(urlparse(self.path).query)
            if (qs.get("t") or [""])[0] == _token():
                self.send_header("set-cookie",
                                 f"pd={_token()}; Path=/; Max-Age=604800; SameSite=Lax")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> int:
    threading.Thread(target=_broker_refresher, daemon=True).start()
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"ops console: http://localhost:{PORT}")
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
