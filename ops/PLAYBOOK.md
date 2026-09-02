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

## 7a. A resting dip-buy is adversely selected — buy the RECLAIM, not the dip

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

**Default entry is therefore CONFIRMATION, not anticipation.** Do not rest a
blind buy-limit at support and hope. Instead arm a trigger that fires when price
comes down to your level AND RECLAIMS it - a higher low, a reclaim of the level,
buyers visibly stepping in. Mechanically this is an armed trigger with condition
`>=` set just above the level, not a buy-limit `<=` below it. The watcher fires
it within ~1s, so nothing is lost in speed - what changes is that you enter when
the thesis is being CONFIRMED rather than only when it is failing.

An anticipatory resting limit is still allowed, but it is now the exception and
must justify itself in the ledger record: say why this level is worth buying
without confirmation (a level defended 3+ times, a forced seller, a gap-fill
you want regardless). Stamp every entry's `entry_mechanism` honestly - the
review compares realized P&L by mechanism, and that comparison is how this
rule gets kept or killed.

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
