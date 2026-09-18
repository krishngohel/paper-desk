# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-18 ~18:10 CT (research session, market closed - Friday evening,
post-close homework after today's full trading day: 6 continuous/preclose/weekly-review
legs). Full rewrite - BWIN's exit (closed this morning +$5.25 on the s6a two-down-close
rule) and today's SMTC partial-fill split are resolved and folded in; the 09-17
version's Priority-1 BWIN item is gone.

**Regime (`ta.py --market`, fresh this session):** SPY 761.69, -0.15% vs EMA21,
RSI14 49.5, structure **downtrend (lower highs + lower lows)**. QQQ 721.45, +1.11%
vs EMA21, RSI14 55.9, **range/mixed**. Weak/mixed tape, no reason to chase size.
Real macro driver this week: the Fed hiked 25bp again under new chair Warsh, 10Y
yield hit 5.04% (2007 highs), record diesel prices - explains SPY's downtrend and
broad materials/industrials weakness. Separately, a genuine crypto-equity rally is
live (Bitcoin >$80k on a CFTC regulatory proposal; COIN/MSTR/HOOD/BMNR/GLXY all
named together in Friday's Benzinga sweep) - checked COIN against rule 3c tonight
(see Watch-only below), still fails on structure despite the real catalyst.

## Mandate & quota status

**Mandate renewed 2026-09-14, `consent.expires_at` 2026-09-28T17:58:50Z - 10 days
runway, no urgency.** Not halted, not expired - verified fresh this session both via
`status` and a direct read of `~/.vibe-trading/live/alpaca/mandate.json`.

**Standing-order quota: MET this session - 6 live conditional entries across 6
distinct symbols**, unchanged from the last review: resting buy-limits ECO 61.90,
SMTC 146.91, ZS 160.75, RBRK 90.15, CRWD 232.00, TXG 58.70. No armed triggers live
(`triggers.jsonl`: 52 total, all cancelled/fired/consumed). Nothing added or
cancelled tonight - the duty-1b hunt (TJGC/DFDV/TMS) and the duty-1 sector
follow-up (COIN) all missed on structure and/or tradability, so no fresh name
earned a resting order and no existing thesis died.

## Book (5 positions, within the 3-6 target)

- **ECO** 10 sh @ avg 82.92, now 85.2573 (+2.82% ROI). Stop 74.38 (12.76% clear,
  s6a mechanical backstop), no target (s6a-governed hold, time_stop 2026-10-15).
  **1 confirmed down close (09-18) - Monday's close is day 2; a second lower close
  is an immediate exit.** Deep add-rung 61.90/27sh still resting. next_earnings
  2026-11-11 (safe).
- **RBRK** 48 sh blended avg 100.9827 (2 rungs, both targets resting: 109.12/29sh
  `1d465b46`, 110.52/19sh `6f618ba8`), now ~106.76 (+5.72% ROI). Structure clean
  uptrend. 3rd-rung add 15sh@90.15 GTC still unfilled (order `4e8ee047`).
  **time_stop 2026-09-19 (this weekend) on both filled rungs - Monday's planning
  leg must decide extend-vs-close if targets haven't filled.** next_earnings
  2026-12-03 (safe).
- **SMTC** 3 sh @ avg 168.28 (post-09-18 partial-fill split: original 12sh target
  order filled 9 of 12 at 185.36 intraday, remaining 3sh still open), now
  ~186.92 (+11.08% ROI). Stop 162.59 (13.02% clear), target 185.35 resting
  (`15d59c27`) for the remaining 3sh - **last mark already sits above 185.35 yet
  the order shows unfilled; confirm at Monday's open whether it filled over the
  weekend gap or needs re-resting.** Deep add-rung 146.91/6sh still resting
  (order `41354f13`). time_stop 2026-09-19. next_earnings 2026-11-23 (safe).
- **TXG** 15 sh @ avg 75.64, now 76.80 (+1.53% ROI). Stop 64.73 (15.72% clear,
  mechanical backstop), no target (s6a-governed, time_stop 2026-10-15). **1
  confirmed down close (09-18) - same Monday-close check as ECO.** Deep add-rung
  58.70/15sh still resting. next_earnings 2026-11-05 (safe).
- **ZS** 17 sh @ avg 193.12, now 198.20 (+2.63% ROI). Stop 188.15 (tightest
  clearance in the book, 5.07% clear). Target 208.03 resting (`489b3ab4`, 4.94%
  away). Deep add-rung 160.75/21sh still resting. time_stop 2026-09-19.
  next_earnings 2026-11-24 (safe).

## Staged / armed for next session - ranked

- **CRWD** - resting GTC buy-limit 232.00 (order `4bab1e47`), unfilled since
  09-14. Structure clean uptrend, TV buy/strong_buy - thesis intact, not dead.
  Real support now sits much lower (~204-210 per recent `ta.py` reads) - a
  candidate for a second, deeper rung if the book ever wants more CRWD exposure;
  not added given existing cybersecurity-cluster concentration (RBRK/ZS/CRWD).
  next_earnings 2026-12-01 (safe).
- No armed (above-market) triggers remain live tonight. Next trading session
  should arm a fresh confirmation trigger if a genuine rule-3c-passing name
  appears; tonight's hunt (4 names: TJGC/DFDV/TMS/COIN) found none.

## Watch only (fails trend gate, tradability, or lacks a fresh catalyst tonight)

**Fresh names hunted tonight (duty 1b, screen.py smallcap-explore lens, 3 full
`ta.py` workups; plus duty-1 sector follow-up), none qualify:**
- **TJGC** ($39.6M dvol, day +59.58%, gap 24.11%) - RSI14 91.0, pos_in_20d_range
  100%, structure explicit "range/mixed" despite a bullish EMA stack/TV
  strong_buy - verified via daily candles (two dojis + an inside bar AT support
  10.6 right before today's gap, i.e. a fresh breakout attempt, not an
  established trend). Rejected on rule 3c. Spread 1.20% (TRADABLE_TIGHT_SIZE)
  would have allowed a probe had structure passed. next_earnings: none found
  (ta.py flags possible delisted-adjacent ticker).
- **DFDV** ($51.9M dvol, day +21.0%) - structure also "range/mixed" (would fail
  3c regardless); moot anyway, spread 3.49% -> UNTRADABLE (playbook s7b).
  next_earnings 2026-11-11.
- **TMS** ($16.0M dvol, day +7.97%) - structure tagged "uptrend" with a
  confirmed morning-star at support 7.01, but literal EMA order fails (EMA21
  7.07 < EMA50 7.13) - the literal 3c test overrides the tag. Also spread 3.70%
  -> UNTRADABLE independently. Double-disqualified. next_earnings 2026-11-12.
- **COIN** (crypto-equity rally follow-up, +11.66% day) - close 194.25 > EMA9
  179.26 > EMA21 176.18 > EMA50 167.57 numerically passes, but structure tagged
  "range/mixed" - verified via `get_stock_bars 1Day 15` rather than trusting the
  tag: closes swung 191.45(09-14)->172.11->164.51->173.97->194.25(09-18), a ~15%
  two-day drop THIS WEEK before today's gap. Rejected on rule 3c - one gap day
  inside an established chop range is not a confirmed uptrend, regardless of the
  genuine BTC>$80k/CFTC catalyst (playbook s11: don't let a known story override
  the chart). Revisit only if COIN/MSTR/HOOD print a real multi-day uptrend, not
  another single gap.

**Repeat rejects, unchanged reasons (not re-run fresh tonight):** RIOT, WDC,
AAOI, CLSK, HOOD, MARA, BMNR, ALMR, BIAF, NCI, GEMI, SOLT/BSOL/HALO/BTDR,
SNDK/MUU/AVGO/LRCX/STX/COHR/AMAT/MTSI/NVDA/INTC/CIFR cluster, CYPH/HUT/PSIX/ADPT,
DSP/ABTC/WOLF/GLOO/AKAN, MSTR/CRCL/XENE, IREN/FPS (verified range-bound/EMA-fail
2026-09-18), FWDI/FTCI/SGML/BKKT/BTGO/MGN/CCXI/SOC/ZTG/ALMU/FEAM/NOK/ETHA/BITO/
IBIT/VRT/ETN. XENE tonight specifically: -30.69% on a real news catalyst (FDA
application filed, but enrollment in depression trials voluntarily paused) -
clinical-risk gap-down, not a buyable dip, long-only rules it out as a short
candidate anyway.

## Macro calendar

- No book or staged-name earnings fall within the next 30 days (ECO 11-11, RBRK
  12-03, SMTC 11-23, TXG 11-05, ZS 11-24, CRWD 12-01) - duty-2 earnings sweep
  tonight found no near-term conflicts.
- No fresh macro event flagged for Monday beyond the already-priced-in Fed
  hike/10Y-yield move (5.04%, 2007 highs) - the dominant driver behind SPY's
  downtrend read above.

## Pruned (no fresh catalyst/edge, or fully explained above)

BWIN (closed 2026-09-18 08:38 CT on the confirmed s6a two-down-close exit,
+$5.25/+0.22%, scored "right" - not re-added without a fresh catalyst). ANGX
(stopped out 2026-09-17, watcher-missed mechanical stop, scored "unlucky").
HOOD/APA (closed 2026-09-16, scored "unlucky"). COIN/MSTR/LITE/SMMT (closed
prior to 09-14, already scored - COIN re-checked fresh tonight per the crypto
catalyst, still fails 3c, see Watch-only above). CYPH/HUT (repeated watcher
silent-misses, no fresh setup on last check). BHVN/RARE (crowd hype/trend-gate
fail, 2026-09-17). IREN/FPS (verified range-bound/EMA-fail via bars, 2026-09-18).

Next session (Monday 2026-09-21, the open/planning leg):
**(1) Read the CONFIRMED Monday close for TXG/ECO FIRST - both already carry one
down close from 09-18; a second consecutive lower close is an immediate s6a exit
on either name, before any hunting.** **(2) Confirm whether SMTC's remaining
3sh target (185.35) filled over the weekend gap or needs re-resting.** **(3)
Decide extend-vs-close on RBRK/ZS's 2026-09-19 time_stops if their targets
haven't filled by then.** **(4) Standing-order quota is 6/6 - no immediate
action needed, but arm a fresh confirmation trigger if a genuine rule-3c-passing
name turns up; tonight's hunt found none.** **(5) ZS remains tightest stop
clearance (5.07%) - continue manual bar-verification given the ongoing watcher
reliability issue (memory: project_watcher_silent_miss).** **(6) Regime
unchanged (SPY downtrend on a real Fed/yield driver, QQQ range) - no reason to
chase size; a live crypto-equity rally (COIN/MSTR/HOOD) sits outside the book's
structure gate and is worth a fresh look only if it stops being a single gap
day.**
