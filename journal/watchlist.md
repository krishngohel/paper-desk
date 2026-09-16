# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-16 ~17:15 CT (research session, market closed - Wednesday evening,
post-close homework after today's full trading day: 8 continuous legs + preclose +
daily review). Full rewrite - the 09-14 version referenced a 4-position book
(ANGX/BWIN/IOT/ZS) that has since grown to 8 positions and a different staged set;
superseded entirely.

**Regime (`ta.py --market`, fresh this session):** SPY 754.05 - now a **confirmed
downtrend** (lower highs + lower lows, -1.17% vs EMA21, RSI14 42.0), a genuine
deterioration from the "range/mixed" read every prior session logged this week. QQQ
709.18 still range/mixed (-1.05% vs EMA21, RSI14 44.2). **Cause: the Fed hiked 25bp
today (new chair Kevin Warsh's first meeting) and struck a hawkish tone in the
press conference - 16 of 18 policymakers project at least one MORE hike before
year-end, and the 10-year yield reclaimed 5% into the close** (Benzinga, multiple
stories 13:32-19:34 UTC 2026-09-16). Stocks chopped both ways intraday (crude fell
3.6% on a Saudi pipeline restart, lifting chips/optics mid-session - AXTI/CIFR/FPS/
BBNX/SMTC all gainers) but sold off hard into the close once Warsh's hawkish
presser landed (Dow -1%+ per the 19:34 UTC story). **Read this as a genuine regime
warning, not noise: two straight sessions of hawkish Fed repricing (09-14 AI-slowdown
selloff, now today's hike) argue for conservative sizing and no chasing until the
tape proves otherwise.** The 09-14 cybersecurity-rotation story (CRWD/RBRK/ZS/PANW/S
rallying while AI-hardware names sold off) is still the dominant sector narrative
layered underneath this macro chop - the book's RBRK/ZS/CRWD exposure is that thesis,
not a fresh idea.

## Mandate & quota status

**Mandate renewed 2026-09-14, `consent.expires_at` 2026-09-28T17:58:50Z - 12 days
runway, no urgency.** Not halted, not expired - verified fresh this session both via
`status` and a direct read of `~/.vibe-trading/live/alpaca/mandate.json`.

**Standing-order quota: MET this session - 6 live conditional entries across 5
distinct symbols.** Inherited 4/4 from the close (IOT resting buy 38.75/30sh, CRWD
resting buy 232.00/6sh, HUT armed trigger trg-20260916-003 @96.80/29sh, CYPH armed
trigger trg-20260916-004 @2.75/400sh - both expire tomorrow 2026-09-17T15:00 CT).
Duty-1b hunt (screen.py explore + 4 fresh full `ta.py` workups: BBNX/ARQT/AXTI/AMRX)
found **zero new qualifying names** - all fail SOP s3c's trend gate (see Watch-only
below). Since research sessions may only stage conservative GTC buy-limits BELOW
today's close at genuine support (not above-market breakout triggers), refilled the
quota by adding TWO deep-pullback probe rungs on existing book names at real,
`ta.py`-identified support: **RBRK add-rung @90.15/15sh** (order 4e8ee047, ~14.1%
below today's close, multi-touch support - doji + bearish-engulfing both tested it
09-10/09-11) and **ZS add-rung @160.75/21sh** (order 4b0ad29d, ~16.1% below close,
single-touch support per L8 - graded down accordingly). Ledger records
t-2026-09-16-002/003, both C-probe, `pending_entry: true`. Flagging explicitly: both
adds are the SAME cybersecurity-rotation cluster as the existing RBRK/ZS/CRWD
exposure - real correlation risk, not diversification; they only fill on a genuine,
large pullback and are sized tiny (~0.11-0.12% equity risk each) precisely because of
that concentration.

## Book (8 positions, well above the 3-6 target)

- **ANGX** 68 sh @ avg 5.39, last 5.30 (-1.7% ROI). Stop 5.05 (4.7% clear), target
  5.95 resting (4cb979aa). **time_stop 2026-09-17 is TOMORROW - the planning/open
  leg MUST run a time_stop_review first thing.** Position remains inside its stop
  (L7: not evidence either way). `tradability` UNTRADABLE tonight (2.79% spread,
  thin $12.3M volume) - factor the poor fill quality into tomorrow's decision.
  next_earnings 2026-11-03 (safe).
- **BWIN** 75 sh @ avg 31.89, last 32.04 (+0.5% ROI). Stop 28.82 (10.2% clear,
  watcher-enforced), **no target - governing exit is 2 CONSECUTIVE lower daily
  closes** (playbook s6a momentum archetype). Closed DOWN today (32.04 vs 32.49
  yesterday) - **first down close.** A second lower close tomorrow triggers the
  exit; check this FIRST at tomorrow's open. time_stop 2026-10-13 (outer backstop).
  next_earnings 2026-11-03 (safe).
- **ECO** 10 sh @ avg 82.92, last 84.74 (+2.2% ROI). Stop 74.38 (12.2% clear,
  mechanical backstop), no target (s6a-style hold). RSI14 83.0 - deep blow-off
  territory, pos_in_20d_range 100%, no down-close yet. next_earnings 2026-11-11
  (safe).
- **IOT** 75 sh @ avg 37.9717, last 40.66 (+7.1% ROI). Stop 38.68 (5.1% clear),
  target 44.68 resting (c07abd8f). Rung2 add 30sh@38.75 GTC still unfilled
  (order 50b8f779) - sits right at the tested multi-touch support (38.68, doji
  09-10 and 09-11), still valid, not stale. time_stop 2026-09-22. next_earnings
  2026-12-03 (safe).
- **RBRK** 48 sh blended avg 100.9827 (2 rungs: 29sh stop 97.10/target 109.12,
  19sh stop 98.50/target 110.52), last 104.98 (+3.9% ROI). Both targets resting.
  **New 3rd rung staged tonight: 15sh @ 90.15 GTC (order 4e8ee047, see quota
  section above).** Structure now clean "uptrend" (was range/mixed on 09-14 - the
  ambiguity flagged in the prior watchlist has resolved itself as the trend
  extended). TV strong_buy/strong_buy/buy. time_stop 2026-09-19. next_earnings
  2026-12-03 (safe).
- **SMTC** 12 sh @ avg 168.28, last 167.55 (-0.4% ROI). Stop 162.59 (3.6% clear),
  target 185.35 resting (15d59c27). Confirmation-trigger entry from today's leg
  (trg-20260916-002, watcher missed it, fired manually) - +11.9% day, MORNING STAR
  reversal at support 146.91, structure clean uptrend. time_stop 2026-09-19.
  next_earnings 2026-11-23 (safe).
- **TXG** 15 sh @ avg 75.64, last 72.68 (-3.9% ROI). Stop 64.73 (10.9% clear,
  mechanical backstop), no target (s6a-style hold). Closed DOWN today (72.68 vs
  74.39 yesterday) - **first down close**, same as BWIN. A second lower close
  tomorrow triggers the exit; check FIRST at tomorrow's open. next_earnings
  2026-11-05 (safe).
- **ZS** 17 sh @ avg 193.12, last 191.58 (-0.8% ROI). Stop 188.15 (**1.8% clear -
  TIGHTEST in the book**), target 208.03 resting (489b3ab4). **New 2nd rung staged
  tonight: 21sh @ 160.75 GTC (order 4b0ad29d, see quota section above).**
  time_stop 2026-09-19. next_earnings 2026-11-24 (safe).

**s6a watch for tomorrow's open (highest-priority item):** BWIN and TXG BOTH now
carry their first confirmed down close from today. A SECOND consecutive lower close
on either at tomorrow's close is an exit per playbook s6a - check both before
anything else next session.

## Staged / armed for next session - ranked

- **HUT** (bitcoin miner) - armed trigger trg-20260916-003, buy>=96.80, 29sh,
  **expires tomorrow 2026-09-17T15:00 CT**. Real move (+7.33% today, $96.6M
  dollar volume), but literal EMA order still fails (EMA21 89.99 < EMA50 95.77,
  inverted) despite an "uptrend" structure tag - graded C, arming above both the
  day high and the next resistance shelf (96.75) to require the whole EMA stack
  to roll forward before it fires. Last check ~10.2%+ OTM and fading late in the
  day - will likely need re-arming with fresh data if it lapses tomorrow, do not
  blindly re-arm the same level. next_earnings 2026-11-04 (safe).
- **CYPH** (Cypherpunk Technologies) - armed trigger trg-20260916-004, buy>=2.75,
  400sh, **expires tomorrow 2026-09-17T15:00 CT**. First name in 11 hunt legs
  today to clear SOP s3c cleanly (uptrend structure + EMA order both pass).
  Caveat: the only analyst note on file (Cantor Fitzgerald, stale) carries a PT
  well below current price, and the position was fading from its highs late in
  the day - re-check the thesis is still intact before trusting a lapse/re-arm
  tomorrow. next_earnings 2026-11-11 (safe).
- **CRWD** - resting GTC buy-limit 232.00 (order 4bab1e47), unfilled since 09-14.
  Price has run hard away from this level (last 241.36, structure now a CONFIRMED
  clean uptrend, TV buy/strong_buy) - the order is further OTM in % terms than
  when staged, but the thesis is intact/validated, not dead, so NOT cancelling
  (a stale-order review is about thesis death, not just distance). Real support
  now sits much lower (204.27 per fresh `ta.py`) - a candidate for a second, even
  deeper rung if the book ever wants more CRWD exposure; not added tonight given
  the correlation concentration already added via the RBRK/ZS rungs above.
  next_earnings 2026-12-01 (safe).

## Watch only (fails trend gate, tradability, or data quality tonight - do not stage)

**Fresh names hunted tonight (duty 1b, screen.py explore + full `ta.py` workups),
none qualify:**
- **BBNX** +15.9% day, $161.6M $vol, EMA order numerically bullish (9>21>50) but
  `key_levels.structure` explicitly "range/mixed" - fails SOP s3c's stricter
  reading (structure tag must not read mixed). pos_in_20d_range 100%, single-day
  extension. next_earnings 2026-10-27.
- **ARQT** +11.4% day, $130.7M $vol - EMA9 (24.38) < EMA21 (24.64), inverted; also
  structure "range/mixed". Clean double-fail.
- **AXTI** +12.5% day, $763.8M $vol - EMA9 (62.4) < EMA21 (64.11), inverted;
  structure "range/mixed". Double-fail despite real liquidity.
- **AMRX** +8.5% day, $92.0M $vol - `key_levels.structure` explicit "downtrend
  (lower highs + lower lows)" despite today's pop. Fails outright.

**Repeat rejects, unchanged reasons (not re-run fresh tonight, no material new
data since today's continuous legs already exhausted them):** DLXY/MEDS/FTFT/ZCSH
(data-quality flags or thin/flat despite huge headline %), BULL/CONL/RETO (downtrend
or range/mixed structure fails), ALHC/JBHT/FANG/MTDR/MGY/SYNA/ON/BLSH/RCAT (today's
decliners - long-only excludes outright).

## Macro calendar

- **2026-09-16 (today): Fed hiked 25bp, hawkish presser (new chair Warsh), 10Y
  reclaimed 5%, 16/18 policymakers project another hike before year-end.** This is
  now the dominant regime fact, not an upcoming risk - SPY closed in a confirmed
  downtrend on it. Size new risk conservatively until the tape proves otherwise.
- **ANGX time_stop 2026-09-17 (tomorrow)** - mandatory time_stop_review at
  tomorrow's planning/open leg, the single most time-sensitive item.
- **BWIN and TXG both on their first down close** - the s6a second-lower-close
  check at tomorrow's close is the other top-priority item (see Book section).
- **HUT and CYPH triggers both expire tomorrow 2026-09-17T15:00 CT** if unfired.
- No book or staged-name earnings fall within the next 30 days (ANGX/BWIN 11-03,
  ECO 11-11, IOT 12-03, RBRK 12-03, SMTC 11-23, TXG 11-05, ZS 11-24, HUT 11-04,
  CYPH 11-11) - the earnings sweep this session found no near-term conflicts.

## Pruned (no fresh catalyst/edge, or fully explained above)

HOOD (stopped out 2026-09-16 on DOJ insider-trading charges against two former
engineers, scored "unlucky" in today's daily review - sound thesis, genuine
stock-specific negative news, not a process failure; not re-added without a fresh
catalyst). APA (stopped out 2026-09-16 on an overnight macro gap through its stop,
also scored "unlucky"). COIN/MSTR/LITE/SMMT (closed prior to 09-14, already scored).
AEO/SPCX (Reddit rank-climbers checked via `social.json` tonight - AEO has no new
information since its earnings crash, SPCX is not a tradable US equity on this
broker; neither pursued, per playbook s11 crowd hype is never a thesis on its own).

Next session (Thursday 2026-09-17, likely the PLANNING leg pre-market):
**(1) ANGX time_stop lands today** - re-decide extend-vs-cancel fresh using
overnight/pre-market price action; note the UNTRADABLE 2.79% spread when weighing
a market-hours exit vs. letting the resting target/stop work. **(2) BWIN/TXG s6a
second-down-close check** - if either closed lower again today, that's an exit
regardless of the fresh unrealized mark (L7). **(3) HUT and CYPH triggers expire
today 15:00 CT** - do not blindly re-arm without fresh data if they lapse.
**(4) Standing-order quota is 6/5 tonight but includes 2 concentrated
cyber-cluster adds (RBRK/ZS) - if either fills, watch the correlation exposure
rather than treating it as free diversification.** **(5) Regime has shifted
meaningfully hawkish (Fed hike + Warsh presser, SPY confirmed downtrend)** - size
new entries conservatively and demand a real trend-gate pass, not just a big
day_change%, until the tape stabilizes.
