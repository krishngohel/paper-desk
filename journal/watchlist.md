# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-22 ~16:15 CT (research session, market closed - Tuesday evening,
post-close homework after a 37-leg continuous trading day). Full rewrite - the
09-18 version described a book that no longer exists (ECO/RBRK/SMTC/ZS as held
positions); all four have since closed (RBRK/SMTC on 09-21 via targets, ECO on
09-22 via its s6a governing exit, ZS on 09-22 via target). Current book is
ARTY/CRWD/TXG.

**Regime (`ta.py --market`, fresh this session):** SPY 773.38, +1.13% vs EMA21,
RSI14 58.5, structure **range/mixed**. QQQ 747.46, +3.96% vs EMA21, RSI14 67.8,
**uptrend (higher highs + higher lows)**. Same read as the last continuous leg -
QQQ carrying the tape, SPY chopping. No reason to chase size.

## Mandate & quota status

**Mandate renewed 2026-09-14, `consent.expires_at` 2026-09-28T17:58:50Z - 6 days
runway.** Not halted, not expired - verified fresh this session via `status`/
`account` and cross-checked against the last continuous leg's own fresh read
(same day, ~90 min earlier).

**Standing-order quota: MET this session - 6 live resting buy-limit entries
across 5 distinct symbols**, comfortably clearing both the >=6-entry and
>=3-distinct-symbol floors: CRWD 204.30 (new tonight, `a1d8b66a`), CRWD 232.00
remainder (`4bab1e47`), TXG 58.70 (`7f98e743`), SMTC 146.91 (`41354f13`), ZS
160.75 (`4b0ad29d`), RBRK 90.15 (`4e8ee047`). TWLO trigger (`trg-20260922-002`,
>=286.20) expired unfired tonight at 15:00 CT, confirmed via full-session 5m
bars (high 286.05, never touched 286.20) - retired in `triggers.jsonl`, not a
watcher miss.

## Book (3 positions, book target 3-6 — at the floor)

- **ARTY** (AI-infra thematic ETF) 47 sh @ avg 79.67, now 79.81 (+0.18% ROI).
  s6a-governed (momentum continuation, no price target), mechanical stop 77.05
  (3.5% clear). Entered 2026-09-22 - first close in the books tonight (79.90 vs
  entry, an up day), governing 2-down-close exit not yet evaluable. No earnings
  (ETF). time_stop 2026-10-22 (outer backstop only).
- **CRWD** 3 sh @ avg 231.22, now 249.69 (+7.99% ROI). Target 264.13 resting
  (`9bfc5894`, 5.79% away), stop 219.15 (12.2% clear), time_stop 2026-10-03.
  Remaining 3sh of the original 6sh order still resting at 232.00 (`4bab1e47`).
  Fresh deep-pullback probe rung added tonight at 204.30 (`a1d8b66a`, 14sh,
  stop 199.50, target 213.90, C/probe) - explicitly NOT a same-thesis add (that
  level sits below the existing position's own stop, so it would only fill after
  the original position had already stopped out; see ledger t-2026-09-22-004 for
  the full bear-case disclosure). next_earnings 2026-12-01 (safe).
- **TXG** 15 sh @ avg 75.64, now 80.70 (+6.69% ROI). s6a-governed (no price
  target), mechanical stop 64.73 (19.8% clear), time_stop 2026-10-15. Closed UP
  today (80.75 vs prior close 79.10) - governing 2-down-close exit not
  triggered, stays open. Deep add-rung 58.70/15sh still resting (`7f98e743`).
  next_earnings 2026-11-05 (safe).

## Staged / armed for next session - ranked

1. **MDB (MongoDB) - PRIORITY, s6a signal CONFIRMED tonight.** momentum_scan's
   stalked setup completed: today's close 427.69 decisively cleared the 407.30
   confirmation level (prior close), with close > EMA9 (395.48) > EMA21 (394.05)
   > EMA50 (378.24) - full trend-gate pass, structure explicit uptrend. **Enter
   at tomorrow's (09-23) regular open, NOT intraday** (per the standing plan and
   because research sessions place no market orders) - stop under the 09-18
   session low (~379-381, verify the exact bar low at the open), probe size,
   hold for days, exit on 2 consecutive lower closes (s6a governing rule). TV
   strong_buy/strong_buy/buy. next_earnings 2026-12-01 (safe).
2. **RBRK** - resting GTC buy-limit 90.15 (`4e8ee047`), unfilled since 09-16.
   Deep pullback add to the closed-out original position's old cluster; no
   current RBRK holding. next_earnings 2026-12-03 (safe).
3. **ZS** - resting GTC buy-limit 160.75 (`4b0ad29d`), unfilled since 09-16.
   Same deep-pullback logic as RBRK; the shallower ZS position that carried this
   symbol closed today at target (+$254.32). next_earnings 2026-11-24 (safe).
4. **SMTC** - resting GTC buy-limit 146.91 (`41354f13`), unfilled since 09-17.
   next_earnings 2026-11-23 (safe).
5. No armed (above-market) confirmation triggers remain live tonight (TWLO
   expired unfired). Next trading session should arm a fresh one if a genuine
   rule-3c-passing name appears intraday - research sessions stage only
   below-market GTC limits per duty 4.

## Watch only (fails trend gate, tradability, or lacks a fresh catalyst tonight)

**Fresh names hunted tonight (duty 1b, screen.py gainers-explore lens, full
`ta.py` workups on the two biggest liquid movers not already on the watchlist):**
- **VKTX** (Viking Therapeutics, $1.6B dollar volume today, day +37.6%, gap
  +28.3% - huge one-day biopharma gap) - RSI14 70.9, pos_in_20d_range 100%,
  TV strong_buy, but `key_levels.structure` explicit **"downtrend (lower highs +
  lower lows)"** - a single gap day inside an established downtrend, not a
  confirmed uptrend (same rejection logic as COIN's 09-18 gap, playbook s11:
  don't let a real story override the chart). Rejected on rule 3c. StockTwits
  trending (#3, 39.1k watchers) - crowd hype noted, not a thesis. Revisit only
  if a second up day confirms the reversal, not another single gap.
- **INOD** (Innodata, AI data-labeling, $369M dollar volume, day +15.84%) -
  fails rule 3c on BOTH tests: `structure` tagged "range/mixed" AND the literal
  EMA order inverted (EMA21 58.41 < EMA50 61.07 despite EMA9>EMA21). 5m tape
  shows a hammer defending 70.37 at resistance 71.68 but no resolved breakout.
  Rejected. next_earnings 2026-11-05 if ever revisited.
- **BB** (BlackBerry, Reddit rank-climber #14, up 83 ranks 24h) - structure
  "range/mixed", **next_earnings 2026-09-24 (2 days out - inside the 2-day
  event-risk window regardless of structure)**. Rejected on both counts.
- **SOFI** (Reddit rank-climber #27, up 77 ranks 24h) - structure "range/mixed",
  TradingView **strong_sell** on moving averages, RSI14 45.8 (no momentum).
  Textbook rank-climber-with-no-structure pass (playbook s11: crowd hype is
  never a thesis) - rejected cleanly, no fresh catalyst or chart to support it.
- Other reddit_rank_climbers checked narratively, not individually worked up
  (AMZN/MRVL/VOO/GOOGL/TSLA/IQ/ASTS/SOXL) - all mega-cap or broad-ETF names
  riding general market chatter, not fresh single-name setups; none flagged a
  dated catalyst in the trending feed worth a dedicated `ta.py` pull tonight.

**Repeat rejects, unchanged reasons (not re-run fresh tonight):** the full
09-18 rejected list (RIOT, WDC, AAOI, CLSK, HOOD, MARA, BMNR, ALMR, BIAF, NCI,
GEMI, SOLT/BSOL/HALO/BTDR, SNDK/MUU/AVGO/LRCX/STX/COHR/AMAT/MTSI/NVDA/INTC/
CIFR cluster, CYPH/HUT/PSIX/ADPT, DSP/ABTC/WOLF/GLOO/AKAN, MSTR/CRCL/XENE,
IREN/FPS) carries forward unchanged - no fresh catalyst surfaced for any of
them tonight.

## Macro calendar

- No book or staged-name earnings fall within the next 30 days except the
  BB event-risk flag above (BB is not held or staged, informational only):
  ARTY none (ETF), CRWD 12-01, TXG 11-05, RBRK 12-03, ZS 11-24, SMTC 11-23,
  MDB 12-01 (all clear of the 2-day window if entered tomorrow).
- No fresh macro event flagged for tomorrow beyond the ongoing regime backdrop
  (SPY range/mixed, QQQ uptrend).

## Pruned (no fresh catalyst/edge, or fully explained above)

ECO (closed 2026-09-22, s6a governing exit on the 2nd lower close, -$48.60,
scored pending review). ZS-original-cluster-position (closed 2026-09-22 at
target, +$254.32). FIVN (entered 2026-09-22 on a confirmation-trigger
watcher-miss fire, stopped out same day -$28.70, scored pending review). RBRK/
SMTC-original-cluster-positions (closed 2026-09-21 at target, +$267.15/+$170.05/
+$57.68). BWIN/ANGX/HOOD/APA/COIN/MSTR/LITE/SMMT/CYPH/HUT/BHVN/RARE (all
pre-09-21, already scored, no change).

Next session (Wednesday 2026-09-23, the open/planning leg):
**(1) MDB is the day's PRIORITY - execute or re-verify the momentum entry at
the open per the plan above, stop under the actual 09-18 session low.** **(2)
Re-check ARTY's and TXG's s6a governing exit against tomorrow's close (both
currently on up-closes, no risk of the 2-down-close trigger yet, but confirm
fresh).** **(3) Standing-order quota is 6/6 across 5 distinct symbols after
tonight's CRWD add - no immediate action needed, but keep hunting for genuine
rule-3c passes to diversify beyond the CRWD/TXG/RBRK/ZS/SMTC cluster.** **(4)
Continue manual bar-verification of every stop/trigger given the ongoing
watcher reliability issue (memory: project_watcher_silent_miss) - today logged
its 5th confirmed silent-miss instance (FIVN) of the training run.** **(5)
Regime: SPY range/mixed, QQQ uptrend - no reason to chase size.**
