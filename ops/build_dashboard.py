"""Build ops/dashboard.html from the journal - stdlib only, deterministic.

Inputs (all optional; the page renders sensibly when empty):
  journal/performance.jsonl  one line per session: ts, session, equity, cash, positions_value, voo_price
  journal/trades.jsonl       trade ledger (open = closed_ts null and not aborted)
  journal/lessons.md         Active-section rules
  journal/YYYY-MM.md         narrative entries (## headers), newest months last
  mandate.json               path from TRADING_MANDATE_PATH env or ~/.vibe-trading/live/alpaca/mandate.json

Run: python ops/build_dashboard.py   (from anywhere; paths resolve relative to this file)
"""

from __future__ import annotations

import html
import json
import math
import os
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOURNAL = ROOT / "journal"
OUT = ROOT / "ops" / "dashboard.html"

SESSION_SLOTS = [
    "8:45", "9:15", "9:45", "10:15", "10:45", "11:15", "11:45",
    "12:15", "12:45", "13:15", "13:45", "14:15", "14:30",
]
START_EQUITY = 100_000.0
BENCH_STAKE = 1_000.0


def _read_jsonl(path: Path) -> list[dict]:
    rows = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows


def _mandate() -> dict | None:
    p = Path(os.environ.get("TRADING_MANDATE_PATH") or Path.home() / ".vibe-trading" / "live" / "alpaca" / "mandate.json")
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _lessons() -> list[str]:
    p = JOURNAL / "lessons.md"
    if not p.is_file():
        return []
    text = p.read_text(encoding="utf-8")
    active = text.split("## Active", 1)[-1].split("## Archive", 1)[0]
    return [m.strip() for m in re.findall(r"^- \*\*(.+?)\*\*", active, re.M)]


def _entries(limit: int = 10) -> list[tuple[str, str]]:
    """(header, body-first-lines) for the newest narrative entries across month files."""
    out: list[tuple[str, str]] = []
    for month_file in sorted(JOURNAL.glob("2*.md"), reverse=True):
        parts = re.split(r"^## ", month_file.read_text(encoding="utf-8"), flags=re.M)
        for chunk in reversed(parts[1:]):
            lines = chunk.strip().splitlines()
            if not lines:
                continue
            out.append((lines[0].strip(), "\n".join(lines[1:8]).strip()))
            if len(out) >= limit:
                return out
    return out


def _fmt_money(v: float) -> str:
    return f"${v:,.2f}"


def _pct(v: float) -> str:
    return f"{v:+.2f}%"


def _series(perf: list[dict]) -> tuple[list[tuple[str, float]], list[tuple[str, float]]]:
    """Return (agent %, VOO %) return-since-inception series, indexed to 0."""
    agent, voo = [], []
    voo0 = next((r["voo_price"] for r in perf if r.get("voo_price")), None)
    for r in perf:
        ts = str(r.get("ts", ""))[:16]
        eq = r.get("equity")
        if isinstance(eq, (int, float)):
            agent.append((ts, (eq / START_EQUITY - 1.0) * 100.0))
        vp = r.get("voo_price")
        if voo0 and isinstance(vp, (int, float)):
            voo.append((ts, (vp / voo0 - 1.0) * 100.0))
    return agent, voo


def _polyline(series: list[tuple[str, float]], lo: float, hi: float, w: int, h: int) -> str:
    if len(series) < 2:
        return ""
    span = (hi - lo) or 1.0
    pts = []
    for i, (_, v) in enumerate(series):
        x = 8 + i * (w - 16) / (len(series) - 1)
        y = 8 + (h - 16) * (1 - (v - lo) / span)
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def _chart(perf: list[dict]) -> str:
    agent, voo = _series(perf)
    w, h = 840, 260
    if len(agent) < 2:
        return '<div class="empty">No sessions recorded yet. The curve starts with the first trading session.</div>'
    vals = [v for _, v in agent + voo]
    lo, hi = min(vals + [0.0]), max(vals + [0.0])
    pad = (hi - lo) * 0.1 or 0.5
    lo, hi = lo - pad, hi + pad
    zero_y = 8 + (h - 16) * (1 - (0 - lo) / (hi - lo))
    labels = json.dumps({
        "agent": [[t, round(v, 3)] for t, v in agent],
        "voo": [[t, round(v, 3)] for t, v in voo],
        "lo": lo, "hi": hi, "w": w, "h": h,
    })
    a_end = agent[-1][1]
    v_end = voo[-1][1] if voo else None
    direct = (
        f'<text class="dlabel a" x="{w-10}" y="20">Agent {_pct(a_end)}</text>'
        + (f'<text class="dlabel v" x="{w-10}" y="38">VOO {_pct(v_end)}</text>' if v_end is not None else "")
    )
    return f"""
<figure class="chart" aria-label="Return since inception, agent vs VOO buy-and-hold">
<svg viewBox="0 0 {w} {h}" id="curve" data-series='{html.escape(labels, quote=True)}'>
  <line class="grid" x1="8" y1="{zero_y:.1f}" x2="{w-8}" y2="{zero_y:.1f}"/>
  <polyline class="line v" points="{_polyline(voo, lo, hi, w, h)}"/>
  <polyline class="line a" points="{_polyline(agent, lo, hi, w, h)}"/>
  {direct}
  <line id="xhair" class="xhair" y1="8" y2="{h-8}" visibility="hidden"/>
</svg>
<div id="tip" class="tip" hidden></div>
<figcaption><span class="key a"></span>Agent equity&nbsp;&nbsp;<span class="key v"></span>VOO buy-and-hold — % return since inception, one point per session</figcaption>
</figure>"""


def _positions_rows(trades: list[dict]) -> str:
    open_tr = [t for t in trades if t.get("closed_ts") is None and not t.get("aborted") and not t.get("pending_entry")]
    if not open_tr:
        return '<div class="empty">No open positions.</div>'
    live: dict[str, dict] = {}
    try:
        payload = json.loads((JOURNAL / "positions_live.json").read_text(encoding="utf-8"))
        for row in payload.get("positions") or []:
            live[str(row.get("symbol", "")).upper()] = row
    except (OSError, ValueError):
        pass

    def _f(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    rows = []
    for t in open_tr:
        sym = str(t.get("symbol", "")).upper()
        lv = live.get(sym, {})
        qty = lv.get("exact_quantity") or lv.get("quantity") or t.get("entry_qty", "")
        cur = _f(lv.get("current_price"))
        pnl = _f(lv.get("unrealized_pnl"))
        avg = _f(lv.get("average_cost")) or _f(t.get("entry_price"))
        roi = (pnl / (avg * _f(qty)) * 100) if (pnl is not None and avg and _f(qty)) else None
        pnl_cls = "up" if (pnl or 0) >= 0 else "down"
        rows.append(
            f"<tr><td>{html.escape(sym)}</td><td class='num'>{qty}</td>"
            f"<td class='num'>{_fmt_money(avg) if avg else ''}</td>"
            f"<td class='num'>{_fmt_money(cur) if cur else '-'}</td>"
            f"<td class='num {pnl_cls}'>{_fmt_money(pnl) if pnl is not None else '-'}</td>"
            f"<td class='num {pnl_cls}'>{_pct(roi) if roi is not None else '-'}</td>"
            f"<td class='num'>{t.get('stop','-')} / {t.get('target') or '-'}</td>"
            f"<td class='mut'>{html.escape(str(t.get('trade_id','')))}</td></tr>"
        )
    return ("<table><thead><tr><th>Symbol</th><th class='num'>Shares</th><th class='num'>Avg cost</th>"
            "<th class='num'>Now</th><th class='num'>P&amp;L</th><th class='num'>ROI</th>"
            "<th class='num'>Stop / Target</th><th>Trade</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def _closed_rows(trades: list[dict]) -> str:
    closed = [t for t in trades if t.get("closed_ts")][-8:]
    if not closed:
        return ""
    rows = "".join(
        f"<tr><td>{html.escape(str(t.get('symbol','')))}</td>"
        f"<td class='num {'up' if (t.get('realized_pnl') or 0) >= 0 else 'down'}'>{_fmt_money(float(t.get('realized_pnl') or 0))}</td>"
        f"<td>{html.escape(str(t.get('exit_reason') or ''))}</td>"
        f"<td>{html.escape(str(t.get('review_verdict') or 'unscored'))}</td></tr>"
        for t in reversed(closed)
    )
    return ("<h2>Closed trades</h2><table><thead><tr><th>Symbol</th><th class='num'>P&amp;L</th>"
            "<th>Exit reason</th><th>Verdict</th></tr></thead><tbody>" + rows + "</tbody></table>")


def _activity(perf: list[dict]) -> str:
    by_day: dict[str, list[str]] = {}
    for r in perf:
        ts = str(r.get("ts", ""))
        if len(ts) >= 16:
            by_day.setdefault(ts[:10], []).append(ts[11:16])
    days = []
    d = date.today()
    while len(days) < 10:
        if d.weekday() < 5:
            days.append(d.isoformat())
        d -= timedelta(days=1)
    cells_html = []
    for day in reversed(days):
        got = by_day.get(day, [])
        cells = []
        for slot in SESSION_SLOTS:
            sh, sm = slot.split(":")
            target = int(sh) * 60 + int(sm)
            # Window must stay under half the 30-min slot spacing or one session
            # would light two adjacent cells.
            hit = any(abs(int(t[:2]) * 60 + int(t[3:5]) - target) <= 14 for t in got if t[:2].isdigit())
            cells.append(f'<i class="{"on" if hit else "off"}" title="{day} {slot} {"ran" if hit else "missed"}"></i>')
        cells_html.append(f'<div class="day"><span>{day[5:]}</span>{"".join(cells)}</div>')
    return '<div class="strip">' + "".join(cells_html) + "</div>"


def build() -> str:
    perf = _read_jsonl(JOURNAL / "performance.jsonl")
    trades = _read_jsonl(JOURNAL / "trades.jsonl")
    mandate = _mandate()
    agent, voo = _series(perf)

    equity = perf[-1]["equity"] if perf else START_EQUITY
    as_of = str(perf[-1].get("ts", ""))[:16].replace("T", " ") + " CT" if perf else "no data yet"
    voo0 = next((r["voo_price"] for r in perf if r.get("voo_price")), None)
    voo0_js = voo0 if voo0 is not None else "null"
    a_ret = agent[-1][1] if agent else 0.0
    v_ret = voo[-1][1] if voo else 0.0
    delta = a_ret - v_ret

    if mandate:
        exp_raw = str(mandate.get("consent", {}).get("expires_at", "")).replace("Z", "+00:00")
        try:
            # Ceil: a mandate expiring in 9.99 days has 10 days left in human terms.
            seconds = (datetime.fromisoformat(exp_raw) - datetime.now(timezone.utc)).total_seconds()
            days_left = math.ceil(seconds / 86400)
        except ValueError:
            days_left = None
    else:
        days_left = None
    if days_left is None:
        pill = '<span class="pill crit">&#9888; mandate unreadable</span>'
    elif days_left < 0:
        pill = '<span class="pill crit">&#9888; MANDATE EXPIRED - run ops/commit_paper_mandate.py</span>'
    elif days_left <= 3:
        pill = f'<span class="pill warn">&#9200; mandate expires in {days_left}d</span>'
    else:
        pill = f'<span class="pill ok">&#10003; mandate active - {days_left}d left</span>'

    lessons = "".join(f"<li>{html.escape(rule)}</li>" for rule in _lessons()) or "<li class='mut'>none yet</li>"
    decisions = "".join(
        f'<details><summary>{html.escape(head)}</summary><pre>{html.escape(body)}</pre></details>'
        for head, body in _entries()
    ) or '<div class="empty">No sessions yet.</div>'

    return f"""<title>Paper Desk</title>
<style>
:root {{ color-scheme: light;
  --page:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --mut:#898781;
  --grid:#e1e0d9; --border:rgba(11,11,11,.10);
  --a:#2a78d6; --v:#eb6834; --good:#006300; --crit:#d03b3b; --warnbg:#fab219; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme: dark;
  --page:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7; --mut:#898781;
  --grid:#2c2c2a; --border:rgba(255,255,255,.10); --a:#3987e5; --v:#d95926; --good:#0ca30c; }} }}
:root[data-theme="dark"] {{ color-scheme: dark;
  --page:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7; --mut:#898781;
  --grid:#2c2c2a; --border:rgba(255,255,255,.10); --a:#3987e5; --v:#d95926; --good:#0ca30c; }}
body {{ background:var(--page); color:var(--ink); margin:0;
  font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; }}
main {{ max-width:880px; margin:0 auto; padding:24px 16px 64px; }}
header {{ display:flex; flex-wrap:wrap; align-items:baseline; gap:12px; margin-bottom:8px; }}
h1 {{ font-size:20px; margin:0; }} h2 {{ font-size:15px; margin:28px 0 8px; }}
.sub {{ color:var(--mut); font-size:13px; }}
.pill {{ font-size:12.5px; padding:2px 10px; border-radius:999px; border:1px solid var(--border); }}
.pill.ok {{ color:var(--good); }} .pill.warn {{ color:var(--ink); background:color-mix(in srgb,var(--warnbg) 25%,transparent); }}
.pill.crit {{ color:#fff; background:var(--crit); }}
.hero {{ display:flex; gap:32px; flex-wrap:wrap; margin:16px 0; }}
.hero b {{ display:block; font-size:30px; font-weight:650; font-variant-numeric:tabular-nums; }}
.hero span {{ font-size:12.5px; color:var(--mut); text-transform:uppercase; letter-spacing:.04em; }}
.up {{ color:var(--good); }} .down {{ color:var(--crit); }}
.chart, table, .strip, .empty, details {{ background:var(--surface); border:1px solid var(--border); border-radius:6px; }}
.chart {{ padding:10px; margin:0; }} svg {{ width:100%; height:auto; display:block; }}
.line {{ fill:none; stroke-width:2; stroke-linejoin:round; }} .line.a {{ stroke:var(--a); }} .line.v {{ stroke:var(--v); }}
.grid {{ stroke:var(--grid); stroke-width:1; }} .xhair {{ stroke:var(--mut); stroke-width:1; stroke-dasharray:3 3; }}
.dlabel {{ font:12px system-ui,sans-serif; fill:var(--ink2); text-anchor:end; }}
figcaption {{ color:var(--mut); font-size:12.5px; padding:8px 4px 2px; }}
.key {{ display:inline-block; width:14px; height:3px; border-radius:2px; vertical-align:middle; margin-right:5px; }}
.key.a {{ background:var(--a); }} .key.v {{ background:var(--v); }}
.tip {{ position:fixed; pointer-events:none; background:var(--surface); border:1px solid var(--border);
  border-radius:4px; padding:4px 8px; font-size:12.5px; color:var(--ink2); font-variant-numeric:tabular-nums; }}
table {{ border-collapse:separate; border-spacing:0; width:100%; font-size:14px; }}
th, td {{ text-align:left; padding:7px 12px; border-bottom:1px solid var(--grid); }}
tr:last-child td {{ border-bottom:none; }}
th {{ color:var(--mut); font-size:12px; text-transform:uppercase; letter-spacing:.04em; font-weight:600; }}
.num {{ text-align:right; font-variant-numeric:tabular-nums; }} .mut {{ color:var(--mut); }}
.empty {{ padding:18px; color:var(--mut); font-size:14px; }}
details {{ margin-bottom:6px; padding:8px 12px; }} summary {{ cursor:pointer; font-size:14px; }}
details pre {{ white-space:pre-wrap; color:var(--ink2); font:12.5px/1.5 ui-monospace,Consolas,monospace;
  overflow-x:auto; margin:8px 0 2px; }}
ul {{ margin:6px 0; padding-left:22px; }} li {{ margin:3px 0; }}
.strip {{ padding:10px 12px; display:flex; gap:10px; flex-wrap:wrap; }}
.day {{ display:flex; align-items:center; gap:3px; font-size:11.5px; color:var(--mut); }}
.day span {{ margin-right:3px; font-variant-numeric:tabular-nums; }}
.day i {{ width:9px; height:9px; border-radius:2px; background:var(--grid); }}
.day i.on {{ background:var(--a); }}
@media (prefers-reduced-motion: no-preference) {{ details {{ transition: background .15s; }} }}
</style>
<main>
<header><h1>Paper Desk</h1>{pill}<span class="sub">long-only paper portfolio, autonomous 30-minute sessions</span></header>
<div class="hero">
  <div><span>Equity</span><b id="eqv">{_fmt_money(equity)}</b></div>
  <div><span>Return</span><b id="retv" class="{'up' if a_ret >= 0 else 'down'}">{_pct(a_ret)}</b></div>
  <div><span>vs VOO</span><b id="vsv" class="{'up' if delta >= 0 else 'down'}">{_pct(delta)} pp</b></div>
  <div><span id="asof-label">Data as of</span><b id="asof" class="sub" style="font-size:16px; font-weight:500; line-height:2.2;">{as_of}</b></div>
</div>
<script id="livecfg" type="application/json">{{"start": {START_EQUITY}, "voo0": {voo0_js}}}</script>
{_chart(perf)}
<h2>Open positions</h2>
{_positions_rows(trades)}
{_closed_rows(trades)}
<h2>Recent decisions</h2>
{decisions}
<h2>Lessons (binding rules)</h2>
<ul>{lessons}</ul>
<h2>Session activity - last 10 market days</h2>
{_activity(perf)}
<p class="sub">Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by ops/build_dashboard.py. Every order shown passed the mandate gate (long-only, allowlist, caps). Journal and full audit ledger live in the repo.</p>
</main>
<script>
(function () {{
  var svg = document.getElementById('curve');
  if (!svg) return;
  var data = JSON.parse(svg.dataset.series), tip = document.getElementById('tip'),
      xh = document.getElementById('xhair'), a = data.agent, v = data.voo;
  svg.addEventListener('mousemove', function (e) {{
    if (a.length < 2) return;
    var r = svg.getBoundingClientRect(), fx = (e.clientX - r.left) / r.width * data.w;
    var i = Math.round((fx - 8) / ((data.w - 16) / (a.length - 1)));
    i = Math.max(0, Math.min(a.length - 1, i));
    var x = 8 + i * (data.w - 16) / (a.length - 1);
    xh.setAttribute('x1', x); xh.setAttribute('x2', x); xh.setAttribute('visibility', 'visible');
    tip.hidden = false;
    tip.textContent = a[i][0] + '  agent ' + a[i][1].toFixed(2) + '%' + (v[i] ? '  voo ' + v[i][1].toFixed(2) + '%' : '');
    tip.style.left = (e.clientX + 14) + 'px'; tip.style.top = (e.clientY - 10) + 'px';
  }});
  svg.addEventListener('mouseleave', function () {{ tip.hidden = true; xh.setAttribute('visibility', 'hidden'); }});
}})();

// Live layer: feature-detects the /api/alpaca proxy (present on the Netlify
// host only). On claude.ai the fetch 404s and the page stays snapshot-static.
(function () {{
  var cfg;
  try {{ cfg = JSON.parse(document.getElementById('livecfg').textContent); }} catch (e) {{ return; }}
  var eqv = document.getElementById('eqv'), retv = document.getElementById('retv'),
      vsv = document.getElementById('vsv'), asof = document.getElementById('asof'),
      label = document.getElementById('asof-label');
  var fails = 0, live = false;

  function fmtMoney(v) {{ return '$' + v.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}); }}
  function fmtPct(v) {{ return (v >= 0 ? '+' : '') + v.toFixed(2) + '%'; }}
  function paint(el, v, suffix) {{
    el.textContent = fmtPct(v) + (suffix || '');
    el.classList.toggle('up', v >= 0); el.classList.toggle('down', v < 0);
  }}

  async function poll() {{
    if (document.hidden) return;
    try {{
      var a = await fetch('/api/alpaca?what=account').then(function (r) {{ if (!r.ok) throw 0; return r.json(); }});
      var eq = parseFloat(a.equity);
      if (!isFinite(eq)) throw 0;
      var ret = (eq / cfg.start - 1) * 100;
      eqv.textContent = fmtMoney(eq);
      paint(retv, ret);
      if (cfg.voo0) {{
        try {{
          var q = await fetch('/api/alpaca?what=quote&symbols=VOO').then(function (r) {{ if (!r.ok) throw 0; return r.json(); }});
          var vq = q.quotes && q.quotes.VOO;
          var bp = vq && vq.bp, ap = vq && vq.ap;
          if (bp > 0 && ap > 0 && Math.abs(ap - bp) / ap < 0.02) {{
            var vooRet = (((bp + ap) / 2) / cfg.voo0 - 1) * 100;
            paint(vsv, ret - vooRet, ' pp');
          }}
        }} catch (e) {{ /* keep last vs-VOO */ }}
      }}
      var now = new Date();
      asof.textContent = now.toLocaleTimeString();
      if (!live) {{ live = true; label.innerHTML = '<span style="color:var(--good)">&#9679; LIVE</span>'; }}
      fails = 0;
    }} catch (e) {{
      fails++;
      if (fails >= 3 && !live) clearInterval(timer); // no proxy on this host - stay static
    }}
  }}
  var timer = setInterval(poll, 20000);
  poll();
}})();
</script>
"""


def _deploy() -> None:
    """Push site/ to Netlify production. Best-effort - a failed deploy never blocks a session."""
    import shutil
    import subprocess

    netlify = shutil.which("netlify") or r"C:\Users\awsom\AppData\Roaming\npm\netlify.cmd"
    try:
        subprocess.run(
            [netlify, "deploy", "--prod", "--no-build"],
            cwd=ROOT, check=True, capture_output=True, timeout=180,
        )
        print("deployed to netlify")
    except Exception as exc:  # noqa: BLE001 - freshness plumbing, never fatal
        print(f"netlify deploy skipped/failed: {exc}")


if __name__ == "__main__":
    import sys as _sys

    page = build()
    OUT.write_text(page, encoding="utf-8")
    site = ROOT / "site" / "index.html"
    site.parent.mkdir(exist_ok=True)
    # The Netlify copy is a full document (no artifact wrapper supplies the skeleton there).
    body = page.replace("<title>Paper Desk</title>\n", "", 1)
    site.write_text("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
                    "<title>Paper Desk</title>"
                    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
                    "<meta name=\"robots\" content=\"noindex\">"
                    "</head><body>" + body + "</body></html>", encoding="utf-8")
    print(f"wrote {OUT} and {site}")
    if "--deploy" in _sys.argv:
        _deploy()
