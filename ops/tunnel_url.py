"""Print (and save) the current console viewing URL: tunnel host + access token.

Cloudflare quick tunnels get a new random hostname on every start, so the URL
is not stable across restarts - this reads whichever one is live now out of
cloudflared's log and pairs it with the console's remote-access token.

Run: <venv python> ops\\tunnel_url.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT / "ops" / "logs"


def main() -> int:
    try:
        log = (LOGS / "tunnel.log").read_text(encoding="utf-8", errors="replace")
    except OSError:
        print("no tunnel.log - is the tunnel running? (ops\\run_tunnel.cmd)")
        return 1
    hosts = re.findall(r"https://[a-z0-9-]+\.trycloudflare\.com", log)
    if not hosts:
        print("tunnel.log has no hostname yet - cloudflared may still be starting")
        return 1
    host = hosts[-1]
    try:
        token = (LOGS / "console_token.txt").read_text(encoding="utf-8").strip()
    except OSError:
        print(f"{host}  (no token file yet - open the console locally once to mint one)")
        return 1
    url = f"{host}/?t={token}"
    (LOGS / "tunnel_url.txt").write_text(url + "\n", encoding="utf-8")
    print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
