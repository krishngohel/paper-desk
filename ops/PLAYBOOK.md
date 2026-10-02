# Trading Playbook

Operator-authored craft reference, read every session alongside `journal/lessons.md`. The playbook is the prior; lessons are what YOUR results have proven or disproven. When a lesson contradicts the playbook, the lesson wins. The full measurement write-ups behind these sections live in `ops/archive/PLAYBOOK_full_2026-10-02.md`.

## 1. Read the tape before the ticker

Run `ta.py --market` first, every session. SPY/QQQ structure sets your posture:
- Both in uptrend structure: longs have tailwind; buy pullbacks to support/VWAP.
- Range/mixed: trade LEVELS (support/resistance bounces), smaller size, faster exits.
- Both in downtrend: long entries need stronger evidence and smaller size; probes only in the most resilient names, or cash.
A stock fighting the tape needs a stronger thesis than one moving with it.

## 2. Trend structure beats indicators

`structure` (higher highs/lows vs lower) from `key_levels` is the primary read; indicators confirm, they do not decide. Classic longs:
- **Pullback in an uptrend:** price pulls back to EMA21/VWAP/named support, holds (5m bars stop making new lows, volume dries up on the dip), then reclaims.
- **Breakout:** clears a `key_levels` resistance on `volume_vs_20d_avg` meaningfully above 1.0. Breakouts without volume are the market's favorite trap.
- **Range bounce:** only in range structure - buy tested support with the stop just below it; a close through the level kills the thesis.
Never knife-catch: a downtrend stock at support is a watch item until structure turns (a higher low forms).

### 2a. The trend gate - the desk's highest-value rule (a strong prior, not a proven edge)

Backtest, 400 days x 25 symbols: buying tested support with no trend requirement had expectancy that FLIPPED SIGN between periods (older 60%: -0.224%/trade, n=1496; newer 40%: +0.819%). Filtered to stocks whose own structure is up (`close > EMA21 > EMA50`), both periods were positive (+0.707%, n=342; +0.815%, n=279), across every mechanism and geometry tested (8 of 8). A SPY-trend filter made both periods worse; the stock's OWN trend is what works.

**Statistical status:** per-trade standard deviation is 7-9% against a ~0.8% mean, and the configuration was chosen from 81, so the bar is Sidak p < 6.3e-04. Neither gate-ON slice clears it (p 0.044 and 0.005); bootstrap says the sign is probably right (P(edge<=0) 2.2% and 0.13%) but the magnitude is unknown. Settling it needs ~959 trades (we have 335). Keep the rule - it flips a significantly LOSING configuration and its cost when wrong is trading less - but never size as if the edge is known. Kelly on the point estimate (~10% of equity) is a trap; with a confidence interval near zero, probe-scale is correct.

**Rules, binding:**
1. No long entry in a stock below its own EMA21, or whose EMA21 is below its EMA50. Range/mixed does not qualify; support in a non-uptrend name is a WATCH item.
2. Expect ~4x fewer setups. That is the mechanism working; no activity goal overrides it.
3. Prefer a 1.0x ATR stop and 2.5x ATR target (measured better in both periods with the filter on: +0.81% / +1.29%).

Live corroboration: 10 of the desk's first 12 closed trades were in names its own thesis called range or downtrend, and they carried essentially all the losses.

## 2b. Candle tells - anatomy at a level is information

`ta.py` detects candle patterns (`candles_daily`, `candles_5m_last_hour`), annotated when they print AT a level.
- **Location is everything.** A hammer AT support is entry evidence; mid-range it is noise. Unannotated patterns are context, never a thesis.
- **Confirmation beats prediction.** A reversal tell confirmed by the NEXT bar on volume, at a level, is B-grade or better; the tell alone is a C-probe.
- **Wicks are the fight's record.** Repeated upper wicks = sellers live there (target just below). Repeated lower wicks = defended floor (stop just under it, not inside it).
- **Inside bars/dojis are compression, not direction.** Only the upside break is actionable long; a downside break means stand down or tighten.
- Cite tells by their printed line ("5m hammer at 100.31 defended, next bar green").

## 3. VWAP is the intraday truth line

Above VWAP buyers control the day; pullbacks to VWAP that hold are entries. Below VWAP longs are counter-tape and need the daily structure to justify them. Repeated failures at VWAP from below = exit longs, don't add.

## 4. ATR is the ruler - stops, targets, and size come from it

- Stops live at a level, not a percent: below the support/pivot the thesis leans on, with ~0.5-1.0 ATR14 of room so noise cannot stop you out.
- Reward:risk >= 2:1 to the FIRST resistance for full-size entries; probes may run at >= 1:1 with reduced size, and the grade records the compromise.
- Size from risk: pick the dollar loss you accept if the stop hits (roughly 0.25-1% of equity is sane craft), then size from it and record the math. A tighter stop for a bigger size is a trap when the stop sits inside the noise.

**Slippage haircut (measured, mandatory).** `entry - stop` is what you INTEND to lose. Across the desk's closed losers, actual loss / planned risk ran median 1.05x, p90 **1.70x**, worst 1.75x - stops fill at market after the level trades, through gaps and spread. So:

    shares = risk_dollars / ((entry - stop) * 1.7)

That is ~40% fewer shares for the same stated risk. State both numbers ("planned $100; at 1.7x worst case ~$170; sized to keep that inside budget"). Two losses this does NOT cover: event gaps (§5) and infrastructure failure (a wedged gate once turned $55 of planned risk into a $239 loss) - size for them separately.

## 5. Events are gap risk that stops cannot protect

- Check `next_earnings` before EVERY entry. No new position within 2 trading days of earnings unless the thesis literally says "earnings play" and sizes for an 8-10% adverse gap.
- Preclose flags every holding with earnings before the next session in the journal AND the daily note; the default is exit or cut to token size before the print.
- Fed decisions and CPI mornings turn the whole tape into an event: reduce, don't chase.

## 6. Time of day changes the game

- First 30-45 min: widest ranges, falsest breakouts. The first-15-minute opening range matters all day; trading the open needs wider stops and smaller size.
- Midday (11:30-13:30 CT): thin, drifty chop where breakouts usually fail; favor patience.
- Last hour: volume returns, trends resume or reverse hard; exit day trades here, not in the closing auction.

## 6a. THE PRIMARY SETUP - momentum continuation (the only significance-cleared backtest edge)

It gets first call on capital; when it and a secondary setup are both available, prefer it.

- **Entry:** the last 3 daily closes strictly rising AND `close > EMA9 > EMA21`; enter at the next open. Never buy a down day.
- **Stop:** under the low of the launch bars (the entry bar and the one before it).
- **Exit:** two CONSECUTIVE lower closes, then sell - not one. **Hold:** days, until the exit fires.

Backtest (14 symbols, 400 days, 287 trades, 10 bp costs, stop assumed to fill first): exit on two down closes +1.96%/trade, t 2.85, p 4.3e-03 vs a Sidak bar of 8.5e-03 for 6 configurations - **significant**; average win +12.1% vs average loss -3.98%. Exiting on the FIRST down close halves it (+0.93%) because ordinary pullbacks inside an uptrend read as reversals. The same rules on 5-minute bars LOSE (-0.12%/trade, t -13.5, n=3,337): the edge lives in the holding period. Never run it intraday; get more trades by widening the universe, never by shortening the timeframe.

**Live caveat:** its first 6 labelled live trades won 1 (-$239), and it selects recent leaders, the bucket lesson L9 flags. The review tracks it in `by_archetype`; an s6a entry in the `leader_10pp+` bucket carries L9's written exception.

## 6b. Evidence standards - what may be called an edge

These bind reviews as much as entries.
- **A point estimate is not a finding.** Report n, standard deviation, and a confidence interval (bootstrap, since trade P&L is fat-tailed).
- **Correct for the search.** Comparing k configurations, the bar is Sidak p < 1-(1-0.05)^(1/k); the best of many is biased by construction.
- **Out-of-sample or it did not happen.** Fit on one time slice, verify on another; an effect that inverts between time slices is a regime, not an edge.
- **Say the sample size that would settle it** ("n >= 959 at this variance" is a plan; "need more data" is a shrug).
- **Size from the confidence interval, never the point estimate.** With an interval straddling zero, the growth-optimal bet is ~zero; half-Kelly on a lower bound at most.
- **Absence of significance is not proof of absence.** A sensible prior with a cheap failure mode may stay as policy, labelled unproven and never sized as proven.

## 7. Volume is the lie detector

Moves on low volume revert; on high volume they continue. `volume_vs_20d_avg` under ~0.7 is a quiet tape. **That gate applies to CONTINUATION theses only** (breakouts, gap-and-go, momentum - anything whose logic is "this keeps going"). A mean-reversion thesis bouncing off a level defended 2+ times is not disqualified by quiet volume - quiet tapes are where range trades live - but it still owes a defended level, a stop just beyond it, and smaller size. State which kind of thesis you hold before citing volume.

## 7a. Entry mechanism: confirmation vs resting limits

A buy-limit resting below the market is adversely selected: you only learn the level failed by getting filled, and when it holds and runs you get nothing. Backtest (2,555 setups, 20 symbols, 400 days):

| mechanism | fills | win rate | expectancy/trade |
|---|---|---|---|
| anticipatory limit | 1829 | 33.2% | +0.340% |
| confirmation, original stop | 1480 | 49.3% | +0.220% |
| confirmation, stop re-anchored to the fill | 1480 | 34.9% | +0.368% |

Confirmation raises the win rate, but buying higher with the old stop shrinks reward; win rate is a vanity metric. **If you take a confirmation entry, re-anchor stop AND target to your fill** using the §2a geometry (1.0x ATR below the entry, 2.5x ATR above), never the levels you would have used for the dip. Both mechanisms were positive in the backtest, and limits filled more often (1829 vs 1480), so over a day they produced more total profit despite the lower per-trade edge - neither is banned; choose per setup. Re-run the backtest before anyone changes this rule again. **Live, the desk's resting limits have lost** (`anticipatory_limit` 5 closed, 20% wins, -$99/trade vs `confirmation_trigger` 12 closed, +$29/trade, as of 2026-09-29), so every resting buy-limit's thesis must say why it should beat that record (SOP 3b). State the mechanism in `entry_mechanism`. At a 33% win rate, 8 losses in 9 trades happens by luck ~15% of the time - never manufacture a lesson from one streak.

## 7b. Tradability is the SPREAD, never the market cap

You pay the bid-ask spread entering AND exiting. `ta.py` returns a `tradability` verdict:
- **TRADABLE** (spread <= 1%): size normally.
- **TRADABLE_TIGHT_SIZE** (1-2.5%): size down; the target must clear the spread with room to spare.
- **UNTRADABLE** (> 2.5%, or no two-sided market): no trade at any size.

**Nothing is excluded by category (operator rule 2026-09-24):** every US stock, ETF, and ADR the broker can execute is a candidate - any market cap, share price, exchange (OTC included), sector, or source, including names that already ran. "Microcap", "mega-cap", "outside our focus", "crowd chatter", "too expensive per share", and "already moved" are category guesses; a pass cites a number measured for THAT symbol (spread, structure, RSI/extension, level, event date). Both directions have cost real trades (YDDL at a 0.89% spread dismissed as "microcap"; META, +38% in a month at a 0.01% spread, dismissed as "mega-cap"). Two checks remain beyond the spread: today's dollar volume, and whether the name can absorb your size without you becoming the move.

## 8. Known failure modes (the review looks for these by name)

- **Chasing:** buying after the move, far from any nameable level - no level, no stop, no trade.
- **Averaging down:** adding to a loser below its stop rationale. Add only into a WORKING thesis at the next planned level.
- **Stop-loosening:** stops move only in the trade's favor.
- **Revenge trading:** re-entering after a stop-out without a NEW written thesis.
- **Ungraded overtrading (grade inflation):** taking size in midday chop or a sub-0.7-volume tape while calling it A-grade. Quiet-tape entries are C-probes at probe size, labelled so.
- **Thesis drift:** a day trade silently becoming a "long-term hold" because it is red. The time_stop exists to kill this.

## 9. Setups the pros actually trade

- **ORB + VWAP:** `opening_range_high/low` from `ta.py` are the day's reference levels. A break of the opening-range high that is ALSO above VWAP, on relative volume >= 1.5, with `rs_vs_spy_pp` positive. Without volume or below VWAP it is the trap version.
- **Gap-and-go:** `gap_pct` >= 2 with a real catalyst (check WHY it gapped) and relative volume >= 2-3; trade the first pullback that holds above VWAP/opening-range low, stop under it. Gaps without catalysts fade more often than they go.
- **Relative strength is a tiebreaker only up to a point.** Intraday, a stock holding up while SPY sags shows real buyers. But on the 20-day measure, names already 10+ points ahead of SPY won 1 of 17 closed trades (-$1,589, the only bucket past the Sidak line - lesson L9), while names 0-10 points ahead or lagging carried the book. Prefer modest-to-in-line 20-day relative strength over the biggest runner; a leader needs L9's written exception.
- **Scale out in R-multiples:** at +2R take 30-50% off and move the stop to breakeven; trail the rest (EMA9 or higher lows); implement it with one broker OCO per lot (SOP, Environment). Exit rules are being measured live (`exit_replay`, SOP 2d); a measured result outranks this default.

## 10. Daily loss budget

Set your own daily loss budget in the first cycle each day and write it in the journal ("today's budget: 3R = $X"; typical budgets are 2-3x per-trade risk). When the day's realized + open losses hit it, or after 3 consecutive stop-outs, switch to MANAGE-ONLY for the rest of the day: exits and resting exits keep working, no new entries, triggers, or rungs. The daily review checks budget compliance; blowing through your own written budget is a named process failure regardless of P&L.

## 11. Trade the screen, not the reputation (LLM-specific)

- **Ticker-prior bias:** your knowledge of a company's story is not a signal; every thesis stands on cited on-screen numbers alone.
- **Bear case before size:** every A-grade full-size entry includes one honest paragraph arguing against itself (what makes it fail, who is selling to you and why) and answers it.
- **Down-tape denial:** LLM agents stay long too long in bearish markets. When the regime turns down, capital preservation IS outperformance - say so in the journal and act like it: smaller probes, faster time-stops, more cash.
- **Repeat-mistake check:** before entering a symbol, search the ledger for your prior trades in it; if you were stopped out, name what is different now.

## 12. The ledger is the strategy

Every stop/target/time_stop written at entry IS the risk system: the broker's resting orders and the watcher execute exactly what you wrote. Write levels you actually want executed at 3:07 pm without you.
