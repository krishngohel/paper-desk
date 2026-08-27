# Autonomous Trading Loop + Learning Journal — Design

**Date:** 2026-08-27
**Builds on:** the completed long-only paper-trading harness (fork branch `long-only` @ 49efd75, gated `ops/trade_cli.py`, active mandate expiring 2026-09-09, hardening report GO).

## Goal

The paper-trading agent runs fully hands-off on the user's machine and Claude subscription: hourly trading sessions during market hours decide and trade through the existing mandate gate, journal every decision with a falsifiable thesis, distill lessons weekly, and publish a live dashboard so the user can watch performance and learning without ever being asked for input. The only manual act that remains is 14-day mandate renewal (deliberate dead-man switch).

**Purpose framing (user, 2026-08-27):** this whole setup is a training ground — the point is to build evidence of trading competence BEFORE any real money is considered. Therefore every trade's complete lifecycle (why it was selected, when and why it was sold, what happened) must be captured as organized, machine-ready data, not only prose. The structured trade ledger below is the canonical dataset for that evaluation.

## Decisions (user-confirmed 2026-08-27)

- **Cadence:** hourly — Mon–Fri sessions at 8:45, 9:45, 10:45, 11:45, 12:45, 13:45, and 14:30 (America/Chicago; market is 8:30–15:00 CT), plus a Friday 15:15 weekly review session. User has subscription headroom and chose maximum useful frequency; beyond hourly adds nothing because the mandate caps execution at 5 orders/day.
- **Reporting:** live artifact dashboard (private URL, updated by the 14:30 session and the Friday review) + append-only journal files in the repo.
- **Renewal:** manual. At mandate expiry the gate denies everything; sessions keep journaling read-only state and the dashboard nags until the user re-runs `ops/commit_paper_mandate.py`.
- Missed sessions (PC off/asleep) are skipped silently; the dashboard's activity strip makes gaps visible.

## Architecture

Three parts, all thin, all riding on the already-hardened harness:

### 1. Scheduler — local Claude Code cron jobs

Eight cron entries (7 weekday trading slots + Friday review) created with Claude Code's local scheduler (CronCreate). Every job's prompt is identical apart from a session-type word:

> Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: {open|intraday|preclose|weekly-review}.

All behavior lives in `SESSION_PROMPT.md` (version-controlled); cron entries are dumb triggers and never need editing to tune the agent.

### 2. Standing operating procedure — `ops/SESSION_PROMPT.md`

One file, four phases; `preclose` and `weekly-review` add extra duties.

1. **Orient.** Run `trade_cli.py status`. If halted, or the market is closed (holiday/weekend — check the clock via a quote timestamp or calendar), append a one-line journal note and stop. If the mandate is expired (deny envelope names it), append a read-only snapshot entry, update the dashboard nag, and stop.
2. **Recall.** Read `journal/lessons.md` (binding rules — a session may not act against a lesson without writing an explicit justification) and the last 10 entries of the current `journal/YYYY-MM.md`, including open theses and their exit conditions.
3. **Decide & act.** Check account, positions, and quotes for the six allowlist symbols. First enforce existing exit conditions (a triggered exit is executed before any new idea). Then at most ONE new idea per session, sized fractionally (a whole AAPL share breaches the $200 cap). Explicit hold is a first-class outcome and must be journaled with a reason. All orders through `trade_cli.py buy|sell` — the mandate gate is the authority; the session records the gate's verdict verbatim and never retries a structural DENY.
4. **Record.** Append a journal entry (fixed template: timestamp, session type, account equity, positions, thesis or hold-reason, actions + gate verdicts, falsifiable exit condition for any new position, watch notes for the next session). Maintain `journal/trades.jsonl`: a buy creates the entry-half record (thesis, lesson_refs, exit_condition are MANDATORY at entry — an order without them may not be placed); a sell completes the matching record (exit_reason, realized P&L, VOO comparison). Append one line to `journal/performance.jsonl`: `{ts, equity, cash, positions_value, voo_price}`.

**preclose additionally:** writes `journal/daily/YYYY-MM-DD.md` (one-page day summary incl. P&L vs VOO) and republishes the dashboard.
**weekly-review additionally:** scores every thesis closed that week (right/wrong and why), updates `journal/lessons.md` (adds, amends, or retires rules — retired rules move to an archive section with the evidence), evaluates whether earlier lessons improved outcomes, and republishes the dashboard.

Sessions never write the mandate file, never touch `~/.vibe-trading` except through `trade_cli.py`, and never place an order outside `trade_cli.py`.

### 3. Dashboard — one private artifact page

Stable URL, redeployed (same file path) by preclose and weekly-review sessions from repo data. Content: equity curve vs $1,000 buy-and-hold VOO since inception, current positions, last ~10 decisions with theses and gate verdicts, current lessons, mandate status with days-to-expiry (red nag when expired), and a session-activity strip (expected vs actual sessions, gaps visible). Static self-contained HTML generated by `ops/build_dashboard.py` (reads journal/performance/audit data, writes `ops/dashboard.html`); the session then publishes it as an artifact. The artifact URL is recorded in `journal/DASHBOARD_URL.txt` after first publish so every later session updates the same page.

## Data layout (all committed to the workspace repo; no secrets in any of it)

```
journal/
  YYYY-MM.md            # append-only session log (narrative), fixed entry template
  daily/YYYY-MM-DD.md   # preclose one-pagers
  lessons.md            # numbered binding rules + archive section (the "learning")
  trades.jsonl          # CANONICAL trade ledger - one JSON object per position lifecycle
  performance.jsonl     # one line per session: ts, equity, cash, positions_value, voo_price
  DASHBOARD_URL.txt     # stable artifact URL
ops/
  SESSION_PROMPT.md     # standing operating procedure (the agent's whole behavior)
  build_dashboard.py    # journal+trades+audit -> dashboard.html
  dashboard.html        # generated, published as the artifact
```

### The trade ledger (`journal/trades.jsonl`) — the evaluation dataset

One JSON object per trade lifecycle. The session that BUYS writes the entry half; the session that SELLS completes it; the weekly review adds the verdict. Fields:

```json
{"trade_id": "t-2026-08-27-001", "symbol": "AAPL",
 "opened_ts": "...", "entry_order_id": "...", "entry_qty": 0.5, "entry_price": 294.10, "entry_notional": 147.05,
 "thesis": "one-paragraph why, written at entry",
 "lesson_refs": ["L3", "L7"],
 "exit_condition": "falsifiable trigger written at entry, e.g. close below 285 or +6% or 10 trading days",
 "closed_ts": null, "exit_order_id": null, "exit_price": null,
 "exit_reason": null,
 "realized_pnl": null, "realized_pnl_pct": null, "holding_days": null,
 "voo_pnl_pct_same_window": null,
 "review_verdict": null, "review_notes": null}
```

`exit_reason` is one of: `exit-condition-hit`, `thesis-invalidated`, `review-decision`, `halt-flatten`, `mandate-expiry-manual`. `review_verdict` is one of: `right`, `wrong`, `lucky` (won for the wrong reason), `unlucky` (sound thesis, adverse outcome) — scored by the Friday review, never by the session that traded. An open record with nulls in the exit half is a live position; the dashboard and weekly review reconcile open records against `trade_cli.py positions` and flag any mismatch. Updates rewrite the record's line in place (read-modify-write of the file is acceptable at this scale; the file is committed on every change so history preserves every intermediate state).

Sessions commit their journal writes (`git add journal; git commit`) so history is auditable; plain commit messages, no AI trailers.

## What "learning" means here (honest definition)

No model training. Learning = every decision is made with the full record of past decisions and measured outcomes in context, under rules the agent itself distilled from those outcomes and must obey or explicitly argue against. Its speed and quality are observable: the lessons file's growth, the weekly right/wrong scoring, and the equity curve vs VOO.

## Error handling

- trade_cli error envelopes (network down, Alpaca outage): journal the envelope, take no action, end session. Never retry orders blindly (timeout may have placed the order — check `orders` first next session; trade_cli passes client-order ids where supported).
- Gate denials: expected behavior, journaled verbatim; structural denials are never retried, quantitative denials may be resized once within the same session.
- Dashboard publish failure: journal it; data is safe in the repo, next session retries.
- Two sessions overlapping (PC wakes late): the daily-order lock and mandate gate make double-execution safe; journal appends are last-writer-wins on separate entries.

## Testing

- `build_dashboard.py` gets a unit test on fixture journal data.
- SESSION_PROMPT.md is "tested" by one supervised dry run of each session type (open, intraday, preclose, weekly-review) before the crons are armed; the dry-run transcripts are the acceptance evidence.
- Cron entries verified by listing them and by the first live day's activity strip.

## Out of scope

- Raising mandate caps (user decision at renewal, informed by whether the 5-order cap binds).
- Any live-money mechanism. Options, crypto, non-allowlist symbols.
- Vibe-Trading's internal runner/LLM.
