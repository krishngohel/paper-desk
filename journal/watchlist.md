# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-02 17:xx CT (evening research session, market closed). Regime: SPY
range/mixed (765.16, +0.05% vs EMA21, RSI14 52.0), QQQ range/mixed (709.24, -0.57% vs
EMA21, RSI14 47.8). Today's book: 4 stop-outs (MRNA -75.13, STDN -135.51, MRVL -57.62,
CRK -96.00) offset by DELL's +81.94 target win = net -282.32 realized; loss budget hit
at 12:16 CT, MANAGE-ONLY the rest of the day (daily review already scored all 5,
promoted W1->L8). **No new orders placed this session** - still 2026-09-02, playbook
s10's MANAGE-ONLY carries through the calendar day; tomorrow's (2026-09-03) planning
leg sets a fresh loss budget and is the first session cleared to act on anything below.
Standing-order quota: 0 live (suspended, loss budget hit - correct per SOP s3b).

**New macro/sector thread found this session:** cloud/software names that BEAT
earnings and RAISED guidance sold off hard anyway on cost/margin concerns - MDB
-12.67% (Q3 beat, but "costs surged" per Benzinga), PANW -8.95% (beat + CEO touting a
"$1T cyber replacement cycle"), CRDO -20% - all same session, all with sell-side desks
RAISING price targets even as the stocks fell (Scotiabank/Citigroup/Goldman on MDB;
Citigroup/Roth/Oppenheimer/Piper Sandler on PANW, targets 15-70% above spot). Distinct
from yesterday's bond-yield-rout theme but rhymes with it - richly-valued software
multiples getting compressed on valuation/cost fears even when execution is fine.
Watch for a confirmed higher low before treating any of these as a bounce, not before.

## Book (1 position)

- **DUOL** 35 sh @ avg 156.41, last 158.00 (+1.02% ROI). Stop 153.75 (2.76% clear),
  target 165.00 resting GTC (`6fa761f6...`). next_earnings 2026-11-04 (safe). No action
  this session (research sessions don't touch working book positions). Time_stop
  2026-09-04.

## Top candidates for tomorrow's planning leg (ranked, none staged tonight)

- **HPE** - NEW name (duty 1b, Reddit rank-climber +147 spots, confirmed via full
  ta.py+get_news workup). Reported Q3 after today's close: adj EPS $1.11 beat $0.93
  est, sales $12.21B beat $11.91B est, RAISED FY26 adj EPS guidance $3.35-3.45 ->
  $3.75-3.85 (vs $3.43 est) and sales guidance up ~$1.7B at the midpoint, Q4 guide
  well above street ($1.20-1.30 EPS vs $1.07 est). CEO: server demand "exceptionally
  high," pipeline "multiples of backlog"; CFO flagged a NEW multi-billion-dollar
  hyperscaler server deal signed after quarter-end. Despite all this, shares slid
  (Benzinga: "Shares Slide Lower Despite Strong Q3, Raised Guidance") - a violent
  earnings-reaction whipsaw (day_high 54.35 -> day_low 46.65 -> recovering to ~49.8
  after-hours). Last-hour tape shows real basing: hammer defended 49.21 (21:15 UTC)
  + bullish engulfing (21:25 UTC), both AT SUPPORT 49.12. TradingView neutral across
  the board (not yet bullish). Spread 0.06%, fully tradable. **Do NOT stage off
  tonight's after-hours prints** - same treatment as any earnings-day name (playbook
  s5): tomorrow's opening tape is the real test of whether 49.12 holds. If it does
  with a confirmed reclaim, this is a DELL-style earnings-reaction-reversal candidate
  (today's DELL trade scored "right" on exactly this pattern). Kill: a gap below
  46.65 (today's low) or failure to hold 49.12 on live volume at the open.
- **CRWD** - price has fallen further since yesterday's cancelled 217.60 trigger
  (today closed 203.42, -4.46%, part of tonight's software-selloff theme alongside
  MDB/PANW/CRDO - not CRWD-specific). Yesterday's trigger level is now stale/too high.
  Fresh support test forming: 2 dojis AT SUPPORT 201.75 in the last hour, but a
  shooting-star rejection at 209.5 shows the bounce hasn't resolved either way yet.
  EMA stack still mildly bullish (EMA9 210.13>EMA21 206.81>EMA50 196.44) despite two
  down days. TradingView now neutral/sell/neutral (degraded from yesterday's
  strong_buy). next_earnings 2026-12-01, clear. Re-workup fresh at tomorrow's open
  around the 201.75 level, not the old 217.60 trigger.
- **GTLB** - up another +10% today on top of yesterday's +16.21% earnings gap (2-day
  cumulative move). RSI14 now 73.9 (genuinely overbought, not just elevated),
  pos_in_20d_range_pct 100%, no resistance_above (pure price discovery). TradingView
  strong_buy/strong_buy/buy, volume 6.13x. Real chase risk after two huge up days -
  only worth a TIGHT probe on a confirmed pullback-and-hold (e.g. a higher low above
  today's 49.11 day-low), never chasing the 53+ highs. next_earnings 2026-12-01, clear.
- **SOLS** - spread improved to 2.47% (TRADABLE_TIGHT_SIZE, was UNTRADABLE yesterday).
  Still chopping in a range: hammer defended 61.07 AT SUPPORT 60.00 this hour, but 2
  dojis at the same level show it's unresolved, not a clean hold yet. TradingView
  neutral/sell/neutral. Genuine multi-touch level (per L8, this matters) - re-check
  at tomorrow's open whether 60.00 has resolved either way before sizing. next_earnings
  2026-10-29, clear.
- **ASND** - still UNTRADABLE after-hours (7.69% spread, bid 250/ask 270 - the same
  recurring broken post-close quote pattern). Underlying thesis intact/improving:
  bullish engulfing AT SUPPORT 249.99 (08-31), today +2.71% on real (not broken-quote)
  price action, TradingView strong_buy/strong_buy. Already stopped out once this week
  (t-2026-08-31-001, -171.95) - any re-entry needs fresh reasoning, not a blind
  restage. Re-check spread once quotes normalize at reopen. next_earnings null (still
  unconfirmed - treat as an unknown-risk flag per playbook s5).
- **TDW** - still UNTRADABLE (3.46% spread, bid 99.5/ask 103), but a real breakout is
  forming underneath the bad quote: +4.57% today, daily bullish engulfing, TradingView
  strong_buy/strong_buy. RSI14 69.8 (elevated). Re-check spread at reopen; this is the
  most "almost there" name on the board once liquidity normalizes. next_earnings
  2026-11-09, clear.

## Passed / killed this session

- **FRVO** - thesis is now BROKEN. The whole setup leaned on the 19.54/18.71-19.15
  support zone holding; price has since fallen to 17.98 (-6.94% more today), decisively
  through that level, TradingView flipped to sell, EMA stack degrading (9<21<50).
  DROP - the Google 396MW PPA catalyst was real but the market stopped paying for it.
  Do not re-stage without a genuinely new higher-low.
- **MRVL** - stopped out THIS MORNING at 201.74 support (t-2026-08-28-002, -57.62).
  Tonight's tape shows a morning star AT SUPPORT 201.74 immediately followed by a
  bearish engulfing at the same level - contested, unresolved, and TradingView has
  gotten MORE bearish since the stop-out (now sell/sell/sell, was neutral-ish before).
  No new thesis distinct from the one that just failed - re-entering here now would be
  the playbook s8 revenge-trade failure mode. PASS until genuinely new evidence
  (a confirmed higher low or a fresh catalyst) appears.
- **MDB** - NEW name (duty 1b). Real Q3 beat but cratered -12.67% same-session as
  PANW/CRDO (see macro thread above). Confirmed daily downtrend (lower highs+lower
  lows, EMA9<EMA21, price<EMA50), TradingView sell/sell/sell. PASS per playbook s2 -
  no counter-trend knife-catch. Watch for a confirmed higher low.
- **PANW** - NEW name (duty 1b). Same sector theme as MDB - Q3 beat, CEO citing a
  "$1T cyber replacement cycle," 4+ same-day analyst PT raises (targets $300-450 vs
  ~$328 spot), yet the stock fell -8.95% and closed in a confirmed downtrend.
  TradingView sell/sell/sell. PASS per playbook s2, same reasoning as MDB. Watch for a
  confirmed higher low.
- **STDN** - closed today (t-2026-09-01-008, -135.51, the 2nd L8/W1 instance - untested
  level probe). No fresh catalyst or evidence since the stop-out. Drop from active
  watch.
- **MRNA** - closed today (t-2026-09-02-trg-01-006, -75.13, confirmation-trigger entry
  that reversed through the stop). No fresh evidence tonight. Drop from active watch.
- **PURR** - trigger `trg-20260901-004` fired at 11.55 this morning but was REFUSED by
  the gate (consumed_note: "fired at 11.55: refused") - root cause not yet
  investigated by any session today. Price context is now 2 days stale. Drop from
  active watch; if a future session sees the same refused-on-fire pattern recur, flag
  it as a possible watcher/gate integration issue worth a written note, not just a
  retry.

## Macro calendar

- **2026-09-04 (Fri) 8:30am ET: NFP jobs report** - last trading day of the
  active-training directive (expires 2026-09-04); elevated volatility risk for
  anything still open into it.
- **2026-09-11 (Fri): CPI report** and **2026-09-15/16: FOMC** - both after the
  training window closes, not an immediate concern for anything staged this week.
- No US market holiday before 2026-09-05 (Labor Day 2026-09-07 falls after window
  close).
- Mandate: 8 days remaining (expires 2026-09-10, per last review).

## Pruned (no fresh catalyst/edge tonight, or already fully explained above)

TENB, IREN, AFRM, PYPL, ESTC, RBRK, GAP, WDAY, DKNG, PD, FROG, NTSK, FIGR, MMED, FSLY,
CRDO (earnings-day breakdown, same theme as MDB/PANW tonight, already flagged
yesterday), AXON, ENOV, SN, WETO, KORU, EIX, PCG, HWM, TITN - quiet or no directional
edge to trade tonight; re-add only on new evidence.

Next session (tomorrow's planning leg, pre-market 2026-09-03): set a fresh daily loss
budget per playbook s10 before resuming full hunting (today's was hit at leg with 4
stop-outs, -282.32 net). Re-check HPE/CRWD/GTLB/SOLS against the live opening tape
before staging anything - none of tonight's levels were tested by real market
liquidity. Retry ASND/TDW once quotes normalize past reopen (both still UNTRADABLE
after-hours on the recurring broken-quote pattern). DUOL is the only book position,
unchanged.
