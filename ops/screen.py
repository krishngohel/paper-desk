"""Whole-US-market screener: sweep every listing the broker can trade, rank lenses.

Primary sweep: TradingView's scanner (one request covers the whole US market -
NASDAQ, NYSE, AMEX/Arca, Cboe, OTC; stocks, ETFs, ADRs; unofficial, fail-soft).
Fallback: Alpaca's screener endpoints (movers + most actives). Output:
journal/universe_scan.json - the ranked candidate lenses every session reads -
plus ops/cache/universe_full.json, EVERY listing with its numbers (look a
symbol up there; it is too big to read whole). Research-only; no orders here.

NOTHING IS SCREENED OUT (operator rule 2026-09-24). No price floor, no volume
floor, no market-cap band, no sector or type exclusion. The only thing that
keeps a listing off the lenses is that Alpaca cannot execute it at all
(`tradable: false` in its asset list) - and even those stay in the full file,
flagged. Lenses RANK, they never exclude: a name absent from the shortlist is
still a candidate, and ta.py's measured spread (playbook s7b) is where
tradability gets judged, per symbol, with a number.

Run: <venv python> ops\\screen.py [--show] [--mode <explore lens>]
"""

from __future__ import annotations

import json
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "journal" / "universe_scan.json"
FULL = ROOT / "ops" / "cache" / "universe_full.json"
TRADABLE_CACHE = ROOT / "ops" / "cache" / "alpaca_tradable.json"

LENS_SIZE = 15  # per shortlist lens; lenses are deduped, so the shortlist is <= 5x this

COLS = ["name", "close", "change", "volume", "relative_volume_10d_calc",
        "market_cap_basic", "exchange", "Value.Traded", "Perf.1M", "type"]


def _row(d: dict) -> dict:
    close, vol = d.get("close") or 0, d.get("volume") or 0
    cap = d.get("market_cap_basic")
    return {
        "symbol": str(d.get("name", "")).split(":")[-1],
        "close": round(float(close), 2),
        "change_pct": round(float(d.get("change") or 0), 2),
        "perf_1m_pct": round(float(d["Perf.1M"]), 1) if d.get("Perf.1M") is not None else None,
        "dollar_volume_m": round(close * vol / 1e6, 1),
        "rel_volume": round(float(d.get("relative_volume_10d_calc") or 0), 2),
        "market_cap_b": round(float(cap) / 1e9, 2) if cap else None,
        "exchange": d.get("exchange"),
        "type": d.get("type"),
    }


def tv_universe() -> list[dict] | None:
    """Every primary US listing in one scanner request. None when the
    unofficial endpoint fails."""
    try:
        import requests

        body = {
            "filter": [
                {"left": "exchange", "operation": "in_range",
                 "right": ["NASDAQ", "NYSE", "AMEX", "CBOE", "OTC"]},
                {"left": "is_primary", "operation": "equal", "right": True},
                {"left": "active_symbol", "operation": "equal", "right": True},
            ],
            "columns": COLS,
            "sort": {"sortBy": "Value.Traded", "sortOrder": "desc"},
            "range": [0, 40000],
        }
        r = requests.post("https://scanner.tradingview.com/america/scan", json=body, timeout=60)
        r.raise_for_status()
        return [_row(dict(zip(COLS, item["d"]))) for item in r.json().get("data") or []]
    except Exception:  # noqa: BLE001 - unofficial endpoint, fail-soft
        return None


def _alpaca_headers() -> dict:
    sys.path.insert(0, str(ROOT / "Vibe-Trading" / "agent"))
    import os

    os.chdir(ROOT / "Vibe-Trading")
    from src.trading.connectors.alpaca import sdk

    cfg = sdk.load_config()
    return {"APCA-API-KEY-ID": cfg.api_key, "APCA-API-SECRET-KEY": cfg.secret_key}


def alpaca_tradable() -> set[str] | None:
    """Symbols Alpaca can execute, refreshed once a day. None when unknown -
    then nothing is dropped."""
    today = date.today().isoformat()
    try:
        cached = json.loads(TRADABLE_CACHE.read_text(encoding="utf-8"))
        if cached.get("date") == today:
            return set(cached["symbols"])
    except Exception:  # noqa: BLE001
        pass
    try:
        import requests

        r = requests.get("https://paper-api.alpaca.markets/v2/assets?status=active&asset_class=us_equity",
                         headers=_alpaca_headers(), timeout=30)
        r.raise_for_status()
        syms = sorted(a["symbol"] for a in r.json() if a.get("tradable"))
        TRADABLE_CACHE.parent.mkdir(parents=True, exist_ok=True)
        TRADABLE_CACHE.write_text(json.dumps({"date": today, "symbols": syms}), encoding="utf-8")
        return set(syms)
    except Exception:  # noqa: BLE001
        return None


def alpaca_fallback() -> list[dict]:
    """Alpaca screener endpoints: movers + most-actives (smaller net, official)."""
    import requests

    headers = _alpaca_headers()
    rows: dict[str, dict] = {}
    try:
        r = requests.get("https://data.alpaca.markets/v1beta1/screener/stocks/most-actives?by=volume&top=100",
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


def _top(rows: list[dict], key, n: int, where=None) -> list[dict]:
    pool = [r for r in rows if where is None or where(r)]
    return sorted(pool, key=lambda r: key(r) or 0, reverse=True)[:n]


# Shortlist lenses: every one gets its own guaranteed slots, so a heavily
# traded leader (META on 2026-09-24: $27B traded, +38% in a month) can never be
# crowded out by the day's percentage movers again.
SHORTLIST_LENSES = {
    "movers":  lambda rows: _top(rows, lambda r: abs(r["change_pct"]), LENS_SIZE),
    "unusual": lambda rows: _top(rows, lambda r: r["rel_volume"], LENS_SIZE),
    "liquid":  lambda rows: _top(rows, lambda r: r["dollar_volume_m"], LENS_SIZE),
    "leaders": lambda rows: _top(rows, lambda r: r["perf_1m_pct"], LENS_SIZE),
    # the raw 1-month list is all sub-$1B rockets; rank the 500 largest
    # companies separately so a mega-cap trend is always in view
    "big_leaders": lambda rows: _top(_top(rows, lambda r: r["market_cap_b"], 500),
                                     lambda r: r["perf_1m_pct"], LENS_SIZE),
}

# Rotating exploration lenses so the desk keeps seeing new corners of the
# market. They rank the same full universe differently; none excludes anything.
EXPLORE_MODES = {
    "gainers":  {"desc": "biggest % gainers today",
                 "pick": lambda rows: _top(rows, lambda r: r["change_pct"], 25)},
    "relvol":   {"desc": "most unusual volume vs 10d norm - something is happening",
                 "pick": lambda rows: _top(rows, lambda r: r["rel_volume"], 25)},
    "smallcap": {"desc": "biggest % movers under $2B market cap",
                 "pick": lambda rows: _top(rows, lambda r: r["change_pct"], 25,
                                           lambda r: r["market_cap_b"] is not None and r["market_cap_b"] < 2)},
    "megacap":  {"desc": "the 25 largest companies, ranked by today's move",
                 "pick": lambda rows: sorted(_top(rows, lambda r: r["market_cap_b"], 25),
                                             key=lambda r: r["change_pct"], reverse=True)},
    "turnover": {"desc": "heavily-traded names ALSO moving 3%+ today",
                 "pick": lambda rows: _top(rows, lambda r: r["dollar_volume_m"], 25,
                                           lambda r: r["change_pct"] >= 3)},
}


def main() -> int:
    universe = tv_universe()
    source = "tradingview_full_market"
    if universe is None:
        universe = alpaca_fallback()
        source = "alpaca_screener_fallback"

    tradable = alpaca_tradable()
    for r in universe:
        r["tradable"] = None if tradable is None else r["symbol"] in tradable
    rows = [r for r in universe if r["tradable"] is not False]

    modes = list(EXPLORE_MODES)
    mode = None
    if "--mode" in sys.argv:
        want = sys.argv[sys.argv.index("--mode") + 1]
        mode = want if want in EXPLORE_MODES else None
    if mode is None:
        mode = modes[datetime.now().hour % len(modes)]

    if source == "tradingview_full_market":
        seen, shortlist = set(), []
        for lens, pick in SHORTLIST_LENSES.items():
            for r in pick(rows):
                if r["symbol"] not in seen:
                    seen.add(r["symbol"])
                    shortlist.append({**r, "lens": lens})
        explore = EXPLORE_MODES[mode]["pick"](rows)
    else:
        shortlist, explore = rows, []

    known = {r["symbol"] for r in shortlist}
    fresh = [r for r in explore if r["symbol"] not in known]
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    payload = {"ts": ts, "source": source,
               "universe_listings": len(universe),
               "broker_tradable": len(rows),
               "not_broker_tradable": sum(1 for r in universe if r["tradable"] is False),
               "filters": "none - every broker-tradable listing is ranked; lenses rank, never exclude",
               "full_universe_file": str(FULL.relative_to(ROOT)),
               "shortlist": shortlist,
               "explore": {"mode": mode, "desc": EXPLORE_MODES[mode]["desc"],
                           "new_names_not_on_shortlist": fresh, "all": explore}}
    OUT.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    FULL.parent.mkdir(parents=True, exist_ok=True)
    FULL.write_text(json.dumps({"ts": ts, "source": source, "rows": universe}), encoding="utf-8")
    print(f"scan: {source}, {len(universe)} listings ({len(rows)} broker-tradable), "
          f"{len(shortlist)} shortlisted across {len(SHORTLIST_LENSES)} lenses, "
          f"explore[{mode}] found {len(fresh)} fresh names -> {OUT}")
    if "--show" in sys.argv:
        for r in shortlist:
            print(r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
