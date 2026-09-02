"""Historical bar loader for the backtester, with an on-disk cache.

Pulls from Alpaca's CONSOLIDATED tape (feed=sip) - the same fix ta.py needed
after iex was found to carry ~0.3% of real volume. SIP is only queryable
outside a ~15 min window, so every request ends SIP_LAG_MIN in the past; a
backtest never wants the live edge anyway.

Bars are cached under ops/cache/bars/ as JSON keyed by symbol+timeframe+range,
so re-running a backtest costs no network and gives byte-identical inputs -
which is what makes results reproducible and comparable between strategy runs.

Run directly to warm the cache:
    <venv python> ops\\bt_data.py AAPL MSFT --days 400 --timeframe 1Day
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "ops" / "cache" / "bars"
DATA = "https://data.alpaca.markets"
SIP_LAG_MIN = 20


def _config():
    """Load broker credentials without importing ta.py (which chdir's on import)."""
    vt = ROOT / "Vibe-Trading"
    if str(vt / "agent") not in sys.path:
        sys.path.insert(0, str(vt / "agent"))
    cwd = os.getcwd()
    try:
        os.chdir(vt)
        from src.trading.connectors.alpaca import sdk
        return sdk.load_config()
    finally:
        os.chdir(cwd)


def _cache_path(symbol: str, timeframe: str, start: str, end: str) -> Path:
    key = f"{symbol.upper()}_{timeframe}_{start[:10]}_{end[:10]}.json"
    return CACHE / key


def load_bars(symbol: str, timeframe: str = "1Day", days_back: int = 400,
              use_cache: bool = True) -> list[dict]:
    """Oldest-first bars: [{t, o, h, l, c, v}, ...]. Empty list on any failure."""
    now = datetime.now(timezone.utc)
    start = (now - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = (now - timedelta(minutes=SIP_LAG_MIN)).strftime("%Y-%m-%dT%H:%M:%SZ")
    path = _cache_path(symbol, timeframe, start, end)
    if use_cache and path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            pass

    import requests

    cfg = _config()
    hdr = {"APCA-API-KEY-ID": cfg.api_key, "APCA-API-SECRET-KEY": cfg.secret_key}
    out: list[dict] = []
    token = None
    for _ in range(20):  # generous page budget; loop exits when the feed says done
        url = (f"{DATA}/v2/stocks/{symbol}/bars?timeframe={timeframe}"
               f"&start={start}&end={end}&limit=10000&feed=sip&adjustment=split")
        if token:
            url += f"&page_token={token}"
        try:
            r = requests.get(url, headers=hdr, timeout=30)
        except Exception:  # noqa: BLE001
            return []
        if not r.ok:
            return []
        j = r.json()
        for b in j.get("bars") or []:
            out.append({"t": b["t"], "o": b["o"], "h": b["h"],
                        "l": b["l"], "c": b["c"], "v": b["v"]})
        token = j.get("next_page_token")
        if not token:
            break
        time.sleep(0.05)

    out.sort(key=lambda b: b["t"])
    if out:
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(out), encoding="utf-8")
    return out


def main() -> int:
    argv = sys.argv[1:]
    days, tf = 400, "1Day"
    skip = set()
    for i, a in enumerate(argv):
        if a == "--days":
            days, skip = int(argv[i + 1]), skip | {i, i + 1}
        elif a == "--timeframe":
            tf, skip = argv[i + 1], skip | {i, i + 1}
    syms = [a.upper() for i, a in enumerate(argv) if i not in skip and not a.startswith("--")]
    if not syms:
        print("usage: bt_data.py SYM [SYM...] [--days N] [--timeframe 1Day|5Min]")
        return 2
    for s in syms:
        bars = load_bars(s, tf, days)
        span = f"{bars[0]['t'][:10]} -> {bars[-1]['t'][:10]}" if bars else "none"
        print(f"  {s:6s} {len(bars):>6} {tf} bars  {span}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
