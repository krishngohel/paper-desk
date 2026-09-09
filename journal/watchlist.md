# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-09 ~16:50 CT (research session, market closed - Wednesday evening,
post-close homework after today's 25-leg continuous relay + weekly-review). Regime:
SPY range/mixed (762.40, -0.42% vs EMA21, RSI14 47.6), QQQ range/mixed (716.31,
+0.22% vs EMA21, RSI14 51.0) - unchanged all day. Today's macro driver shifted from
Monday/Tuesday's jobs-report/Fed-hike story to a fresh one (get_news, 2026-09-09):
**Brent crude topped $100/barrel for the first time since July as US-Iran strikes
escalated** - broad equities slipped on the oil spike, but BTC held ~$78-79k
"defying Fed hike fears" per Wintermute (ETF inflows strong, $72k flagged as key
support) while Glassnode separately warned Bitcoin's 69.3% supply-in-profit raises
real pullback risk, and Arthur Hayes floated a possible $70k retest before any
resumed rally - a genuinely two-sided crypto backdrop, not a clean tailwind or
headwind. CPI Friday (09-11) and FOMC (09-15/16) remain the calendar's key dates.

## Mandate & quota status

**Mandate expires 2026-09-10T21:11:52Z (~1 day out, Thursday ~16:11 CT)** - flagged
again, needs human renewal (`ops/commit_paper_mandate.py`) before then; this is now
inside 24h, the most urgent this flag has been.

**Standing-order quota: 4 live conditional entries across 3 distinct symbols (COIN
x1 @172.05, HOOD x2 @108.85/100.70, MSTR x1 @121.40) - BELOW the >=6-across->=3
target. FAILED LEG on the quota.** What stopped it: COIN's rung1 (174.75) filled
today converting to a position (no longer a conditional entry), and the CHYM/META
triggers armed this morning expired naturally at today's 15:00 CT close per the
day's own accepted-lapse policy - dropping the live count from 7 to 4 through normal
operation, not through an unreplaced cancel. This session then hunted hard to
refill it: fresh full workups on 10 names tonight (BAND, JILL, AEO, ROIV, CRWV, MU,
SNDK, ALAB, CRWD, CSR - see below) plus reconfirmation that SIG/ODD/NET/FBL/METU/
SKUU/YMAT/ASO/UI (already rejected by today's continuous legs) still apply - none
cleared the trend gate + tradability + data-quality bar cleanly enough to justify a
new resting order, and forcing one into a level that doesn't independently qualify
would be trading to fill a quota, not the market (rule 6). Tomorrow's planning leg
inherits this shortfall and should treat refilling it as a priority once the fresh
overnight tape is available.

## Book (4 positions)

- **COIN** 12 sh @ 174.75, last 174.72 (-0.02% ROI, day_change -2.15% today). Stop
  163.29, target 203.40 not yet resting (rung2 buy 10sh@172.05 still resting - that
  order IS the entry-side conditional counted above). time_stop **2026-09-10
  (tomorrow)** - planning leg must re-decide extend-vs-cancel. next_earnings
  2026-10-29 (safe). **Caution flag, new tonight:** TradingView consensus flipped
  to sell/sell/sell (was neutral-to-mixed) despite Goldman Sachs maintaining Buy and
  raising its PT to $219 same session (get_news, 17:23 UTC) - a genuine split
  between sell-side fundamentals (bullish) and TV's technical/momentum read
  (bearish). Price is currently doji-consolidating (5+ touches this evening) AT
  SUPPORT 172.03 - almost exactly the resting rung2 level - real defense in
  progress, not yet broken. EMA stack still bullish (EMA9 179.74>EMA21 174.31>
  EMA50 166.87). Watch closely at the open; this is a genuine two-sided read, not a
  clean thesis-intact call.
- **IOT** 75 sh @ 37.9717, last 38.65 (+1.68% ROI, day_change -4.36% today). Stop
  36.31, target 44.68 resting (c07abd8f). time_stop **2026-09-10 (tomorrow)**.
  next_earnings 2026-12-03 (safe). Same caution as COIN: TV flipped sell/sell/sell
  tonight, RSI14 48.7 neutral, EMA order still bullish (39.43>39.25>37.41 - barely,
  EMA9/EMA21 nearly converged). Price doji-consolidating AT SUPPORT 38.04 the last
  hour (4 touches) - a fresh, still-holding defended level just above the position's
  own cost basis. No action needed (stop/target untouched, L7 applies), but not a
  complacent hold either.
- **LITE** 4 sh @ 1011.79, last 988.98 (-2.25% ROI). Stop 981.00, target 1046.63
  resting (46e843d7). time_stop 2026-09-11. next_earnings 2026-11-05 (safe). Tape
  tonight is repeatedly contesting resistance 999.67 (a morning star + multiple
  dojis AT RESISTANCE in the last hour) without resolving either way - thesis
  intact, no new information.
- **SMMT** 200 sh @ 16.78, last 17.54 (+4.53% ROI). Stop 16.78 (trailed to
  breakeven 2026-09-08), target 18.24 resting (ae308e9e). time_stop 2026-09-12.
  next_earnings 2026-10-19 (safe). Structure confirmed uptrend, RSI14 69.6
  (elevated, oscillators read sell), pos_in_20d_range_pct 98.7% - fully extended,
  no resistance_above (price discovery) and no nearby support to stage a
  conservative add without chasing. No fresh add tonight, same as last review.

## Staged for next session - ranked (unchanged, reinforced by tonight's news)

- **HOOD** - Carryover pullback-to-support setup: 108.81 (untested) and 100.68
  (hammer-defended 08-31). Trend gate still passes (EMA9 113.13>EMA21 107.51>
  EMA50 104.66). Fresh bullish reinforcement tonight: Mizuho maintained Outperform
  and raised its PT to $140 (get_news, 14:15 UTC) - well above both resting rungs
  and the 125.38 target. Today's -2.62% pullback is in line with the broader
  oil-spike-driven equity slip, not company-specific. Two rungs resting: 15sh
  @108.85 (stop 102.24, target 125.38) + 12sh @100.70 (stop 94.09, target 117.23).
  Grade B, probe. Kill: close below 102.24, or the whole bounce attempt fails to
  reach either rung.
- **MSTR** - Carryover doji-defended-support setup: 121.38 (defended once, 09-02).
  Trend gate still passes (EMA9 131.98>EMA21 122.34>EMA50 110.79). Fresh bullish
  reinforcement tonight: Canaccord Genuity raised its price forecast to $179
  (get_news, 14:34 UTC, "Strategy stock surging... alongside Bitcoin gains").
  Genuinely two-sided crypto backdrop though (see macro note above - BTC holding
  but Glassnode/Hayes both flag real pullback risk to $70-72k) - kept small and
  single-rung deliberately for that reason, unchanged. Single rung resting: 10sh
  @121.40 (stop 112.74, target 143.05). Grade C, probe. Kill: close below 112.74,
  or a confirmed BTC breakdown (not just a dip) before the rung fills.

## Watch only (fails trend gate, tradability, or data quality - do not stage)

- **CRWD** - Re-checked fresh tonight (now flat, both rungs closed today for a
  combined -$45.66, both scored "right" by today's weekly review - structure
  downgrade / repeated resistance rejection, not a discipline failure). Tonight's
  tape shows the **identical pattern recurring**: a bearish engulfing AT RESISTANCE
  209.5 today (day_change -1.1%), plus 4 more dojis AT RESISTANCE 209.5 this
  evening - the exact same rejection-at-resistance signature the desk just closed
  for cause. Daily structure tag still "range/mixed" despite a nominally-bullish
  EMA order (210.52>208.18>200.12). Re-entering into the same unresolved rejection
  the position was just closed out of, with no new differentiating catalyst, would
  be reopening a thesis that was correctly killed hours ago - explicitly held off,
  not chased. Re-check only if a fresh catalyst appears or the 209.5/217.5
  resistance zone is cleanly cleared on real volume.
- **BAND** (Bandwidth) - NEW name (duty 1b, tonight's shortlist, +11.94% day_change,
  $57.4M $vol). **Fails trend gate: EMA21 48.75 < EMA50 53.55**, inverted, despite a
  confirmed morning-star reversal and 4 dojis defending support 48.15 this evening.
  Also **UNTRADABLE: 19.46% spread** (40.17/48.83 after-hours quote) - even setting
  the after-hours-widening caveat aside, the trend-gate fail alone disqualifies it.
  TradingView buy/buy/buy is a real tailwind but doesn't override two independent
  hard fails. next_earnings 2026-10-29, clear. Watch only; re-check if the EMA
  stack flips.
- **JILL** (J.Jill) - NEW name (duty 1b, tonight's shortlist, +10.89% day_change,
  $19.4M $vol, thin). next_earnings is **today** (2026-09-09) - this IS the
  earnings-reaction day (gap +11.79%, faded from a 23.48 high to 20.89 low, closed
  21.74). EMA9(20.08)>EMA21(19.58)>EMA50(18.09) is numerically ordered bullish, but
  **key_levels.structure reads "range/mixed"** - per SOP s3c the structure TAG
  itself is the gate, not just the raw EMA numbers (same literal-read precedent
  applied to NET and others by today's continuous legs) - reject on that basis.
  RSI14 73.8 and pos_in_20d_range_pct 100% add real extension risk on top. Spread
  3.39% (UNTRADABLE) on only $19.4M volume - likely after-hours widening/thin book,
  not necessarily a live concern, but combined with the structure-tag fail and the
  extension, not worth staging tonight. Six daily dojis/hammers/bullish-engulfing
  AT SUPPORT 18.61 over the past week is a genuinely defended base if the structure
  tag ever flips to uptrend - worth remembering, not worth chasing.
- **AEO** (American Eagle) - Reddit rank-climber (136->7, +129, tonight's social
  pull) - checked per duty 1b/social-as-idea-source discipline, NOT a thesis on its
  own (playbook s11: crowd hype is never a thesis). next_earnings also today
  (2026-09-09): gapped down and crashed intraday from a 19.35 high to a 14.81 low
  on the print, day_change **-11.59%** - a down-mover on a bad earnings reaction,
  not a long candidate. TradingView sell/strong_sell/neutral confirms. Exactly the
  case the doctrine warns about: real chatter, no bullish thesis behind it. Reject,
  not a long setup.
- **ROIV** (Roivant) - Real Phase 2 clinical-readout catalyst from Tuesday remains
  in force (unchanged), but still too extended to stage: RSI14 73.5, pos_in_20d_
  range_pct 100%, no resistance_above (price discovery). Tonight's tape is pure
  consolidation (7 straight dojis this evening, day_change only +1.16%) - still no
  fresh pullback level has printed to stage a probe against without chasing. Highest-
  priority watch, re-check at Thursday's open for a carved-out level.
- **CRWV** (CoreWeave) - Yesterday's momentum thesis has **reversed**: today
  day_change -6.79% (round-tripping most of Tuesday's +12.1% pop), rs_vs_spy_pp
  -6.35 (real underperformance, not just a red day), repeated shooting-star
  rejections AT RESISTANCE 95.14 tonight. EMA21/EMA50 gap technically flipped to
  bullish order (89.18 vs 88.96, a 0.22-point crossover) but that's noise-level
  given today's price actually fell hard - the technicality doesn't override the
  actual tape. No company-specific catalyst on either day (get_news still finds
  none). Demoting from "closest technical flip" to plain watch-only; the story
  reversed.
- **SNDK/MU/ALAB** (AI memory/DRAM shortage sector story, tracked since 2026-09-05)
  - re-checked fresh tonight. SNDK: still fails, EMA21 1574.01 < EMA50 1625.5 (gap
  51.49, narrower than Friday's 67.66). MU: still fails but the gap keeps closing -
  EMA21 957.16 < EMA50 964.32 (gap only 7.16, was 11.74 last check) - closest of the
  three to flipping; next_earnings 2026-09-30, now **3 weeks out, inside next
  month's window, flag increasingly**. ALAB: recovering - +3.89% today (bounce off
  yesterday's -6.74% crash), TradingView back to buy/buy (was sell/strong_sell),
  rs_vs_spy_pp +4.33, but EMA9 293.17 < EMA21 298.64 < EMA50 329.11 still clearly
  inverted, structure still "range/mixed". None stageable; MU is the one to watch
  most closely for a flip.
- **CSR** (Custom Truck One Source... note: NYSE ticker CSR, +8.9% day_change,
  explore-adjacent) - NEW-ish name, checked fresh. **Fails trend gate: EMA21 53.97
  < EMA50 54.87**, inverted. Also **UNTRADABLE: 3.51% spread** ($118.4M $vol,
  should be tighter - after-hours widening likely, but the trend-gate fail alone
  disqualifies it regardless). TradingView buy/buy/buy. Watch only.

## Macro calendar

- **2026-09-10 (Thu): mandate expires ~21:11:52Z (~16:11 CT)** - needs human
  renewal before then; flagged with increasing urgency each session, now <24h out.
- **2026-09-11 (Fri): CPI report.**
- **2026-09-15/16: FOMC** - the actual rate decision. Reinforced further tonight by
  a second, distinct macro thread (Brent >$100 on US-Iran strikes) layered on top
  of Monday/Tuesday's jobs-report/rate-odds story - two independent reasons for
  elevated volatility risk into the FOMC, both bearing on COIN/MSTR/HOOD's
  correlated BTC exposure specifically. Flag again as it approaches.
- **MU next_earnings 2026-09-30** - now inside 3 weeks; re-flag with increasing
  urgency if it stays on watch that long.

## Pruned (no fresh catalyst/edge, or fully explained above)

DUOL (closed +306.70, "right"), CHPT (closed -96.00, unlucky, see lessons.md W2),
TSLA (closed -402.25 combined, unlucky both, gate-outage attribution), CRWD (both
rungs closed today -$45.66 combined, both "right" - see Watch-only entry above for
tonight's fresh re-check, not re-added to staging), ASND/CRCL/MRVL/CRK/AAPL/STDN/
MRNA/PURR and the longer 08-31-through-09-04 prune list (VRNS/TLYS/TENB/IREN/AFRM/
PYPL/ESTC/RBRK/GAP/WDAY/DKNG/PD/FROG/NTSK/FIGR/MMED/FSLY/CRDO/AXON/ENOV/SN/WETO/
KORU/EIX/PCG/HWM/FRVO/MDB/PANW/AMD/NBIS/INTC/AMBA/TITN/AMC/EFX/NX/PL/AOUT/AEHR/BE/
CIFR/WDC/GWRE/ASAN/SNOW/HPE) - quiet or no directional edge; full reasoning in
`journal/archive/2026-09-part7.md` and `journal/YYYY-MM.md`, re-add only on new
evidence. Today's session-long rejects (SIG, ODD, NET, FBL, METU, SKUU, YMAT, ASO,
UI, FTFT, SUNE, IRD, TTAN, TBBK, BRZE, TYRA, BIAF, CASY, SKDD) - trend-gate/
earnings-day/data-quality fails per today's continuous-leg journal entries, not
re-verified tonight (no material change since this afternoon). Tonight's fresh
rejects: BAND, JILL, AEO, ROIV (still watch, not pruned), CRWV, SNDK, MU, ALAB
(still watch, not pruned), CSR - see Watch-only section above for reasons.

Next session (Thursday's PLANNING leg, pre-market 2026-09-10): **(1) COIN/HOOD/
MSTR time_stops all land TODAY (2026-09-10)** - re-decide extend-vs-cancel for all
three resting/partial positions before the open, using overnight price action and
the TV-flip caution on COIN specifically. **(2) Mandate expires today
~21:11:52Z (~16:11 CT)** - this is the session that needs to actually renew it or
flag it as urgently lapsing; check `ops/commit_paper_mandate.py`. **(3) Standing-
order quota is currently 4/6 (FAILED, see above)** - refill with the freshest
overnight tape once available; tonight's rejects (BAND/JILL/AEO/CRWV/CSR
especially) are unlikely to have changed enough overnight to reconsider without new
evidence. (4) Reset the daily loss budget per playbook s10 fresh for the day. (5)
COIN's rung2 (172.05) sits almost exactly at tonight's defended support (172.03) -
watch for a fill at the open given TV's bearish flip; don't be complacent about the
existing bullish thesis if it does fill.
