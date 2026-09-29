# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-29 evening (research leg after Tuesday's close). Mandate live
(`mandate.json` expires_at 2026-10-12T21:40:10Z, read fresh). Not halted.

**Regime (`ta.py --market`, 09-29 close):** SPY 764.2, -0.18% vs EMA21, RSI 49.1,
range/mixed. QQQ 737.93, +1.52% vs EMA21, RSI 59.3, range/mixed. 10Y yield 5.29% (2007
high), 30Y at a 2002 high (Benzinga 09-29): rate shock is the live tail risk. Neutral
posture, s6a only.

## Standing orders

0 live buy orders, 0 armed triggers (all six anticipatory rungs cancelled 09-29 under the
`by_entry_mechanism` record). Only resting order: CRWD sell 264.13. Nothing staged
tonight: no name below reached a numeric trigger worth arming above market.

## Book (2 positions, target 3-6)

- **CRWD** 3 sh @ 231.22, Tue close 262.74 (+$94 / +13.6%). Target 264.13 resting
  (`9bfc5894`, +0.5%), stop 219.15, time_stop 2026-10-03. Resistance 263.87; 5m hammer/
  doji/marubozu-sell right under it. next_earnings 2026-12-01.
- **TXG** 15 sh @ 75.64, Tue close 90.04 (+$216 / +19.0%). s6a-governed (exit on TWO
  consecutive lower closes), stop 64.73, no target. Verified from MCP daily bars: closes
  09-25 85.71, 09-28 88.50, 09-29 90.04 - up day, streak 0. RSI 77.1, ATR 5.01.
  next_earnings 2026-11-05.

## Ranked - Wednesday hunt

1. **Manage the book first** (CRWD target; TXG close-pattern; watcher silent-miss -
   cross-check stops vs 5m bars).
2. **MSFT - WAIT, no order.** Close 508.96 > EMA9 504.32 > EMA21 498.65 > EMA50 472.67,
   structure "uptrend" (ta.py, passes 3c). RSI 58.4 (neutral_45-60), rs_vs_spy +0.05pp
   (L9 clean), vol 1.02x, spread 0.04%, $11.1B. Third session pinned under resistance
   509.95 (daily doji AT RESISTANCE 09-23 and 09-29, inside bar 09-28; 5m morning star
   there). **Trigger:** confirmation only - daily close above 513.73 (prior-day high
   513.33/next level) or 5m reclaim of 511.65 (day high) on volume >1.2x; then re-anchor
   stop/target to the fill. Planned: probe, ~$100 risk, stop under 498 (EMA21) or 493.81,
   target 530. Grade B/C. Kill: close below EMA21 498.65. next_earnings 2026-10-28.
3. **STX - WAIT, no order.** Close 913.45 > EMA9 895.02 > EMA21 871.84 > EMA50 859.51,
   uptrend, RSI 57.9, rs -0.72pp, vol 0.68x (thin), spread 0.07%, ATR 49.8. Day of 5m
   dojis AT RESISTANCE 921.78. **Trigger:** daily close > 925.44, or 5m break of 923.10
   (day high) with volume >1.2x. Planned: probe, stop under 870.38 (Mon low), target
   936.49 then ~975. Kill: close below EMA21 872. next_earnings 2026-10-27.
4. **MU - earnings 09-30: no entry before the print clears.** Was L9 (rs +15.7pp)
   and RSI 60-70 blocked on 09-27; re-run `--check` at the 10-01 open against the
   post-print price.
5. **QCOM / BE / P / TWLO / OKTA - L9 blocked (leader_10pp+, 0/16).** Watch only, enter
   only with a written L9 exception. BE +13% on 09-29 (Benzinga) - still a leader.
6. **AMAT / KLAC - fail 3c (EMA21 < EMA50).** Qualify only after EMA21 crosses EMA50
   (AMAT ~495.86). JNJ: revisit on reclaim of 271.55 with volume.

## Watch only / rejects

**09-29 evening vets (screen.py smallcap explore + StockTwits trending + scan):**
- **FICO** (-27.2%, worst day since 1989 on the Fannie/Freddie single pricing grid that
  lets VantageScore compete; Benzinga): close 617.87 < EMA9 843.9 < EMA21 933.1 < EMA50
  1049.9, RSI 16.3, structure downtrend, 10.9x volume, spread 0.08%. 3c FAIL. A crash into
  a structural franchise threat, not a base; revisit only after a multi-day base above
  the 595.19 low. TRU/EFX are the read-through names (not vetted).
- **XRPN** (+25%, 52M traded, 15.8x volume): spread 3.77% UNTRADABLE (bid 13.00 / ask
  13.50), RSI 98.5, range/mixed, shooting star rejecting 17.00 - reject on its own numbers.
- **NAUT** (+29.7%, $30.8M, spread 0.70% TRADABLE): close 1.36 vs EMA21 1.02 / EMA50 1.13,
  structure range/mixed -> 3c FAIL by tag; one-day gap spike, stop distance vs ATR 0.12
  is wide (support 0.95, 30% away). Pass.
- **TTD** (StockTwits #2, $267M, spread 0.17%): close 12.05 < EMA9 12.92 < EMA21 13.56 <
  EMA50 15.08, RSI 29.2, downtrend, 0% of 20d range. 3c FAIL.
- Other explore-lens names (SLXN 0.32, SOAR 0.39, QSI 0.96, SLE, WYY, MF, AIFU, LONA,
  EEIQ, OIO, ONEN, PLUT): $0.0-9M traded except SLXN $81M/SOAR $76M (sub-$0.40 stocks,
  wide-tick risk); none given a thesis this session.
- Earlier rejects carried, unchanged reasons: APLD, NVTS, APP, SMMT, KOD, SHMD, JD, TOST,
  CELH, SEDG, F, SUIL, AKAM, MCHP, ON, AMBA, BYD, XPEV, NCPL, VST, DASH, CRDO, SMCI, HUM,
  OPEN, NBIS (all 3c FAIL or UNTRADABLE per prior vets), XOM, UPST, VKTX, SOFI, MSTR/CRCL,
  RIOT/CLSK/HOOD/MARA, SNDK/AVGO/LRCX/NVDA/INTC, IREN. Dropped 09-29: RBRK/ZS/SMTC (rungs
  cancelled, no live thesis).

## Macro calendar

- Earnings: MU 09-30 (Wed, per earlier notes; timing unverified - Benzinga said 09-30), then CRWD 12-01, PLTR
  11-02, TXG 11-05, MSFT 10-28, STX 10-27, BE 10-27, QCOM 11-04, FICO 11-04.
- Macro: 10Y 5.29%, 30Y at 2002 high; no Fed/CPI date flagged from what is on screen.

## Next session (Wednesday 2026-09-30, PLANNING leg pre-market)

Set the day's loss budget; confirm consent.expires_at fresh; cross-check CRWD/TXG stops
vs 5m bars; TXG s6a: streak 0 as of 09-29 close (check 09-30 close vs 90.04); MU reports
09-30, no MU entry until the print clears; work MSFT/STX only on their confirmation
triggers.
