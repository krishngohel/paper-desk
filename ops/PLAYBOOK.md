# Trading Playbook

Operator-authored craft reference. Read it at the start of every session alongside
`journal/lessons.md`. Difference between the two: the playbook is the baseline of
known trading craft; lessons are what YOUR results have proven or disproven. When
a lesson contradicts the playbook, the lesson wins - it is evidence, this is prior.

## 1. Read the tape before the ticker

Run `ta.py --market` first, every session. SPY/QQQ structure sets your posture:
- Both in uptrend structure: longs have tailwind; buy pullbacks to support/VWAP.
- Range/mixed: trade LEVELS (support/resistance bounces), smaller size, faster exits.
- Both in downtrend: long entries need stronger evidence and smaller size. (During a
  training window with an activity floor, this means C-grade probes at token size in
  the most resilient names - the floor is satisfied honestly, never by abstaining.)
A stock fighting the tape needs a stronger thesis than one moving with it.

## 2. Trend structure beats indicators

`structure` (higher-highs/higher-lows vs lower) from key_levels is the primary read;
indicators confirm, they do not decide. Classic longs:
- **Pullback-in-uptrend**: structure up, price pulls back to EMA21/VWAP/named support,
  holds it (5m bars stop making new lows, volume dries up on the dip), then reclaims.
- **Breakout**: price clears a resistance level from key_levels on volume_vs_20d_avg
  meaningfully above 1.0. Breakouts WITHOUT volume are the market's favorite trap.
- **Range bounce**: only in range structure - buy at tested support with the stop just
  below it; the level IS the trade, so a close through it kills the thesis.
Do not counter-trend "knife-catch": a downtrend stock at support is a watch item,
not a buy, until structure turns (a higher low forms).

### 2a. MEASURED 2026-09-03 - this is the single highest-value rule on the desk

This section was an assertion for a week. It has now been tested on 400 days x
25 symbols, and it is the difference between a losing strategy and a winning one.
Buying a tested support level with NO trend requirement, versus the same setups
filtered to stocks whose own structure is up (close > EMA21 > EMA50):

| period | filter | trades | win rate | expectancy/trade |
|---|---|---|---|---|
| older 60% | none | 1496 | 28.6% | **-0.224%** |
| older 60% | stock uptrend | 342 | 41.5% | **+0.707%** |
| newer 40% | none | 877 | 38.4% | +0.819% |
| newer 40% | stock uptrend | 279 | 40.1% | +0.815% |

Unfiltered, the strategy's expectancy FLIPS SIGN between periods - it made money
in one market and lost it in another, and no stop/target geometry fixed that (a
27-config sweep produced train mean -0.65% vs test mean +1.61%; a SPY-above-EMA21
market filter made both periods worse). The stock's OWN trend is what fixed it:
positive expectancy in both halves, across both entry mechanisms and both
geometries tested - 8 of 8 combinations profitable.

### Statistical status - added 2026-09-04, and it downgrades the claim above

The table was reported as settled. It is not. Running the proper tests:

| slice | trades | mean/trade | t | p | verdict |
|---|---|---|---|---|---|
| older 60%, gate OFF | 1489 | -0.42% | -2.3 | 0.02 | losing, real |
| older 60%, gate ON | 335 | +0.77% | 2.02 | 0.044 | **not significant** |
| newer 40%, gate ON | 283 | +1.34% | 2.84 | 0.005 | **not significant** |

Per-trade standard deviation is 7-9%, which is enormous next to a ~0.8% mean.
And the configuration was chosen after searching 81 combinations, so the honest
bar is the Sidak-corrected one: **p < 6.3e-04**, not 0.05. Neither gate-ON
result clears it. Bootstrap agrees (P(edge<=0) = 2.2% train, 0.13% test) - the
sign is probably right, the magnitude is not established.

**What would settle it: about 959 trades** at the observed mean and variance;
we have 335. That is ~3x more history or symbols, and it is the reason to widen
the backtest universe rather than to trade harder.

**So treat 2a as a well-motivated prior, not a proven edge.** Keep it - it
agrees with s2's long-standing craft argument, it flips the sign of a
significantly-losing configuration, and its cost when wrong is trading less.
But do NOT size as though the edge is known.

**Sizing follows from that.** Kelly on the point estimate says risk ~10% of
equity per trade (b=2.16, p=0.456). That number is a trap: Kelly assumes the
edge is measured exactly, and ours has a 95% CI whose lower bound is ~0.03%/trade
- indistinguishable from zero. When the CI includes ~zero, the growth-optimal
bet also rounds to ~zero. Size like an unproven edge: probe-scale, and let the
sample accumulate. Overbetting an edge that turns out to be noise is the fastest
way to hit the death floor, and the penalty for overbetting is mathematically
far worse than for underbetting.

**Rules, binding:**
1. **No long entry in a stock trading below its own EMA21, or whose EMA21 is
   below its EMA50.** Range/mixed structure does NOT qualify - the measured edge
   requires an actual uptrend. A support level in a non-uptrend name is a WATCH
   item; say so and move on.
2. **Expect to trade far less.** The filter cut trade count by ~4x (1496 -> 342).
   That is the mechanism working, not a failure to find setups, and it overrides
   any activity target: L4's floor is satisfied by an honest hunt, never by
   taking a setup this rule forbids.
3. **Prefer a 1.0xATR stop and 2.5xATR target** over the old 0.5/1.5. Measured
   better in both periods with the filter on (train +0.81%, test +1.29%).

**Corroboration from the live book:** of the desk's first 12 closed trades, 10
were entered in names its own thesis described as "range", "range/mixed", or
"downtrend" - i.e. this rule would have forbidden them. Those 10 are where
essentially all the losses came from. The rule was in the playbook the whole
time; nothing enforced it at setup selection.

## 2b. Candle tells - anatomy at a level is information

`ta.py` detects candle patterns mechanically (`candles_daily`, `candles_5m_last_hour`):
doji, hammer, shooting star, marubozu, engulfing, inside bar, morning star - each
annotated when it printed AT a support/resistance level. Read them like this:
- **Location is everything.** A hammer AT SUPPORT = buyers defended a level that
  matters (entry evidence). The same hammer mid-range is noise. Patterns without a
  level annotation are context, never a thesis.
- **Confirmation beats prediction.** A reversal tell (hammer, morning star, engulfing)
  is confirmed by the NEXT bar going its way on volume; entering on the tell alone is
  a C-grade probe, entering on tell + confirmation + level is B or better.
- **Wicks are the fight's record.** Repeated upper wicks at a price = sellers live
  there (your target belongs just below it). Repeated lower wicks = defended floor
  (stop belongs just under it, not inside it).
- **Inside bars/dojis are compression, not direction** - they mark WHERE a move will
  start, the break direction decides which side you take (long-only: only the upside
  break is actionable; a downside break just means stand down or tighten stops).
- Cite tells by their printed line ("5m hammer at 100.31 defended, next bar green")
  in the thesis, same as levels and indicator numbers.

## 3. VWAP is the intraday truth line

Above VWAP: buyers control the day; pullbacks TO VWAP that hold are entries.
Below VWAP: sellers control; longs are counter-tape and need the daily structure
to justify them. Repeated failures at VWAP from below = exit longs, don't add.

## 4. ATR is the ruler - stops, targets, and size come from it

- Stops live at a level, not a percent: below the support/pivot your thesis leans on,
  with breathing room ~0.5-1.0 ATR14 so normal noise cannot stop you out.
- Reward:risk >= 2:1 to the FIRST resistance for full-size entries. (Probes under an
  active training directive may run at >=1:1 with reduced size - the grade records the
  compromise so the review can price it.)
- Size from risk, not conviction alone: decide the dollar loss you accept if the stop
  hits (for this book, roughly 0.25-1% of equity per trade is sane craft), then
  shares = risk_dollars / (entry - stop). Record this math in the sizing rationale.
  Tighter stop -> larger size is a trap when the stop is inside the noise band.

**SLIPPAGE HAIRCUT (measured 2026-09-04, mandatory).** `entry - stop` is what you
INTEND to lose, not what you lose. Measured across the desk's own closed losers
(gate-wedge trades excluded): actual loss / planned risk ran median 1.05x, mean
1.07x, p90 **1.70x**, worst **1.75x**. A stop is an instruction to sell at market
once a level trades, not a guaranteed fill - gaps, spread, and one-bar slides all
land on your side of it.

So compute size with a haircut, not the nominal stop:

    effective_risk_per_share = (entry - stop) * 1.7        # p90, not the median
    shares = risk_dollars / effective_risk_per_share

Sizing to the p90 rather than the median is deliberate: risk budgets exist to
survive the bad tail, and a budget that is only right half the time is not a
budget. In practice this means **~40% fewer shares** for the same stated risk.
State both numbers in the sizing rationale ("planned risk $100; at the 1.7x
measured slippage factor, worst-case ~$170; sized to keep THAT inside budget").

Two loss sources this does NOT cover, and which must be sized for separately:
event gaps (playbook s5 - an earnings print can gap 8-10% straight through any
stop) and infrastructure failure (a wedged order gate turned a $55 planned risk
into a $239 loss on 2026-09-03; the watcher now auto-clears provably-phantom
markers, but assume some exposure remains).

## 5. Events are gap risk that stops cannot protect

Stops execute only while the market trades. An earnings print gaps straight through
them. Hard rules:
- `next_earnings` is checked before EVERY entry. No new position within 2 trading
  days of that symbol's earnings unless the thesis literally says "earnings play"
  and sizes for a possible 8-10% adverse gap.
- Preclose flags every holding with earnings before the next session in the journal
  AND the daily note; default action is to exit or cut to token size before the print.
- Macro days (Fed decisions, CPI mornings) turn the whole tape into an event: if the
  market whipsaws violently around a scheduled time, that is why - reduce, don't chase.

## 6. Time of day changes the game

- First 30-45 min: widest ranges, falsest breakouts. Levels from the FIRST 15 minutes
  (opening range) matter all day. Trading the open needs wider stops = smaller size.
- Midday (11:30-13:30 CT is the quietest stretch): thin volume, drifty chop -
  breakouts here usually fail; favor patience over action.
- Last hour: volume returns, trends resume or reverse hard; day-trade exits happen
  here, not in the close auction. Preclose session cleans the book deliberately.

## 7. Volume is the lie detector

Price moves on low volume revert; on high volume they continue. volume_vs_20d_avg
under ~0.7 = a quiet tape whose signals are weak. A level break on 2x volume is
information; the same break on 0.5x is noise.

**Scope: the 0.7 threshold gates CONTINUATION theses, not every setup.** Read the
sentence above literally - it is about a *level break* being real. Volume is the
evidence that buyers are committing, so it is mandatory for breakouts, gap-and-go,
momentum, and any thesis whose logic is "this move keeps going."

The mirror case is different. If the thesis is mean reversion - price is bouncing
off a level it has defended repeatedly, and you expect it to revert INTO the
range rather than break out of it - then low volume is not disqualifying. Quiet
tapes are precisely where range trades live: the same 0.5x volume that makes a
breakout a lie makes a range hold more likely. What such a trade still owes you
is a level the tape has actually defended (two or more touches you can point to),
a stop just beyond it, and smaller size, because a quiet tape also means thinner
exits.

Applying the 0.7 gate to every candidate turns any range-bound day into a
mandatory no-trade day - on 2026-08-31 it passed eight of ten names in a
range/mixed regime, several of which were bouncing off defended support. That is
the rule misfiring, not the market being empty. State which kind of thesis you
hold BEFORE citing volume, and apply the gate only to continuation setups.

## 6a. THE PRIMARY SETUP - momentum continuation (the only measured edge)

Added 2026-09-10. Everything else in this playbook is craft or prior. This is the
one archetype that has cleared a properly corrected significance test, so it gets
first call on capital and attention.

**The setup, exactly:**
- **Entry:** the last **3 daily closes strictly rising**, AND `close > EMA9 > EMA21`.
  Enter at the next open. Never buy a down day - "any downward motion, don't buy".
- **Stop:** under the low of the launch bars (the entry bar and the one before it).
- **Exit:** **two CONSECUTIVE lower closes**, then sell. Not one.
- **Hold:** days, not minutes. Let it run until the exit rule fires.

**Measured** (14 symbols, 400 days, 287 trades, costs 10bp round trip, stop
assumed to fill before target, gaps at the open):

| exit rule | trades | win rate | net/trade | t |
|---|---|---|---|---|
| first down close | 287 | 45.6% | +0.93% | 2.22 |
| break of prior low | 287 | 40.8% | +1.03% | 2.27 |
| **two down closes** | **287** | **36.9%** | **+1.96%** | **2.85** |

p = 4.3e-03 against a Sidak bar of 8.5e-03 for the 6 configurations searched -
**significant**. Average win **+12.1%** against average loss -3.98%.

**Why two down closes, not one.** This is the counter-intuitive part and the
whole edge: exiting on the FIRST down day halves expectancy (+0.93% vs +1.96%)
because average win collapses from 12.1% to 6.1%. Ordinary pullbacks inside a
real uptrend read as reversals. You must sit through one down day.

**Why this must NOT be run intraday.** The identical rules on 5-minute bars lose
-0.12%/trade with t = -13.5 across 3,337 trades - reliably, significantly
negative. Win rate collapses to 18.7% because entering after 2-3 rising bars buys
a local high and exiting on the first turn sells a local low. The edge lives in
the HOLDING PERIOD: a fixed ~0.10% round-trip cost is rounding error on a 12%
move and fatal on a 0.3% one. Scalping this idea is not a smaller version of it,
it is the inverse of it.

**Expect roughly one trade every other day per 14 symbols.** More volume comes
from widening the symbol universe, never from shortening the timeframe.

## 6b. Evidence standards - what may be called an edge

Adopted 2026-09-04 after a measured "improvement" failed its own significance
test. These are the rules for believing a number, and they bind reviews as much
as entries.

- **A point estimate is not a finding.** Report n, standard deviation, and a
  confidence interval with any expectancy claim. Trade P&L is fat-tailed and
  skewed, so prefer the bootstrap interval over the normal one.
- **Correct for the search.** If k configurations were compared, the bar is
  Sidak: p < 1-(1-0.05)^(1/k). Searching 81 configs at p<0.05 finds a false
  "winner" ~98% of the time. The best of many is a biased estimate by
  construction.
- **Out-of-sample or it did not happen.** Fit on one time slice, verify on
  another. An effect that inverts between slices (as stop/target geometry did
  here) is a regime, not an edge.
- **Say the sample size that would settle it.** "n>=959 at this variance" is a
  plan; "we need more data" is a shrug.
- **Size from the CI, never the point estimate.** Kelly is exact only when the
  edge is known exactly. With an interval straddling zero, the growth-optimal
  bet is ~zero. Half-Kelly on a lower-bound edge, never full Kelly on a mean.
- **Absence of significance is not proof of absence.** A sensible prior with a
  cheap failure mode (like s2a) may be kept as policy while its evidence
  accumulates - but it must be LABELLED unproven, and never sized as if proven.

## 7a. Entry mechanism: what the backtest actually proved

A buy-limit resting below the market is a bet that a level holds. But you only
ever learn it did NOT hold by getting filled: the fill IS the evidence against
your thesis. When the level holds and the stock runs, you get nothing. So the
mechanism systematically fills you on your losers and misses your winners.

Measured on this desk's first 21 ledger records (2026-09-02): 10 anticipatory
limits filled -> 5 of the 6 that closed were losses. Of the 9 that never filled,
SOLS never traded within $0.56 of our level and ran +8%, and TITN dipped to our
level then ran +15%. The winners escaped; the losers filled. ASND is the whole
pattern in one trade: the ladder sat unfilled while price ran to 268.20, then
price reversed, filled us on the way down, and stopped us out for -$171.95.

**CORRECTED 2026-09-02 by backtest (2,555 setups, 20 symbols, 400 days, each
setup tested every way; costs 10bp round trip; stop assumed to fill before
target; gaps fill at the open).** The intuition above is only half right, and
the naive fix was WORSE than the disease:

| mechanism | fills | win rate | expectancy/trade |
|---|---|---|---|
| anticipatory limit | 1829 | 33.2% | +0.340% |
| confirmation, same stop | 1480 | 49.3% | **+0.220%** |
| confirmation, stop re-anchored to the fill | 1480 | 34.9% | **+0.368%** |

Read those rows carefully, because they say three different things:

1. **Confirmation really does raise the win rate** - 33% to 49%, a huge jump.
   The adverse-selection intuition is REAL.
2. **But winning more often is not the same as making more money.** Buying the
   reclaim means buying higher; keeping the original stop then shrinks reward
   and widens risk, and the naive version gives back more edge than the extra
   wins are worth. Win rate is a vanity metric.
3. **Re-anchoring the stop to the actual fill fixes it** - stop 0.5xATR below
   your ENTRY, target 1.5xATR above your ENTRY, not below/above the original
   level. Then confirmation is the best arm per trade.

**Rules that follow.** If you take a confirmation entry, re-anchor stop AND
target to your fill price; never inherit the levels you would have used had you
bought the dip. And note the throughput trade-off: anticipatory limits filled
1829 times vs 1480, so over a day they produce MORE total profit despite lower
per-trade edge. Both are positive-expectancy; neither is banned. Choose per
setup, state which you used in `entry_mechanism`, and re-run the backtest
before anyone changes this rule again.

**The most important number here is not in the table:** at a 33% win rate,
losing 8 of 9 trades has a ~15% chance of happening by pure luck. The desk's
first losing streak was NOT evidence of a broken strategy, and the review must
not manufacture lessons from it.

## 7b. Tradability is the SPREAD, never the market cap

Small does not mean untradable. The question is only ever: can I get in and out
at a sane price? You cross the bid-ask spread entering AND exiting, so the
spread is a fixed toll you pay before any profit exists.

`ta.py SYM` returns a `tradability` block with the measured spread and a verdict:

- **TRADABLE** (spread <= 1%): normal cost, size normally.
- **TRADABLE_TIGHT_SIZE** (1-2.5%): real toll. Size down and demand a target
  that clears the spread with room to spare - a 2% scalp on a 2% spread is a
  guaranteed loss.
- **UNTRADABLE** (>2.5%, or no two-sided market): no trade exists here at any
  size. A 20% spread means you are down 20% the instant you fill.

**Never exclude a name as "microcap" or "small cap" as a category.** That is a
guess standing in for a measurement, and on 2026-08-31 it cost a real
opportunity: WETO/AEHL/NCRA were rightly passed (16-29% spreads) but YDDL was
dismissed in the same breath while carrying a 0.89% spread and $68M of volume -
a perfectly tradable name thrown out by association. If a mover clears the
spread test and has real dollar volume, it earns a full workup regardless of
how small the company is. Reject it on structure, extension, or catalyst if the
evidence says so - but reject it on evidence, one name at a time.

Two liquidity checks remain independent of spread: today's dollar volume (thin
books slip on exit even when the quoted spread looks fine) and whether the name
can absorb your intended size without you becoming the move.

## 8. Known failure modes (the review will look for these by name)

- **Chasing**: buying AFTER the move, far from any level, because it is running.
  If the entry isn't near a level you can name, there is no stop, hence no trade.
- **Averaging down**: adding to a loser below your stop rationale. Adding is only
  valid into a WORKING thesis at the next planned level.
- **Stop-loosening**: moving a stop away from price to avoid taking the loss.
  Stops move only in the trade's favor.
- **Revenge trading**: re-entering a symbol immediately after a stop-out without a
  NEW thesis. One stop-out = that thesis is dead; write why before touching it again.
- **Ungraded overtrading**: taking size in midday chop or sub-0.7 volume tape while
  calling it A-grade. Under an activity floor the failure mode is not trading often -
  it is LYING ABOUT GRADES. Quiet-tape entries are C-probes at probe size, labeled so.
- **Thesis drift**: a day trade silently becoming a "long-term hold" because it's red.
  The time_stop exists precisely to kill this.

## 9. Setups the pros actually trade (research-backed archetypes)

- **ORB + VWAP double confirmation** (the classic): `opening_range_high/low` from ta.py
  are the day's reference levels. A break of ORH that is ALSO above VWAP, on relative
  volume >= 1.5, with `rs_vs_spy_pp` positive, is the highest-probability long of the
  morning. A break WITHOUT volume or below VWAP is the trap version.
- **Gap-and-Go**: `gap_pct` >= 2 with a real catalyst (check news - WHY did it gap) and
  rel_volume >= 2-3: trade the first pullback that holds above VWAP/ORL, stop under it.
  Gaps without catalysts fade more often than they go.
- **Relative strength is the tiebreaker**: between two setups, take the one whose
  `rs_vs_spy_pp` is higher - a stock shrugging off a weak tape has real buyers.
- **Scale out in R-multiples**: at +2R take 30-50% off and move the stop to breakeven;
  trail the rest (EMA9 or higher-lows). All-or-nothing exits leave money on both sides;
  ladder your target rungs to implement this mechanically.

## 10. Daily loss budget - the one rule every professional shares

Set YOUR OWN daily loss budget in the first cycle of each day (write it in the journal:
e.g. "today's budget: 3R = $X"). When the day's realized+open losses hit it, or after 3
consecutive stop-outs, switch to MANAGE-ONLY for the rest of the day: exits and brackets
keep working, no new entries. This is not an operator cap - it is the self-discipline
that separates traders from tilt (documented across every professional risk framework:
typical budgets are 2-3x per-trade risk). The weekly review checks budget compliance;
blowing through your own written budget is a named process failure regardless of P&L.

## 11. Trade the screen, not the reputation (LLM-specific, benchmark-documented)

Research on LLM trading agents (StockBench, memory-controlled benchmarks) documents the
failure modes YOU are most at risk of:
- **Ticker-prior bias**: "knowing" a company from training data and trading that opinion
  instead of the chart in front of you. Your knowledge of a company's story is NOT a
  signal - the bars, levels, volume, and catalyst on screen are. Every thesis must stand
  on cited on-screen numbers alone.
- **Bear-case debate before size**: for every A-grade full-size entry, write the honest
  bear case against your own thesis (one paragraph: what would make this fail, who is
  selling to you and why) and answer it. Multi-agent research shows adversarial review
  materially improves decisions; you are both analysts.
- **Down-tape denial**: LLM agents systematically underperform in bearish markets by
  staying too long. When the regime turns down, capital preservation IS outperformance -
  say it in the journal and act like it (smaller probes, faster time-stops, more cash).
- **Repeat-mistake check**: before entering any symbol, search the ledger for your prior
  trades in it - if you were stopped out, name what is DIFFERENT now.

## 12. The ledger is the strategy

Every trade's stop/target/time_stop written at entry IS the risk management system -
the watcher and resting orders execute exactly what you wrote. Sloppy levels = sloppy
machine behavior. Write levels you actually want executed at 3:07pm without you.
