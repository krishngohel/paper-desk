# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-17 ~16:10 CT (research session, market closed - Thursday evening,
post-close homework after today's full trading day: 6 continuous/preclose legs).
Full rewrite - the 09-16 version's top item (ANGX time_stop / BWIN-TXG down-close
watch) has been resolved: ANGX was stopped out intraday today, TXG/ECO reset clean,
and BWIN's second down close is now CONFIRMED with an actual printed close.

**Regime (`ta.py --market`, fresh this session):** SPY 762.60, -0.05% vs EMA21,
RSI14 50.3, structure **downtrend (marginal)** - essentially unchanged from every
leg today. QQQ 716.92, +0.60% vs EMA21, RSI14 53.2, **range/mixed**. Weak/mixed
tape, no reason to chase size. No fresh macro catalyst today (yesterday's Fed
hike/Warsh presser remains the dominant recent driver, already priced in).

## Mandate & quota status

**Mandate renewed 2026-09-14, `consent.expires_at` 2026-09-28T17:58:50Z - 11 days
runway, no urgency.** Not halted, not expired - verified fresh this session both via
`status` and a direct read of `~/.vibe-trading/live/alpaca/mandate.json`.

**Standing-order quota: MET this session - 6 live conditional entries across 6
distinct symbols**, restored from a 4/4 carry-in (below floor after today's HUT/CYPH
trigger cancellations). Inherited 4 resting buy-limits (CRWD 232.00, IOT 38.75, RBRK
90.15, ZS 160.75) and added two fresh deep-pullback probe rungs tonight: **SMTC
@146.91/6sh** (order `41354f13`, the exact 09-16 confirmed morning-star base, ~17.5%
below close) and **ECO @61.90/27sh** (order `3f329eaf`, the only support level on
file for an extremely blow-off-extended name, ~28% below close - a crash-scenario
probe, not a near-term thesis). No armed triggers remain live (HUT, both CYPH
attempts all cancelled/watcher-missed today; PSIX expired unfired at 15:00 CT and
was not replaced - today's hunt found no fresh rule-3c-passing name to arm).

## PRIORITY 1 (unconditional): BWIN exit due at next session's open

BWIN's playbook s6a governing rule (2 consecutive lower daily closes -> exit) is now
**CONFIRMED**, not provisional: 09-16 close 32.04 (first down close, vs 09-15's
higher close) and TODAY's actual printed close 31.97 (`bars BWIN 1d 5`) - a second,
confirmed lower close. This is a research session (market closed, no market orders
per SOP, and research's five duties don't include position exits) - not acting on it
tonight is correct discipline, not a lapse. **The very next trading session's FIRST
action, before any hunting, must be `sell BWIN 75sh` (exit_reason
exit-condition-hit).** BWIN's mechanical stop (28.82, 9.9% clear) remains a real
backstop overnight in the meantime.

## Book (7 positions, above the 3-6 target - will drop to 6 once BWIN closes)

- **BWIN** 75 sh @ avg 31.89, actual close 31.97 (+0.25% ROI). Stop 28.82 (9.9%
  clear). **EXIT DUE - see Priority 1 above.** next_earnings 2026-11-03 (safe,
  moot once closed).
- **ECO** 10 sh @ avg 82.92, actual close 86.25 (+4.02% ROI). Stop 74.38 (13.7%
  clear, mechanical backstop), no target (s6a-style hold, time_stop 2026-10-15).
  RSI14 84.3, pos_in_20d_range 100% - genuine blow-off extension; no down-close
  yet, holds clean. New deep add-rung 61.90/27sh resting (see quota section).
  next_earnings 2026-11-11 (safe).
- **IOT** 75 sh @ avg 37.9717, last ~40.1 (+5.7% ROI). Stop 38.68 (tightest
  clearance in the book, ~3.6%), target 44.68 resting (`c07abd8f`). Rung2 add
  30sh@38.75 GTC still unfilled (order `50b8f779`), sits at tested multi-touch
  support (38.68). time_stop 2026-09-22. next_earnings 2026-12-03 (safe).
- **RBRK** 48 sh blended avg 100.9827 (2 rungs, both targets resting: 109.12/29sh
  `1d465b46`, 110.52/19sh `6f618ba8`), last ~107.5, +~6.5% ROI. Structure clean
  uptrend. 3rd-rung add 15sh@90.15 GTC still unfilled (order `4e8ee047`).
  time_stop 2026-09-19. next_earnings 2026-12-03 (safe).
- **SMTC** 12 sh @ avg 168.28, actual close 178.19 (+5.89% ROI). Stop 162.59
  (8.7% clear), target 185.35 resting (`15d59c27`). Structure clean uptrend,
  TradingView strong_buy. New deep add-rung 146.91/6sh resting (order `41354f13`,
  the exact 09-16 morning-star base). time_stop 2026-09-19. next_earnings
  2026-11-23 (safe).
- **TXG** 15 sh @ avg 75.64, actual close 76.98 (+1.77% ROI). Stop 64.73 (15.9%
  clear, mechanical backstop), no target (s6a-style hold, time_stop 2026-10-15).
  Reset clean today (76.98 vs 09-16's 72.68 first-down-close) - no down-close,
  holds. next_earnings 2026-11-05 (safe).
- **ZS** 17 sh @ avg 193.12, last ~194-197 (+~1-2% ROI). Stop 188.15 (tight,
  ~3-4% clear). Target 208.03 resting (`489b3ab4`). Deep add-rung 21sh@160.75
  GTC still unfilled (order `4b0ad29d`). time_stop 2026-09-19. next_earnings
  2026-11-24 (safe).

## Staged / armed for next session - ranked

- **CRWD** - resting GTC buy-limit 232.00 (order `4bab1e47`), unfilled since
  09-14. Price has run well away from this level; structure clean uptrend, TV
  buy/strong_buy - thesis intact/validated, not dead. Real support now sits much
  lower (~204 per recent `ta.py`) - candidate for a second, deeper rung if the
  book ever wants more CRWD exposure; not added given existing cybersecurity-
  cluster concentration (RBRK/ZS/CRWD). next_earnings 2026-12-01 (safe).
- No armed (above-market) triggers remain live tonight - all of HUT/CYPH/PSIX
  from the last two days are cancelled or expired unfired. Next trading session
  should arm a fresh confirmation trigger if a genuine rule-3c-passing name
  appears; tonight's hunt (5 names) found none.

## Watch only (fails trend gate, tradability, or lacks a fresh catalyst tonight)

**Fresh names hunted tonight (duty 1b, screen.py explore + 5 full `ta.py`
workups), none qualify:**
- **BHVN** (Biohaven) +15.14% day, $78.3M vol - structure explicit "downtrend",
  EMA21 14.04 < EMA50 14.44 inverted. No fresh catalyst in `get_news` (most
  recent items are a 09-10 FDA partial clinical hold and a 09-08 RBC downgrade,
  both stale/negative) - looks like an unexplained bounce off a beaten-down base.
  next_earnings 2026-11-09.
- **RARE** (Ultragenyx) +14.6% day, $169.7M vol - deeply inverted EMA stack
  (EMA9 15.22 < EMA21 18.80 < EMA50 23.62), structure "downtrend". Also tonight's
  #1 StockTwits/Reddit rank-climber (rank 278->25 in 24h) with no fresh news
  beyond a string of September downgrades/PT cuts - textbook playbook s11
  crowd-hype-is-not-a-thesis case; the trend gate kills it independently anyway.
  next_earnings 2026-11-03.
- **FCEL** +14.52%, $163.8M vol - close but fails on the letter: structure tag
  reads "uptrend" but EMA21 17.22 < EMA50 19.70 (still inverted, EMA50 hasn't
  caught up), same near-miss pattern as AMD/GNRC/VICR rejected earlier today.
  next_earnings 2026-12-17.
- **XE** +11.81%, $138.7M vol - structure "downtrend", full EMA stack inverted
  (EMA9<EMA21<EMA50). next_earnings 2026-11-16.
- **INIO** +14.91%, $268.2M vol - UNTRADABLE outright (5.45% spread), also
  range/mixed structure with EMA21<EMA50. Rejected before structure was even
  relevant. next_earnings 2026-10-27.

**Repeat rejects from earlier today, unchanged reasons (not re-run fresh
tonight):** SDGR/TEM/AMDL (structure-tag or EMA-order fail), AMD (EMA21<EMA50),
GNRC/VICR/GLOO (EMA21<EMA50 despite real catalysts/volume), HPE/MRVL/DELL/BE
(pass rule 3c but sub-0.7x volume and/or actively rejected at resistance on the
live tape), MNOV (parabolic/extended, no nearby defended level), RTB (UNTRADABLE
spread + downtrend, doubly disqualified).

## Macro calendar

- No book or staged-name earnings fall within the next 30 days (BWIN 11-03, ECO
  11-11, IOT 12-03, RBRK 12-03, SMTC 11-23, TXG 11-05, ZS 11-24, CRWD 12-01) -
  duty-2 earnings sweep tonight found no near-term conflicts.
- No fresh macro events flagged for tomorrow (2026-09-18); the Fed
  hike/Warsh-presser regime shift from 09-16 remains the dominant recent driver,
  already reflected in the regime read above.

## Pruned (no fresh catalyst/edge, or fully explained above)

ANGX (stopped out 2026-09-17 10:20 CT, watcher-missed mechanical stop, manually
enforced at 4.96, -$29.24 realized - scored later in review, not re-added without
a fresh catalyst). HOOD/APA (closed 2026-09-16, already scored "unlucky", not
re-added). COIN/MSTR/LITE/SMMT (closed prior to 09-14, already scored). CYPH/HUT
(three watcher silent-misses across both names 09-16/09-17; CYPH's underlying
uptrend may still be real but requires a genuine pullback/support retest with
volume before re-arming, not a chase off the missed levels - not pursued tonight,
no fresh setup found on a quick re-check). BHVN/RARE (see Watch-only above -
crowd hype, trend-gate fail, not pursued per playbook s11).

Next session (Friday 2026-09-18, likely the open/planning leg):
**(1) SELL BWIN 75sh IMMEDIATELY as the first action - the s6a second-lower-close
exit is confirmed, not provisional (see Priority 1 above).** **(2) Standing-order
quota is 6/6 tonight - no immediate action needed, but consider arming a fresh
confirmation trigger if a genuine rule-3c-passing name turns up, since no armed
triggers remain live.** **(3) IOT and ZS remain the tightest stop clearances in
the book - continue manual bar-verification every leg given the still-open
watcher reliability issue (4 confirmed silent-misses over 09-16/09-17: ANGX stop,
CYPH x2, HUT).** **(4) Regime unchanged (SPY marginal downtrend, QQQ range) - no
reason to chase size; book returns to 6 positions (within the 3-6 target) once
BWIN closes, so there is no pressure to prune further, but also no urgency to add
beyond what's already staged.**
