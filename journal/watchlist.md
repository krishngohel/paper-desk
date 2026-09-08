# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-08 21:50 CT (research session, market closed - Tuesday evening,
post-close homework after today's 16-leg continuous relay + weekly-review).
Regime: SPY range/mixed (765.96, -0.0% vs EMA21, RSI14 51.3), QQQ range/mixed
(718.36, +0.52% vs EMA21, RSI14 53.1) - unchanged all session per every continuous
leg today. Today's real macro driver (get_news, 2026-09-08): Brent crude near $98
pushed the 10-year Treasury yield above 4.8% (a 3-year high), reigniting inflation
fears and pricing in a Fed rate hike NEXT WEEK - Dow -578pts, S&P/Nasdaq both
slipped. This is a fresh, DIFFERENT macro thread from Friday's jobs-report/BTC
story but points the same direction (hawkish Fed odds firming into the 09-15/16
FOMC) - reinforces the correlated-BTC-risk caveat already written into the COIN/
MSTR staged theses below. ROIV was the day's standout idiosyncratic winner
(+17-18%) on a genuine Phase 2 clinical readout, unrelated to the macro theme.

**CRWD GATE UNWEDGED 15:43 CT today (watcher entry, journal/2026-09.md) - the
`pending_action_unresolved` fault that blocked the rung2 sell across 26
consecutive continuous legs (2026-09-03 through today's close) was traced to a
phantom pending-action marker (act_8746182f1cbe42998e5955ba1eb9c563, 404 at the
broker, no real order) and cleared.** CRWD rung2 (t-2026-09-03-005, 15sh, CLOSE
decision standing since this morning's 08:35 CT planning leg) should be sellable
again once the market reopens - **tomorrow's opening/planning leg's FIRST action
should be retrying that sell**, now with a real chance of clearing rather than the
rule-8 retry-and-log ritual. Fresh `ta.py CRWD` this session (21:xx CT) shows the
gate would actually PASS now too (close 210.02 > EMA21 208.23 > EMA50 199.38) -
irrelevant to the CLOSE decision itself (that was made on structure/resistance-
rejection grounds, not the trend gate), but worth knowing if a fresh CRWD thesis
is ever considered later.

**Mandate: expires 2026-09-10T21:11:52Z (~2.0 days out, Thursday ~16:11 CT)** -
flagged again; needs human renewal (`ops/commit_paper_mandate.py`) before then.

**Standing-order quota status (re-confirmed this session via fresh `orders` +
`triggers.jsonl`, unchanged): 8 live conditional entries across 5 distinct
symbols - COIN x2, IOT x2, HOOD x2, MSTR x1 resting GTC buy-limits, plus LITE x1
armed confirmation trigger (trg-20260908-001, >=999.75, expires
2026-09-09T15:00:00-05:00).** Quota (>=6 across >=3 symbols) met. Full theses/
stops/targets/sizing in `journal/trades.jsonl` (t-2026-09-04-001..004) and
`journal/triggers.jsonl`. Nothing filled overnight; all orders still status "new".

## Book (2 positions)

- **CRWD** 15 sh @ avg 211.382 (rung1 already closed today for -$23.61, a
  discretionary time-stop decision, scored "right" - see 2026-09-08 weekly
  review), last 209.50 (-0.89% ROI). Stop 205.49 (resting), target CANCELLED
  (CLOSE decision standing since 08:35 CT this morning - structure downgraded to
  range/mixed, repeated rejection at resistance 217.5, CRWD-specific gap down).
  Sell blocked all day by the gate fault above; gate now cleared - **tomorrow's
  first action is retrying the sell**, not re-opening the thesis. next_earnings
  2026-12-01 (safe).
- **SMMT** 200 sh @ avg 16.78, last 17.28 (+2.98% ROI), after-hours quote wide
  (bid 17.00/ask 17.47, 2.73% spread - normal after-hours widening, not a live
  tradability concern until market reopens). Stop 16.78 (trailed to breakeven
  2026-09-08 planning leg), target 18.24 resting GTC (ae308e9e-1a36...).
  next_earnings 2026-10-19 (safe). Structure "uptrend (higher highs + higher
  lows)" confirmed, EMA9 15.58>EMA21 14.66>EMA50 14.45, RSI14 68.6,
  pos_in_20d_range 93.7%. Thesis intact (Akeso HARMONi-2 catalyst not
  contradicted), time_stop 2026-09-12. No fresh add: extended, no nearby support
  to stage a conservative pullback buy without chasing.

## Staged for next session - ranked

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

- **ROIV** (Roivant Sciences) - NEW name (duty 1b, tonight's top mover). +17-18%
  today on a GENUINE catalyst: Phase 2 PHocus trial for mosliciguat (rare lung
  disease, PH-ILD) met its primary endpoint with a statistically significant
  placebo-adjusted result (Benzinga, 2026-09-08 10:03 UTC), followed same-day by
  TWO fresh analyst PT raises on the data (Jefferies to $52, HC Wainwright to
  $47, both above spot ~41.5) - a real clinical readout, not sentiment. Trend
  gate PASSES: close 41.48 > EMA21 35.96 > EMA50 35.07. But **too extended to
  chase right now**: RSI14 72.8, pos_in_20d_range_pct 100% (fresh high, no
  resistance_above level even printed), today's own tape shows a shooting-star
  rejection at 41.4 in the last hour - the only support level ta.py can name
  (35.7) is ~14% below spot and predates today's gap, not a genuine post-catalyst
  base. **Highest-priority watch on this list**: real catalyst + gate pass, just
  needs the first live session to carve an actual pullback level before this is
  stageable without chasing. Re-check at Wednesday's open.
- **CRWV** (CoreWeave) - NEW name (duty 1b). +12.1% today, $5.1B dollar volume,
  rs_vs_spy_pp +12.71 (strong idiosyncratic outperformance on a day the broader
  tape was down on oil/yields). `get_news` found no CRWV-specific catalyst - only
  a generic "whale options activity" grouping and an indirect Nvidia-chip-value
  piece; not enough to call a real thesis (playbook s11: trade the screen, not a
  vibe). **Fails trend gate, barely: EMA21 88.59 < EMA50 88.85** (a 0.26-point
  gap, essentially flat/converging) despite close 99.83 far above both. Structure
  "range/mixed". Watch only; closest technical flip of tonight's new names, but
  still needs its own catalyst before it's a thesis even if the EMAs cross.
- **DOCN** (DigitalOcean) - NEW name (duty 1b). +13.6% today, $548M dollar
  volume, TradingView strong_buy. No DOCN-specific catalyst surfaced in
  tonight's news pull. **Fails trend gate clearly: EMA21 117.66 < EMA50 127.52**,
  and close 126.69 is itself still below EMA50. Six separate doji touches AT
  126.05 support in the last hour is a genuinely repeated defense (would be
  L8-qualified if the gate passed) - worth remembering if the EMA stack ever
  catches up, but not close tonight. Spread 1.86% (TRADABLE_TIGHT_SIZE) - would
  need to size down even if it qualified. Watch only.
- **SNDK/MU/ALAB** (AI memory/DRAM shortage sector story, tracked since
  2026-09-05) - all re-checked fresh this session. SNDK: still fails, EMA21
  1554.62 < EMA50 1622.28 (was 1535.93/1618.57 Friday - gap narrowing slightly).
  MU: still fails, EMA21 949.85 < EMA50 961.59 (structure now reads "uptrend" as
  higher-highs/higher-lows, but the EMA ordering itself hasn't flipped yet);
  next_earnings 2026-09-30 - inside 3 weeks, flag if this drags on. ALAB:
  **deteriorated** - down -6.74% today (vs Friday's +7.38%), EMA21 298.34 < EMA50
  329.64 (gap widened, not narrowed), TradingView now sell/strong_sell (was
  strong_buy), rs_vs_spy_pp -6.17 (real underperformance, not just a red day).
  Demoting ALAB from "closest to qualifying" - the story reversed, not just
  paused. Re-check SNDK/MU next session for the flip; ALAB needs a fresh reason
  to stay on the list at all.

## Macro calendar

- **2026-09-11 (Fri): CPI report.**
- **2026-09-15/16: FOMC** - the actual rate decision behind the Fed-hike-odds
  moves. Reinforced today (2026-09-08): Brent crude near $98 pushed the 10Y
  Treasury yield above 4.8% (3-year high), pricing in a hike next week - the
  single most important date on the book for COIN/MSTR/HOOD given their
  correlated BTC exposure. Flag again as it approaches.
- Mandate: expires 2026-09-10T21:11:52Z (~2.0 days out, ~16:11 CT Thursday) -
  confirmed fresh at today's 15:24 CT weekly review. Needs human renewal
  (`ops/commit_paper_mandate.py`) before Thursday close.

## Pruned (no fresh catalyst/edge, or fully explained above)

DUOL (closed +306.70, target hit, scored "right"), CHPT (closed -96.00, scored
unlucky, see lessons.md W2), TSLA (closed -402.25 combined across 2 rungs, scored
unlucky both - see 2026-09-04 daily review, gate-outage attribution), CRWD rung1
(t-2026-09-03-003, closed -23.61 today, scored "right" - Labor Day weekend
mechanically stretched its 2-day time_stop to 5, closed on structure/resistance
failure the moment a session could act), VRNS/TLYS/TENB/IREN/AFRM/PYPL/ESTC/RBRK/
GAP/WDAY/DKNG/PD/FROG/NTSK/FIGR/MMED/FSLY/CRDO/AXON/ENOV/SN/WETO/KORU/EIX/PCG/HWM/
FRVO/MRVL/MDB/PANW/STDN/MRNA/PURR - quiet or no directional edge; re-add only on
new evidence. **Pruned this session (housekeeping - stale 4+ days with no
re-verification since being added, most on clean single-session gate/spread
fails that don't change without fresh evidence): AMD, NBIS, INTC, AMBA, TITN,
AMC, EFX, NX, PL, AOUT, AEHR, BE, CIFR, WDC, GWRE, ASAN, SNOW, HPE** - full
original rejection reasons (mostly EMA21<EMA50 or untradable spread) live in
`journal/archive/2026-09-part7.md`; re-add fresh only if a new catalyst surfaces.

Next session (Wednesday's PLANNING leg, pre-market 2026-09-09): **(0) retry the
CRWD rung2 sell FIRST** - the gate fault that blocked it for 26 legs cleared
15:43 CT today (phantom pending-action marker, proven 404 at broker); this is
now a normal retry, not a rule-8 ritual. (1) Check all 8 standing conditional
entries (COIN/IOT/HOOD/MSTR rungs + LITE trigger) against overnight news before
trusting any fill - today's fresh oil/yield/Fed-hike macro thread adds to the
correlated-BTC risk already priced into COIN/MSTR. (2) ROIV is the top new
watch item - check if the open carves a genuine pullback level off today's
extension. (3) Reset the daily loss budget per playbook s10 fresh for the day.
(4) Mandate: 2026-09-10T21:11:52Z, ~2.0 days out - flag again, one session
closer to needing renewal.
