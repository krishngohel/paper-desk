# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-10-11 Sun (research; ranking unchanged from 10-09; FTXR/ENOR/CAR/DJT/KLRA/CUE/GEV/KO/AMT/CCI/SNOW/BIII/GIW vetted and rejected or parked, see Watch only; BIII/GIW are ~$10 cash shells, ATR $0.01, spreads 51.6% / 2.75% UNTRADABLE).
Mandate (verified in the 10-09 review): expires_at 2026-10-12T21:40:10Z. **Monday 10-12 is the
LAST valid session; human renewal needed.** An s6a hold (days) outlives the mandate, so any Monday
entry must carry a resting broker stop (it keeps working after expiry) and the thesis must say so.

**Regime (`ta.py --market`, 10-09 close):** SPY 778.57, +1.15% vs EMA21, RSI 60.0, range/mixed.
QQQ 751.27, +1.57%, RSI 61.1, range/mixed. Neutral posture, s6a first, confirmation entries only.
10Y ~5.26% is the tail risk (10-09 news: Nasdaq rebounded from a Thursday OpenAI-driven selloff;
TMUS -12% on a SpaceX spectrum deal). No Fed/CPI date confirmed from on-screen data.

## Standing orders

0 live orders, 0 armed triggers. Book flat (0 of 3-6). Nothing staged: s6a enters at the NEXT OPEN,
which only a market-hours leg can do (no market orders in research), and no resting rung beats the
`anticipatory_limit` record (6 closed, 33% wins, -$66/trade).

## Ranked - Monday 10-12 hunt

1. **V and MA - the two workable s6a candidates (10-09 close; both +2.6-2.9% marubozu days, payments
   re-rated, Baird PT raise on MA).** Both pass 3c only barely: EMAs are bunched.
   - **V:** close 385.45 > EMA9 372.18 > EMA21 369.98 > EMA50 368.44, RSI 58.8 prior close
     (`neutral_45-60`), rs 20d +0.03pp (in line, NOT L9), ATR 6.53 (1.7%), spread 0.30%, $2.3B traded,
     vol 0.96x, ext 2.86 ATR (`extended_2.5atr+`: 1 of 7 wins, -$223, context-only, not significant).
     Resistance 385.57 (morning star + dojis AT it into the close). s6a launch-low stop 370.37 (3.9%).
     `--check V 386`: no SIGNIFICANT bucket; goods neutral_45-60 (suggestive), outperforming_0-10pp;
     context-only bads: market-up 3 of 18, extension. earnings 10-27.
   - **MA:** close 589.14 > EMA9 570.14 > EMA21 568.18 > EMA50 567.88, RSI 56.8 prior close, rs 20d
     -0.46pp (`lagging_spy`, W9 suggestive 6 of 9), ATR 10.11 (1.7%), spread 0.46%, $1.4B, vol 0.85x,
     ext 2.51 ATR. Support 588.11 (dojis held it x5 late), resistance 592.97 / 601.23. Stop 568.49 (3.5%).
     `--check MA 590`: no SIGNIFICANT bucket; goods lagging_spy, neutral_45-60. earnings 10-29.
   - **Plan (open slot / planning leg), pick ONE, MA first (better buckets, tighter stop):** s6a market
     entry at the 10-12 open ONLY if the gap is within +-0.7% and the first 5m bars hold above the
     prior close level (MA 588, V 384). A gap UP beyond +0.7% (chasing a 2.5-ATR-extended close) = pass,
     wait for a hold at support (MA 580.9-588, V 378.5) instead. Probe B/C: risk $100 / ((entry-stop) x
     1.7): MA ~(590-568.49)=21.5 -> ~2.7 -> 2 sh (~$1.2k); V ~(386-370.37)=15.6 -> ~3.8 -> 3 sh (~$1.2k).
     No numeric target; `sell QTY --stop S --gtc` rested the same cycle (stop survives mandate expiry).
     Archetype `momentum_s6a`, entry_mechanism `market`. Kill: two consecutive lower closes, or close
     below EMA21 (V 369.98, MA 568.18). Both report within 3 weeks; exit/cut before 10-27 / 10-29.
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
5. **DELL / EWY / MU / MPC / VLO.** DELL stale (earnings 11-27; 5m hold above 574 on volume >1.2x),
   EWY stale (hold above 194.0), MU only on a 1042.4 reclaim on volume >1.2x, MPC/VLO W4 RSI 60+.
   DELL and EWY are untouched for 4+ sessions: they drop off at the 10-12 review unless a trigger fires.

## Watch only / rejects

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
- Macro: 10Y ~5.26%; no Fed/CPI date confirmed from on-screen data. **Mandate expires 2026-10-12
  21:40Z - renewal (ops/commit_paper_mandate.py) is a human action; a lapse stops all order actions.**

## Next session (Monday 2026-10-12, PLANNING leg pre-market)

Set the loss budget; re-verify `consent.expires_at` (Monday is the last valid session); read the gap
scan; check MA and V pre-market gaps against #1 and enter ONE as a probe at the open only if the gap
qualifies, with the broker stop resting the same cycle; run `trade_context.py --check` on the actual
open price first. Otherwise work ABBV/ZS/CIEN/MRNA pullbacks on confirmation triggers only. Run at
least one fresh `ta.py` workup per leg. Book is 0 of 3-6.
