# Autonomous Trading Loop Implementation Plan

> Executed inline (superpowers:executing-plans) same-session by the controller that holds the loaded dataviz/artifact-design context. Spec: docs/superpowers/specs/2026-08-27-autonomous-trading-loop-design.md — its data layout, ledger schema, cadence, and SOP phases are binding and not restated here.

**Goal:** hands-off hourly trading sessions via local cron, structured trade ledger, live artifact dashboard.

## Global Constraints
- All spec constraints (long-only harness untouched; sessions act only through `ops/trade_cli.py`; ledger fields mandatory at entry).
- Dashboard palette/tokens: dataviz reference palette (series-1 blue `#2a78d6`/`#3987e5` = agent equity; series-2 orange `#eb6834`/`#d95926` = VOO; chrome/ink tokens per reference; status `critical #d03b3b` for expired mandate, delta-good `#006300`/`#0ca30c`). System sans, tabular-nums for figures, both themes via `:root` tokens + `prefers-color-scheme` guard + `data-theme` override, explicit body background, single y-axis, legend + direct labels for the 2 series, crosshair tooltip, no body horizontal scroll.
- Plain commit messages, no AI trailers. Python 3.11 venv at `.venv`.

## Tasks
- [ ] **A. Journal scaffold + `ops/SESSION_PROMPT.md`** — create `journal/` per spec layout (empty `trades.jsonl`, `performance.jsonl`, seeded `lessons.md` with rules L1–L3 baseline discipline rules, `daily/` dir, current-month log with a genesis entry); write the full SOP file implementing the spec's four phases, entry/ledger templates, and edge-case handling. Commit.
- [ ] **B. `ops/build_dashboard.py` + test** — pure-stdlib generator: reads `journal/performance.jsonl`, `journal/trades.jsonl`, `journal/lessons.md`, last N narrative entries, mandate JSON (`~/.vibe-trading/live/alpaca/mandate.json`, path overridable for tests), audit tail; emits self-contained `ops/dashboard.html` per the design tokens above (header: title, mandate pill with days-to-expiry, equity hero + delta vs VOO; SVG 2-series line chart with hover crosshair; positions table from open ledger records; last 10 decisions; lessons; activity strip of expected-vs-logged sessions). Pytest on fixture data: chart renders both series, expired mandate shows critical pill, empty data renders without error. Run tests green; generate from real (near-empty) data. Commit.
- [ ] **C. First publish** — publish `ops/dashboard.html` as private artifact (favicon 📈, stable name), write `journal/DASHBOARD_URL.txt`, commit.
- [ ] **D. Cron jobs** — 8 local jobs (Mon–Fri 8:45/9:45/10:45/11:45/12:45/13:45/14:30, Fri 15:15 review), prompt = "Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: X." Verify with cron list.
- [ ] **E. Supervised dry runs** — run one `intraday` session (subagent following the SOP verbatim; live if market open) and one `weekly-review` (expect graceful no-op: no closed trades). Verify: journal entry format, ledger integrity, performance line appended, dashboard regenerated + republished to same URL, commits made. Fix SOP wording where the dry run stumbles; re-run once.
- [ ] **F. Close-out** — memory update, report to user with dashboard URL and what happens next.
