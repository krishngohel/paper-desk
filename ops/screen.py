"""Whole-US-market screener: sweep ~10k listed stocks, rank a tradable shortlist.

Primary sweep: TradingView's scanner (one request covers the whole US market;
unofficial - fail-soft). Fallback: Alpaca's screener endpoints (movers + most
actives). Output: journal/universe_scan.json - the ranked candidate list every
session reads. Research-only; no orders here.

Ranking favors what a day-trading long can actually use: liquid names moving
TODAY on above-normal volume. Illiquid microcaps produce garbage fills and
garbage training data, so a liquidity floor applies to the SHORTLIST - the
model may still research/trade ANY symbol it names via ta.py; this file is
discovery, not permission.

Run: <venv python> ops\\screen.py [--show]
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "journal" / "universe_scan.json"

MIN_PRICE = 2.0
MIN_DOLLAR_VOLUME = 20_000_000  # today, $
SHORTLIST = 40


def tv_sweep() -> list[dict] | None:
    """One scanner request over the full US market; rows ranked by |change| and
    relative volume. Returns None when the unofficial endpoint fails."""
    try:
        import requests

        cols = ["name", "close", "change", "volume", "relative_volume_10d_calc",
                "market_cap_basic", "exchange"]
        body = {
            "filter": [
                {"left": "exchange", "operation": "in_range", "right": ["NASDAQ", "NYSE", "AMEX"]},
                {"left": "is_primary", "operation": "equal", "right": True},
                {"left": "type", "operation": "in_range", "right": ["stock", "fund"]},
                {"left": "close", "operation": "greater", "right": MIN_PRICE},
                {"left": "active_symbol", "operation": "equal", "right": True},
            ],
            "columns": cols,
            "sort": {"sortBy": "volume", "sortOrder": "desc"},
            "range": [0, 900],
        }
        r = requests.post("https://scanner.tradingview.com/america/scan", json=body, timeout=15)
        r.raise_for_status()
        rows = []
        for item in r.json().get("data") or []:
            d = dict(zip(cols, item["d"]))
            close, vol = d.get("close"), d.get("volume")
            if not close or not vol or close * vol < MIN_DOLLAR_VOLUME:
                continue
            rows.append({
                "symbol": str(d.get("name", "")).split(":")[-1],
                "close": round(float(close), 2),
                "change_pct": round(float(d.get("change") or 0), 2),
                "dollar_volume_m": round(close * vol / 1e6, 1),
                "rel_volume": round(float(d.get("relative_volume_10d_calc") or 0), 2),
                "market_cap_b": round(float(d.get("market_cap_basic") or 0) / 1e9, 2),
                "exchange": d.get("exchange"),
            })
        return rows
    except Exception:  # noqa: BLE001 - unofficial endpoint, fail-soft
        return None


def alpaca_fallback() -> list[dict]:
    """Alpaca screener endpoints: movers + most-actives (smaller net, official)."""
    sys.path.insert(0, str(ROOT / "Vibe-Trading" / "agent"))
    import os

    os.chdir(ROOT / "Vibe-Trading")
    from src.trading.connectors.alpaca import sdk
    import requests

    cfg = sdk.load_config()
    headers = {"APCA-API-KEY-ID": cfg.api_key, "APCA-API-SECRET-KEY": cfg.secret_key}
    rows: dict[str, dict] = {}
    try:
        r = requests.get("https://data.alpaca.markets/v1beta1/screener/stocks/most-actives?by=volume&top=50",
                         headers=headers, timeout=10)
        for it in (r.json().get("most_actives") or []):
            rows[it["symbol"]] = {"symbol": it["symbol"], "dollar_volume_m": None,
                                  "change_pct": None, "source": "most_active"}
    except Exception:  # noqa: BLE001
        pass
    try:
        r = requests.get("https://data.alpaca.markets/v1beta1/screener/stocks/movers?top=50",
                         headers=headers, timeout=10)
        j = r.json()
        for it in (j.get("gainers") or []):  # long-only book: gainers only
            rows[it["symbol"]] = {"symbol": it["symbol"], "change_pct": it.get("percent_change"),
                                  "close": it.get("price"), "source": "gainer"}
    except Exception:  # noqa: BLE001
        pass
    return list(rows.values())


def main() -> int:
    rows = tv_sweep()
    source = "tradingview_full_market"
    if rows is None:
        rows = alpaca_fallback()
        source = "alpaca_screener_fallback"

    if rows and source == "tradingview_full_market":
        movers = sorted(rows, key=lambda r: abs(r.get("change_pct") or 0), reverse=True)[:25]
        unusual = sorted(rows, key=lambda r: r.get("rel_volume") or 0, reverse=True)[:25]
        liquid = sorted(rows, key=lambda r: r.get("dollar_volume_m") or 0, reverse=True)[:15]
        seen, shortlist = set(), []
        for r in movers + unusual + liquid:
            if r["symbol"] not in seen:
                seen.add(r["symbol"])
                shortlist.append(r)
        shortlist = shortlist[:SHORTLIST]
        universe_size = len(rows)
    else:
        shortlist = rows[:SHORTLIST]
        universe_size = len(rows)

    payload = {"ts": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), "source": source,
               "screened_liquid_names": universe_size,
               "filters": {"min_price": MIN_PRICE, "min_dollar_volume": MIN_DOLLAR_VOLUME},
               "shortlist": shortlist}
    OUT.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    print(f"scan: {source}, {universe_size} liquid names screened, top {len(shortlist)} shortlisted -> {OUT}")
    if "--show" in sys.argv:
        for r in shortlist[:12]:
            print(r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
