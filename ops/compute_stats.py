"""Distill journal/trades.jsonl into journal/stats.json - the hard numbers every
session and review reasons from. No vibes: expectancy, win rate, and P&L broken
down by setup grade, probe status, symbol, and holding time. Recomputed by every
weekly review and available to any session.

Run: <venv python> ops\compute_stats.py [--show]
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "journal" / "trades.jsonl"
OUT = ROOT / "journal" / "stats.json"


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def bucket_stats(trades: list[dict]) -> dict:
    pnls = [_f(t.get("realized_pnl")) for t in trades]
    pnls = [p for p in pnls if p is not None]
    if not pnls:
        return {"n": len(trades), "closed": 0}
    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p <= 0]
    return {
        "n": len(trades), "closed": len(pnls),
        "win_rate_pct": round(100 * len(wins) / len(pnls), 1),
        "total_pnl": round(sum(pnls), 2),
        "avg_win": round(sum(wins) / len(wins), 2) if wins else None,
        "avg_loss": round(sum(losses) / len(losses), 2) if losses else None,
        "expectancy_per_trade": round(sum(pnls) / len(pnls), 2),
        "largest_win": round(max(pnls), 2), "largest_loss": round(min(pnls), 2),
    }


def _band(v, cuts):
    """cuts = [(upper_bound, label), ..., (None, label)] - first bound v is under wins."""
    if v is None:
        return "unknown"
    for bound, label in cuts:
        if bound is None or v < bound:
            return label
    return "unknown"


def _fisher(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact p for the 2x2 table [[a, b], [c, d]]."""
    from math import comb

    r1, c1, n = a + b, a + c, a + b + c + d

    def p(x):
        return comb(c1, x) * comb(n - c1, r1 - x) / comb(n, r1)

    obs = p(a)
    lo, hi = max(0, r1 + c1 - n), min(r1, c1)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs * (1 + 1e-9)))


def _alignment(c: dict) -> str:
    sym, spy = c.get("sym_trend"), c.get("spy_trend")
    if sym == "up":
        return "stock_up+market_up" if spy == "up" else "stock_up+market_not_up"
    if sym == "down":
        return "stock_downtrend"
    return "stock_trend_mixed" if sym else "unknown"


DIMENSIONS = {
    "by_market_trend": lambda c: c.get("spy_trend") or "unknown",
    "by_symbol_trend": lambda c: c.get("sym_trend") or "unknown",
    "by_trend_alignment": lambda c: _alignment(c),
    "by_rel_strength_20d": lambda c: _band(c.get("rel_strength_20d"), [
        (0, "lagging_spy"), (10, "outperforming_0-10pp"), (None, "leader_10pp+")]),
    "by_rsi14_at_entry": lambda c: _band(c.get("rsi14"), [
        (45, "weak_<45"), (60, "neutral_45-60"), (70, "strong_60-70"), (None, "overbought_70+")]),
    "by_extension_above_ema20": lambda c: _band(c.get("ext_ema20_atr"), [
        (1, "near_ema20_<1atr"), (2.5, "moderate_1-2.5atr"), (None, "extended_2.5atr+")]),
    "by_run_from_open": lambda c: _band(c.get("run_from_open_pct"), [
        (0, "below_open"), (3, "up_0-3pct"), (None, "chasing_3pct+")]),
    "by_gap": lambda c: _band(c.get("gap_pct"), [
        (-2, "gap_down_2pct+"), (2, "flat"), (None, "gap_up_2pct+")]),
    "by_entry_time": lambda c: c.get("entry_bucket") or "unknown",
    # Known only after the fact - context for the review, not a pre-trade filter.
    "by_market_during_hold": lambda c: _band(c.get("spy_ret_hold_pct"), [
        (-0.5, "spy_fell_0.5pct+"), (0.5, "spy_flat"), (None, "spy_rose_0.5pct+")]),
}


def trend_stats(closed: list[dict]) -> dict:
    """How the tape at entry, and the path while held, relate to outcome. Reads
    journal/trade_context.json (written by ops/trade_context.py - network-bound,
    run by the review); stays silent about trades it has not measured yet."""
    path = ROOT / "journal" / "trade_context.json"
    try:
        ctx = json.loads(path.read_text(encoding="utf-8")).get("trades", {})
    except (OSError, ValueError):
        return {"trend_context": "journal/trade_context.json missing - run ops/trade_context.py"}
    rows = [(t, ctx[t["trade_id"]]) for t in closed
            if "error" not in ctx.get(t["trade_id"], {"error": 1})
            and _f(t.get("realized_pnl")) is not None]
    if not rows:
        return {"trend_context": "no closed trades measured yet"}

    def by(fn) -> dict:
        groups = defaultdict(list)
        for t, c in rows:
            groups[fn(c)].append(t)
        return {k: bucket_stats(v) for k, v in sorted(groups.items())}

    out = {
        "trend_context_coverage": f"{len(rows)} of {len(closed)} closed trades measured "
                                  "(buckets under ~10 trades are anecdotes, not findings)",
        **{name: by(fn) for name, fn in DIMENSIONS.items()},
    }

    # Which buckets differ from the rest of the book by more than chance? Fisher
    # exact on wins vs losses, with a Sidak threshold over every bucket tested -
    # slicing 30 ways guarantees a few "patterns" that are pure noise.
    tests = []
    total_w = sum(1 for t, _ in rows if _f(t["realized_pnl"]) > 0)
    for dim, buckets in out.items():
        if not dim.startswith("by_"):
            continue
        for label, st in buckets.items():
            n_in = st.get("closed", 0)
            if label == "unknown" or n_in < 5 or len(rows) - n_in < 5:
                continue
            w_in = round(n_in * st["win_rate_pct"] / 100)
            n_out, w_out = len(rows) - n_in, total_w - w_in
            tests.append({"bucket": f"{dim}.{label}", "n": n_in,
                          "win_pct": st["win_rate_pct"],
                          "rest_win_pct": round(100 * w_out / n_out, 1),
                          "total_pnl": st["total_pnl"],
                          "p": round(_fisher(w_in, n_in - w_in, w_out, n_out - w_out), 5)})
    tests.sort(key=lambda r: r["p"])
    sidak = round(1 - 0.95 ** (1 / len(tests)), 5) if tests else None
    out["trend_signals"] = {
        "tests": len(tests), "sidak_p_threshold": sidak,
        "significant": [r for r in tests if sidak and r["p"] < sidak],
        "suggestive_p_under_0.05": [r for r in tests if r["p"] < 0.05 and not (sidak and r["p"] < sidak)],
    }

    # Side-by-side medians: the quickest read of what separated winners from losers.
    feats = ["rel_strength_20d", "rsi14", "ext_ema20_atr", "run_from_open_pct", "gap_pct",
             "below_20d_high_atr", "atr_pct", "spy_ret_5d", "spy_intraday_at_entry_pct",
             "mfe_atr", "mae_atr", "target_progress", "spy_ret_hold_pct", "hold_days"]
    wins = [c for t, c in rows if _f(t["realized_pnl"]) > 0]
    losses = [c for t, c in rows if _f(t["realized_pnl"]) <= 0]

    def med(cs, k):
        vals = sorted(v for v in (c.get(k) for c in cs) if v is not None)
        return round(median(vals), 2) if vals else None

    out["winners_vs_losers_median"] = {
        "n": {"winners": len(wins), "losers": len(losses)},
        **{k: {"winners": med(wins, k), "losers": med(losses, k)} for k in feats},
    }

    # Loss anatomy from the path: did price ever move for the thesis at all?
    anatomy = defaultdict(list)
    for t, c in rows:
        if _f(t["realized_pnl"]) > 0:
            continue
        mfe = c.get("mfe_atr")
        kind = ("never_worked_<0.3atr_favorable" if mfe is not None and mfe < 0.3 else
                "gave_back_1atr+_favorable" if mfe is not None and mfe >= 1.0 else
                "partial_0.3-1atr_favorable" if mfe is not None else "unknown")
        anatomy[kind].append(t)
    out["loss_anatomy"] = {k: {**bucket_stats(v), "trade_ids": [t["trade_id"] for t in v]}
                           for k, v in sorted(anatomy.items())}

    # Exit replay: the same entries under alternative exit rules (trade_context.py
    # replays each on its own 1-min path). Converted to dollars on the trade's
    # entry notional, so it is comparable with realized P&L. A rule that cuts
    # losers also cuts winners - `winners_hurt` keeps that cost visible.
    replay_rows = [(t, c["exit_replay"]) for t, c in rows if c.get("exit_replay")]
    if replay_rows:
        rules = [k for k in replay_rows[0][1] if k != "actual"]
        actual_total = sum(_f(t["realized_pnl"]) for t, _ in replay_rows)
        table = {}
        for rule in rules:
            deltas, hurt, saved = [], 0, 0
            for t, r in replay_rows:
                notional = _f(t.get("entry_notional")) or (
                    (_f(t.get("entry_price")) or 0) * (_f(t.get("entry_qty")) or 0))
                d = (r[rule] - r["actual"]) / 100 * notional
                deltas.append(d)
                if d < -0.005 and _f(t["realized_pnl"]) > 0:
                    hurt += 1
                if d > 0.005 and _f(t["realized_pnl"]) <= 0:
                    saved += 1
            n = len(deltas)
            mean = sum(deltas) / n
            sd = (sum((x - mean) ** 2 for x in deltas) / (n - 1)) ** 0.5 if n > 1 else 0
            table[rule] = {
                "total_pnl": round(actual_total + sum(deltas), 2),
                "delta_vs_actual": round(sum(deltas), 2),
                "trades_changed": sum(1 for x in deltas if abs(x) > 0.005),
                "losers_saved": saved, "winners_hurt": hurt,
                # Paired t on the per-trade dollar difference; |t| under ~2 is noise.
                "paired_t": round(mean / (sd / n ** 0.5), 2) if sd else None,
            }
        out["exit_replay"] = {"n": len(replay_rows), "actual_total_pnl": round(actual_total, 2),
                              "rules": table}

    # Verdict audit: "unlucky" claims a sound thesis. A loss whose price never
    # moved 0.3 ATR in its favor is evidence the entry itself was wrong.
    flags = []
    for t, c in rows:
        mfe = c.get("mfe_atr")
        if (_f(t["realized_pnl"]) <= 0 and t.get("review_verdict") == "unlucky"
                and mfe is not None and mfe < 0.3):
            flags.append({"trade_id": t["trade_id"], "symbol": t.get("symbol"),
                          "realized_pnl": t["realized_pnl"], "mfe_atr": mfe,
                          "mae_atr": c.get("mae_atr")})
    losers_scored = [t for t, _ in rows if _f(t["realized_pnl"]) <= 0 and t.get("review_verdict")]
    out["verdict_audit"] = {
        "losers_scored": len(losers_scored),
        "losers_called_unlucky": sum(1 for t in losers_scored if t["review_verdict"] == "unlucky"),
        "losers_called_wrong": sum(1 for t in losers_scored if t["review_verdict"] == "wrong"),
        "unlucky_but_never_worked": flags,
    }
    return out


def main() -> int:
    trades = []
    if LEDGER.is_file():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            try:
                t = json.loads(line)
            except ValueError:
                continue
            if not t.get("aborted") and not t.get("pending_entry"):
                trades.append(t)
    closed = [t for t in trades if t.get("closed_ts")]

    by_grade = defaultdict(list)
    for t in closed:
        by_grade[str(t.get("setup_grade") or "ungraded")].append(t)
    by_symbol = defaultdict(list)
    for t in closed:
        by_symbol[str(t.get("symbol"))].append(t)

    # Entry mechanism is the head-to-head that decides playbook 7a: does buying a
    # CONFIRMED reclaim beat resting a blind dip-buy limit? Records written before
    # 2026-09-02 predate the field; infer them as anticipatory_limit, which is what
    # they all were.
    def mechanism(t: dict) -> str:
        m = t.get("entry_mechanism")
        if m in ("confirmation_trigger", "anticipatory_limit", "market"):
            return m
        return "anticipatory_limit (inferred, pre-2026-09-02)"

    by_mechanism = defaultdict(list)
    for t in closed:
        by_mechanism[mechanism(t)].append(t)

    # Archetype: is the live record of each setup what its backtest promised?
    # s6a momentum is the desk's only measured edge (+1.96%/trade backtested) and
    # also selects the recent leaders L9 flags - this is where that tension gets
    # settled. Records before 2026-10-02 predate the field; infer from the thesis.
    def archetype(t: dict) -> str:
        a = t.get("archetype")
        if a:
            return str(a)
        th = str(t.get("thesis") or "")
        if re.search(r"s6a|§6a|momentum.continuation", th, re.I):
            return "momentum_s6a (inferred)"
        if re.search(r"\bORB\b|opening.range", th, re.I):
            return "orb_s9 (inferred)"
        if re.search(r"s2a|§2a|support|bounce|pullback|reclaim", th, re.I):
            return "support_bounce_s2a (inferred)"
        return "other (inferred)"

    by_archetype = defaultdict(list)
    for t in closed:
        by_archetype[archetype(t)].append(t)

    verdicts = defaultdict(int)
    for t in closed:
        verdicts[str(t.get("review_verdict") or "unscored")] += 1

    stats = {
        "computed_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "overall": bucket_stats(closed),
        "open_positions": sum(1 for t in trades if not t.get("closed_ts")),
        "by_grade": {g: bucket_stats(ts) for g, ts in sorted(by_grade.items())},
        "by_probe": {"probe": bucket_stats([t for t in closed if t.get("probe")]),
                     "full_size": bucket_stats([t for t in closed if not t.get("probe")])},
        "by_symbol": {s: bucket_stats(ts) for s, ts in sorted(by_symbol.items())},
        "by_entry_mechanism": {m: bucket_stats(ts) for m, ts in sorted(by_mechanism.items())},
        "by_archetype": {a: bucket_stats(ts) for a, ts in sorted(by_archetype.items())},
        "review_verdicts": dict(verdicts),
        # Review debt: every closed trade waiting for a verdict. The review
        # scores ALL of these, however old - a skipped review must not leave
        # trades permanently unlearned-from.
        "unscored_closed": [t["trade_id"] for t in closed if not t.get("review_verdict")],
        "by_exit_reason": {r: bucket_stats([t for t in closed if t.get("exit_reason") == r])
                           for r in sorted({str(t.get("exit_reason")) for t in closed})},
    }
    stats.update(trend_stats(closed))
    OUT.write_text(json.dumps(stats, indent=1), encoding="utf-8")
    print(f"stats over {len(closed)} closed / {len(trades)} total trades -> {OUT}")
    if "--show" in sys.argv:
        print(json.dumps(stats["overall"], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
