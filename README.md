# Paper Desk

An autonomous, long-only paper trading agent. Claude makes every trading decision;
a hard-coded mandate gate makes sure certain decisions can never be made at all.
Built as a training ground: the goal is a fully labeled record of decisions and
outcomes that proves (or disproves) trading competence before real capital is
ever discussed.

**Live dashboard:** equity vs VOO benchmark, open positions with ROI, every
decision with its reasoning, and the agent's own rulebook as it evolves.

## How it works

```
                    +--------------------------+
   market data ---> |  continuous session relay | ---> orders --+
   (screener, TA,   |  (Claude, all market day) |               |
   candles, news)   +--------------------------+                v
                          |         ^                 +------------------+
                          v         |                 |   mandate gate   |
                    journal, trade  |                 | long-only, cash, |
                    ledger, lessons +---- learns ---- |  audit, kill-    |
                                                      |     switch       |
                                                      +------------------+
                                                                |
                    15s watcher enforces stops  <---- broker (Alpaca paper)
```

- **Decisions**: a relay of Claude sessions runs from market open to close in
  manage / hunt / strike cycles - screening the whole US market, reading levels,
  indicators and candlestick tells, stalking named triggers, and entering with a
  written thesis, numeric stop/target, and sizing rationale. Evenings and
  weekends run research sessions that maintain a battle plan and may stage
  conservative resting orders for the next open.
- **Execution**: resting limit-order ladders at the broker (instant fills at
  chosen levels), a 15-second watcher that enforces every stop mechanically,
  and 30-minute fallback sessions if the relay ever dies.
- **The gate**: every order passes through a forked
  [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) mandate engine that
  structurally refuses short selling, leverage, and anything outside US
  equities/ETFs - regardless of what the model decides. Kill switch is a file;
  its existence halts everything. Every action lands in a tamper-evident
  hash-chained audit ledger.
- **Learning**: every trade is a labeled record (thesis, setup grade, stop,
  target, outcome, review verdict). A weekly review scores each closed trade -
  right, wrong, lucky, or unlucky - and writes binding lessons the agent must
  obey or argue against in writing. Hard statistics (win rate, expectancy, P&L
  by setup grade) are recomputed from the ledger and loaded before every
  decision.

## What's in this repo

```
ops/            the machinery: session SOP + playbook (the agent's doctrine),
                trade CLI, watcher, screener, TA engine, dashboard generator
journal/        the record: monthly narrative logs, trades.jsonl (the labeled
                dataset), lessons.md (earned rules), stats.json, watchlist
docs/           specs, implementation plans, and the guardrail hardening report
netlify/        read-only serverless proxy for the live dashboard
```

The Vibe-Trading fork (mandate gate, long-only enforcement, audit ledger) lives
in a separate local repository and is not published here.

## Safety posture

- Paper account only; the credentials in use cannot touch a live endpoint.
- Long-only is enforced in code and adversarially tested: a sell can never
  exceed held quantity, verified down to contradictory-broker-row edge cases.
- The agent cannot modify its own mandate, and sessions run under a permission
  allowlist that denies writes to the trading store.
- The trading loop once refused an instruction injected through an
  unauthenticated channel - by its own judgment. That behavior is now doctrine.

## Status

Paper training run in progress. Nothing here is financial advice; the point of
the exercise is to find out honestly whether this approach deserves real money,
and the ledger will answer that either way.
