"""Reconstruct the market/trend context of every filled trade, and the path price
took while it was held, into journal/trade_context.json.

The ledger records what a session THOUGHT at entry. This records what the tape
actually looked like - measured the same way for every trade, so winners and
losers can be compared on equal terms:

  market  : SPY daily trend (close vs EMA20/EMA50), SPY 5d/20d return, SPY's
            intraday move at the entry moment
  symbol  : daily trend, 20d return, relative strength vs SPY, RSI14, ATR%,
            extension above EMA20 in ATRs, distance below the 20d high, the
            entry day's gap, and how far it had already run from the open
  timing  : entry time-of-day bucket (ET)
  path    : max favorable / adverse excursion while held (in % and in ATRs),
            share of the target distance reached, SPY's move over the hold
  replay  : what each closed trade would have returned under alternative exit
            rules (breakeven / trailing stops, half off at +1 ATR) on the same path

Daily indicators use only bars that CLOSED before the entry day - no lookahead.
Path metrics use 1-min SIP bars from the entry minute to the exit.

compute_stats.py folds this file into stats.json (by_market_trend,
by_symbol_trend, winners_vs_losers, loss_anatomy, verdict_audit...). It is
network-bound, so snapshots never run it; the review runs it first.

Run: <venv python> ops\\trade_context.py [--refresh]   (--refresh recomputes all)
     <venv python> ops\\trade_context.py --check SYM PRICE
         pre-trade: measures a candidate entry the same way and names every
         trend bucket it falls in, with that bucket's record from stats.json.
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median

sys.path.insert(0, str(Path(__file__).parent))
import bt_data  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "journal" / "trades.jsonl"
OUT = ROOT / "journal" / "trade_context.json"
BARS = bt_data.CACHE / "trade_context"
VERSION = 3  # 3: exit_replay
CT = timezone(timedelta(hours=-5))  # the desk writes naive stamps in CDT
ET = timezone(timedelta(hours=-4))


# ---------------------------------------------------------------- timestamps

_ISO = re.compile(r"(\d{4}-\d{2}-\d{2})(?:[T ]~?(\d{2}):(\d{2})(?::(\d{2})(?:\.\d+)?)?)?\s*(Z|[+-]\d{2}:\d{2})?")


def parse_ts(raw) -> tuple[datetime | None, bool]:
    """Ledger stamps come in every shape: ISO with offset, ISO Z, naive (CT),
    '2026-09-15T~08:34 CT (...)', bare dates with prose. Returns (utc, approx)."""
    if not raw:
        return None, True
    s = str(raw)
    m = _ISO.search(s)
    if not m:
        return None, True
    day, hh, mm, ss, tz = m.groups()
    approx = len(s) > 32 or "~" in s or "approx" in s.lower() or "x" in s[11:16]
    if hh is None:
        # date only: the fill was a resting order, assume it printed at the open
        hh, mm, ss, approx = "08", "30", "00", True
    dt = datetime.fromisoformat(f"{day}T{hh}:{mm}:{ss or '00'}")
    if tz == "Z":
        dt = dt.replace(tzinfo=timezone.utc)
    elif tz:
        sign = 1 if tz[0] == "+" else -1
        dt = dt.replace(tzinfo=timezone(sign * timedelta(hours=int(tz[1:3]), minutes=int(tz[4:6]))))
    else:
        dt = dt.replace(tzinfo=CT)
    return dt.astimezone(timezone.utc), approx


# ---------------------------------------------------------------- bars

def _fetch(symbol: str, timeframe: str, start: datetime, end: datetime) -> list[dict]:
    """Oldest-first SIP bars for an explicit window, cached forever (the past
    does not change)."""
    # SIP rejects windows that reach into the last ~15 minutes.
    end = min(end, datetime.now(timezone.utc) - timedelta(minutes=bt_data.SIP_LAG_MIN))
    key = f"{symbol}_{timeframe}_{start:%Y%m%d%H%M}_{end:%Y%m%d%H%M}.json"
    path = BARS / key
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    import requests

    cfg = bt_data._config()
    hdr = {"APCA-API-KEY-ID": cfg.api_key, "APCA-API-SECRET-KEY": cfg.secret_key}
    out, token = [], None
    for _ in range(20):
        url = (f"{bt_data.DATA}/v2/stocks/{symbol}/bars?timeframe={timeframe}"
               f"&start={start:%Y-%m-%dT%H:%M:%SZ}&end={end:%Y-%m-%dT%H:%M:%SZ}"
               f"&limit=10000&feed=sip&adjustment=split")
        if token:
            url += f"&page_token={token}"
        r = requests.get(url, headers=hdr, timeout=30)
        if not r.ok:
            return []
        j = r.json()
        out += [{"t": b["t"], "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]}
                for b in j.get("bars") or []]
        token = j.get("next_page_token")
        if not token:
            break
        time.sleep(0.05)
    out.sort(key=lambda b: b["t"])
    # Only cache windows that are fully in the past (SIP lag), so a partial day
    # is never frozen into the cache.
    if out and end < datetime.now(timezone.utc) - timedelta(minutes=bt_data.SIP_LAG_MIN):
        BARS.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(out), encoding="utf-8")
    return out


def _t(b) -> datetime:
    return datetime.fromisoformat(b["t"].replace("Z", "+00:00"))


# ---------------------------------------------------------------- indicators

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
    gains = [max(b - a, 0.0) for a, b in zip(vals[:-1], vals[1:])]
    losses = [max(a - b, 0.0) for a, b in zip(vals[:-1], vals[1:])]
    ag, al = sum(gains[:n]) / n, sum(losses[:n]) / n
    for g, l in zip(gains[n:], losses[n:]):
        ag, al = (ag * (n - 1) + g) / n, (al * (n - 1) + l) / n
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def _atr(bars, n=14):
    if len(bars) < n + 1:
        return None
    trs, pc = [], bars[0]["c"]
    for b in bars[1:]:
        trs.append(max(b["h"] - b["l"], abs(b["h"] - pc), abs(b["l"] - pc)))
        pc = b["c"]
    a = sum(trs[:n]) / n
    for tr in trs[n:]:
        a = (a * (n - 1) + tr) / n
    return a


def _trend(closes) -> str | None:
    """up = close > EMA20 > EMA50; down = close < EMA20 < EMA50; else mixed.
    Young listings without 50 bars use close vs EMA20 and EMA20's 5-bar slope."""
    e20, e50 = _ema(closes, 20), _ema(closes, 50)
    if e20 is None:
        return None
    c = closes[-1]
    if e50 is None:
        e20_prev = _ema(closes[:-5], 20)
        if e20_prev is None:
            return None
        e50 = e20_prev  # slope proxy: rising EMA20 reads like EMA20 > EMA50
    if c > e20 > e50:
        return "up"
    if c < e20 < e50:
        return "down"
    return "mixed"


def _ret(closes, n):
    return round(100 * (closes[-1] / closes[-1 - n] - 1), 2) if len(closes) > n else None


def _r(v, d=2):
    return None if v is None else round(v, d)


# ---------------------------------------------------------------- exit replay

def exit_replay(path: list[dict], entry: float, atr: float, actual_ret: float) -> dict:
    """Return (%) the trade would have made under alternative exit rules, replayed
    on the same 1-min path. Each rule only ADDS an earlier exit: if it never fires,
    the trade keeps its actual exit. A rule arms on the bar whose high reaches the
    threshold and is checked from the NEXT bar (no same-bar guessing); a bar that
    opens below the stop fills at its open, as a real stop would."""
    out = {"actual": _r(actual_ret)}

    def stop_rule(arm_atr: float, trail_atr: float | None) -> float:
        armed, peak = False, entry
        for b in path:
            if armed:
                stop = entry if trail_atr is None else max(entry, peak - trail_atr * atr)
                if b["l"] <= stop:
                    return 100 * (min(stop, b["o"]) / entry - 1)
            peak = max(peak, b["h"])
            if peak >= entry + arm_atr * atr:
                armed = True
        return actual_ret

    out["breakeven_after_0.5atr"] = _r(stop_rule(0.5, None))
    out["breakeven_after_1atr"] = _r(stop_rule(1.0, None))
    out["trail_1atr_after_1atr"] = _r(stop_rule(1.0, 1.0))
    hit = any(b["h"] >= entry + atr for b in path)
    out["half_off_at_1atr"] = _r(0.5 * 100 * atr / entry + 0.5 * actual_ret if hit else actual_ret)
    return out


# ---------------------------------------------------------------- per trade

def context_for(t: dict) -> dict:
    sym = str(t["symbol"]).upper()
    entry = float(t["entry_price"])
    t_in, in_approx = parse_ts(t.get("opened_ts"))
    t_out, out_approx = parse_ts(t.get("closed_ts"))
    if t_in is None:
        return {"error": "unparseable opened_ts"}
    entry_day = t_in.astimezone(ET).date()
    day_open_utc = datetime.combine(entry_day, datetime.min.time(), ET).astimezone(timezone.utc)

    d_start = day_open_utc - timedelta(days=130)
    sym_d = _fetch(sym, "1Day", d_start, day_open_utc + timedelta(days=1))
    spy_d = _fetch("SPY", "1Day", d_start, day_open_utc + timedelta(days=1))
    prior = [b for b in sym_d if _t(b).astimezone(ET).date() < entry_day]
    spy_prior = [b for b in spy_d if _t(b).astimezone(ET).date() < entry_day]
    today = next((b for b in sym_d if _t(b).astimezone(ET).date() == entry_day), None)
    if len(prior) < 26 or len(spy_prior) < 55:
        return {"error": f"not enough daily history ({len(prior)} bars)"}

    c = [b["c"] for b in prior]
    sc = [b["c"] for b in spy_prior]
    atr = _atr(prior)
    e20 = _ema(c, 20)
    hi20 = max(b["h"] for b in prior[-20:])
    sym20, spy20 = _ret(c, 20), _ret(sc, 20)

    et_in = t_in.astimezone(ET)
    mins = et_in.hour * 60 + et_in.minute
    if in_approx and et_in.strftime("%H:%M") == "09:30":
        bucket = "open_resting_fill"
    elif mins < 9 * 60 + 30:
        bucket = "premarket"
    elif mins < 10 * 60 + 30:
        bucket = "first_hour"
    elif mins < 14 * 60:
        bucket = "midday"
    else:
        bucket = "late_day"

    ctx = {
        "v": VERSION, "symbol": sym, "entry_utc": t_in.isoformat(), "entry_ts_approx": in_approx,
        "entry_bucket": bucket,
        "spy_trend": _trend(sc), "spy_ret_5d": _ret(sc, 5), "spy_ret_20d": spy20,
        "sym_trend": _trend(c), "sym_ret_20d": sym20,
        "rel_strength_20d": _r(sym20 - spy20) if sym20 is not None and spy20 is not None else None,
        "rsi14": _r(_rsi(c), 1),
        "atr_pct": _r(100 * atr / c[-1]) if atr else None,
        "ext_ema20_atr": _r((entry - e20) / atr) if atr and e20 else None,
        "below_20d_high_atr": _r((hi20 - entry) / atr) if atr else None,
        "gap_pct": _r(100 * (today["o"] / c[-1] - 1)) if today else None,
        "run_from_open_pct": _r(100 * (entry / today["o"] - 1)) if today else None,
    }

    # SPY's move from the prior close to the entry moment (intraday tide).
    spy_i = _fetch("SPY", "15Min", day_open_utc, t_in + timedelta(minutes=15))
    upto = [b for b in spy_i if _t(b) <= t_in]
    if upto:
        ctx["spy_intraday_at_entry_pct"] = _r(100 * (upto[-1]["c"] / sc[-1] - 1))

    # Path while held, on 1-min bars from the entry minute. Open trades are
    # measured up to now.
    lag = datetime.now(timezone.utc) - timedelta(minutes=bt_data.SIP_LAG_MIN)
    end = min(t_out or lag, lag)
    t0 = t_in.replace(second=0, microsecond=0)
    path: list[dict] = []
    if end > t_in:
        path = [b for b in _fetch(sym, "1Min", t0, end + timedelta(minutes=1))
                if t0 <= _t(b) <= end]
        spy_p = [b for b in _fetch("SPY", "1Min", t0, end + timedelta(minutes=1))
                 if t0 <= _t(b) <= end]
        if path:
            hi, lo = max(b["h"] for b in path), min(b["l"] for b in path)
            ctx["mfe_pct"] = _r(100 * (hi / entry - 1))
            ctx["mae_pct"] = _r(100 * (lo / entry - 1))
            if atr:
                ctx["mfe_atr"] = _r((hi - entry) / atr)
                ctx["mae_atr"] = _r((entry - lo) / atr)
            tgt = t.get("target")
            try:
                tgt = float(tgt)
            except (TypeError, ValueError):
                tgt = None
            if tgt and tgt > entry:
                ctx["target_progress"] = _r(min((hi - entry) / (tgt - entry), 1.5))
        if len(spy_p) >= 2:
            ctx["spy_ret_hold_pct"] = _r(100 * (spy_p[-1]["c"] / spy_p[0]["o"] - 1))
    exit_px = t.get("exit_price")
    if exit_px is not None and t.get("closed_ts"):
        ret = 100 * (float(exit_px) / entry - 1)
        ctx["ret_pct"] = _r(ret)
        if path and atr:
            ctx["exit_replay"] = exit_replay(path, entry, atr, ret)
        if "spy_ret_hold_pct" in ctx:
            ctx["excess_vs_spy_pct"] = _r(ret - ctx["spy_ret_hold_pct"])
        ctx["hold_days"] = _r((t_out - t_in).total_seconds() / 86400, 1) if t_out else None
        ctx["exit_ts_approx"] = out_approx
    ctx["closed"] = bool(t.get("closed_ts"))
    return ctx


def filled(t: dict) -> bool:
    return (not t.get("aborted") and not t.get("pending_entry")
            and t.get("entry_price") is not None and t.get("opened_ts"))


def check(symbol: str, price: float) -> int:
    """Classify a live candidate into the same buckets the review measures."""
    import compute_stats

    now = datetime.now(timezone.utc)
    c = context_for({"symbol": symbol, "entry_price": price, "opened_ts": now.isoformat()})
    if "error" in c:
        print(json.dumps(c))
        return 1
    for k in ("mfe_pct", "mae_pct", "mfe_atr", "mae_atr", "target_progress", "spy_ret_hold_pct"):
        c.pop(k, None)
    try:
        stats = json.loads(compute_stats.OUT.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        stats = {}
    sig = stats.get("trend_signals", {})
    flagged = {r["bucket"]: "suggestive" for r in sig.get("suggestive_p_under_0.05", [])}
    flagged.update({r["bucket"]: "SIGNIFICANT" for r in sig.get("significant", [])})
    buckets = []
    for dim, fn in compute_stats.DIMENSIONS.items():
        if dim == "by_market_during_hold":  # only knowable after the exit
            continue
        label = fn(c)
        rec = stats.get(dim, {}).get(label, {})
        buckets.append({"bucket": f"{dim}.{label}", "closed": rec.get("closed", 0),
                        "win_pct": rec.get("win_rate_pct"), "total_pnl": rec.get("total_pnl"),
                        "signal": flagged.get(f"{dim}.{label}")})
    print(json.dumps({"symbol": symbol.upper(), "price": price, "context": c,
                      "buckets": buckets}, indent=1))
    return 0


def main() -> int:
    if "--check" in sys.argv:
        i = sys.argv.index("--check")
        return check(sys.argv[i + 1], float(sys.argv[i + 2]))
    refresh = "--refresh" in sys.argv
    trades = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        try:
            trades.append(json.loads(line))
        except ValueError:
            continue
    old = {}
    if OUT.is_file() and not refresh:
        try:
            old = json.loads(OUT.read_text(encoding="utf-8")).get("trades", {})
        except ValueError:
            old = {}
    out, n_new, errors = {}, 0, []
    for t in trades:
        if not filled(t):
            continue
        tid = t["trade_id"]
        prev = old.get(tid)
        # A closed trade's context is final; open trades are re-measured each run.
        if prev and prev.get("v") == VERSION and prev.get("closed") and "error" not in prev:
            out[tid] = prev
            continue
        try:
            out[tid] = context_for(t)
            n_new += 1
        except Exception as exc:  # noqa: BLE001 - one bad record must not sink the file
            out[tid] = {"error": f"{type(exc).__name__}: {exc}"}
        if "error" in out[tid]:
            errors.append(f"{tid}: {out[tid]['error']}")
    OUT.write_text(json.dumps({"computed_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                               "trades": out}, indent=1), encoding="utf-8")
    print(f"trade context: {len(out)} filled trades ({n_new} measured this run) -> {OUT}")
    for e in errors:
        print("  ERROR", e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
