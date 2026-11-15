"""Serve the dashboard on localhost with the same read-only Alpaca proxy as netlify/functions/alpaca.mjs.

Keys come from ~/.vibe-trading/alpaca.json and stay on this machine. Endpoint allowlist only -
there is deliberately NO order/write path here.

Run: python ops/serve_local.py [port]   (default 8888, rebuilds the page first)
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
PAPER = "https://paper-api.alpaca.markets"
DATA = "https://data.alpaca.markets"
CREDS = json.loads((Path.home() / ".vibe-trading" / "alpaca.json").read_text(encoding="utf-8"))


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - stdlib name
        url = urlparse(self.path)
        if url.path in ("/api/alpaca", "/.netlify/functions/alpaca"):
            return self._proxy(parse_qs(url.query))
        return super().do_GET()

    def _proxy(self, qs: dict) -> None:
        what = (qs.get("what") or [""])[0]
        if what == "account":
            target = f"{PAPER}/v2/account"
        elif what == "positions":
            target = f"{PAPER}/v2/positions"
        elif what == "quote":
            symbols = re.sub(r"[^A-Za-z,.]", "", (qs.get("symbols") or [""])[0])
            if not symbols:
                return self._send(400, b'{"error":"symbols required"}')
            target = f"{DATA}/v2/stocks/quotes/latest?symbols={symbols}"
        else:
            return self._send(400, b'{"error":"unknown what"}')
        req = urllib.request.Request(target, headers={
            "APCA-API-KEY-ID": CREDS["api_key"], "APCA-API-SECRET-KEY": CREDS["secret_key"]})
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                self._send(res.status, res.read())
        except urllib.error.HTTPError as exc:
            self._send(exc.code, exc.read())
        except Exception:  # noqa: BLE001 - page falls back to its snapshot
            self._send(502, b'{"error":"upstream unreachable"}')

    def _send(self, status: int, body: bytes) -> None:
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("cache-control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8888
    subprocess.run([sys.executable, str(ROOT / "ops" / "build_dashboard.py")], check=False)
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(ROOT / "site")))
    print(f"Paper Desk at http://localhost:{port}", flush=True)
    server.serve_forever()
