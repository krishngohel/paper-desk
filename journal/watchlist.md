# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-01 17:10 CT (evening research session, after a 14-leg continuous relay
+ 2 daily-reviews earlier today hit the loss budget at leg 10 and closed the book to
3 filled positions). Regime: SPY range/mixed (761.78, -0.39% vs EMA21, RSI14 48.6), QQQ
range/mixed (707.64, -0.85% vs EMA21, RSI14 46.6) - unchanged from every leg today.
**New macro thread found this session:** a global bond-yield rout hit high-multiple
tech/software today (10Y yield to a 19-month high, Fed rate-hike odds repriced to 68%
on hawkish Warsh remarks) - CRWD, AXON, ALAB, LITE, TER, CRDO all fell 5-17% on this
theme per `get_news`, largely NOT company-specific. Distinguish this from an idiosyncratic
breakdown when grading dip-buys in these names over the next few sessions.
Source: `journal/universe_scan.json` (17:01 CT relvol explore lens) and
`journal/social.json` (17:02 CT) - both re-screened this leg per duty 1b.

## Book positions (3, all bracketed, none touched this session per research-session rules)

- **CRK** 300 sh @ avg 15.67, closed 16.02 (+2.2% ROI). Stop 15.30, target 17.00 resting
  GTC (`c118fa9e...`). RSI14 70.8, **fully extended (100% of 20d range), no
  resistance_above** - real chase risk if adding here, so NOT adding despite the
  strong TradingView strong_buy read. next_earnings 2026-11-02 (safe). Hold as-is.
- **DUOL** 35 sh @ avg 156.41, closed 158.77 (+1.5% ROI). Stop 153.75, target 165.00
  resting GTC (`6fa761f6...`). Also fully extended (100% of 20d range), no
  resistance_above - same no-add reasoning as CRK. next_earnings 2026-11-04 (safe).
  Hold as-is.
- **MRVL** 10 sh @ avg 211.472, closed 210.39 (-0.5% ROI). Stop 202.00, target 222.64
  resting GTC across 2 orders (`9184e057...` 8sh + `7c26ff3e...` 2sh). **Weakening
  read: TradingView flipped to sell/strong_sell** (was neutral last week), RSI14 44.8,
  pos_in_20d_range_pct only 4.3% (near the bottom of its range). Testing support
  201.74 repeatedly today (2 shooting-star rejections above it, but no breakdown below
  it either - contested, not resolved). Stop 202.00 sits right at this support, watcher
  will enforce if it breaks. next_earnings 2026-12-01 (safe). Watch closely, no add.

## Staged / armed this session (live conditional entries)

- **STDN** 100 sh @ 16.00 GTC (`1eff3a96-b6f6-41cc-8931-d3e739e42e2c`). Ledger
  `t-2026-09-01-008` (C-probe). Restaged after the loss-budget cancellation of the
  original 14.85 stage (`t-2026-08-31-005`) - price has moved up ~11% since, so the
  level was rebuilt fresh (16.00, below today's 16.40 day-low, near yesterday's 16.11
  close) rather than leaving a stale price resting. Structure confirmed uptrend,
  volume 3.31x, but **100% of 20d range - fully extended, real chase risk**, no
  resistance_above. Stop 14.65 (~1x ATR14), target 18.70, time_stop 2026-09-05. Kill:
  a close back below 14.65 or the uptrend structure breaking (lower low).
- **PURR** trigger `trg-20260901-004`, buy 200 sh >= 11.55 GTC-equivalent, expires
  2026-09-02T15:00 CT. Re-armed after the loss-budget cancellation of
  `trg-20260901-003` (thesis was intact at cancellation). Range/mixed, choppy last
  hour (morning star then 2 sell marubozu then a hammer defend) - arming above the
  vwap/opening-range reclaim rather than buying the contested low. Stop 11.00, target
  12.60. Kill: cancel if a confirmed lower low prints before it fires.
- **CRWD** trigger `trg-20260901-005`, buy 15 sh >= 217.60 GTC-equivalent, expires
  2026-09-02T15:00 CT. **Fresh thesis, distinct from the stopped-out `t-2026-08-31-002`**
  (-247.54, self-flagged untested level) - today's -7.57% drop to 215.07 is the
  macro bond-rout theme (see header), not a company-specific break; EMA stack still
  bullish, Monday's catalysts (Fal.Con, Cognizant, Snowflake, Google Cloud, AI Partner
  Specialization) unaffected. Arming above the contested 217.5 resistance rather than
  buying today's chop. Stop 211.00, target 226.00 (R:R only 1.27:1 - kept small/probe
  for that reason despite the B-grade thesis). Kill: a continued macro slide (10Y
  yield still climbing) that never lets it reclaim 217.60.
- **MRNA** trigger `trg-20260901-006`, buy 10 sh >= 152.50 GTC-equivalent, expires
  2026-09-02T15:00 CT. NEW name this session (duty 1b). +8.28% day on volume that
  finally cleared the 0.7 continuation gate (0.83x, was 0.50x/0.62x earlier legs
  today) - but the **final two 5m bars into the close were both selling marubozu**,
  so buying the 154.27 close directly would risk chasing a fade. Arming above 152.50
  (a vwap-area reclaim/hold, below today's high) to require tomorrow's buyers to
  actually show up first. RSI14 67.5 and pos_in_20d_range_pct 83.3% both flag real
  extension after an already-large multi-week run - graded C/probe, sized very small
  (10 sh) for that reason. Stop 148.50, target 161.37. Kill: a confirmed break below
  vwap 150.91 before it fires.

**Standing-order quota (binds `research` sessions too, SOP duty 3b): 4 live conditional
entries across 4 distinct symbols (STDN, PURR, CRWD, MRNA) - below the >=6/>=3 floor on
raw count, meets the symbol-diversity floor. FAILED LEG on the raw-count clause; see
"blocked/passed this session" below for exactly what stopped a fuller count** (broken
post-close quotes on FRVO/ASND/SOLS/TDW, and no genuine non-extended entry on the three
book names). Next session should retry FRVO/ASND/SOLS/TDW once quotes refresh past
market reopen - all four theses are otherwise live, not killed.

## Blocked / passed this session (full workups, no order placed)

- **FRVO** (Fervo Energy) - real, confirmed catalyst (396MW Google geothermal PPA,
  Cape Station), +26.92% day, volume 9.44x, support 19.54 defended repeatedly. Gate
  **rejected** a 19.45 GTC buy-limit: `{"status": "blocked", "code": "PRICE_BAND",
  "detail": "buy limit 19.45 is 13.3% through quote ref 17.16 (band 10.0%) -
  fat-finger guard"}`. Root cause: `trade_cli quote FRVO` returned bid 17.16/ask 0.00 -
  an invalid one-sided post-close quote, the same recurring IEX-lag pattern seen
  repeatedly today (ASND, TENB, CRWD, TITN). Declined to chase the broken quote down
  to 17.x (would abandon the real 19.54 support level entirely) - dropped, not forced,
  same precedent as TITN. Ledger `t-2026-09-01-007` marked `aborted`. **Re-attempt at
  19.45/19.10 (2-rung, 70+50sh, stop 18.40/target 21.80) once quotes refresh past
  market reopen** - the thesis is unchanged and still the strongest catalyst-backed
  setup on the board.
- **ASND** - spread 9.52% (bid 250/ask 275), the same broken post-close quote pattern -
  UNTRADABLE right now regardless of thesis. Underlying setup (BioMarin settlement,
  5 sell-side reiterations) unchanged; structure still range/mixed, bullish engulfing
  AT SUPPORT 249.99 on 08-31. Re-check once quotes refresh; note this name already
  stopped out once today (`t-2026-08-31-001`, -171.95) - any re-entry needs this fresh
  reasoning, not a blind re-stage of the old ladder.
- **SOLS** - spread 2.64% (bid 60.45/ask 62.07) - UNTRADABLE right now. Chopping in a
  range (repeated rejections at resistance 62.52, one hammer defend at support 60.0,
  net undecided) - even with a working quote this remains a "wait for resolution" name,
  not yet a clean setup. Re-check spread + structure together at reopen.
- **TDW** - spread 5.66% (bid 94.5/ask 100) - UNTRADABLE, same broken-quote pattern.
  Volume 1.59x now clears the s7 gate and the tape has been genuinely defending
  resistance 97.5 (bullish engulfing, hammer defends) - worth a same-day recheck once
  quotes refresh at reopen, this is the closest "almost-there" name on the board.
- **CRDO** (Credo Technology) - surfaced via duty 1b (11,621 StockTwits watchers +
  Reddit rank-climber, +86 spots to rank 24 - genuine crowd-attention confluence, but
  per playbook s11 the chart earns the grade, not the crowd). **next_earnings is
  TODAY (2026-09-01)** - that IS the catalyst: -16.76% day, gapped down, downtrend
  structure (lower highs+lower lows), TradingView strong_sell. Last-hour tape at
  support 185.87 is genuinely mixed (2 hammer defends but also 2 bearish engulfings at
  the same level) - unresolved, no confirmed higher low. PASS per playbook s2 (no
  counter-trend knife-catch). Watch for a confirmed higher low before reconsidering.
- **AXON** - surfaced via duty 1b, -8.41% day, downtrend structure, TradingView
  strong_sell across the board. `get_news` confirms this is the SAME macro bond-rout
  theme as CRWD (no AXON-specific catalyst; analyst PTs from Aug are all well above
  spot: MS $640, Piper Sandler $732, UBS $600). Last-hour tape is pure compression
  (4 dojis at support 516.15, no resolving break). PASS per playbook s2 - compression
  is not direction; watch for the break.
- **MRNA/PURR/CRWD** - see "staged/armed" above, all three converted to armed triggers
  rather than outright passes.
- **ENOV** - downtrend, bullish engulfing at resistance 22.23 immediately failed with a
  shooting-star rejection the next hour. PASS (playbook s2, unconfirmed bounce).
- **SN** - violent single-day reversal to the bottom of an otherwise-uptrend range
  (pos_in_20d_range_pct 0%), one hammer defend at 174.43 against repeated selling
  rejections. PASS (playbook s2, no higher low yet). Watch for a reclaim above 174.43.
- **WETO** - bounce inside a severe multi-day crash (EMA50 41.98 vs last_close ~6),
  shooting-star rejection at support intraday. PASS (playbook s2, falling-knife bounce).
- **KORU** - volume 0.62x misses the s7 gate, no fundamentals data available (likely a
  recent listing), pure compression in the last hour. PASS.

## Vetted and passed (playbook s2 - falling knives / broken quotes, no near-term buy)

- **EIX / PCG** - California utility wildfire-liability crisis (SB 492 failed to cap
  liability), Edison -22.6%/PG&E -19.3% on the catalyst day, wave of analyst PT cuts,
  no support levels left on `ta.py`. Still a textbook falling knife - would need a
  confirmed higher low AFTER the legal situation stabilizes (weeks away at best).
  PCG's old probe (`t-2026-08-28-003`) stays cancelled. No new order.
- **HWM** (Howmet) - downtrend, repeated rejections at support 243.68, mixed
  macro/competitive catalysts (oil spike + SpaceX turbine-casting competitive threat).
  WATCH ONLY - a reclaim of 249.28 off a higher low above 243.68 would be the earliest
  bounce signal worth a probe. No new order.
- **TITN** - gate PRICE_BAND-blocked on 08-31 by a broken quote (bid 17.48/ask 0.00);
  real setup (defended support, TradingView strong_buy) but no company catalyst found.
  Re-examine once broker quotes refresh past reopen - not re-checked this leg.

## Macro calendar (confirmed 2026-08-29 via web_search; bond-rout item new this session)

- **2026-09-01 (today): global bond-yield rout** - 10Y yield to a 19-month high, Fed
  rate-hike odds repriced to 68% on hawkish Warsh remarks. Hit CRWD/AXON/ALAB/LITE/TER/
  CRDO hardest (high-multiple software/growth). Watch whether this is a one-day
  repricing or a multi-day theme before treating any of these dips as clean pullbacks.
- **2026-09-04 (Fri) 8:30am ET: NFP jobs report** - last trading day of the
  active-training directive; elevated volatility risk for anything still open.
- **2026-09-11 (Fri): CPI report** and **2026-09-15/16: FOMC** - both after the
  training window closes (2026-09-04), not an immediate concern for currently-staged
  probes, but the FOMC decision is now more consequential given today's yield move.
- No US market holiday before 2026-09-05 (Labor Day 2026-09-07 falls after window close).

## Pruned (no fresh catalyst/edge tonight, or already fully explained above)

TENB, IREN, AFRM, PYPL, ESTC, RBRK, GAP, WDAY, DKNG, PD, FROG, NTSK, FIGR, MMED, FSLY -
quiet or no directional edge to trade tonight; re-add only on new evidence.

Next session (planning leg, pre-market 2026-09-02 or the next `open`/`continuous`
slot): re-check `orders`/triggers for fills against overnight news, **retry FRVO/ASND/
SOLS/TDW once quotes refresh past reopen** (all four blocked purely by broken
post-close quotes tonight, not by thesis), re-verify MRVL's 201.74 support and the
TradingView sell flip, and set a fresh daily loss budget per playbook s10 before
resuming full hunting (today's budget was hit at leg 10, 3/3 stop-outs, -$629.49).
