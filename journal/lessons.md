# Lessons

Binding rules for every trading session. A session may act against a rule only
with a written justification in its journal entry naming the rule. Rules are
added, amended, or retired ONLY by a review session (the Friday weekly review,
and the daily post-close review while the training directive is in force),
citing trade_ids as evidence. Seed rules L1-L3 are discipline rules, present
from day one. Candidate patterns that lack evidence live under "Watch patterns"
below until a review promotes or discards them.

## Active

- **L1 — Size deliberately, and say why.** Position size is fully your decision
  (mandate v4 opened the whole paper account). Every entry states its sizing
  reasoning: why this notional relative to conviction, the exit distance, and
  the rest of the book. Unexplained size is treated by the weekly review as a
  process failure even when the trade wins. (Seed rule; amended by operator
  2026-08-27 when the $200/$1000 caps were removed at the user's direction.)
- **L2 — The gate is right.** A structural denial means the idea was outside
  the contract; drop it. Do not restructure an order to chase a denied idea.
  (Seed rule.)
- **L3 — No thesis, no trade.** If the thesis or its falsifiable exit condition
  cannot be written in two honest sentences, the trade does not exist. Hold is
  a position. (Seed rule.)

- **L5 — A ladder rung that fills is the thesis that actually happened, not the
  one written.** When a laddered entry fills only its highest/most-extended
  rung while the lower pullback-confirmation rungs go unfilled, the base-hold
  the thesis leaned on never actually confirmed - manage the position as the
  weaker, chase-adjacent version of the setup (tighter stop toward the fill
  price or nearest support, smaller add tolerance), not as if full
  confirmation occurred. Check which rung filled before trusting the original
  thesis narrative. (Added 2026-08-28 weekly review, evidence: t-2026-08-28-001
  ESTC - only the 100.30 breakout-confirm rung filled; the 99.30/99.80
  pullback rungs that would have confirmed the base never did. Single-trade
  evidence - revisit as more ladder trades close.)
- **L6 — Same-day time_stops need enough clock left to work.** A "flat by
  preclose today" time_stop written on an entry after ~14:00 CT gives a
  multi-hour archetype (base-and-reclaim, pullback-in-uptrend) under ~2.5
  hours to develop before it's force-closed regardless of whether the thesis
  is still valid. For afternoon entries on setups that need time, either
  extend the time_stop to the next session's open or size/grade the trade
  knowing the clock, not the thesis, may end it. (Added 2026-08-28 weekly
  review, evidence: t-2026-08-28-001 ESTC entered 14:20 CT, closed by its own
  time-stop at 14:32 CT with neither the stop nor target ever touched - the
  loss was pure noise, not thesis failure. Single-trade evidence - revisit as
  more afternoon entries close.)

- **L8 — A probe's fill level needs an actual multi-touch defense, not just a reversal candle or "buyers stepping in" narrative.** A level that has been tested and held 2+ times intraday (dojis/hammers/engulfings AT the same price, repeatedly) is real support; a level chosen because a reversal candle printed near it, with no repeated defense, is a weaker bet even when everything else about the setup (grade, sizing, catalyst check) is done honestly. Manage/size these the same as any C-probe, but do not expect them to outperform multi-touch setups. (Promoted 2026-09-02 daily review from watch pattern W1, now with 2 instances: t-2026-08-31-002 CRWD -$247.54, opening_range_low never tested by a live dip before staging; t-2026-09-01-008 STDN -$135.51, thesis's own words: "not a clean single-level defense." Contrast same-week probes on genuinely multi-touch levels - ASND, CRCL, MRVL (4 touches) - which, while not all winners, at least tested the mechanism as designed.)

- **L7 — A trade is not bad until it is closed.** Unrealized drawdown inside the
  stop is the thesis still running, not evidence against it. Never exit early
  because a position is red: the levels you committed to in writing - stop,
  target, time_stop - ARE the decision, and overriding them because the mark
  looks ugly is exactly the panic the ledger will score as a process failure.
  The same cuts the other way: an open position in profit is not a win, must not
  be counted as one, and must not justify extra risk elsewhere. Only CLOSED
  trades are evidence - reviews score them, `stats.json` counts them, and watch
  patterns are built from them; an open book, green or red, proves nothing and
  may never be cited as evidence for or against a rule. When you do close, close
  for a reason written in advance; "it was down" is not one. (Operator rule,
  2026-09-02, at the user's direction.)

## Watch patterns (candidate lessons, not yet binding)

Hypotheses a review named but could not yet support with enough evidence. These
are NOT rules and must never be cited as one - they exist so a pattern spotted
once is still remembered when its second instance arrives. Every review reads
this section, checks each entry against the trades closed since, and either
promotes it to an Active lesson (evidence now sufficient), leaves it with the
new count, or discards it with a reason. A pattern that survives here with no
new instances for 15 trading days is discarded as noise.

- **W2 — a confirmation-breakout thesis whose sole analyst support is a single
  Hold-rated note (not Buy) paired with a lagging daily downtrend may be a
  weaker setup than volume alone suggests.** Volume/level confirmation
  (playbook s7/s2b) was genuine, but the "catalyst" itself was thin - one
  analyst, and even that one wasn't bullish. Seen 1x: CHPT (t-2026-09-03-004),
  confirmation-trigger entry, stopped out -$96.00 (-2.98%) within ~42 minutes.
  Added 2026-09-03 daily review. Revisit if a second instance of
  single-weak-note-plus-lagging-structure closes. Checked 2026-09-04 daily
  review against the day's only closes (TSLA x2, t-2026-09-03-006/008) - not
  a match (multi-catalyst B-grade thesis, not a single weak note), still
  n=1, no change. Checked again 2026-09-08 weekly review against the only
  trade closed since (CRWD rung1, t-2026-09-03-003, confirmation-trigger
  breakout that failed to continue past resistance) - not a match (real
  multi-headline catalyst cluster at entry, closed on a time-stop/structure
  downgrade, not a single-weak-note setup), still n=1, ~5 of 15 trading days
  elapsed, no promotion/discard. Checked again 2026-09-09 daily review against
  the only trade closed since (CRWD rung2, t-2026-09-03-005 - the second rung
  of the same ladder, closed on the identical decision) - not a match for the
  same reason, still n=1, ~6 of 15 trading days elapsed, no promotion/discard.
  Checked again 2026-09-14 weekly review against all 4 trades closed since
  (COIN t-2026-09-04-001, LITE t-2026-09-09-trg-08-001, META
  t-2026-09-10-trg-10-001, SMMT t-2026-09-03-007) - none match: COIN was an
  L8 support-pullback (not a confirmation-breakout), LITE and SMMT both had
  genuine multi-source/dated catalysts (Corning-Verizon deal + DB Buy init;
  Akeso Phase 3 readout) with bullish trend structure (not a lagging
  downtrend), META's catalyst (Meta Muse launch) likewise paired with a
  clean uptrend stack. Still n=1, ~9 of 15 trading days elapsed, no
  promotion/discard. Checked again 2026-09-15 weekly review: zero trades
  closed since the 2026-09-14 review (nothing to compare), still n=1, ~10 of
  15 trading days elapsed, no promotion/discard. Checked again 2026-09-16
  weekly review against the 2 trades closed since (APA t-2026-09-15-003, HOOD
  t-2026-09-04-003) - neither matches: APA is a momentum-continuation entry
  (s6a archetype, not a confirmation-breakout with an analyst-note catalyst)
  stopped out on a broad macro gap; HOOD is an anticipatory_limit
  support-pullback stopped out on a stock-specific negative news catalyst
  (DOJ charges), not a breakout thesis at all. Still n=1, ~11 of 15 trading
  days elapsed, no promotion/discard. Checked again 2026-09-18 weekly review
  against the 4 trades closed since (IOT t-2026-09-04-002, ANGX
  t-2026-09-10-trg-10-002, BWIN t-2026-09-14-001, SMTC-split
  t-2026-09-18-002) - none match: IOT is an anticipatory_limit trailed-stop
  exit with no breakout/catalyst framing; ANGX was a clean multi-touch
  breakout stopped via a watcher infra miss on the STOP (not a catalyst or
  thesis problem); BWIN is an s6a momentum entry, not a confirmation-breakout
  with an analyst note; SMTC-split's parent thesis was explicitly
  catalyst-agnostic (day_change alone, no analyst note at all, not even a
  weak one). Still n=1, ~13 of 15 trading days elapsed - close to the 15-day
  discard window with no second instance yet.

- **W3 — a momentum-continuation entry (s6a) whose own thesis discloses thin
  relative volume (well under 1.0x 20d avg) as a confirmation weakness may be
  more fragile to a violent gap reversal than a volume-confirmed instance of
  the same archetype.** Seen 1x: APA (t-2026-09-15-003) - structure gate
  passed cleanly and day 1 even confirmed with an up-close, but
  volume_vs_20d_avg was only 0.48x at entry (flagged honestly in the thesis
  itself, the same flag noted for TXG's B-grade). Overnight the position
  gapped straight through its mechanical stop on a broad risk-off shock (10Y
  yield >5%, Benzinga 2026-09-15) that overwhelmed even a sector-positive
  tailwind (oil >$105 same day). Scored "unlucky" not "wrong" precisely
  because the disclosed volume weakness cannot yet be shown to have CAUSED
  the gap - but the co-occurrence of thin-volume entry + fast, hard reversal
  is worth tracking. Added 2026-09-16 weekly review. Revisit if a second
  thin-volume (<1.0x) momentum entry closes, especially via a
  gap-through-stop rather than an orderly close-based exit. Checked again
  2026-09-18 weekly review against the only s6a momentum-continuation entry
  closed since (BWIN t-2026-09-14-001) - not a match: BWIN's own thesis
  disclosed volume_vs_20d_avg 17.68x at entry, the opposite of thin, and it
  exited cleanly on the governing close-pattern rule rather than a
  gap-through-stop. Still n=1, no promotion/discard.

## Archive

(Retired rules move here with the retirement reason and evidence.)

- **L4 — Activity is data (training window).** RETIRED 2026-09-15 weekly
  review. Original text: "Through 2026-09-04: an entry-less market-hours
  session is a failed session absent a hard blocker... The weekly review
  scores grade-vs-outcome to determine empirically where the bar belongs."
  (Operator seed rule, 2026-08-28.) The rule's own window closed 2026-09-04
  and SOP rule 6 says explicitly "After 2026-09-04 this directive expires and
  rule 6's normal form resumes" - no review formally closed it out until now,
  11 trading days late. Process note, not a trade-level finding: at least one
  ledger sizing_rationale since the window closed (t-2026-09-14-001 BWIN)
  still invoked "active-training directive: size on conviction, no
  floor/ceiling" - the sizing latitude itself is likely still valid under L1
  (mandate v4 removed the size caps permanently, not on a training-window
  timer), but citing an expired directive by name is sloppy and worth
  sessions catching themselves. Not reopening or rescoring any past trade
  over this - each was graded on its own merits above.
