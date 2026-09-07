# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-07 22:10 CT (research session, market closed - Labor Day evening,
7th research leg this weekend).
Regime unchanged from Friday's close (no new bars possible over the weekend): SPY
uptrend (770.19, +0.55% vs EMA21, RSI14 55.7), QQQ range/mixed (718.96, +0.66% vs
EMA21, RSI14 53.6). Friday's tape: a hot August jobs report (+106k beat) pushed
September Fed-hike odds from 49.4% to 60.2%, sending Bitcoin below $80k and
dragging every BTC-proxy (COIN, MSTR, gold miners) and several richly-valued
growth names (LULU -17.4%, FICO -16.7%, PATH -16.6%, GWRE -19.9%) down hard - a
real, identified macro catalyst, not noise. Idiosyncratic winners existed
alongside the selloff: SNDK +11.9% and IOT +3.7% both moved on their own news,
independent of the crypto/rate-hike story.

**TIME_STOP FLAG for Tuesday's planning leg (surfaced this session):** all 3 open
book records (CRWD rungs t-2026-09-03-003/005, SMMT t-2026-09-03-007) carry
`time_stop: 2026-09-05` with exit_condition "...or by 2026-09-05 review, whichever
comes first" - that date has now elapsed (today is Sunday 2026-09-06) with the
market closed the entire time, so it was never actionable. This is NOT a stop/
target breach (both positions remain healthy, well inside their bands - see Book
below) but the WRITTEN exit condition's time leg has technically passed. Research
sessions place no market orders and weekend quotes are stale/broken (CRWD bid
201.87/ask 0.00 as of the last check - unusable). **Tuesday's planning leg must
make this the FIRST decision on the book: either write a fresh justification to
extend the time_stop (per L3 - a held position needs a current thesis, not just
an old one that hasn't been stopped out) or close at the open.** Do not let this
elapse silently a second time.

**New this session: SNDK's move is not idiosyncratic - it's the leading edge of a
sector-wide AI memory/DRAM shortage story.** `get_news` confirms a TechInsights
report predicting DRAM prices up 200%+ through 2027 on AI demand ("AI Memory Crunch
Is About to Hit '10 Out of 10' Craziness"), plus $2B of new US chip investment in
South Korea. The whole memory/semi complex moved together Friday: MU +5.9%
(Reddit mentions rank 4->1 today), ALAB +7.4% (whale options activity), WDC +5.8%,
KLAC +7.3%, STX +6.3%, CBRS +10.3%. This is a real, dated, multi-name catalyst worth
tracking for a possible EMA flip - see Watch-only below, none qualify yet.

Today (Sat 2026-09-05) and through the weekend the market is closed; next trading
day is Monday 2026-09-07 **except that is Labor Day (US market holiday) - the next
actual trading session is Tuesday 2026-09-08.** The standing-order-quota (phase 2
s3b) and trend-gate (s2a/s3c) rules remain in force. The active-training directive
(rule 6) expired 2026-09-04; rule 6 now reverts to its normal "do not trade to look
busy" form, though the quota/gate rules stay binding.

**Mandate: expires 2026-09-10T21:11:52Z (~16:11 CT Thursday)** - confirmed this
session by reading `~/.vibe-trading/live/alpaca/mandate.json` directly (read-only).
That's after Tuesday 2026-09-08 and Wednesday 2026-09-09's sessions but still mid-day
Thursday 2026-09-10 - renewal (`ops/commit_paper_mandate.py`, human-run only) is
needed before Thursday's close or before Thursday's session if trading past 16:11 CT
is wanted that day.

**Standing-order quota status (re-confirmed this session, unchanged): 7 live conditional buy entries staged
across 4 distinct symbols (COIN x2, IOT x2, HOOD x2, MSTR x1) - quota (>=6 across
>=3 symbols) met.** All 7 are conservative GTC buy-limits BELOW Friday's close at
named support levels (never chase-priced, per research duty 4), sized as probes
given weekend gap risk. Full theses/stops/targets/sizing in `journal/trades.jsonl`
(t-2026-09-04-001 COIN, -002 IOT, -003 HOOD, -004 MSTR). Tuesday's (next trading
day, post-Labor-Day) planning leg must re-check every resting order against the
weekend's news before treating any fill as confirmed - a fill over a 3-day weekend
carries more gap risk than a normal overnight fill.

## Book (2 positions)

- **CRWD** 30 sh @ avg 211.382 (2 confirmation rungs), last 213.10 (+0.81% ROI).
  Stop 204.39/205.49 (both resting GTC), target 230.15/231.25 (both resting GTC).
  next_earnings 2026-12-01 (safe). EMA9 211.5>EMA21 208.08>EMA50 198.63 (trend gate
  pass), key_levels structure flagged range/mixed but the EMA stack is clean uptrend.
  RSI14 53.1, not extended. No action - fully bracketed, healthy.
- **SMMT** 200 sh @ avg 16.78, last 17.61 (+4.95% ROI). Stop 16.295, target 18.24
  (resting GTC). next_earnings 2026-10-19 (safe). Structure "uptrend (higher highs +
  higher lows)" confirmed, RSI14 71.6, pos_in_20d_range 100% - fully extended, no
  resistance above (breaking new highs). No fresh add here: extended, no nearby
  support to stage a conservative pullback buy without materially chasing.

## Staged for Tuesday (next trading session) - ranked

- **COIN** - L8-qualified multi-touch support 174.73 (3 separate defenses across
  three sessions: doji 09-02, morning star 09-03, hammers today). Trend gate passes
  (184.64 > EMA21 173.81 > EMA50 166.76). Today's -4.38% fade is the identified
  jobs-report/Fed-hike/BTC-below-80k catalyst, shared with MSTR below - real
  correlated risk, not two independent bets. Two rungs staged: 12sh @174.75 (stop
  163.29, target 203.40) + 10sh @172.05 (stop 160.59, target 200.70). Grade B,
  probe. Kill: a close below 163.29, or BTC/crypto tape breaking meaningfully
  worse (Fed actually delivers the hike) before either rung fills.
- **IOT** - NEW name (duty 1b). +3.74% on 4.15x rel volume, $23.5B mkt cap, genuinely
  liquid (playbook s7b - not excluded on size). Trend gate passes (40.20 > EMA21
  39.23 > EMA50 37.26). Real catalyst: five analyst PT raises today, all above spot,
  even from Neutral/Hold desks (BNP $55, Piper $46, Truist $48, MS $49, JPM $52) -
  consistent with a post-earnings beat-and-raise. Two rungs staged: 40sh @38.70
  (stop 36.31, target 44.68) + 35sh @38.05 (stop 35.66, target 44.03). Grade B,
  probe. Kill: a close below 36.31, or the 41.24 resistance capping the stock with
  no pullback ever reaching either rung (fine - miss, not a failure).
- **HOOD** - Carryover from 09-03; the 125.10 breakout trigger died (never fired,
  day faded). Fresh pullback-to-support setup instead: 108.81 (untested) and 100.68
  (hammer-defended 08-31, stronger). Trend gate passes (122.11 > EMA21 105.66 >
  EMA50 103.68). Same jobs-report/Fed-hike catalyst driving today's -2.15% fade.
  Two rungs staged: 15sh @108.85 (stop 102.24, target 125.38) + 12sh @100.70 (stop
  94.09, target 117.23). Grade B, probe. Kill: close below 102.24, or the whole
  bounce attempt fails to reach either rung and price just grinds sideways/down
  without a real test.
- **MSTR** - Carryover from 09-03; both breakout triggers (146/148) died (never
  fired, day reversed -1.46%/-3.22% gap on the same BTC-below-80k catalyst). Fresh
  setup: 121.38 doji-defended support (09-02). Trend gate passes (142.80 > EMA21
  119.83 > EMA50 110.13). Single rung staged (smaller, C-grade): 10sh @121.40 (stop
  112.74, target 143.05) - kept deliberately small given it shares the exact same
  BTC-macro risk factor as the COIN order above (correlated, not diversified). Kill:
  close below 112.74, or BTC confirms a real breakdown (not just today's dip) before
  the rung fills.

## Watch only (fails trend gate or thesis unresolved - do not stage)

- **SNDK** - re-checked fresh this session (2026-09-05): **still fails trend gate,
  EMA21 1535.93 < EMA50 1618.57**, unchanged from Friday - no flip yet despite the
  DRAM-shortage sector catalyst (see above). TradingView strong_buy, RSI14 61.1,
  structure still "range/mixed" per key_levels. Needs the EMA stack to actually flip
  AND a confirmed hold above range before tradeable. Re-check Tuesday.
- **MU** - NEW name (duty 1b, sector-catalyst hunt). +5.92% Friday, RS vs SPY +6.4pp,
  TradingView strong_buy, Reddit mention rank 4->1 in 24h. Real catalyst: AI
  memory/DRAM shortage story (TechInsights: DRAM prices +200% through 2027), same
  story driving SNDK. **Fails trend gate: EMA21 944.67 < EMA50 959.72** despite
  close (1016.59) > EMA21 - the EMA50 hasn't caught up from the prior downtrend yet,
  same pattern as SNDK. Daily structure labeled "uptrend" but last-hour 5m tape
  shows a bearish engulfing + marubozu SELL bar at support 991.1 before a hammer
  defense - mixed, not a clean breakout. Watch only; re-check Tuesday for the EMA
  flip.
- **ALAB** - NEW name (duty 1b, sector-catalyst hunt). +7.38% Friday on 2.02x volume,
  TradingView strong_buy, morning-star reversal + bullish engulfing at support 308 in
  the last hour. Same memory/semi sector catalyst. **Fails trend gate: EMA21 299.19 <
  EMA50 330.55** (close 310.4 > EMA21 but not > EMA50-ordering); key_levels structure
  itself reads "range/mixed". Watch only; re-check Tuesday.
- **WDC** - checked, NOT staged. +5.8% Friday on the same memory catalyst (Benzinga:
  "investors return to memory plays"), but weaker than MU/ALAB: **close 467.46 is
  already below EMA21 469.36** (fails the gate's first leg, not just the EMA21>EMA50
  ordering), structure explicitly "range/mixed", TradingView neutral (not strong_buy
  like its peers). Weakest of the four memory names checked - pass, cite these
  numbers if re-considered.
- **CIFR** (bitcoin miner) - still fails the binding trend gate: EMA21 (17.03) <
  EMA50 (19.70), unchanged from Friday. Strong social sentiment (19 bull/0 bear per
  StockTwits) and a real theme (crypto rally) do not override the gate. Last-hour 5m
  shows a morning-star reversal at support 17.44 - watch for the flip, re-check
  Tuesday.
- **AMD** - NEW name (duty 1b, evening re-hunt). screen.py explore/turnover lens:
  +4.69% Friday, $9.3B dollar volume, TradingView buy/strong_buy. News: same
  sector-wide AI-chip-capacity story (TSM "scrambles to feed the AI boom",
  Benzinga 2026-09-04), no AMD-specific catalyst. **Fails trend gate: EMA21 475.63
  < EMA50 496.22** despite close 477.57 barely above EMA21; structure "range/mixed".
  Spread 0.05% (TRADABLE). Watch only; re-check Tuesday.
- **NBIS** (Nebius) - NEW name (duty 1b, evening re-hunt). +7.48% Friday on
  $3.3B dollar volume, TradingView buy/strong_buy, StockTwits 16 bull/3 bear
  (best sentiment ratio of tonight's candidates). Daily candles show a genuine
  multi-touch defense of 201.89 (2 dojis + bullish engulfing, then a marubozu buy
  bar) - real level, would be L8-qualified if the gate passed. **Fails trend gate:
  EMA21 216.36 < EMA50 219.46**, structure "range/mixed". Spread 0.12% (TRADABLE).
  Watch only; re-check Tuesday for the EMA flip - closest of tonight's misses to
  qualifying.
- **INTC** - NEW name (duty 1b, Sunday re-hunt, turnover/gainers lens). +4.51%
  Friday, $9.25B dollar volume, TradingView buy/strong_buy, StockTwits 13 bull/0
  bear. No real catalyst though - Mizuho reiterated Neutral and CUT its PT to $92
  the same day (below spot), part of the broad chip-sector jobs-report move, not
  an Intel-specific story. **Fails trend gate: EMA21 93.59 < EMA50 102.28** despite
  close 95.8 > EMA21 - same lagging-EMA50 pattern as SNDK/MU/ALAB. Spread 0.01%
  (TRADABLE). Watch only; the thin/negative catalyst (a PT cut) makes this a lower
  priority re-check than the memory names even if the gate flips.
- **AMBA** (Ambarella) - NEW name (duty 1b, Sunday afternoon re-hunt, top-40
  shortlist by dollar volume $327.5M/rel volume 4.43x). **Fails trend gate hard:
  close 62.89 < EMA21 71.21 < EMA50 71.85**, structure explicit "downtrend (lower
  highs + lower lows)", TradingView strong_sell/strong_sell corroborating (not just
  the gate). RSI14 32.4 (oversold but no reversal candle at the 59.35 support doji
  has been confirmed yet). Spread 0.22% (TRADABLE) - liquidity is fine, structure is
  not. Watch only; needs a confirmed base + EMA flip before reconsidering, not close
  to qualifying.
- **TITN** (Titan Machinery) - NEW name (duty 1b, Sunday afternoon re-hunt,
  smallcap explore lens). Actually PASSES the trend gate (26.22 > EMA9 21.75 >
  EMA21 20.29 > EMA50 19.73, TradingView strong_buy) but **UNTRADABLE on spread:
  bid 24.00/ask 26.20 = 8.76% spread** (playbook s7b) - down ~8.8% the instant you
  fill, no scalp survives that toll regardless of setup quality. Also RSI14 74.7 and
  pos_in_20d_range 100% (fully extended) even if the spread were fine. Rejected on
  a measured number, not a size guess; removed from the stale Pruned-list mention
  below since this is now a specific, current rejection reason.
- **AMC** - NEW name (duty 1b, Sunday evening re-hunt, relvol lens). Technically
  PASSES the EMA trend gate (close 2.65 > EMA21 2.57 > EMA50 2.42, TradingView
  strong_buy) but key_levels structure reads "range/mixed" with repeated
  rejections at resistance (shooting star at 2.67 on 08-31, bearish engulfing AT
  2.67 on 09-03, doji AT 2.76 on 09-04) - chop at a ceiling, not a confirmed
  breakout. `get_news` shows the catalyst is a CEO-vs-Robinhood tokenization
  feud, not a fundamental driver, and one Benzinga piece flags the real story is
  892M diluted shares (up from 100M) - textbook crowd/meme risk (playbook s11:
  the crowd is often the exit liquidity, ticker-prior bias warning literally
  about names like this). Watch only; would need a confirmed close above 2.76
  on real volume before this is anything but chop.
- **GWRE** (Guidewire) - NEW name (duty 1b, Labor Day evening re-hunt, main
  shortlist - -19.93% Friday on 3.93x volume, $758M dollar volume, never checked
  despite three research legs passing over it). Post-drop bull case is real:
  Oppenheimer reiterated Outperform PT $210 and Wells Fargo Overweight PT $195
  (both 2026-09-04, both well above spot 162.42) - analysts see value here. But
  structure says otherwise: **close 162.42 is below EMA21 183.41** (fails the
  gate's first leg outright, not just EMA21/50 ordering), `structure` "range/
  mixed", `pos_in_20d_range_pct` 0% (sitting at the 20-day low), TradingView
  sell/sell/sell. A shooting star (09-01, rejected 205.27) preceded the crash -
  sellers were already in control before the drop. This is a falling-knife
  post-earnings-gap, not a defended level (playbook s2: "a downtrend stock at
  support is a watch item, not a buy, until structure turns"). Watch only;
  needs an actual EMA flip and a confirmed higher low, not just analyst PTs,
  before this is tradeable. next_earnings 2026-12-03.
- **ASAN** (Asana) - NEW name (duty 1b, Labor Day evening re-hunt, main
  shortlist - -12.69% Friday on 3.71x volume, $152M dollar volume). Beat Q2
  estimates and raised full-year revenue guidance but gave a soft Q3 EPS
  outlook (Benzinga 2026-09-04) - a guide-down disguised as a beat, and
  multiple desks raised PTs anyway (DA Davidson $9, Baird $10, both still
  below/near spot 8.81, weaker support than GWRE's analyst gap). **Fails trend
  gate outright: close 8.81 < EMA9 9.65 < ... and `structure` explicit
  "downtrend (lower highs + lower lows)"**, TradingView sell/sell,
  `pos_in_20d_range_pct` 0%. StockTwits 9 bull/4 bear - mild crowd optimism,
  not a thesis (playbook s11). Watch only; needs a confirmed base before
  reconsidering. next_earnings 2026-12-02.
- **EFX** (Equifax) - NEW name (duty 1b, Sunday evening re-hunt, relvol lens).
  -6.37% Friday on 2.7x volume. **Fails trend gate: close 177.05 < EMA21 185.33
  < ... EMA50 177.42**, structure "downtrend (lower highs + lower lows)",
  TradingView strong_sell/sell corroborating. Also **UNTRADABLE: 2.82% spread**
  (bid 175/ask 180) - fails both tests independently. Clean pass.
- **NX** - NEW name (duty 1b, Sunday evening re-hunt, relvol lens). +22.23% on
  6.99x volume, EMA stack technically passes (22.93 > EMA21 19.9 > EMA50 18.94)
  despite key_levels mislabeling structure "downtrend" (lagging pivot read) -
  but **UNTRADABLE: 19.83% spread** (bid 22.21/ask 27.10) kills it regardless of
  structure. $42.9M dollar volume is real but the quoted market is not tradable
  at any size.
- **PL** (Planet Labs) - NEW name (duty 1b, Sunday evening re-hunt, relvol
  lens). -1.25% on 3.92x volume, $585M dollar volume. **Fails trend gate hard:
  close 18.12 < EMA21 21.15 < EMA50 23.58**, RSI14 28.0, TradingView
  strong_sell/strong_sell. Not close.
- **AOUT** (American Outdoor Brands) - NEW name (duty 1b, 6th weekend pass,
  gainers lens). +44.66% Friday on 65.46x rel volume, $64.2M dollar volume.
  Real catalyst: Q1 earnings beat + Roth Capital reiterated Buy, PT raised to
  $17 (Benzinga 2026-09-04). **Fails trend gate: EMA21 11.46 < EMA50 11.89**
  (close 14.48 is a fresh earnings gap the EMAs haven't caught up to yet - same
  lagging-EMA50 pattern as SNDK/MU/ALAB/INTC). Also RSI14 70.3 and
  pos_in_20d_range 100% - fully extended into 14.80/14.97 resistance, no
  pullback room even if the gate passed. StockTwits 6 bull/3 bear (thin
  sample). Spread 0.48% (TRADABLE). Watch only; re-check Tuesday for the EMA
  flip, lower priority given the extension.
- **AEHR** (Aehr Test Systems) - NEW name (duty 1b, 6th weekend pass, gainers
  lens). +13.1% Friday, $390M dollar volume, hammer-defended 74.23 on 09-01
  then a marubozu buy bar 09-04 - genuine multi-touch structure. Same
  semiconductor-test-equipment space as the building AI-memory story (SNDK/MU/
  ALAB). **Fails trend gate: close 86.26 < EMA21 92.85** (fails the gate's
  first leg, not just the EMA21/50 ordering), structure "range/mixed",
  TradingView neutral (moving_averages sell, oscillators buy - mixed signal).
  StockTwits 11 bull/1 bear (best ratio of tonight's set). Spread 0.58%
  (TRADABLE). Watch only; needs to reclaim EMA21 before qualifying.
- **BE** (Bloom Energy) - NEW name (duty 1b, Sunday re-hunt, turnover lens).
  +7.35% Friday on $4.06B dollar volume, TradingView strong_buy, StockTwits 9
  bull/1 bear, Reddit rank 12 (mentions 13). Real, dated catalyst: confirmed
  S&P 500 index-inclusion news (Benzinga 2026-09-04, "Bloom Energy... Set to
  Join S&P 500") plus falling Treasury yields - inclusion is a genuine forced-flow
  catalyst, not sentiment. Daily candles: bullish engulfing at support 197.5
  (2026-09-01), marubozu momentum bar (2026-09-04). **Fails trend gate: EMA21
  220.82 < EMA50 235.07** despite close 252.87 well above both; pos_in_20d_range
  100% (fully extended, at highs - even if the gate flipped, chasing a new high
  with no pullback would need a fresh, tighter thesis). Spread 0.13% (TRADABLE).
  Watch only; re-check Tuesday for the EMA flip AND a pullback entry, not a
  chase at the current extension.
- **SNOW** - faded hard off Wednesday's highs (spiked 384.56, closed ~355-356, well
  below VWAP). Never re-verified against a live session since 09-03. Stale; needs a
  confirmed reclaim of VWAP/range before treating as tradeable again.
- **HPE** - earnings-reaction reversal candidate (49.12 support, DELL-style whipsaw)
  from 09-01/02. Never re-checked against a live open since. Stale; re-verify at
  Tuesday's open before treating the level as still valid, or prune if no fresh
  evidence surfaces.

## Macro calendar

- **2026-09-07 (Mon): Labor Day, US market holiday** - no session. Next trading day
  is Tuesday 2026-09-08.
- **2026-09-11 (Fri): CPI report.**
- **2026-09-15/16: FOMC** - the actual rate decision behind today's hike-odds move;
  now the single most important date on the book for COIN/MSTR/HOOD given their
  correlated BTC exposure. Flag again as it approaches.
- Mandate: last read as ~6 days remaining (2026-09-04 14:12 CT leg). Re-verify exact
  expiry wording at Tuesday's planning leg; do not let it lapse unnoticed.

## Pruned (no fresh catalyst/edge, or fully explained above)

DUOL (closed +306.70, target hit, scored "right"), CHPT (closed -96.00, scored
unlucky, see lessons.md W2), TSLA (closed -402.25 combined across 2 rungs, scored
unlucky both - see 2026-09-04 daily review, gate-outage attribution), VRNS/TLYS/
TENB/IREN/AFRM/PYPL/ESTC/RBRK/GAP/WDAY/DKNG/PD/FROG/NTSK/FIGR/MMED/FSLY/CRDO/AXON/
ENOV/SN/WETO/KORU/EIX/PCG/HWM/FRVO/MRVL/MDB/PANW/STDN/MRNA/PURR - quiet or no
directional edge; re-add only on new evidence.

Next session (Tuesday's PLANNING leg, pre-market 2026-09-08, first session after the
Labor Day weekend): **(0) resolve the TIME_STOP FLAG above FIRST** - CRWD (both
rungs) and SMMT hit time_stop 2026-09-05, elapsed over the closed weekend; write a
fresh hold justification or close at the open. (1) check every one of the 7 staged
rungs above against the weekend's news before trusting any fill - a 3-day-weekend
fill carries more gap risk than a normal overnight one. (2) AMD/NBIS (added
2026-09-05 evening), INTC/BE (added 2026-09-06 morning), AMBA/TITN (added
2026-09-06 afternoon), AMC/EFX/NX/PL (added 2026-09-06 evening), and AOUT/AEHR
(added 2026-09-06 late evening) all fail either the trend gate or tradability -
NBIS closest to an EMA flip, BE most extended (100% of 20d range) even if it
flips, AMBA in a clean confirmed downtrend (not close), TITN passes the gate but
is UNTRADABLE on an 8.76% spread, AMC passes the EMA gate on paper but is chop
at resistance with a meme/dilution catalyst (not a real thesis), NX passes the
gate but is UNTRADABLE at 19.83% spread, AOUT is a fresh earnings gap with EMAs
still lagging (extended, low priority), AEHR needs to reclaim EMA21. SNDK/CIFR/
MU/ALAB/WDC EMA stacks re-verified fresh 2026-09-05 (all still fail trend gate)
- re-check again Tuesday for a possible flip, especially MU/ALAB given the
building DRAM-shortage catalyst. (3) Mandate re-confirmed 2026-09-06 19:34 CT
by reading the file directly: expires 2026-09-10T21:11:52Z (~16:11 CT Thursday)
- flag for renewal before Thursday. (4) Reset the daily loss budget per
playbook s10 fresh for the day. (5) GWRE and ASAN (added 2026-09-07 evening,
duty 1b) both checked and rejected - GWRE fails trend gate on close<EMA21
despite two analyst PT raises above spot, ASAN is in a confirmed downtrend
despite a Q2 beat; neither worth a re-check until their EMA stacks actually
turn.
