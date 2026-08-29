"""Social sentiment sweep: StockTwits + Reddit, for idea discovery only.

Pulls (all public, read-only, fail-soft per source):
  - StockTwits trending symbols (what retail is watching RIGHT NOW)
  - StockTwits per-symbol streams for watch/candidate names -> bull/bear counts
  - Reddit ticker mentions (WSB + investing subs) via ApeWisdom, with 24h rank
    momentum (reddit.com itself 403s unauthenticated scripts)

Output: journal/social.json - an IDEA SOURCE for research sessions, never a
signal. Doctrine: crowd chatter flags names worth running through ta.py and the
news check; it never justifies an entry by itself (see PLAYBOOK s11 - the crowd
is often the exit liquidity). Research-only; no orders here.

Run: <venv python> ops\\social.py [SYM1 SYM2 ...]   (extra syms = stream checks)
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "journal" / "social.json"
UA = {"User-Agent": "paper-desk-research/1.0 (personal paper-trading study)"}

def stocktwits_trending() -> list[dict]:
    import requests

    r = requests.get("https://api.stocktwits.com/api/2/trending/symbols.json",
                     headers=UA, timeout=12)
    r.raise_for_status()
    out = []
    for s in (r.json().get("symbols") or [])[:20]:
        out.append({"symbol": s.get("symbol"), "title": s.get("title"),
                    "watchlist_count": s.get("watchlist_count")})
    return out


def stocktwits_stream(symbol: str) -> dict | None:
    import requests

    try:
        r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json",
                         headers=UA, timeout=12)
        r.raise_for_status()
        msgs = r.json().get("messages") or []
        bull = bear = 0
        for m in msgs:
            s = ((m.get("entities") or {}).get("sentiment") or {}).get("basic")
            if s == "Bullish":
                bull += 1
            elif s == "Bearish":
                bear += 1
        return {"symbol": symbol, "messages_sampled": len(msgs), "bullish": bull,
                "bearish": bear, "unlabeled": len(msgs) - bull - bear}
    except Exception:  # noqa: BLE001 - fail-soft per symbol
        return None


def reddit_sweep() -> list[dict]:
    """Reddit ticker mentions via ApeWisdom (reddit.com 403s unauthenticated
    scripts; ApeWisdom aggregates WSB + investing subs and adds rank momentum)."""
    import html
    import requests

    r = requests.get("https://apewisdom.io/api/v1.0/filter/all-stocks/page/1",
                     headers=UA, timeout=12)
    r.raise_for_status()
    out = []
    for it in (r.json().get("results") or [])[:30]:
        rank, prev = it.get("rank"), it.get("rank_24h_ago")
        out.append({
            "symbol": it.get("ticker"),
            "name": html.unescape(str(it.get("name") or "")),
            "mentions_24h": it.get("mentions"),
            "upvotes": it.get("upvotes"),
            "rank": rank,
            "rank_24h_ago": prev,
            "rank_change": (prev - rank) if isinstance(rank, int) and isinstance(prev, int) else None,
        })
    return out


def main() -> int:
    watch_syms = [a.upper() for a in sys.argv[1:] if a.isalpha()][:12]

    trending: list[dict] = []
    try:
        trending = stocktwits_trending()
    except Exception as exc:  # noqa: BLE001
        print(f"stocktwits trending failed (fail-soft): {exc}")

    # sentiment streams: explicit syms + top trending
    stream_syms = list(dict.fromkeys(watch_syms + [t["symbol"] for t in trending[:8]
                                                   if t.get("symbol")]))[:14]
    streams = [s for s in (stocktwits_stream(sym) for sym in stream_syms) if s]

    reddit_top: list[dict] = []
    try:
        reddit_top = reddit_sweep()
    except Exception as exc:  # noqa: BLE001
        print(f"reddit (apewisdom) failed (fail-soft): {exc}")

    climbers = sorted((r for r in reddit_top if (r.get("rank_change") or 0) > 0),
                      key=lambda r: r["rank_change"], reverse=True)[:10]

    payload = {
        "ts": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "doctrine": "idea source only - names here get ta.py + news vetting like any "
                    "other candidate; crowd hype is never a thesis (PLAYBOOK s11)",
        "stocktwits_trending": trending,
        "stocktwits_sentiment": streams,
        "reddit_mentions": reddit_top,
        "reddit_rank_climbers": climbers,
    }
    OUT.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    print(f"social: {len(trending)} trending, {len(streams)} sentiment streams, "
          f"{len(reddit_top)} reddit tickers -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
