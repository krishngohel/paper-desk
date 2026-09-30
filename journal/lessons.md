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

- **L9 — A name that has already outrun SPY by 10+ points over 20 days is still
  a candidate, but the thesis must cite L9 and say, in writing, why this one is
  different; size it knowing the bucket's record.** Amended 2026-09-24 by operator
  rule "nothing is screened out": L9 was being read as a ban and kept META (+38%
  in a month) out of view. It is a disclosure and sizing rule, never an
  exclusion - a leader is worked up like any other name. The
  measured record: `by_rel_strength_20d.leader_10pp+` is 0 wins in 16 closed
  trades (rest of book 11 of 16 = 68.8%), total -$1,688.53, Fisher p = 0.00007
  vs the Sidak threshold 0.0019 (27 tests) - the only bucket to clear the
  corrected line. The same conditions read from the other side: 0-10pp
  outperformers 5/7 wins (+$807.20, p 0.032, suggestive) and names lagging SPY
  6/9 (+$419.21, p 0.035, suggestive) - so rank candidates by preferring
  in-line-to-modest relative strength over the biggest 20d runner. `ops/
  trade_context.py --check SYM PRICE` prints this bucket (SOP 4c); if it says
  `leader_10pp+`, the thesis must cite "L9" and give a concrete reason (dated
  catalyst not yet in the 20d move, base reset, etc.) - "momentum" or "sector
  rotation" alone is the reason the bucket lost. Caveats, stated plainly:
  correlation over a small overlapping sample (16 trades include same-symbol
  ladders - CRWD x3, TSLA x2 - so the effective n is lower and p is overstated
  in absolute terms, though it clears the line by ~27x), heavily clustered in
  the 08-28 to 09-15 trades, and NOT proven causal. It also sits in tension
  with the s6a momentum archetype, which by construction selects recent leaders
  - that tension is unresolved; s6a entries in this bucket must carry the
  written exception. Re-check as the sample grows; retire if the bucket's p
  drifts back above 0.2. (Added 2026-09-23 daily review. Evidence: the 16
  closed trades in stats.json `trend_signals.significant`; latest instances
  t-2026-09-15-004 ECO rs +34.22pp, t-2026-09-22-001 FIVN rs +11.99pp.)
  Re-checked 2026-09-25 daily review (34 closed): bucket unchanged at 0 wins
  in 16 (-$1,688.53), Fisher p 0.00013 vs Sidak 0.0019; the two trades
  closed since 09-23 (ARTY rs +4.91pp, MDB rs +4.91pp) were both outside
  the bucket. Still binding; not retired.
  Re-checked 2026-09-29 daily review (35 closed): bucket unchanged at 0 wins
  in 16 (-$1,688.53), p 0.00019 vs Sidak 0.0019 (27 tests). The one trade
  closed since (PLTR t-2026-09-25-001, rs +8.36pp) was outside the bucket
  and also lost. No entry to the bucket since 09-15; the sample is not
  growing, so this is a stale-but-standing result. Still binding.
  Re-checked 2026-09-30 daily review (37 closed): CRWD t-2026-09-14-002
  (rs +24.98pp, entered 09-21, scored today) is in the bucket and WON
  +$99.12 (mfe_atr 2.84), the bucket's first win: now 1 of 17, -$1,589.41,
  Fisher p 0.00175 vs Sidak 0.00183 (28 tests) - still on the significant
  side of the line, but by a hair, and the first counter-instance is in.
  Read plainly: that win was an anticipatory_limit pullback fill (232.00
  limit near EMA9/VWAP, dated sector-rotation catalyst, filled 3 of 6 sh),
  not a chase of the extension - consistent with the lesson's own
  "concrete reason" clause. n=1 win does not retire the rule; if the
  bucket's p crosses above 0.05 on further wins, retire it. Still binding.

## Watch patterns (candidate lessons, not yet binding)

Hypotheses a review named but could not yet support with enough evidence. These
are NOT rules and must never be cited as one - they exist so a pattern spotted
once is still remembered when its second instance arrives. Every review reads
this section, checks each entry against the trades closed since, and either
promotes it to an Active lesson (evidence now sufficient), leaves it with the
new count, or discards it with a reason. A pattern that survives here with no
new instances for 15 trading days is discarded as noise.

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

  Checked again 2026-09-23 daily review against the 6 trades scored
  today: SMTC (t-2026-09-16-001) entered at 0.21x volume - the disclosed thin
  volume - and WON +11.43% (mfe_atr 2.2), a direct counter-instance; ECO
  (0.83x) lost but by the orderly s6a two-lower-closes exit, not a gap. APA
  (t-2026-09-15-003) was re-audited from unlucky to wrong (mfe_atr 0.12).
  Tally: thin-volume entries 1 gap-reversal loss vs 1 clean win - the pattern
  is contradicted as often as supported. Still n=1 support; ~6 of 15 trading
  days elapsed. Leaning discard if no thin-volume gap reversal by ~2026-10-07.

  Checked again 2026-09-25 daily review against ARTY (t-2026-09-22-003,
  0.97x volume) and MDB (t-2026-09-23-001, 1.06x): neither is thin (<1.0x
  in the W3 sense is borderline for ARTY at 0.97x) and both exited by the
  orderly two-lower-closes rule, not a gap-through-stop. No new instance.
  Still n=1 support / 1 counter (SMTC). ~8 of 15 trading days elapsed.

  Checked again 2026-09-29 daily review against PLTR (t-2026-09-25-001):
  not a match (the 0.1x volume at entry was an 08:58 CT early-morning
  artifact the thesis itself disclaimed; it exited by the orderly
  two-lower-closes rule with the 182.94 stop never near). No new instance.
  ~10 of 15 trading days elapsed; discard on ~2026-10-07 absent a
  thin-volume gap reversal.

  Checked again 2026-09-30 daily review against MSFT (t-2026-09-30-001)
  and CRWD (t-2026-09-14-002): neither is an s6a entry (MSFT was a
  secondary-archetype resistance break, 0.12x volume an early-morning
  artifact; CRWD a pullback limit at 1.87x) and MSFT's exit was an
  ordinary stop inside a day, not a gap-through-stop. No new instance.
  ~11 of 15 trading days elapsed; discard on ~2026-10-07 as planned.

- **W4 - RSI14 at entry: 60-70 has lost every time; 45-60 has carried the
  book.** `by_rsi14_at_entry.strong_60-70`: 0 wins in 9 closed trades,
  -$994.07 (win rate vs rest of book 0% vs 47.8%, Fisher p 0.013);
  `neutral_45-60`: 10 of 19 wins (52.6% vs 7.7% for the rest, p 0.011,
  +$616.85). Both are suggestive only (p above the 0.0019 Sidak line, 27
  tests) and heavily entangled with L9 (leaders tend to have RSI 60-70; not
  independent evidence). Seen 1x (first recorded 2026-09-23 daily review).
  Promote if it crosses the Sidak line or if it still separates winners from
  losers after excluding `leader_10pp+` names; discard if p drifts above 0.2
  or after 15 trading days without support.
  Updated 2026-09-25 daily review (34 closed): still 0 wins in the
  `strong_60-70` bucket, now 10 trades / -$1,003.94 (Fisher p 0.0135), with
  ARTY (t-2026-09-22-003, RSI 62.2, rs +4.91pp, -$9.87) the newest loss.
  Independence test run (trade_context.json, closed trades with 20d rs
  under +10pp, i.e. not `leader_10pp+`): n=18; RSI 45-60 = 10 of 14 wins
  (+$1,372.64), RSI 60-70 = 0 of 2 (ASND -$171.95, ARTY -$9.87). Direction
  agrees, but n=2 outside the leader bucket is far too small to call the
  effect independent of L9. Seen 2x outside L9 names; still not promoted.
  Updated 2026-09-29 daily review (35 closed): `strong_60-70` is now 0 of
  11, -$1,061.96, p 0.0068 (Sidak 0.0019, so still suggestive); PLTR
  (t-2026-09-25-001, RSI 67.4, rs +8.36pp, mfe_atr 0.01, -$58.02) is the
  newest loss and the THIRD outside the leader bucket (ASND, ARTY, PLTR:
  0 of 3), against RSI 45-60 non-leaders at 10 of 14. Direction keeps
  agreeing but n=3 outside L9 is still too small to call it independent.
  Seen 3x outside L9. Practical note for sessions: PLTR's own thesis
  named this bucket and entered anyway, so the disclosure worked but did
  not change the decision; a strong_60-70 entry should size below a
  neutral_45-60 one until this resolves. Not promoted.
  Updated 2026-09-30 daily review (37 closed): `strong_60-70` is now
  1 of 12, -$962.84 - CRWD (t-2026-09-14-002, RSI 60.4, rs +24.98pp,
  +$99.12) is the bucket's first win, a counter-instance, though it is a
  leader_10pp+ name and so does not bear on the outside-L9 count (still
  0 of 3). MSFT (RSI 58.4) fell in neutral_45-60 and lost, so that bucket
  is 10 of 21 (47.6%, +$504.13, p 0.035, suggestive). Direction still
  agrees, the separation is weaker, n outside L9 unchanged at 3. Not
  promoted.

- **W5 - resting limit buys that fill AT the open have lost every time.**
  `by_entry_time.open_resting_fill`: 0 wins in 5 closed trades, -$715.10
  (expectancy -$143.02, vs -$15.05 book-wide); Fisher p not under 0.05, so
  this is anecdote-grade. It overlaps playbook s7a (resting dip-buys fill
  when the thesis is failing) and the `anticipatory_limit` scoreboard
  (5 post-09-02 trades, 20% wins, -$495.95), so it is probably the same
  effect seen through the time-of-day lens, not independent evidence.
  Seen 5x (first recorded 2026-09-25 daily review). Promote if it crosses
  p 0.05 with n>=8, or fold into s7a's mechanism finding; discard after 15
  trading days with no new instance or if a resting fill at the open wins.
  Checked 2026-09-30 daily review: CRWD t-2026-09-14-002 was a resting
  buy-limit that filled at the open (3 of 6 sh at 231.22, 08:30:13 CT) and
  WON +$99.12 - but `compute_stats` bucketed it as `first_hour`, not
  `open_resting_fill` (still 0 of 5, -$715.10), so the stats do not show
  the counter-instance. By the watch pattern's own discard clause ("if a
  resting fill at the open wins") this is a counter-instance: the pattern
  is now 0 of 5 bucketed plus 1 win by hand-classification. It is
  weakened, not discarded - the CRWD limit sat 9 days at a live EMA9 level
  on a leader in an intact uptrend, structurally different from the
  pre-09-15 gap-down open fills. Flag for the operator: the bucket rule
  in trade_context/compute_stats misses fills that arrive in the first
  minute via a partial fill on a multi-day-old order.

- **W6 - C-grade probes are the losing half of the book.** `by_grade`: C =
  14 closed, 2 wins (14.3%), -$545.10, expectancy -$38.94; B = 19 closed,
  8 wins (42.1%), +$25.37, expectancy +$1.34. Rough Fisher on C vs the rest
  is about p 0.06 (not under 0.05, not near the 0.0019 Sidak line), and C
  probes are mostly resting-limit rungs from research sessions, so it
  entangles with W5 and s7a. Seen once as a measured split (first recorded
  2026-09-25 daily review). Practical read for sizing only: a C-grade
  rung has no measured edge on this desk, so its size should reflect that.
  Promote if p crosses 0.05 with n>=20 C trades; discard if C's win rate
  converges to B's or after 15 trading days with no new C closes.
  Checked 2026-09-29: no C-grade trade has closed since 09-25 (C still 14
  closed, 2 wins, -$545.10), and the quota that produced the C rungs was
  retired today, so new C closes will be rare. W5 likewise: no new
  open-resting-fill (still 0 of 5, -$715.10). Both unchanged; the
  15-trading-day clock keeps running (~2026-10-16 for W6).
  Checked 2026-09-30: no C-grade trade closed (CRWD and MSFT were both
  B); C still 14 closed, 2 wins, -$545.10. Unchanged.

- **W7 - entries taken while SPY's own trend read "up" have done worse than
  entries in "mixed" markets.** `by_market_trend`: up = 18 closed, 3 wins
  (16.7%), -$858.15, expectancy -$47.67; mixed = 17 closed, 8 wins (47.1%),
  +$288.36, +$16.96. `stock_up+market_up` is 2 of 11 (18.2%, -$555.00).
  Rough Fisher on 3/18 vs 8/17 is about p 0.07, not near the 0.0019 Sidak
  line, and it is not in `trend_signals`. It is heavily entangled with L9
  (the 16 leader_10pp+ losses were bought in the late-August/early-
  September up tape) and with W4, so it is probably the same effect seen
  through the market lens, not independent evidence. Counter-intuitive
  enough (a tailwind should help) that it is worth tracking rather than
  believing. Checked 2026-09-30: CRWD and MSFT both entered in "mixed" SPY
  trend (won/lost), so `up` is unchanged at 3 of 18 (16.7%, -$858.15) and
  `mixed` is 9 of 19 (47.4%, +$314.54); no new `up` instance.
  Seen 1x (first recorded 2026-09-29 daily review). Promote only
  if it still separates after excluding `leader_10pp+` and RSI 60-70
  entries; discard if p drifts above 0.2 or after 15 trading days
  (~2026-10-20) with no supporting close.

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

- **W2 (watch pattern) - single Hold-rated analyst note plus lagging daily
  downtrend as a weak confirmation-breakout catalyst.** DISCARDED 2026-09-23
  daily review: n=1 (CHPT t-2026-09-03-004, -$96.00) for ~14 trading days
  through checks on 2026-09-04, 09-08, 09-09, 09-14, 09-15, 09-16, 09-18, and
  today (ZS, RBRK x2, ECO, SMTC, FIVN - none is a single-weak-note-plus-
  lagging-structure case), a second instance never arrived. Reason: 15-day
  no-new-instance rule.
