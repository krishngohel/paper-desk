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

- **L4 — Activity is data (training window).** Through 2026-09-04: an entry-less
  market-hours session is a failed session absent a hard blocker (halt/expiry/
  closed market/broken data). Selectivity is expressed through setup GRADES and
  probe sizing, never through abstaining - a C-grade probe that loses teaches
  more than a hold that proves nothing. The weekly review scores grade-vs-outcome
  to determine empirically where the bar belongs. (Operator seed rule,
  2026-08-28, at the user's direction.)

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

(none currently - W1 promoted to L8 in the 2026-09-02 daily review.)

## Archive

(Retired rules move here with the retirement reason and evidence.)
