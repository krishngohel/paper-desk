# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-10-08 evening (research leg after the daily review; PTC/ZS/DDOG/SNPS vetted; AAPL promoted to #1).
Mandate verified from live/alpaca/mandate.json 10-08: expires_at 2026-10-12T21:40:10Z (2 trading sessions left: Fri 10-09, Mon 10-12). Not halted.

**Regime (`ta.py --market`, 10-08 close):** SPY 773.93, +0.66% vs EMA21, RSI 55.9,
range/mixed. QQQ 747.58, +1.23%, RSI 58.7, range/mixed. Neutral posture, s6a first,
confirmation triggers only. 10Y 5.29% remains the tail risk. No Fed/CPI date confirmed.

## Standing orders

0 live orders, 0 armed triggers. Book flat (0 of 3-6). Nothing staged: s6a enters at the
NEXT OPEN, which only a market-hours leg can do (no market orders in research), and no
resting rung beats the `anticipatory_limit` record (6 closed, 33% wins, -$66/trade).

## Ranked - Friday 10-09 hunt

1. **AAPL - the one clean s6a candidate (`momentum_scan` at the 10-08 close).** Close 340.42
   (3 rising closes, +2.26% over 3d) > EMA9 335.45 > EMA21 332.76 > EMA50 ~326, uptrend
   structure, RSI 57.0 prior close (`neutral_45-60`), rs_vs_spy 20d +4.82pp
   (`outperforming_0-10pp`, NOT L9), ext 1.27 ATR, spread 0.01%, $12B traded, ATR 6.53 (1.96%).
   `trade_context --check AAPL 340.5`: no SIGNIFICANT bucket; goods: neutral_45-60 (10 of 21,
   suggestive), outperforming_0-10pp (5 of 11, +$627); context-only bads: market-up 3 of 18,
   gap.flat 4 of 20. Today it rejected 342.99 resistance three times (shooting star 341.39,
   bearish engulfing 19:00Z) on 0.50x volume - the entry bar is the open, not a breakout.
   **Plan (planning leg or open slot):** s6a market entry at the 10-09 open ONLY if the gap
   is within +-0.7% and the first 5m bars hold above 338.5 (not gapping down through the
   10-08 launch lows). Stop 332.78 (under the 10-07/10-08 launch lows; ledger and broker stop
   identical), no numeric target (exits on two consecutive lower closes) - OCO not possible,
   rest `sell QTY --stop 332.78 --gtc`. Probe B: risk $100 / ((340.5-332.78) x 1.7) = ~7 sh
   (~$2.4k notional); risk 2.24%, below L9/W4 danger zones. Archetype `momentum_s6a`,
   entry_mechanism `market`. Kill: two lower closes, or close below EMA21 332.76.
   Repeat-mistake check: ledger holds one filled AAPL trade (t-2026-08-26-001, +$7.96) and two aborted records, no stop-out. next_earnings 11-02.
2. **ABBV (10-04 vet, still valid).** Close 262.82 > EMA9 > EMA21 261.72 > EMA50 258.09, RSI 53.8
   (`neutral_45-60`), rs +1.46pp, spread 0.38%. Earlier legs waited on a VWAP reclaim. **Trigger
   (confirmation):** 5m hold above 265.0 on volume >1.2x and above VWAP; re-run `--check ABBV 265`
   first. Probe: stop 259.9, target 277.9, ~11 sh. Kill: close below EMA21 261.72. earnings 10-30.
3. **DELL (10-03 vet).** Close 562.52 > EMA9 548.56 > EMA21 535.98 > EMA50 491.31, RSI 58.0,
   rs +9.39pp (0.6pp under L9 - recheck), ATR 29 (5.2%). **Trigger:** 5m hold above 574 on volume
   >1.2x and above VWAP. Stop 545, target 646, ~2 sh (tiny). Kill: close below EMA21 535.98.
   earnings 11-27. Stale 3 sessions with no trigger - drops off if still untouched at the 10-12 review.
4. **EWY (10-04 vet, Korea ETF).** Close 191.88 > EMA9 186.35 > EMA21 184.15 > EMA50 177.83, RSI
   57.2, rs +6.73pp, spread 0.39%. **Trigger:** 5m hold above 194.0 on volume >1.2x and above
   VWAP. Stop 187.8, target 209.4, ~9 sh. Kill: close below EMA21 184.15. ETF, no earnings;
   gap-risk basket (Korea close/FX). Stale 3 sessions; same drop rule as DELL.
5. **MU - post-print consolidation (10-08 scan: -4.79%, liquid lens).** Was 1074.89 vs EMA21
   1029.61 on 10-02; today's -4.8% needs a fresh `ta.py MU` before any trigger. **Trigger
   (if still above EMA21):** hold above 1108.72 on volume >1.2x, or a 1032 support hold. Kill:
   close below EMA21. earnings 12-23.
6. **MPC / VLO (refiners, one of the two only).** MPC close 422.33 > EMA21 395.93 > EMA50 364.29,
   RSI 69.0 (W4), vol 0.72x, trigger: 5m hold above 431.08 on volume >1.2x, stop under 402.38,
   B/C probe, earnings 11-03. VLO 406.30, RSI 65.6, trigger: hold above 419.04, earnings 10-22.
   Both stale and W4 RSI 60+; ranked last.

## Watch only / rejects

- **PTC (new 10-08 vet, big_leaders lens) - passes the literal s6a scan, REJECTED for entry.**
  Close 193.73 > EMA9 171.77 > EMA21 156.86 > EMA50 147.96, but RSI 80.7, 1m +38.5% (L9
  leader), pos 100% of the 20d range, spread 1.19% TRADABLE_TIGHT_SIZE, and the s6a launch-low
  stop (192.94) sits 0.41% away - inside the noise of a 3.6% ATR name; today's candles are
  dojis/inside bars AT 196.05 on a 0.07% day. The stop-in-the-noise breaks 4b's sizing math.
  Watch for a pullback to EMA9 ~171.8 with a multi-touch hold. next_earnings 11-11.
- **ZS (new 10-08 vet) - passes 3c and s6a (216.81 > EMA9 206.81 > EMA21 199.14, stop 209.96,
  3.16% risk), BLOCKED by L9 + W4.** rel strength 20d +26.63pp (`leader_10pp+` SIGNIFICANT, 1 of 18),
  RSI 64.3 prior close (`strong_60-70`, 1 of 12), ext 2.01 ATR, day closed in dojis at 216.97.
  Only a pullback to EMA9 ~207 / 209.96 with a dated catalyst or multi-touch hold earns the
  written L9 exception. next_earnings 11-24.
- **DDOG (new 10-08 vet) - passes 3c (273.80 > EMA9 270.73 > EMA21 259.48 > EMA50 252.78) but
  fails the stalk:** RSI 64.6 (W4), 1m +32.3% (L9 leader), bearish engulfing 10-07 and shooting
  star 10-05 both AT resistance 280.7, vol 0.99x. Needs a clean close above 281.25 on volume
  >1.2x with the L9 exception, else a pullback to EMA9. next_earnings 11-05.
- **SNPS (new 10-08 vet) - passes 3c, extended.** Close 497.75 > EMA9 475.9 > EMA21 446.78 > EMA50
  423.58, RSI 72.1 (prior 74.7, W4), 1m +25.4% (L9 leader), shooting star at 511.95, spread
  0.95%, no resistance overhead. Watch only: pullback to EMA9 ~476 with a hold. earnings 12-09.
- **PCRX (+44.4%, rel vol 50x, $1.05B traded, 10-08 scan):** a one-day gap with no checked base
  (earlier legs passed as a chase). Only a pullback holding VWAP with a news check; no
  `ta.py` verdict on file tonight beyond the scan row.
- **Explore lens (smallcap) 10-08:** RDHL, CIIT, BYRN (+16.8%, 1m +27.8%, a 25.9% s6a risk
  stop), GRDX, CABO, PARA, CDTG, CLGN, GFUZ, RZAI, IPSC, LXEH, CRE, CPHI, INV: sub-$10
  spikes, most with 1m negative and no placeable stop - noise tonight. FLYE (+82.7% on rel vol
  7,278x), SXTC (-87.9%), DKI, MI: spike-and-collapse, no thesis.
- **STX / WDC:** below EMA21 after the 10-02 Toshiba HDD scare (STX 848.99 < EMA9, RSI 46) -
  3c FAIL, falling knife until a higher low forms.
- **3c FAILS / EMA21 < EMA50 (pass until they flip):** TXN, KLAC, RKLB (closest), CSCO (closest),
  GOOG, AMZN, LLY, NOW, ORCL, AVGO, GE, SCKT.
- **L9-blocked leaders (need a pullback + written exception):** META (RSI 61.1, rs +19.7pp,
  earnings 10-28), LITE (1085, RSI 66.5), HPE (69.33 on 10-02; 1m +35.8% still, trigger only a
  multi-touch hold at EMA9 ~64 / 60.68), TER (earnings 10-21), ENTG (spread 1.83%), ADI, INTC,
  NTRA, BE, ARM, TWLO, ILMN, MSTR, MRVL, AMD, NVDA.
- **UNTRADABLE:** REBN (spread 2.80%), PS (5.93%).
- **Older rejects, unchanged:** NU, FICO, NAUT, TTD, APLD, NVTS, APP, SMMT, KOD, SHMD, JD, TOST,
  CELH, SEDG, F, SUIL, AKAM, MCHP, ON, AMBA, BYD, XPEV, NCPL, VST, DASH, CRDO, SMCI, HUM, OPEN,
  NBIS, XOM, UPST, VKTX, SOFI, CRCL, RIOT/CLSK/HOOD/MARA, LRCX, IREN, RBRK, SMTC, MSFT, NTAP,
  SYNA, OKTA, CTVA (spin-off distortion), NXL (halt risk).

## Macro calendar

- Earnings: TER 10-21, INTC/VLO 10-22, STX/BE 10-27, MSFT/GOOGL/NOW/META 10-28, ABBV 10-30,
  ENTG 10-29, AAPL 11-02, PLTR 11-02, MPC/SPCX/CTVA 11-03, QCOM/FICO 11-04, DDOG/NTRA/TXG 11-05,
  PTC 11-11, ZS 11-24, DELL 11-27, CRWD 12-01, HPE 12-03, SNPS 12-09, MU 12-23.
- Macro: 10Y 5.29%; no Fed/CPI date confirmed from on-screen data. **Mandate expires
  2026-10-12 21:40Z - renewal (ops/commit_paper_mandate.py) is a human action; a lapse stops
  all order actions.**

## Next session (Friday 2026-10-09, PLANNING leg pre-market)

Set the 10-09 loss budget; re-verify `consent.expires_at`; read the gap scan; check AAPL's
pre-market gap against the s6a plan above (#1) and, if it qualifies at the open, enter as a
probe with the broker stop resting the same cycle; work ABBV/DELL/EWY/MU on confirmation
triggers only (`trade_context.py --check` first). Book is 0 of 3-6.
