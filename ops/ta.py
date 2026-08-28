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


def _candle_anatomy(b: dict) -> dict:
    o, h, l, c = float(b["open"]), float(b["high"]), float(b["low"]), float(b["close"])
    rng = h - l or 1e-9
    body = abs(c - o)
    return {"o": o, "h": h, "l": l, "c": c, "range": rng, "body": body,
            "body_pct": body / rng, "up": c >= o,
            "upper_wick": (h - max(o, c)) / rng, "lower_wick": (min(o, c) - l) / rng}


def candle_tells(bars: list[dict], levels: dict | None = None, atr: float | None = None,
                 last_n: int = 6) -> list[str]:
    """Detect classic candlestick tells in the most recent bars, annotated with
    LOCATION (at support/resistance) - a pattern at a level is information, the
    same pattern mid-air is noise. Detection is mechanical; meaning is the model's."""
    if len(bars) < 3:
        return []
    out = []
    supports = (levels or {}).get("support_below", []) or []
    resistances = (levels or {}).get("resistance_above", []) or []
    near = (atr or 0) * 0.5 or None

    def _at_level(price: float) -> str:
        if near:
            for s in supports:
                if abs(price - s) <= near:
                    return f" AT SUPPORT {s}"
            for r in resistances:
                if abs(price - r) <= near:
                    return f" AT RESISTANCE {r}"
        return ""

    recent = bars[-last_n:]
    for i, b in enumerate(recent):
        a = _candle_anatomy(b)
        label = str(b.get("time", ""))[:16]
        loc = _at_level(a["l"] if a["lower_wick"] > a["upper_wick"] else a["h"])
        if a["body_pct"] < 0.12:
            out.append(f"{label}: doji (indecision){loc}")
        elif a["lower_wick"] > 0.55 and a["body_pct"] < 0.35:
            out.append(f"{label}: hammer/long lower wick (buyers defended {round(a['l'],2)}){loc}")
        elif a["upper_wick"] > 0.55 and a["body_pct"] < 0.35:
            out.append(f"{label}: shooting star/long upper wick (sellers rejected {round(a['h'],2)}){loc}")
        elif a["body_pct"] > 0.85:
            out.append(f"{label}: marubozu ({'strong buying' if a['up'] else 'strong selling'}, full-body)")
        if i >= 1:
            p = _candle_anatomy(recent[i - 1])
            if a["up"] and not p["up"] and a["c"] > p["o"] and a["o"] < p["c"] and a["body"] > p["body"]:
                out.append(f"{label}: BULLISH ENGULFING of prior bar{_at_level(a['l'])}")
            if not a["up"] and p["up"] and a["c"] < p["o"] and a["o"] > p["c"] and a["body"] > p["body"]:
                out.append(f"{label}: bearish engulfing of prior bar{_at_level(a['h'])}")
            if a["h"] < p["h"] and a["l"] > p["l"]:
                out.append(f"{label}: inside bar (compression - watch the break)")
        if i >= 2:
            p1, p2 = _candle_anatomy(recent[i - 2]), _candle_anatomy(recent[i - 1])
            if (not p1["up"] and p1["body_pct"] > 0.5 and p2["body_pct"] < 0.3
                    and a["up"] and a["body_pct"] > 0.5 and a["c"] > (p1["o"] + p1["c"]) / 2):
                out.append(f"{label}: MORNING STAR (3-bar bullish reversal){_at_level(p2['l'])}")
    return out[-8:]


def _pivots(daily: list[dict], wing: int = 2) -> tuple[list[float], list[float]]:
    """Swing highs (resistance) and swing lows (support) from daily bars."""
    highs, lows = [], []
    for i in range(wing, len(daily) - wing):
        h = float(daily[i]["high"])
        l = float(daily[i]["low"])
        if all(h >= float(daily[j]["high"]) for j in range(i - wing, i + wing + 1)):
            highs.append(round(h, 2))
        if all(l <= float(daily[j]["low"]) for j in range(i - wing, i + wing + 1)):
            lows.append(round(l, 2))
    return highs, lows


def key_levels(daily: list[dict]) -> dict:
    """Support/resistance and structure the model should trade around."""
    out: dict = {}
    if len(daily) < 6:
        return out
    last = float(daily[-1]["close"])
    highs, lows = _pivots(daily)
    out["resistance_above"] = sorted([h for h in highs if h > last])[:3]
    out["support_below"] = sorted([l for l in lows if l < last], reverse=True)[:3]
    prev = daily[-2]
    out["prior_day"] = {"high": round(float(prev["high"]), 2),
                        "low": round(float(prev["low"]), 2),
                        "close": round(float(prev["close"]), 2)}
    # Trend structure over the last 10 bars: sequence of highs and lows.
    recent = daily[-10:]
    hh = sum(1 for a, b in zip(recent[:-1], recent[1:]) if float(b["high"]) > float(a["high"]))
    hl = sum(1 for a, b in zip(recent[:-1], recent[1:]) if float(b["low"]) > float(a["low"]))
    if hh >= 6 and hl >= 6:
        out["structure"] = "uptrend (higher highs + higher lows)"
    elif hh <= 3 and hl <= 3:
        out["structure"] = "downtrend (lower highs + lower lows)"
    else:
        out["structure"] = "range/mixed"
    vols = [float(b.get("volume") or 0) for b in daily[-21:-1]]
    if vols and float(daily[-1].get("volume") or 0):
        out["volume_vs_20d_avg"] = round(float(daily[-1]["volume"]) / (sum(vols) / len(vols)), 2)
    return out


def next_earnings(symbol: str) -> str | None:
    """Next earnings date via yfinance - EVENT RISK; fail-soft to null."""
    try:
        import yfinance as yf

        t = yf.Ticker(symbol)
        try:
            dates = t.earnings_dates
            if dates is not None and len(dates):
                import pandas as pd

                future = dates.index[dates.index > pd.Timestamp.now(tz=dates.index.tz)]
                if len(future):
                    return str(future.min().date())
        except Exception:  # noqa: BLE001
            pass
        cal = t.calendar
        if isinstance(cal, dict):
            ed = cal.get("Earnings Date")
            if ed:
                return str(ed[0] if isinstance(ed, (list, tuple)) else ed)
    except Exception:  # noqa: BLE001
        return None
    return None


def market_context() -> dict:
    """SPY + QQQ regime snapshot - trade WITH the tape, not against it."""
    out = {}
    for sym in ("SPY", "QQQ"):
        try:
            daily = _fetch_bars(sym, "1Day", days_back=120, limit=60)
            closes = _closes(daily)
            last = closes[-1]
            e21 = _ema(closes, 21)
            rsi = _rsi(closes)
            lv = key_levels(daily)
            out[sym] = {"last": round(last, 2),
                        "vs_ema21_pct": round((last / e21 - 1) * 100, 2) if e21 else None,
                        "rsi14": round(rsi, 1) if rsi else None,
                        "structure": lv.get("structure")}
        except Exception as exc:  # noqa: BLE001
            out[sym] = {"error": str(exc)[:120]}
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
        print("usage: ta.py SYMBOL | ta.py --market")
        return 2
    if sys.argv[1] == "--market":
        print(json.dumps({"market": market_context()}, indent=2))
        return 0
    symbol = sys.argv[1].upper()
    daily = _fetch_bars(symbol, "1Day", days_back=120, limit=60)
    intra = _fetch_bars(symbol, "5Min", days_back=1, limit=78)
    lv = key_levels(daily)
    ind = local_indicators(symbol)
    out = {"symbol": symbol,
           "indicators": ind,
           "key_levels": lv,
           "candles_daily": candle_tells(daily, lv, ind.get("atr14"), last_n=5),
           "candles_5m_last_hour": candle_tells(intra, lv, ind.get("atr14"), last_n=12),
           "next_earnings": next_earnings(symbol),
           "tradingview": tradingview_rating(symbol)}
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
