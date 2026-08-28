# Trading Playbook

Operator-authored craft reference. Read it at the start of every session alongside
`journal/lessons.md`. Difference between the two: the playbook is the baseline of
known trading craft; lessons are what YOUR results have proven or disproven. When
a lesson contradicts the playbook, the lesson wins - it is evidence, this is prior.

## 1. Read the tape before the ticker

Run `ta.py --market` first, every session. SPY/QQQ structure sets your posture:
- Both in uptrend structure: longs have tailwind; buy pullbacks to support/VWAP.
- Range/mixed: trade LEVELS (support/resistance bounces), smaller size, faster exits.
- Both in downtrend: long entries need exceptional evidence; mostly stand aside -
  cash is a position and this book is long-only by design.
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

## 3. VWAP is the intraday truth line

Above VWAP: buyers control the day; pullbacks TO VWAP that hold are entries.
Below VWAP: sellers control; longs are counter-tape and need the daily structure
to justify them. Repeated failures at VWAP from below = exit longs, don't add.

## 4. ATR is the ruler - stops, targets, and size come from it

- Stops live at a level, not a percent: below the support/pivot your thesis leans on,
  with breathing room ~0.5-1.0 ATR14 so normal noise cannot stop you out.
- Reward:risk >= 2:1 to the FIRST resistance. If the next resistance is closer than
  2x your stop distance, the trade doesn't pay - skip it.
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

## 8. Known failure modes (the review will look for these by name)

- **Chasing**: buying AFTER the move, far from any level, because it is running.
  If the entry isn't near a level you can name, there is no stop, hence no trade.
- **Averaging down**: adding to a loser below your stop rationale. Adding is only
  valid into a WORKING thesis at the next planned level.
- **Stop-loosening**: moving a stop away from price to avoid taking the loss.
  Stops move only in the trade's favor.
- **Revenge trading**: re-entering a symbol immediately after a stop-out without a
  NEW thesis. One stop-out = that thesis is dead; write why before touching it again.
- **Overtrading quiet tape**: forcing entries in midday chop or sub-0.7 volume days
  to feel productive. The directive asks for your best trades, not constant ones.
- **Thesis drift**: a day trade silently becoming a "long-term hold" because it's red.
  The time_stop exists precisely to kill this.

## 9. The ledger is the strategy

Every trade's stop/target/time_stop written at entry IS the risk management system -
the watcher and resting orders execute exactly what you wrote. Sloppy levels = sloppy
machine behavior. Write levels you actually want executed at 3:07pm without you.
