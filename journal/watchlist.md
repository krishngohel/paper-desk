# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-10-18 Sun (research; COP/RTX folded into watch-only, ranking unchanged), prior pass 2026-10-17 Sat. Levels below were re-run with `ta.py` on the 10-16 close (markets closed
since); anything not marked "10-16" is older and stale. Mandate: expires_at 2026-10-27T17:45:52Z
(re-verify each planning leg; renewal is a human action).

**Regime (`ta.py --market`, 10-16 close):** SPY 763.25, -0.93% vs EMA21, RSI 44.3, downtrend. QQQ 709.8,
-3.53%, RSI 35.5, downtrend. Tape sold off hard Friday (MU -5.6%, AMD -6.0%, SOXL -12.7%, INTC -5.8%, SNDK -6.9%).
Defensive posture (playbook §1/§11): probes only in the most resilient names, or cash. No Fed/CPI date confirmed.
MCP servers: `alpaca-paper` connected, `vibe-research` timed out; no news cross-check this session.

## Standing orders

0 live orders, 0 armed triggers. Book flat (0 of 3-6). Nothing staged: no resting rung beats the
`anticipatory_limit` record (6 closed, 33% wins, -$66/trade) in a downtrend tape, and s6a enters at the next
open, which only a market-hours leg can do.

## Ranked - Monday 10-19 hunt (all stalks are PULLBACK holds; nothing qualifies at Friday's price)

0. **XLE (10-17 vet, social idea; new).** Close 68.24 > EMA9 66.14 > EMA21 64.82 > EMA50 63.34 (passes 3c),
   uptrend (HH+HL), +2.54% Friday with SPY -1.1% (rs_vs_spy 3.9pp; 20d rs +5.91pp = `outperforming_0-10pp`,
   5 of 11, +$626), spread 0.07%, $2.5B traded, vol 1.16x, 100% of 20d range, no resistance above, ATR 1.32
   (1.9%). Marubozu close after a 10-15 bearish engulfing. Cautions: `--check XLE 68.24` prior RSI 68.7
   (`strong_60-70` 1 of 12, W4), ext 2.54 ATR (`extended_2.5atr+` 14.3% wins, n=14), no dated catalyst on screen
   (news tools down); no earnings (ETF). Not a chase at 68.24. **Trigger: pullback that holds EMA9 ~66.1 (multi-
   touch on 5m, vol dries up on the dip) then reclaims VWAP; OR a break above Friday's high 68.33 that holds
   with the 5m tape above VWAP and day vol >1.2x AND the first hour does not fade the gap.** Probe B/C,
   `confirmation_trigger`. At a 66.3 entry: stop ~64.8 (EMA21 / 1 ATR), risk $100 / (1.5 x 1.7) = ~39 sh; target
   ~70.3 (2.5 ATR). Kill: close below EMA21 64.82.
1. **ABBV (10-16 re-vet).** Close 285.42 > EMA9 277.92 > EMA21 271.54 > EMA50 264.08 (passes 3c), uptrend
   (HH+HL), rs 20d in line (+1.73pp today; `--check` not yet run, run it at the real price), ATR 6.43 (2.3%),
   $1.65B traded, vol 1.16x, 100% of 20d range, no resistance above (high 291.4 on 10-13). Cautions: RSI 70.5
   live (69.0 prior = `strong_60-70`, 1 of 12; W4), bearish engulfing 10-13 then an inside bar, spread read
   1.69% after hours (stale book, re-check live), earnings 10-30 (time_stop must be <= 10-28). **Trigger: only
   a multi-touch hold of EMA9 ~278 (5m bars stop making new lows, vol dries up on the dip) then a reclaim of
   VWAP, OR a clean break of 291.4 on vol >1.2x with the 5m tape above VWAP.** Probe B/C, risk $100 /
   ((entry - 1 ATR) x 1.7); at 278 entry, stop ~271.0 (EMA21), 100 / (7 x 1.7) = 8 sh. Target ~295. Kill:
   close below EMA21 271.54. Mechanism `confirmation_trigger`.
2. **ACN (10-16 vet, from the s6a scan).** Close 229.68 > EMA9 213.84 > EMA21 202.61 > EMA50 190.40 (passes
   3c), uptrend, spread 0.37%, $1.7B traded, vol 0.93x, 100% of range, no resistance above, next_earnings
   12-17. Blocked as an entry now: `--check ACN 229.68` = `leader_10pp+` SIGNIFICANT (rs 20d +16.99pp, 1 of
   18), RSI 70.6 prior (`overbought_70+`, 0 of 3), ext 3.28 ATR (`extended_2.5atr+`, 14.3% wins), +18.2% in 20
   days, no dated catalyst on screen (news tools down). The shooting-star-free hammer at 223.96 held on 10-16
   (prior day high 227.86 / low 216.27). **Trigger: only a pullback that resets the base - multi-touch hold at
   216.3 (10-15 low) with vol >1.2x, written L9 exception naming the catalyst.** Stop under 212 (EMA9), ~5
   sh. Kill: close below EMA9 213.84.
3. **CDNS (10-16 vet): FAILS 3c now** (319.51 < EMA9 333.93, EMA21 330.65 > EMA50 326.05 but close under both
   short EMAs), downtrend (LH+LL), spread 1.63%, earnings 10-26 inside the window. Watch only: reclaim of
   EMA21 ~330.7 on volume after earnings, not before.
4. **MSFT (10-13 s6a plan, expired).** 529.05 now, -1.93% on the day, RSI cooled from 71. Re-qualify from a
   fresh close scan; earnings 10-28. Prior MSFT trade lost $72.94 (look it up before reuse).

## Watch only / rejects

- **XLAB / AMRO (10-19 evening vets, explore[smallcap]) - REJECTED.** XLAB 3.06 (+25% on 7.5x vol, $206M traded,
  spread 0.34%): EMA9 1.76 < EMA21 1.98 < EMA50 3.28, downtrend (LH+LL), one-day spike off a 0.94 base, shooting
  star at 3.84 on 10-16; fails 3c. AMRO 5.61: new listing, 3 daily bars, no EMAs/key levels, day range 4.91-8.64
  (shooting star at 8.64), no stop level to place. XLE 10-19 close refresh: 67.80, shooting star 68.51 on the
  day, prior RSI 69.0; #0 trigger unchanged.

- **COP / RTX (10-18 vets, explore[turnover]; new).** COP 146.51: passes 3c (EMA9 138.64 > EMA21 134.60 > EMA50
  131.02), uptrend, spread 0.24%, $1.1B traded, vol 1.18x, 100% of range, no resistance; but RSI 74.4
  (`overbought_70+`, 0 of 3), +3.4% Friday marubozu after a 10-15 bearish engulfing, ext ~2.4 ATR above EMA9; earnings
  11-05. `--check COP 146.51`: `leader_10pp+` SIGNIFICANT (rs 20d +10.94pp, 1 of 18), ext 3.61 ATR, RSI 74.7: L9
  exception needed, none exists. Same energy theme as XLE (#0): no chase; stalk only a hold of EMA9 ~138.6 (stop under 134.6 EMA21). RTX 193.92:
  EMA21 189.00 < EMA50 199.70, range/mixed, fails 3c; earnings 10-20 inside the window. Missed.

- **KHC / WFC / NEM (10-17 vets from social trending).** KHC 23.68: EMA21 23.14 < EMA50 24.19, fails 3c
  (shooting star 23.64, earnings 11-04). WFC 83.87: EMA21 82.84 < EMA50 84.83, range/mixed, fails 3c; doji at
  support 83.72 held, earnings 2027-01-14: revisit if EMA21 crosses above EMA50. NEM 118.6: passes 3c on EMAs
  (EMA21 117.55 > EMA50 117.17) but structure range/mixed, five dojis at resistance 119.05, earnings 10-22
  inside the window: no entry.
- **SITC / TCRT (10-17 evening vets, explore[smallcap]) - REJECTED, fail 3c.** SITC 3.43 (+14.95% gap on 5.96x):
  EMA21 3.14 < EMA50 3.18, structure downtrend (LH+LL), spread 2.03% TIGHT_SIZE, earnings 11-05. TCRT 2.63
  (+15.1%, $85M traded, spread 0.40%): EMA21 1.51 < EMA50 1.60, range/mixed, sellers rejected 2.58 in the last hour,
  resistance 4.4. Both are one-day spikes off a base below their EMAs.
- **Explore[relvol] 10-17:** SUPP, NSEP, RSPS, RSPF, SSS are thin ETFs (rel_volume artifacts, flat price);
  SGRX 0.87 sub-$1 spike. Nothing to vet.
- **IAM (10-16 vet, movers/explore) - REJECTED.** +25.9% to 23.81 (day high 25.0, low 21.6), only 2 daily bars
  (new listing): no EMA21/EMA50, so 3c cannot be evaluated and `key_levels` is empty; spread 1.93%
  (TRADABLE_TIGHT_SIZE), $67M traded, no earnings date, no catalyst checked. No stop level to place.
- **COHR (dropped, was #4):** collapsed 312 -> 232.9 (-7.4% Friday, gap -6.1%), downtrend, RSI 33.8, under all EMAs,
  strong_sell. Falling knife; support 220.68 only. The 316 reclaim plan is dead.
- **CEG (dropped, was a parked reclaim):** 271.37 < EMA9 280.71 and EMA21 277.73, range/mixed, RSI 46.9; the
  306 reclaim plan is dead. Support 269.53 was defended 5+ times intraday Friday (dojis AT SUPPORT) but
  structure is not an uptrend: no entry.
- **S (SentinelOne, social idea) - REJECTED.** 21.58 < EMA9 23.75 and EMA21 23.71 (> EMA50 22.47), -7.5% on 1.65x,
  bearish engulfing AT resistance 23.95, RSI 40.6, 0.0% of 20d range. Falling knife.
- **CBRS (social idea) - REJECTED.** 127.21, -10.9% on 1.28x, EMA9 151 < EMA21 168 < EMA50 186, RSI 27.0,
  downtrend, no support below. Falling knife, earnings 11-10.
- **ILMN - UNTRADABLE** (spread 4.70%), downtrend. **A / VEEV / VSTM (10-15 vets):** A and VEEV are
  `leader_10pp+`; A only on a pullback to EMA9 ~171.7 with multi-touch (earnings 11-25); VEEV chase (RSI 74),
  pullback to ~295 only; VSTM spread 2.84% UNTRADABLE.
- **LMT / CASY (10-16 s6a scan):** EMA21 < EMA50, 3c fail. **TJX / CBOE:** `leader_10pp+` SIGNIFICANT, no
  catalyst. The rest of the 10-16 s6a list: inverse/leveraged ETFs (SOXS, SQQQ, QID, SNDQ) and 15-21%
  stop-risk spikes (NCPL, IREZ, MWYN).
- **10-19 close s6a scan (86 of 88 screened, 7 names):** MAR 390.70 qualifies mechanically (> EMA9 376.33 >
  EMA21 365.55 > EMA50 358.75, uptrend, stop 386 = 1.2%) but `--check` = `leader_10pp+` SIGNIFICANT (rs +14.3pp),
  prior RSI 74.9 (`overbought_70+` 0 of 3), ext 3.58 ATR, after-hours spread 1.27%; no dated catalyst, so no L9
  exception. Pass. MCK 1010.43: UNTRADABLE (4.81% delayed spread), RSI 75.5. ACN 236.93 / TJX 147.36: L9 as
  before. CBRZ/MWYN/OLB: 10-23% stop risk spikes.
- **MRNA / SHOP / SNOW / MTD / P / PTC / DDOG / SNPS (L9 leaders, pullback only).** MRNA 218.01 (-7.8% Friday),
  SHOP 169.52 (-4.8%), P 124.01 (-7.0%): all gave back part of their run; re-run `ta.py` and `--check` before
  any use. A trigger needs a multi-touch hold at EMA9 plus the written L9 exception. Earnings: SHOP 11-03,
  MRNA/DDOG 11-05, SNPS 12-09, PTC 11-11.
- **Explore[smallcap] 10-16:** SEED, SGRX, XELB, RUBI, ACTU, POAS, UPLD, XHG, MRNO, FVN, ETS, RTSN are sub-$15
  spikes with <$10M traded (SGRX/RUBI are sub-$1 with 20x+ relvol); TCRT 2.63 (+86% 1m, $84M) a spike. No base,
  no stop with room. Not vetted further.
- **3c FAILS / EMA21 < EMA50 (pass until they flip):** TXN, KLAC, RKLB, CSCO, GOOG, AMZN, LLY, NOW, ORCL, AVGO,
  GE, SCKT, WMT, BABA, GEV, AMT, CCI, CUE, XBI, AAOI, JPM, AMAT.
- **L9-blocked leaders (need a pullback + written exception):** META (earnings 10-28), LITE, HPE, TER (10-21),
  ENTG, ADI, INTC, NTRA, BE, ARM, TWLO, MSTR, MRVL, AMD, NVDA, CRWD, OKTA, RBRK, CRDO, ZS, CIEN.
- **UNTRADABLE:** REBN (2.80%), PS (5.93%), ILMN (4.70%), SMJF, KLRA, VSTM.
- **Older rejects, unchanged:** NU, FICO, TTD, APLD, NVTS, APP, SMMT, SHMD, JD, TOST, CELH, SEDG, F, SUIL, AKAM,
  MCHP, ON, AMBA, BYD, XPEV, NCPL, VST, DASH, SMCI, HUM, OPEN, NBIS, XOM, UPST, VKTX, SOFI, CRCL,
  RIOT/CLSK/HOOD/MARA, LRCX, IREN, SMTC, NTAP, SYNA, CTVA, NXL, QSI, STX/WDC, AAPL, SVC, KO, DJT, CAR, ENOR, FTXR.

## Macro calendar

- Earnings: TER 10-21, INTC/VLO 10-22, LMT 10-22, CDNS 10-26, V 10-27, STX/BE 10-27, MSFT/GOOGL/NOW/META/ILMN
  10-28/10-29, MA/ENTG 10-29, ABBV 10-30, AAPL/PLTR 11-02, SHOP/MPC/SPCX/CTVA 11-03, COHR/QCOM/FICO 11-04,
  DDOG/NTRA/TXG/MRNA/QSI 11-05, CEG 11-09, CBRS 11-10, PTC 11-11, WMT 11-19, ZS/A 11-24/11-25, DELL 11-27,
  CRWD/P 12-01, S/HPE 12-03, SNPS 12-09, ACN 12-17, MU 12-23.
- Macro: no Fed/CPI date confirmed from on-screen data. Mandate expires 2026-10-27 17:45Z; renewal
  (`ops/commit_paper_mandate.py`) is a human action.

## Next session (Tuesday 2026-10-20, PLANNING leg pre-market)

Write the loss budget; re-verify `consent.expires_at` (10-27); read the gap scan; re-run `ta.py` on XLE/ABBV/ACN before
using any level here. Both indexes are still in downtrend (10-19 close: SPY 766.48, -0.47% vs EMA21; QQQ 718.36,
-2.16%): probes or cash, confirmation triggers only, cash is acceptable. No clean s6a name qualified at the 10-19
close (MAR is L9 with no catalyst). If the relay misses the planning leg, the first leg of the day does these
duties whatever its slot name. RTX reports 10-20, TER 10-21. W7 discard is due at Tuesday's review.
