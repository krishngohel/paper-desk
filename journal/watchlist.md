# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-10-01 evening (research leg after Thursday's close). Mandate valid
(exp 2026-10-12; re-read fresh). Not halted.

**Regime (`ta.py --market`, 10-01 close):** SPY 763.99, -0.15% vs EMA21, RSI 48.9,
range/mixed. QQQ 742.03, +1.75% vs EMA21, RSI 61.1, range/mixed. 10Y 5.29% rate shock is
the tail risk. Neutral posture, s6a first, confirmation triggers only.

## Standing orders

0 live orders, 0 armed triggers. Nothing staged: Friday is a gap-risk open and no name has a
numeric above-market trigger worth arming overnight; no rung beats the `anticipatory_limit`
record (6 closed, 33% wins, -$66/trade).

## Book (1 position, target 3-6)

- **TXG** 15 sh @ 75.64, 10-01 close 88.74 (< prior 90.36 = lower close 1 of 2), +$171 / +15%.
  s6a-governed: **Friday 10-02 close below 88.74 = second lower close = SELL.** Stop 64.73, no
  target. RSI 73.3, EMA9 84.95 > EMA21 77.71 > EMA50 65.40. next_earnings 2026-11-05.

## Ranked - Friday 10-02 hunt

1. **Manage TXG first** (close vs 88.74).
2. **MPC - best 3c pass with sane L9 profile.** Close 420.15 > EMA9 400.08 > EMA21 393.25 >
   EMA50 362.16, RSI 68.2 (ta; trade_context RSI 57.1 neutral bucket), rs +3.13pp =
   `outperforming_0-10pp` (11 closed, 45.5%, +$626.59), +6.4% today on 0.7x volume (thin),
   spread 0.20%, $877M. NOT an s6a entry (3 rising closes fails: 09-30 shooting star), so
   secondary archetype, B/C probe. **Trigger:** 5m break and hold above 431.08 (resistance)
   with volume >1.2x, or a pullback hold of 411.41 (opening-range high). Stop under 402.38
   or 388.16 support, re-anchor to the fill. Kill: close below EMA21 393.25.
   next_earnings 11-03. Run `trade_context.py --check` fresh at the time.
3. **MU - post-print follow-through.** Close 1097.39 > EMA9 1060.96 > EMA21 1025.18 > EMA50
   973.51, RSI 63.4, +3.0% on 1.8x volume after the double beat, bullish engulfing at support
   1032, ~11 points under resistance 1108.72, spread 0.05%. **Trigger:** confirmation only -
   hold above 1108.72 with volume >1.2x; do not chase a gap above it. Stop under 1060 (EMA9),
   probe. Kill: close below 1032. next_earnings 12-23.
4. **STX - broke my 925.44 trigger on the close (945.57), but L9.** Close > EMA9 909.5 > EMA21
   882.7 > EMA50 866.6, RSI 61.8, vol 0.66x (thin), morning star. 20d rs +12.83pp =
   `leader_10pp+` (SIGNIFICANT, 1 of 17): an entry needs a written L9 exception (none today).
   Stop would sit under 870.38. next_earnings 10-27.
5. **INTC - passes 3c, blocked by L9.** Close 120.0, 20d rs +29.89pp. Watch only.
6. **NTRA (new 10-01) - passes 3c, fails on extension/RSI.** Close 408.47 > EMA9 399.64 >
   EMA21 375.01 > EMA50 334.91, RSI 77.2, +27% 1m, shooting stars 09-30 and 10-01 at 427.47 /
   423.43, ATR 13.24 (3.2%), spread 0.49%. Watch only until RSI resets or a base forms; stop
   would be under 375 = 8% risk.
7. **QCOM / BE / P / TWLO / OKTA / MRNA / ALAB / ARM / SNDK / SOXL - big_leaders / s6a
   scan names, L9 blocked.** Momentum scan 10-01 sane-risk lists: SOXL 3.13%, SPCX 2.60%,
   OKTA 2.61%, TWLO 2.38%, SNDK 1.78%, P 1.66%. SPCX: RSI 51, close 148.07 > EMA9 149.09
   fails (below EMA9 today), range, no thesis. GOOGL fails 3c (EMA21 < EMA50).

## Watch only / rejects

**10-01 new-name vets (research duty 1b):**
- **CTVA** (-83.8%, $1.1B traded, 0.08% spread): NOT a signal. Corteva completed its spin-off
  of Vylor (VYLR) 10-01 (Benzinga); the price drop is mechanical and ta.py's EMAs (65.85 /
  74.59 / 79.16, RSI 5.8) are unadjusted for it. Needs a few clean post-spin closes before any
  trend read. **VYLR** (the spun entity, Nasdaq) is a new listing with no history: no
  structure to read, watch for a base.
- **NXL** (+76%, $486M on 3,649x volume): Benzinga: 10-year South American distribution deal,
  circuit-breaker halt up, market cap about $3.5M. Close 7.55 off a day high of 8.38 with
  shooting star + bearish engulfing in the last hour; EMA9 5.12 < EMA21 5.56 < EMA50 8.13 =
  3c FAIL; halt risk; no stop is placeable at a fillable price. Rejected on structure.
- **SDEV / VEEA / QSI / SES / BIRD / XRPN** (momentum scan risk 25-30%): stop distances are
  unusable for a numeric stop; NAMM/LONA/OM/CMCT spikes have no catalyst checked and no trend
  read; none worked up. Remain no-thesis.

**Older rejects, unchanged:** NU (3c FAIL, RSI 35), FICO (downtrend), NAUT, TTD, APLD, NVTS,
APP, SMMT, KOD, SHMD, JD, TOST, CELH, SEDG, F, SUIL, AKAM, MCHP, ON, AMBA, BYD, XPEV, NCPL,
VST, DASH, CRDO, SMCI, HUM, OPEN, NBIS, XOM, UPST, VKTX, SOFI, MSTR/CRCL, RIOT/CLSK/HOOD/MARA,
LRCX/NVDA/AVGO, IREN, RBRK/ZS/SMTC (no live thesis), MSFT (stopped 09-30, thesis dead).

## Macro calendar

- Earnings: INTC 10-22, STX 10-27, BE 10-27, MSFT/GOOGL 10-28, MPC/SPCX 11-03, CTVA 11-03,
  QCOM 11-04, FICO 11-04, NTRA/TXG 11-05, PLTR 11-02, MU 12-23, CRWD 12-01.
- Macro: 10Y 5.29%, 30Y at a 2002 high; ISM manufacturing slipped in September (Benzinga
  10-01); no Fed/CPI date confirmed from what is on screen.

## Next session (Friday 2026-10-02, PLANNING leg pre-market)

Set the day's loss budget; confirm consent.expires_at fresh; TXG close vs 88.74 decides the
exit; read gap scan for MPC/MU/STX; work MPC/MU on confirmation triggers only
(`trade_context.py --check` first); refill the book (1 of 3-6) only with 3c-passing names.
