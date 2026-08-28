# Watchlist - Monday battle plan

Maintained by `research` sessions (evenings/weekends). Each name: draft thesis, the
EXACT numeric trigger that turns it into a trade, planned size/stop/target/grade, and
the kill condition. Monday's pre-market planning leg reads this FIRST.

Built 2026-08-28 18:45 CT (Friday research session). Regime: SPY range/mixed (769.28,
+0.58% vs EMA21, RSI14 55.9), QQQ range/mixed (716.44, +0.34% vs EMA21, RSI14 51.4) - no
broad tailwind, trade levels per playbook s1. Source: `journal/universe_scan.json`
(17:53 CT shortlist, 1500 liquid names screened). **Caveat carried into every name
below: alpaca-paper/vibe-research MCP tools (news, screeners, fundamentals) were
unavailable this session (10+ consecutive sessions now) - every mover's CATALYST is
unconfirmed. Monday's planning leg should get_news check anything here before trusting
the technical read, especially the two staged orders below.**

## Ranked candidates

1. **MRVL** (STAGED - see below) - semiconductor, -10.48% day on 1.95x volume, TradingView
   sell/sell, but structure range/mixed (not downtrend) with support 211.13 tested 4x on
   5m bars into the close and holding. Range-bounce probe staged below Friday's close
   (216.55). Trigger already live via resting GTC limit at 211.50. If it does NOT fill:
   watch for a reclaim above opening_range_low 220.20 on volume as an alternate,
   stronger-confirmation entry (would upgrade grade). Kill: close below 202.00 (stop) or
   below 201.83 support with no bounce - stand aside, downtrend confirmed. next_earnings
   2026-12-01 (safe).

2. **PCG** (STAGED - see below) - utility, -7.54% day on 4.65x volume (real catalyst
   likely, unconfirmed), TradingView strong_sell throughout, but a hammer reversal tell
   AT support 16.53 printed at 19:55 CT after 3 prior tests held. Small conservative
   range-bounce probe staged below Friday's close (16.61) at 16.45. Kill: close below
   16.00 (stop) - if TradingView's bearish read is right and this is catalyst-driven,
   expect a gap through the stop, not a clean stop-out; Monday's open print is the first
   real test. next_earnings 2026-10-22 (safe).

3. **TENB** - cybersecurity, flat day but healthiest structure seen this scan: EMA9>EMA21>
   EMA50 (uptrend), TradingView buy/strong_buy, THREE separate 5m hammers (buyers defended
   37.98, 38.15, 37.24) despite one selling marubozu - repeated dip-buying all session.
   No genuine support close enough to Friday's close (37.65) to stage conservatively
   (nearest named support 34.62 is 8% away). WATCH, no order staged. Trigger: a pullback
   to the 36.00-36.50 VWAP/EMA21 zone that holds with a 5m higher low, OR a clean break
   above today's high 38.26 on rel_volume >= 1.5 - either would be a B-grade entry (real
   structure, not a level bet). Planned stop ~35.50 (under the defended 37.24 print isn't
   right for a fresh pullback entry - use whatever low actually holds, minus ~0.5xATR
   1.1), target 39.30 (first resistance). Kill: close below 34.62 (structure breaks).
   next_earnings 2026-10-28 (safe).

4. **AFRM** - BNPL, gapped +11.1% then faded hard to flat (day high 90.36 -> close 77.76),
   pos_in_20d_range 84.7%, repeated seller rejections AT resistance 78.69/80.65 in the
   last hour (shooting stars, bearish engulfing, doji) - a failed gap-and-go, exactly the
   playbook s9 "fade" pattern, not the "go" pattern. TradingView still strong_buy (lagging
   the fade). WATCH, no order staged - no clean level close enough to Friday's close in
   either direction to stage a probe without chasing or guessing the gap-fill depth.
   Two possible Monday triggers: (a) reclaim above 78.69-80.65 resistance on volume =
   gap-continuation long, stop below 74.51; or (b) a hold at support 74.51-72.97 on a
   pullback = bounce long, stop below 71.75. Either is a C-grade probe given the failed
   first attempt. next_earnings 2026-11-05 (safe).

5. **PYPL** - fintech, -12.68% day (gap -12.52%), RSI14 35.1, pos_in_20d_range 0% (at the
   day/range low), TradingView strong_sell, a 19:45 CT hammer+bullish-engulfing bounce
   attempt was immediately killed by a bearish engulfing at 19:50 - sellers still in
   firm control, no confirmed higher low. Classic falling-knife per playbook s2 (a watch
   item, not a buy, until structure turns). WATCH ONLY, no order staged - nearest support
   (43.74) is 18% below, far too deep to stage a probe against. Trigger: only a confirmed
   HIGHER LOW on daily/5m bars above the 52.73 day-low, not a bounce off it intraday.
   next_earnings 2026-10-27 (safe).

6. **ESTC** - already traded this week (t-2026-08-28-001, C-probe, closed flat/-0.26% on
   its own time-stop). Now extremely extended: RSI14 77.3, pos_in_20d_range 100%, gap_pct
   25.1% off Wednesday's close, zero resistance_above levels (broke through everything),
   and the last hour of 5m bars turned distinctly bearish into the close (shooting stars
   at 100.81/100.92, a marubozu sell, a bearish engulfing, four dojis) - momentum fading
   after the gap. WATCH ONLY, no order staged - too extended to buy and no fresh base has
   formed yet. Trigger: a genuine pullback to a NEW base (watch where 5m bars stop making
   new lows Monday) followed by a reclaim, not a chase of Friday's highs. Per L5 (this
   week's own lesson): if a ladder is used again here, weight whichever rung actually
   fills, not the one hoped for. next_earnings 2026-11-19 (safe).

7. **RBRK** - continued weakness, -13.11% day, closed AT the day low (93.02) after a week
   of grinding down from a post-earnings spike. Only one bullish 5m print (a 19:05
   marubozu) in an otherwise weak tape; TradingView mixed (moving_averages buy, oscillators
   sell) - no clean read. WATCH ONLY. Trigger: a confirmed higher low above 93.02 with a
   reclaim of 99.92 (first resistance) - until then this is a knife, not a bounce, per
   playbook s2. next_earnings 2026-12-03 (safe).

8. **IREN** - bitcoin miner, -12.6% day, key_levels structure explicitly "downtrend
   (lower highs + lower lows)" despite a late-session bullish attempt (bullish engulfing +
   two buying marubozu 19:00-19:20 CT, then compression). TradingView strong_sell.
   WATCH ONLY per playbook s2 (downtrend names are watch items until structure turns, no
   counter-trend catch). Trigger: a confirmed higher low forming above 34.81 (today's
   low) on a 5m/daily basis - not yet present. next_earnings 2026-11-05 (safe).

Pruned from consideration entirely (no tradable structure): VISN/IRE/MVLL/LPTH/BRUN/AEMD/
MSTX/SLS/CONL/SOLS/AXTI/XHLD/SOLT/SHAZ/CRML/LABU/AEHR/INFQ/LABD - sub-$3B or unrated
market cap, illiquid/gappy microcaps, or single-print volume spikes (GIGL/SPTB/PULS/IAUM/
PALL/ZSL/SCHP/EWJ/ACM/AIA/SUNB/ESI/LABD) with no repeatable level structure worth a
numeric trigger.

## Staged orders

- **MRVL** buy-limit 10 sh @ 211.50 GTC (order `5d4f1e58-3616-4a04-a3ba-c24fd633d2e1`),
  staged 2026-08-28 18:45 CT. Ledger: `t-2026-08-28-002` (pending_entry). Stop 202.00,
  target 222.64, time_stop 2026-09-03.
- **PCG** buy-limit 100 sh @ 16.45 GTC (order `cc6fe7f6-edcc-401a-a501-3e579b29b6e9`),
  staged 2026-08-28 18:45 CT. Ledger: `t-2026-08-28-003` (pending_entry). Stop 16.00,
  target 17.02, time_stop 2026-09-03.

Monday's planning leg (phase 0-1 of the `open`/first `continuous` session): re-check
`orders` for fills on both, re-check overnight news on both symbols before trusting
either level (neither could be news-verified this session), and cancel either whose
thesis is invalidated by a gap or a headline before the open.
