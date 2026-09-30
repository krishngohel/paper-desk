# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-30 evening (research leg after Wednesday's close). Mandate valid
(expires 2026-10-12 per prior entries; re-read fresh). Not halted.

**Regime (`ta.py --market`, 09-30 close):** SPY 762.63, -0.35% vs EMA21, RSI 47.8,
range/mixed. QQQ 739.77, +1.61% vs EMA21, RSI 60.2, range/mixed. 10Y 5.29% rate shock is
the tail risk. Neutral posture, s6a only.

## Standing orders

0 live orders, 0 armed triggers. Nothing staged: no name reached a numeric trigger worth
arming above market, and no rung beats the `anticipatory_limit` record.

## Book (1 position, target 3-6)

- **TXG** 15 sh @ 75.64, 09-30 close 90.345 (up vs 90.04, streak 0), +$230 / +20%.
  s6a-governed (exit on TWO consecutive lower closes), stop 64.73, no target. RSI 77.
  next_earnings 2026-11-05.
- Closed 09-30: CRWD +$99.12 (right), MSFT -$72.94 stopped out (wrong). Both scored.

## Ranked - Thursday 10-01 hunt

1. **Manage TXG first** (close vs 90.345; lower = streak 1).
2. **MU - post-print, re-run `trade_context.py --check` at the open.** Reported 09-30 after
   close: Benzinga "Q4 double beat, sees even stronger year ahead", supply "much tighter in
   2027-28". Pre-print close 1065.11 > EMA9 1051.85 > EMA21 1018 > EMA50 969 (passes 3c),
   RSI 59.8, rs -0.63pp, spread 0.04%, resistance 1108.72, support 1032. Gap reaction unseen.
   **Trigger:** confirmation only, after the gap settles (hold above the opening-range high,
   volume >1.2x); do not chase a gap through 1108.72. Stop under 1032, re-anchor to the fill.
   Probe. Kill: gap-and-fade below 1032. next_earnings passed.
3. **INTC - passes 3c, blocked by L9.** Close 120.23 > EMA9 117.27 > EMA21 110.71 > EMA50
   104.41, RSI 61.8, 20d rs +29.89pp = `leader_10pp+` (SIGNIFICANT, 1 of 17), ATR 6.13 (5%),
   daily morning star, spread 0.12%, $11.2B. next_earnings 10-22. Watch only; an entry needs
   a written L9 exception (none today: +256% in 12 months, no base reset).
4. **STX - WAIT.** Close 913.45 > EMA9 895 > EMA21 872 > EMA50 860, RSI 57.9, vol 0.68x.
   **Trigger:** daily close > 925.44, or 5m break of 923.10 with volume >1.2x. Stop under
   870.38, target 936.49 then ~975. Kill: close below EMA21 872. next_earnings 10-27.
   **MSFT:** stopped out 09-30, thesis dead; needs a fresh thesis (close above 513.73).
5. **GOOGL - fails 3c today.** Close 344.08 < EMA50 345.76, EMA9 343.63 ~ EMA21 343.64, RSI
   49.8, rs +2.64pp, vol 1.41x, 5m hammers/doji AT RESISTANCE 349.14. Qualifies only after
   a close above 345.76 with EMA21 > EMA50. next_earnings 10-28.
6. **QCOM / BE / P / TWLO / OKTA / MRNA / ALAB / ARM - L9 blocked (big_leaders lens).**
   Watch only. AMAT / KLAC fail 3c (EMA21 < EMA50).

## Watch only / rejects

**09-30 evening vets:** **NU** (StockTwits trending): close 12.66 < EMA9 13.19 < EMA21 13.76
< EMA50 14.03, RSI 35.3, 12.5% of 20d range, +8.4% bounce day - 3c FAIL. **GOOGL, INTC**
above. CBRS/APP/SOFI trending, not re-vetted (APP/SOFI carried 3c fails). Explore smallcap
names FNGR 0.18, RETO 0.11, ZBAO 0.10, LIQT 0.53 (sub-$1 shells) and LGHL ($111M on 73x
volume, -44% 1m) given no thesis: no workup done, no trend read.

**09-29 vets, unchanged:**
- **FICO** (-27.2%): close 617.87 < EMA9 < EMA21 < EMA50, RSI 16.3, downtrend. 3c FAIL;
  revisit only after a multi-day base above 595.19.
- **XRPN**: spread 3.77% UNTRADABLE (09-29), RSI 98.5. **NAUT**: range/mixed, 3c FAIL,
  30% stop distance. **TTD**: downtrend, RSI 29.2, 3c FAIL.
- Earlier rejects carried: APLD, NVTS, APP, SMMT, KOD, SHMD, JD, TOST, CELH, SEDG, F, SUIL,
  AKAM, MCHP, ON, AMBA, BYD, XPEV, NCPL, VST, DASH, CRDO, SMCI, HUM, OPEN, NBIS (3c FAIL or
  UNTRADABLE per prior vets), XOM, UPST, VKTX, SOFI, MSTR/CRCL, RIOT/CLSK/HOOD/MARA,
  SNDK/AVGO/LRCX/NVDA, IREN, RBRK/ZS/SMTC (no live thesis).
- **Momentum scan 09-30:** SDEV/SVRN/PACB risk 55/30/30% (unusable stops), PMVP risk 17.6%
  on $2.4M volume, P risk 4.19% (W4/L9), RBRK risk 3.42% (L9).

## Macro calendar

- Earnings: MU reported 09-30 (beat), INTC 10-22, STX 10-27, BE 10-27, MSFT/GOOGL 10-28,
  QCOM 11-04, FICO 11-04, TXG 11-05, PLTR 11-02, CRWD 12-01.
- Macro: 10Y 5.29%, 30Y at a 2002 high; no Fed/CPI date flagged from what is on screen.

## Next session (Thursday 2026-10-01, PLANNING leg pre-market)

Set the day's loss budget; confirm consent.expires_at fresh; TXG close-pattern check; read
MU's after-hours reaction and run `trade_context.py --check MU`; work MU/STX on
confirmation triggers only; refill the book (1 of 3-6) - s6a candidates are thin (only
P/RBRK at sane risk, both L9-blocked).
