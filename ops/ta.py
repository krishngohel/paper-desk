"""Technical-analysis research: computed indicators + TradingView consensus.

Local indicators are computed from our own broker bars (authoritative, always
available). The TradingView block is ADVISORY context fetched from their public
scanner endpoint (unofficial - may vanish or rate-limit; result is null then).
Nothing here places orders; this is pure research input for session theses.

Run from anywhere: <venv python> ops\\ta.py SYM
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT / "Vibe-Trading")
sys.path.insert(0, "agent")

from src.trading.connectors.alpaca import sdk  # noqa: E402

PROFILE = "alpaca-paper-trade"
DATA = "https://data.alpaca.markets"


def _fetch_bars(symbol: str, timeframe: str, days_back: int, limit: int) -> list[dict]:
    """Read-only bar fetch straight from the data API with a proper start window
    (the connector's get_historical_bars omits `start`, so it only sees today)."""
    import requests
    from datetime import datetime, timedelta, timezone

    cfg = sdk.load_config()
    start = (datetime.now(timezone.utc) - timedelta(days=days_back)).strftime("%Y-%m-%dT%H:%M:%SZ")
    bars: list[dict] = []
    token = None
    for _ in range(4):
        url = (f"{DATA}/v2/stocks/{symbol}/bars?timeframe={timeframe}&start={start}"
               f"&limit={min(limit, 1000)}&feed={cfg.feed}&adjustment=split&sort=desc")
        if token:
            url += f"&page_token={token}"
        r = requests.get(url, headers={"APCA-API-KEY-ID": cfg.api_key, "APCA-API-SECRET-KEY": cfg.secret_key}, timeout=10)
        r.raise_for_status()
        j = r.json()
        for b in j.get("bars") or []:
            bars.append({"time": b["t"], "open": b["o"], "high": b["h"], "low": b["l"], "close": b["c"], "volume": b["v"]})
        token = j.get("next_page_token")
        if not token or len(bars) >= limit:
            break
    bars = bars[:limit]
    bars.sort(key=lambda b: b["time"])  # oldest-first for the indicator math
    return bars


def _closes(bars):
    return [float(b["close"]) for b in bars if b.get("close") is not None]


def _ema(vals, n):
    if len(vals) < n:
        return None
    k = 2 / (n + 1)
    e = sum(vals[:n]) / n
    for v in vals[n:]:
        e = v * k + e * (1 - k)
    return e


def _rsi(vals, n=14):
    if len(vals) < n + 1:
        return None
    gains, losses = [], []
    for a, b in zip(vals[:-1], vals[1:]):
        d = b - a
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    ag, al = sum(gains[:n]) / n, sum(losses[:n]) / n
    for g, l in zip(gains[n:], losses[n:]):
        ag = (ag * (n - 1) + g) / n
        al = (al * (n - 1) + l) / n
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def _atr(bars, n=14):
    if len(bars) < n + 1:
        return None
    trs = []
    prev_close = float(bars[0]["close"])
    for b in bars[1:]:
        h, l, c = float(b["high"]), float(b["low"]), float(b["close"])
        trs.append(max(h - l, abs(h - prev_close), abs(l - prev_close)))
        prev_close = c
    a = sum(trs[:n]) / n
    for tr in trs[n:]:
        a = (a * (n - 1) + tr) / n
    return a


def local_indicators(symbol: str) -> dict:
    daily = _fetch_bars(symbol, "1Day", days_back=120, limit=60)
    intra = _fetch_bars(symbol, "5Min", days_back=1, limit=78)
    closes = _closes(daily)
    out: dict = {"daily_bars": len(daily), "intraday_bars": len(intra)}
    if closes:
        last = closes[-1]
        out["last_close"] = round(last, 2)
        rsi = _rsi(closes)
        out["rsi14"] = round(rsi, 1) if rsi else None
        for n in (9, 21, 50):
            e = _ema(closes, n)
            out[f"ema{n}"] = round(e, 2) if e else None
        macd_f, macd_s = _ema(closes, 12), _ema(closes, 26)
        out["macd"] = round(macd_f - macd_s, 3) if macd_f and macd_s else None
        atr = _atr(daily)
        out["atr14"] = round(atr, 2) if atr else None
        window = closes[-20:]
        out["pos_in_20d_range_pct"] = round(100 * (last - min(window)) / (max(window) - min(window)), 1) if max(window) > min(window) else None
    if intra:
        pv = v = 0.0
        for b in intra:
            vol = float(b.get("volume") or 0)
            typ = (float(b["high"]) + float(b["low"]) + float(b["close"])) / 3
            pv += typ * vol
            v += vol
        out["vwap_today"] = round(pv / v, 2) if v > 0 else None
        out["day_high"] = round(max(float(b["high"]) for b in intra), 2)
        out["day_low"] = round(min(float(b["low"]) for b in intra), 2)
    return out


def tradingview_rating(symbol: str) -> dict | None:
    """TradingView scanner consensus - advisory, unofficial, fail-soft."""
    try:
        import requests

        cols = ["Recommend.All", "Recommend.MA", "Recommend.Other", "RSI", "close"]
        body = {"symbols": {"tickers": [f"NASDAQ:{symbol}", f"NYSE:{symbol}", f"AMEX:{symbol}"], "query": {"types": []}},
                "columns": cols}
        r = requests.post("https://scanner.tradingview.com/america/scan", json=body, timeout=8)
        r.raise_for_status()
        rows = r.json().get("data") or []
        if not rows:
            return None
        d = dict(zip(cols, rows[0]["d"]))

        def verdict(x):
            if x is None:
                return None
            return ("strong_buy" if x >= 0.5 else "buy" if x >= 0.1 else
                    "neutral" if x > -0.1 else "sell" if x > -0.5 else "strong_sell")

        return {"summary": verdict(d.get("Recommend.All")),
                "moving_averages": verdict(d.get("Recommend.MA")),
                "oscillators": verdict(d.get("Recommend.Other")),
                "tv_rsi": round(d["RSI"], 1) if d.get("RSI") is not None else None,
                "tv_close": d.get("close")}
    except Exception:  # noqa: BLE001 - advisory input, never fatal
        return None


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: ta.py SYMBOL")
        return 2
    symbol = sys.argv[1].upper()
    out = {"symbol": symbol, "indicators": local_indicators(symbol),
           "tradingview": tradingview_rating(symbol)}
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
