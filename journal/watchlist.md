# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-04 evening (research session, market closed). Regime: SPY uptrend
(770.19, +0.55% vs EMA21, RSI14 55.7), QQQ range/mixed (718.96, +0.66% vs EMA21,
RSI14 53.6). Today's tape: a hot August jobs report (+106k beat) pushed September
Fed-hike odds from 49.4% to 60.2%, sending Bitcoin below $80k and dragging every
BTC-proxy (COIN, MSTR, gold miners) and several richly-valued growth names (LULU
-17.4%, FICO -16.7%, PATH -16.6%, GWRE -19.9%) down hard - a real, identified macro
catalyst (Benzinga, multiple 2026-09-04 stories), not noise. Idiosyncratic winners
existed alongside the selloff: SNDK +11.9% (chip/memory catalyst) and IOT +3.7%
(earnings-beat analyst PT raises) both moved on their own news, independent of the
crypto/rate-hike story.

Today's active-training directive (SESSION_PROMPT.md rule 6) closed out its LAST day
(daily review already ran, scoring TSLA's closed trades). Tomorrow (Sat 2026-09-05)
and through the weekend the market is closed; next trading day is Monday 2026-09-07
**except that is Labor Day (US market holiday) - the next actual trading session is
Tuesday 2026-09-08.** The standing-order-quota (phase 2 s3b) and trend-gate (s2a/s3c)
rules remain in force regardless of the training directive's expiry.

**Standing-order quota status (this session): 7 live conditional buy entries staged
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

- **SNDK** - NEW name (duty 1b). +11.45% on 1.25x volume, real catalyst (chip/memory
  cycle, "SanDisk Jumps 10%" - Benzinga), TradingView strong_buy. **Fails trend gate:
  EMA21 1535.93 < EMA50 1618.57** despite the huge up-day - still technically a
  downtrend by the s2a/s3c rule. Daily candles show a marubozu buy day after a
  doji/inside-bar compression, but the last hour's 5m tape (shooting star + a late
  marubozu SELL bar into the close) looks like a fading breakout, playbook s7's
  familiar warning sign. Needs the EMA stack to actually flip AND a confirmed hold
  above today's range before this becomes tradeable. Re-check Tuesday.
- **CIFR** (bitcoin miner) - still fails the binding trend gate: EMA21 (17.03) <
  EMA50 (19.70). Strong social sentiment (19 bull/0 bear per StockTwits) and a real
  theme (crypto rally) do not override the gate. WATCH ONLY until the EMA stack
  flips - re-check Tuesday, it has been trending toward a flip.
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
ENOV/SN/WETO/KORU/EIX/PCG/HWM/TITN/FRVO/MRVL/MDB/PANW/STDN/MRNA/PURR - quiet or no
directional edge; re-add only on new evidence.

Next session (Tuesday's PLANNING leg, pre-market 2026-09-08, first session after the
Labor Day weekend): check every one of the 7 staged rungs above against the weekend's
news before trusting any fill: a 3-day-weekend fill carries more gap risk than a
normal overnight one. Re-verify SNDK/CIFR's EMA stacks for a possible flip. Re-verify
mandate expiry. Reset the daily loss budget per playbook s10 fresh for the day.
