# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-10-04 (Sunday research leg; TXN rejected, ADI to Watch; ranks unchanged).
Mandate verified from mandate.json 10-04: expires_at 2026-10-12T21:40Z. Not halted.

**Regime (`ta.py --market`, 10-02 close):** SPY 769.64, +0.54% vs EMA21, RSI 54.2,
range/mixed. QQQ 749.58, +2.53% vs EMA21, RSI 64.9, range/mixed, record highs on a weak
payrolls print (Benzinga: pared Fed-tightening bets). Neutral posture, s6a first,
confirmation triggers only. 10Y 5.29% remains the tail risk.

## Standing orders

0 live orders, 0 armed triggers. Nothing staged: Monday opens after a weekend gap and no
name has a numeric above-market trigger worth arming over the weekend; no rung beats the
`anticipatory_limit` record (6 closed, 33% wins, -$66/trade).

## Book (1 position, target 3-6)

- **TXG** 15 sh @ 75.64, 10-02 close 93.42 (> 10-01 close 88.74, so lower-close streak = 0),
  +$267 / +23%. Broker GTC stop 64.73 resting (order 975776c7). s6a: sell only on two
  CONSECUTIVE lower closes (cancel the stop first). RSI 77, resistance 95.16 (dojis there
  all last hour), EMA9 86.66. next_earnings 2026-11-05.

## Ranked - Monday 10-05 hunt

1. **Manage TXG first** (Monday close vs 93.42).
2. **Re-run `momentum_scan.py` at the Monday close for Tuesday entries** (never intraday).
   Friday-final-close list: HPE 9.08% risk, P 6.16%, AMD 5.77%, MRVL 6.86%, NVDA 3.81%,
   SOXL 13.63% - all leader-bucket / W4 RSI 60-70 names; none has a probe stop under ~3%.
3. **AAPL (new 10-03 vet, liquid lens) - passes 3c, in the good buckets.** Close 333.69 >
   EMA21 331.16 > EMA50 325.19 (below EMA9 333.76 by 0.07), RSI 54.8 (`neutral_45-60`),
   rel strength +2.13pp (`outperforming_0-10pp`, not L9), spread 0.10%, $11.4B traded, vol
   0.79x, ATR 7.04 (2.1%). Resistance 334.99 (morning star + dojis there last hour), then
   336.22 (09-30 shooting star), 342.99; support 319.35. **Trigger (confirmation):** Monday
   5m hold above 335.2 with volume >1.2x and above VWAP; `--check AAPL 335.2` printed no
   significant loss bucket (market-up bucket 3 of 18 is context). Probe B/C: stop 328.2
   (1 ATR; 325.81 prior-day low is the structural line), target 352.8 (2.5 ATR), risk $100 /
   (7.0 x 1.7) = ~8 sh. Kill: close below EMA21 331.16. next_earnings 10-29.
3b. **DELL (new 10-03 vet, turnover lens) - passes literal 3c, good buckets.** Close 562.52 >
   EMA9 548.56 > EMA21 535.98 > EMA50 491.31, RSI 58.0 (`neutral_45-60`), rel strength +9.39pp
   (`outperforming_0-10pp`, 0.6pp under the L9 line - recheck Monday), ext 1.26 ATR, spread
   0.09%, $3.1B traded, vol 0.59x (thin; continuation thesis, so C/B probe only), ATR 29.01
   (5.2%). Structure tag range/mixed; inside bar 09-29, doji at support 530.45 10-01.
   **Trigger (confirmation):** Monday 5m hold above 574 (resistance 573.8) on volume >1.2x and
   above VWAP; `--check DELL 574` printed no significant bucket (suggestive: RSI 45-60 good;
   market-up context bad). Stop 545 (1 ATR), target 646 (2.5 ATR), risk $100 / (29 x 1.7) = ~2
   sh; tiny, say so. Kill: close below EMA21 535.98. next_earnings 11-27.
4. **HPE (new 10-02 vet) - passes literal 3c, L9-blocked today.** Close 69.33 > EMA9 63.79 >
   EMA21 60.78 > EMA50 56.12, RSI 69.3 (prior-close 62.7 = W4 strong_60-70), +7.8% on 1.13x
   volume, gap +6.9%, spread 0.16%, $2.0B traded. Catalysts: Daiwa upgrade to Outperform PT
   75 (10-02), Citi PT 92 (10-01). 1m +33% = `leader_10pp+`. Structure tag range/mixed. Last
   hour: marubozu up then shooting star 69.67 and two selling marubozus. **Trigger:** none
   today; only a pullback that holds EMA9 ~63.8 / support 60.68 on a multi-touch defense (L8)
   with `--check` fresh. Kill: close below 60.68. next_earnings 12-03.
4. **TER (new 10-02 vet) - passes literal 3c, L9-blocked.** Close 449.04 > EMA9 406.39 >
   EMA21 388.64 > EMA50 377.45, RSI 69.8, +8.0% on 1.38x volume, gap +6.25%, spread 0.45%,
   $1.5B. 1m +34% leader bucket; ATR 20.39 puts a 1-ATR stop 4.5% away. Day closed in dojis
   (compression). Watch only: needs a base or a pullback toward the 419.37 prior-day high
   with hold. next_earnings 10-21 (inside two weeks; no entry within 2 days of it).
5. **ENTG (new 10-02 vet) - structure uptrend, but spread 1.83% TRADABLE_TIGHT_SIZE.**
   Close 166.47 > EMA9 154.14 > EMA21 147.86 > EMA50 143.51, RSI 69.0, +5.0%, 1m +28%
   leader bucket, bearish engulfing 09-30 then reclaimed. Target would have to clear a 1.8%
   round trip. Watch only. next_earnings 10-29.
6. **MPC - 3c literal pass, thin.** Close 422.33 > EMA9 404.53 > EMA21 395.93 > EMA50
   364.29, RSI 69.0 (prior 68.2), vol 0.72x, spread 0.66%, rs -0.25pp today, resistance
   431.08, bearish engulfing in the last hour. **Trigger:** 5m break and hold above 431.08
   with volume >1.2x. Stop under 402.38 (EMA9 region) or 388.16, re-anchor to the fill,
   B/C probe. Kill: close below EMA21 395.93. next_earnings 11-03.
7. **VLO (new 10-02 vet, social trending) - same refiner group as MPC.** Close 406.30 >
   EMA9 394.74 > EMA21 385.64 > EMA50 355.07, RSI 65.6, vol 0.65x, hammer defending 389.61
   today, resistance 419.04, spread 0.33%. Pairs with MPC: only one of the two. **Trigger:**
   hold above 419.04 on volume >1.2x. next_earnings 10-22.
8. **MU - post-print consolidation.** Close 1074.89 (-2.0%) > EMA9 1063.74 > EMA21 1029.61 >
   EMA50 975.47, RSI 59.0, selling marubozu today, two shooting stars at 1072.5 late.
   **Trigger:** hold above 1108.72 with volume >1.2x; or a support-1032 hold. Stop under
   1032. Kill: close below 1029.61 (EMA21). next_earnings 12-23.

## Watch only / rejects

- **STX (-10.5%) / WDC (-10.2%):** sold on Toshiba's plan to double AI data-center HDD
  supply (Benzinga 10-02) on 3.6x / 3.3x volume. STX now 848.99 < EMA9 897.40, RSI 46.2,
  gap -14%, 20d range 44%, close below EMA21 879.61 - 3c FAIL.
  Falling-knife until a higher low forms; WDC likewise. Rotate off the ranked list.
- **INTC / NTRA / STX-adjacent leaders (L9 blocked):** INTC 119.33, NTRA 410.35 (RSI 77
  prior), BE, ARM, TWLO, ILMN, MSTR, MRVL, AMD, NVDA - all `big_leaders` with 1m +29-38%.
- **NOW (new 10-02 vet, social trending):** close 134.38 vs EMA21 134.99 = below EMA21,
  3c FAIL, RSI 50.2, rs -3.1pp. Pass.
- **META (new 10-03 vet) - passes 3c, L9-blocked.** Close 728.08 > EMA9 725.05 > EMA21 695.07
  > EMA50 650.31, RSI 61.1 (W4 strong_60-70), rel strength +19.7pp = `leader_10pp+`
  SIGNIFICANT bucket, 4 inside bars then hammer 727.5, vol 0.54x, spread 0.03%, resistance
  779.82. Watch only; needs a dated catalyst or a pullback to EMA9/713.19 with a multi-touch
  hold. next_earnings 10-28.
- **LITE (new 10-03 vet) - passes literal 3c, blocked.** Close 1085.42 > EMA9 987.98 > EMA21
  947.35 > EMA50 885.71, RSI 66.5 (W4 strong_60-70), 1m +25.1% (L9 leader), 20d range 100%
  with no resistance overhead, ATR 66.26 (6.1%), spread 0.12%, vol 0.98x. Extended; needs a
  pullback to EMA9 ~988 with a multi-touch hold. next_earnings 11-05.
- **TXN (new 10-04 vet) - 3c FAIL.** Close 293.80 > EMA9 279.64 > EMA21 273.50 but EMA21 < EMA50
  275.44, RSI 69.8 (W4), spread 1.42% TRADABLE_TIGHT_SIZE, resistance 297.58, next_earnings
  10-21. Pass until EMA21 > EMA50.
- **ADI (new 10-04 vet) - passes 3c, extended.** Close 417.15 > EMA9 396.81 > EMA21 385.65 >
  EMA50 380.77, RSI 72.0 (W4), shooting star at 421.7 on 10-02, 20d range 100%, vol 0.80x,
  spread 0.98%, ATR 11.26. Watch only: needs a pullback hold at EMA9 ~397 / support 377.40.
  next_earnings 11-24.
- **PS (new 10-03 vet) - UNTRADABLE.** Spread 5.93% (bid 50.88 / ask 53.99), $10.8M traded,
  vol 0.27x. Pass.
- **CSCO (new 10-03 vet, turnover lens) - 3c FAIL, closest to flipping.** Close 112.20 > EMA21
  109.09 but EMA21 < EMA50 111.56, EMA9 108.71, RSI 56.6, +3.2% on 0.96x volume, 20d range
  100%, resistance 112.22/112.95, spread 0.09%. Becomes a candidate only once EMA21 > EMA50
  (a few more closes above ~112). next_earnings 11-12.
- **ORCL / AVGO / GE (new 10-03 vets) - 3c FAIL.** ORCL 142.30 < EMA21 143.03 (RSI 48.2,
  doji at 143.67); AVGO 355.14 < EMA21 356.20 < EMA50 371.12 (RSI 47.3); GE 309.56 in a
  downtrend (RSI 34.6, below all EMAs, 20d range 8%). Earnings ORCL 12-10, AVGO 12-09, GE 10-20.
- **Small-cap explore lens (smallcap):** GOW (+29.9%, 1m -59.5%), NIVF (0.13), ICU, NNBR,
  SSM, CABO, SNES, AUID, NEOV: all 1m-downtrend or sub-$5 spikes with no checked catalyst
  or placeable stop. AMOD +198% (rel vol 108x, cap $10M), SDEV +104% (1m +780%), XRPN +68%
  (stop 55% away): spike-and-halt risk, no structure, no thesis. FLUX/ZNB/CYCU/QTEX: rel
  volume 37-919x on sub-$4 names - noise.
- **Older rejects, unchanged:** NU, FICO, NAUT, TTD, APLD, NVTS, APP, SMMT, KOD, SHMD, JD,
  TOST, CELH, SEDG, F, SUIL, AKAM, MCHP, ON, AMBA, BYD, XPEV, NCPL, VST, DASH, CRDO, SMCI,
  HUM, OPEN, NBIS, XOM, UPST, VKTX, SOFI, CRCL, RIOT/CLSK/HOOD/MARA, LRCX, IREN, RBRK/ZS/SMTC,
  MSFT, NTAP, SYNA, OKTA, LRCX, CTVA (spin-off distortion), NXL (halt risk).

## Macro calendar

- Earnings: TER 10-21, INTC 10-22, VLO 10-22, STX 10-27, BE 10-27, MSFT/GOOGL 10-28, NOW
  10-28, ENTG 10-29, PLTR 11-02, MPC/SPCX/CTVA 11-03, QCOM/FICO 11-04, NTRA/TXG 11-05, CRWD
  12-01, HPE 12-03, MU 12-23.
- Macro: 10Y 5.29%; September payrolls weak on 10-02 (pared Fed-hike bets, Nasdaq 100 at
  record); no Fed/CPI date confirmed from what is on screen. Mandate expires 2026-10-12.

## Next session (Monday 2026-10-05, PLANNING leg pre-market)

Set the day's loss budget; confirm consent.expires_at fresh; read the gap scan; re-check
TXG vs its 93.42 close and the resting stop 975776c7; work MPC/MU on confirmation
triggers only (`trade_context.py --check` first); refill the book (1 of 3-6) only with
3c-passing names and a written L9 exception where the bucket is `leader_10pp+`.
