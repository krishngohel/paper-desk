# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-10-13 Tue post-close (daily review): #1 rewritten. The MA/V Monday plan never ran (no relay
legs on 10-12) and both closed off the s6a scan on 10-13. MSFT is the new #1 s6a candidate from the 10-13
close scan. DELL/EWY dropped as stale. Everything below #1 is unchanged from the 10-11 research.
10-13 evening research: ranking unchanged (SHOP/BMBL/JPM/AMAT vetted, all pass-on-entry; see rejects).
**10-15 post-close review: EVERY level below is two sessions stale.** No session ran on 10-14 or 10-15
(account usage limit; see journal). The MSFT 10-14-open plan in #1 is expired, not live. On 10-15 QQQ
closed in downtrend structure (728.0, -1.41% vs EMA21) and SPY range/mixed (771.79, +0.09%). The 10-16
planning leg must re-run `ta.py` on every name before using any trigger here. 10-15 close s6a scan:
A 175.55 (stop 171.67, 2.21%, $298M; unvetted - needs `ta.py`, `--check`, earnings date) is the only new
tight-stop name; MRNA 236.50 / MTD 1639.04 are L9 leaders; ABLV/BSP/MRNX carry 12-20% stop risk. MSFT dropped off.
Mandate: renewed by the human 10-13 midday; expires_at 2026-10-27T17:45:52Z (re-verify each planning leg).

**Regime (`ta.py --market`, 10-13 close):** SPY 778.01, +0.89% vs EMA21, RSI 59.3, range/mixed.
QQQ 743.57, +0.42%, RSI 54.5, range/mixed. Neutral posture, s6a first, confirmation entries only.
10Y ~5.26% is the tail risk. No Fed/CPI date confirmed from on-screen data.

## Standing orders

0 live orders, 0 armed triggers. Book flat (0 of 3-6). Nothing staged: s6a enters at the NEXT OPEN,
which only a market-hours leg can do (no market orders in research), and no resting rung beats the
`anticipatory_limit` record (6 closed, 33% wins, -$66/trade).

## Ranked - Wednesday 10-14 hunt

1. **MSFT - s6a candidate from the 10-13 close scan (3 rising closes, 3d +3.99%). PLAN EXPIRED (10-14 open
   never traded); re-qualify from a fresh close scan before reuse.** Close 543.45 > EMA9
   529.73 > EMA21 517.56 > EMA50 496.02 (passes 3c), structure uptrend (HH+HL), ATR 11.52 (2.13%), spread
   0.08%, $12.97B traded, vol 1.07x, rs 20d +4.81pp (`outperforming_0-10pp`, NOT L9), ext 2.38 ATR,
   100% of 20d range, no resistance above. **Cautions:** RSI 71.2 at the 10-13 close (prior 70.3), so
   a 10-14 entry sits in `overbought_70+` (0 of 3) / W4 territory (RSI 60+ is 1 of 15, p 0.012, not
   significant). The 10-13 daily candle was a shooting star rejecting 551.15, and the close was below
   VWAP 546.15. `--check MSFT 543.45` (10-13 PM): no SIGNIFICANT bucket; good: outperforming_0-10pp; context-only
   bads: market-up 3 of 18, strong_60-70, gap flat. Prior MSFT trade lost $72.94; look it up and name
   what is different before entry (playbook §11). earnings 10-28.
   - **Plan (planning leg/open slot):** an s6a market entry at the 10-14 open ONLY if the open is within
     +-0.7% of 543.45 AND the first 5m bars hold above 542.5 (10-13 low 542.55). An open above 551.15
     (the shooting-star high) = chasing, so pass. Re-run `--check` at the real open. Probe C (W4 +
     shooting star): s6a launch-low stop 535.70 (the 10-12 low, ~0.67 ATR below, room is thin), risk
     $100 / ((543.5-535.7) x 1.7 = 13.3) = 7.5, so 5 sh (~$2.7k, trimmed for the overbought bucket). No
     numeric target; rest `sell 5 --stop 535.70 --gtc`. Archetype `momentum_s6a`, mechanism `market`.
     Kill: two consecutive lower closes, or a close below EMA21 517.56. Exit/cut by 10-26 (earnings 10-28).
   - **MA / V (the 10-09 plan):** dead. The 10-12 open was never traded (relay outage). On 10-13 they
     sat ~2 ATR extended (MA 602, V 392 intraday), and neither is on the 10-13 close scan. Pullback-hold
     stalks only: MA 588.1-580.9, V 378.5, with vol >1.2x.
   - **MTD (10-13 scan):** close 1598.03, s6a stop 1549.78 (3.0%), but rs 20d +19.3pp is `leader_10pp+`
     (SIGNIFICANT, 1 of 18), RSI 68.1 (W4), ext 2.55 ATR. Pass unless L9's written exception has a dated
     catalyst. The rest of the 10-13 scan (TCRT/ELOG/JYD/PDSB/YHC with 13-75% stop risk, HLP/PUL under
     $1M traded, P at RSI 80, CJUN a buffer ETF) is spike or illiquid. No thesis.
2. **MRNA (new 10-09 vet, big_leaders lens) - catalyst-driven, BLOCKED by L9 + W4 + extension.**
   +14.1% to 225.00 (52-wk high; marubozu) on the NIH personalised-cancer-vaccine initiative (Benzinga/NYT
   10-09) plus Nasdaq-100 inclusion - a dated catalyst, but a one-day pop. close 225 > EMA9 198.9 >
   EMA21 182.5 > EMA50 139.3, RSI 72.1 live (63.8 prior close = `strong_60-70`, 1 of 12), rs 20d
   +42pp (`leader_10pp+` SIGNIFICANT, 1 of 18), ext 3.19 ATR, ATR 15.17 (6.7%), spread 0.05%, $6.2B
   traded, vol 1.7x, 5m closed in shooting star/inside bars at 225.0, no overhead resistance. Not a
   Monday-open candidate. L9 exception would need a pullback that resets the base: **trigger only a
   multi-touch hold at the opening-range low ~206.7 / EMA9 ~199 on volume >1.2x.** Stop under 193, ~4 sh.
   Kill: close below EMA21 182.5. next_earnings 11-05.
3. **ABBV (10-04 vet, still valid).** Close 276.47 (10-09 scan) > EMA21; earlier legs waited on a
   pullback to ~268. `--check ABBV` before arming; prior-close RSI sat in W4's 60-70 zone this week,
   so only a pullback entry. Probe: stop ~259.9. Kill: close below EMA21. earnings 10-30.
4. **ZS (~210.7 pullback) / CIEN (~410 pullback)** - the existing Friday stalks; L9 leaders. Trigger
   only a multi-touch hold at those levels with the written exception; spreads were wide intraday
   (ZS 2.6%, CIEN 6.8% at points), so re-check tradability first. ZS earnings 11-24.
   **COHR (10-11 vet, turnover lens) - confirmation stalk, no Monday-open entry.** Close 312.62 > EMA21
   308.44 > EMA50 302.84 (passes 3c), but below EMA9 316.02, structure range/mixed, RSI 51.9, rs 20d
   +0.5pp (in line, NOT L9), ATR 22.0 (7.0%), spread 0.25%, $2.5B traded, vol 1.15x, hammer at 309.19 on
   10-07, earnings 11-04. `--check COHR 316`: no SIGNIFICANT bucket; goods neutral_45-60 (suggestive),
   outperforming_0-10pp. **Trigger: armed buy >= 316.0 (EMA9 / resistance 315.7 reclaim) only if the
   5m tape shows vol >1.2x and price above VWAP.** Probe B/C: stop 294 (1 ATR), target ~371 (2.5 ATR),
   risk $100 / (22 x 1.7) = 2.7 -> 2 sh. Kill: close below EMA21 308.44. Not armed (research, no
   conditional beats the anticipatory record without the live tape).
5. **MU / MPC / VLO.** MU only on a 1042.4 reclaim on volume >1.2x; MPC/VLO W4 RSI 60+. (DELL/EWY
   dropped 10-13: no trigger in 4+ sessions, no fresh catalyst.)
   Intraday stalks from 10-13 legs: SNOW VWAP ~360 reclaim then 370.55 on vol >1.0x; ZS hold ~218;
   CIEN 405 reclaim on volume; MRNA ~205 hold/reclaim; ABBV hold ~267.5.

## Watch only / rejects

- **SHOP / BMBL / JPM / AMAT (10-13 evening vets, big_leaders + social + movers).** SHOP 176.52 > EMA9 166.05 >
  EMA21 155.76 > EMA50 147.2 passes 3c, uptrend, spread 0.59%, $1.24B, but RSI 72.9 (prior 76.7, W4
  `overbought_70+`), ext ~3 ATR (ATR 6.67), 94.7% of 20d range, inside bar 10-13 after a 10-08 shooting
  star, vol 0.72x, earnings 11-03: pullback to EMA9 ~166 with a multi-touch hold only. BMBL 5.95, +56.6% on
  29x volume, RSI 90.8, structure range/mixed, 100% of range, catalyst unverified (news tools down):
  chase, no stop level, REJECTED. JPM 331.43 < EMA21 337.76 < EMA50 346.19, RSI 37.3, earnings printed
  10-13 (bearish engulfing at 343.31): 3c FAIL. AMAT 464.24, -6.3% gap-down below EMA21 494.7/EMA50 497.1,
  downtrend, RSI 40.3: 3c FAIL, falling knife (support 436.3).

- **CEG / BABA (10-11 evening vets, turnover lens).** CEG 298.07 > EMA9 281.66 > EMA21 275.18 > EMA50 273.38
  passes 3c, RSI 62.3 (`strong_60-70`, W4: 1 of 12), rs 20d +2.81pp (in line, not L9), ext 2.15 ATR, ATR 4.8%,
  spread 0.08%, $1.25B, 95% of 20d range, resistance 305.8 / 309.8, earnings 11-09. `--check CEG 306`: no
  SIGNIFICANT bucket, W4 context-only bad. Parked: only a >= 306.99 (prior-day high) reclaim on vol >1.2x with
  W4 acknowledged, or a pullback to EMA9 ~282. BABA 111.37 > EMA21 110.05 but EMA21 < EMA50
  114.63 = 3c FAIL, RSI 51.1, spread 0.29%; watch only for the EMA21/EMA50 flip. earnings 11-24.

- **SMJF / SVC (10-11 late PM vets, smallcap lens) - REJECTED.** SMJF 1.53 < EMA9 1.65 < EMA21 1.99 < EMA50
  4.04, RSI 38.9, spread 14.19% UNTRADABLE (Sunday book, re-check live), shooting star at 1.75. SVC 7.15 > EMA21
  6.69 but EMA21 < EMA50 7.31 (3c fail), downtrend structure, spread 3.41% UNTRADABLE, earnings 11-04.

- **XBI / AAOI (10-11 vets) - REJECTED, 3c fail.** XBI (biotech ETF, spread 0.15%) 153.77 < EMA21 155.33
  < EMA50 156.43, RSI 46.0, bearish engulfing / shooting star at 157.47 / 152.4 earlier in the week.
  AAOI 109.64 > EMA21 109.51 but < EMA50 111.67, ATR 8.6%, tape sold off from 119.9 to 105.9; TV "sell".

- **SNOW / AMT / CCI (10-10 late PM vets, turnover lens).** SNOW passes 3c (368.89 > EMA9 343.82 > EMA21
  337.62 > EMA50 324.91; +7.4% on 2.0x vol, spread 0.27%, ATR 3.9%, earnings 12-02) but `--check SNOW 370`
  = `leader_10pp+` SIGNIFICANT (rs +10.26pp) + `strong_60-70` (RSI 68.8, W4) + ext 2.22 ATR: no
  Monday entry. Only a multi-touch hold at EMA9 ~344 / support 332 with the L9 exception. AMT 182.24 > EMA21
  169.74 but EMA21 < EMA50 170.99 (3c fail), +9.3% gap, spread 1.27% tight-size, earnings 10-27. CCI 79.64 > EMA21
  70.79 but EMA21 < EMA50 72.98 (3c fail), RSI 71.6, +15.6% on 3.8x vol, earnings 10-21.

- **KLRA / CUE / GEV / KO (10-10 PM vets).** KLRA UNTRADABLE (spread 3.25%), 11.61 < EMA21 12.07 < EMA50
  14.57. CUE 27.66 > EMA21 27.11 but < EMA50 27.91 (3c fail), +23.9% gap, ATR 13%, spread 1.15%. GEV 1004.73
  > EMA21 972.96 but EMA21 < EMA50 977.92 (3c fail by 5 pts; flips on a close ~+1%), vol 0.49x, earnings 10-28.
  KO 88.05 > EMA21 87.27 > EMA50 87.21 passes 3c by 0.07 (bunched), RSI 54.8, ATR 1.5%, vol 0.65x (quiet),
  rs -0.22pp, earnings 10-27: a low-vol drifter with no catalyst, no trigger; revisit only on a volume
  reclaim of 89.36.

- **FTXR / ENOR / CAR / DJT (10-10 vets) - all REJECTED, 3c fail.** FTXR (relvol lens, a fund) 41.53 < EMA21
  41.95 < EMA50 43.15, RSI 42.5. ENOR 35.36 < EMA21 35.69 > EMA50 35.58 mixed, RSI 43.2; Saturday quote
  spread 37.6% is stale-book noise, re-check Monday. CAR 105.98 < EMA21 113.71 < EMA50 128.3, RSI 35.8,
  bearish engulfing. DJT 8.11 < EMA21 8.76 < EMA50 9.01, RSI 34.7, 0.0% of 20d range. Falling knives.

- **P (new 10-09 vet, big_leaders lens) - REJECTED.** Close 154.49, RSI 81.5 (prior 80.0), +52.6% 1m
  (L9 leader), ext far above EMA21 128.9, shooting star 10-08 at 157.05, vol 0.49x; no `--check` needed.
  Only a pullback toward EMA9 ~143 with a multi-touch hold. next_earnings 12-01.
- **QSI (new 10-09 vet, explore lens) - REJECTED.** 1.53, +23.8% on rel vol ~5x, sub-$2 company-announced
  19-of-20 amino-acid milestone (a development-stage claim), 1m +101%, RSI 70.6, repeated dojis and
  selling marubozus AT 1.55 resistance, VWAP 1.58 above the close (closed below VWAP), spread 0.66%
  TRADABLE. 3c technically passes (1.53 > 1.08 > 0.93) but a 24% gap-and-fade at resistance with a
  $0.16 ATR has no placeable stop with room. Watch for a 1.09-1.25 hold. next_earnings 11-05.
- **WMT (new 10-09 vet) - 3c FAIL:** close 111.35 > EMA21 107.63 but EMA21 < EMA50 108.66; vol 0.52x.
  Watch for the EMA21/EMA50 flip. earnings 11-19.
- **PTC (10-08 vet) - passes the literal s6a scan, REJECTED.** RSI 80.7, L9 leader, s6a launch-low stop
  0.41% from entry sits inside the noise of a 3.6% ATR name. Pullback to EMA9 ~171.8 only.
- **DDOG** - passes 3c but RSI 64.6 (W4), L9 leader, bearish engulfing / shooting star AT resistance 280.7.
  Needs a clean close above 281.25 on volume >1.2x with the L9 exception, else a pullback to EMA9.
- **SNPS** - passes 3c, extended (RSI 72.1, shooting star at 511.95). Pullback to EMA9 ~476 only.
- **AAPL** - the 10-09 s6a plan died: gap and open broke the 338.5 hold condition, and the close was
  -1.11% on the day. The 10-08 close is no longer the launch; no s6a until three fresh rising closes.
  next_earnings 11-02.
- **Scan names without a thesis (10-09):** WFF (+499%, rel vol 277x), VEEA (+47%), ZYBT, PDSB, MRNX,
  KOD, NAUT, OFAL, SVC, DNA: spike lenses, no checked base. SXTC (-56.7%), DKI (-54%), MLEC: spike-and-
  collapse. Biotech names moving with the MRNA/NIH news (BNTX, NVAX, PCVX) are sympathy plays, not vetted.
- **STX / WDC:** below EMA21 after the 10-02 HDD scare - falling knife until a higher low forms.
- **3c FAILS / EMA21 < EMA50 (pass until they flip):** TXN, KLAC, RKLB (closest), CSCO (closest),
  GOOG, AMZN, LLY, NOW, ORCL, AVGO, GE, SCKT, WMT.
- **L9-blocked leaders (need a pullback + written exception):** META (earnings 10-28), LITE, HPE, TER
  (earnings 10-21), ENTG (spread 1.83%), ADI, INTC, NTRA, BE, ARM, TWLO, ILMN, MSTR, MRVL, AMD, NVDA,
  CRWD, OKTA, RBRK, CRDO.
- **UNTRADABLE:** REBN (spread 2.80%), PS (5.93%).
- **Older rejects, unchanged:** NU, FICO, TTD, APLD, NVTS, APP, SMMT, SHMD, JD, TOST, CELH, SEDG, F,
  SUIL, AKAM, MCHP, ON, AMBA, BYD, XPEV, NCPL, VST, DASH, SMCI, HUM, OPEN, NBIS, XOM, UPST, VKTX,
  SOFI, CRCL, RIOT/CLSK/HOOD/MARA, LRCX, IREN, SMTC, MSFT, NTAP, SYNA, CTVA (spin-off distortion),
  NXL (halt risk).

## Macro calendar

- Earnings: TER 10-21, INTC/VLO 10-22, V 10-27, STX/BE 10-27, MSFT/GOOGL/NOW/META 10-28, MA/ENTG 10-29,
  ABBV 10-30, AAPL 11-02, PLTR 11-02, MPC/SPCX/CTVA 11-03, QCOM/FICO 11-04, DDOG/NTRA/TXG/MRNA/QSI 11-05,
  PTC 11-11, WMT 11-19, ZS 11-24, DELL 11-27, CRWD 12-01, P 12-01, HPE 12-03, SNPS 12-09, MU 12-23.
- Macro: 10Y ~5.26%; no Fed/CPI date confirmed from on-screen data. Mandate expires 2026-10-27
  17:45Z. Renewal (ops/commit_paper_mandate.py) is a human action.

## Next session (Wednesday 2026-10-14, PLANNING leg pre-market)

Set the loss budget; re-verify `consent.expires_at`; read the gap scan; check MSFT's pre-market gap
against #1 and enter only if the open qualifies, with the broker stop resting the same cycle; run
`trade_context.py --check` on the actual open price first. Otherwise work the intraday stalks in #5 on
confirmation triggers only. Run at least one fresh `ta.py` workup per leg. Book is 0 of 3-6.
If the relay misses the planning leg again (as on 10-12 and the 10-13 morning), the first leg of the
day does these duties whatever its slot name.
