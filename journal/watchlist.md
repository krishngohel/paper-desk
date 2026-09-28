# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-28 evening (research leg after Monday's close). Mandate RENEWED
(`consent.expires_at` 2026-10-12T21:40:10Z, read fresh 22:00Z).

**Regime (`ta.py --market`, fresh 09-28 close):** SPY 765.61, -0.02% vs EMA21, RSI14
50.3, structure **range/mixed**. QQQ 736.53, +1.47% vs EMA21, RSI14 58.3, **range/mixed**
(was uptrend Friday). Monday was a risk-off tape for growth (MSFT -1.3%, APP/APLD weak);
10Y-yield/rate-shock still the live tail risk. No reason to chase size.

## Mandate & quota status

Mandate live to 2026-10-12. Not halted.

**Standing-order quota: MET - 6 live resting buy-limits across 5 symbols, 0 armed
triggers (NVDA trg-20260928-001 expired unfired):** CRWD 204.30 (`a1d8b66a`, 14sh) and
CRWD 232.00 remainder (`4bab1e47`, 3sh left), TXG 58.70 (`7f98e743`), SMTC 146.91
(`41354f13`), ZS 160.75 (`4b0ad29d`), RBRK 90.15 (`4e8ee047`). Most rungs sit 15-25%
below market (far from any near-term fill) - the planning leg should decide whether to
re-price the ones whose thesis still holds. No new rungs added tonight.

## Book (3 positions, target 3-6 - one below the low end)

- **PLTR - EXIT FIRED, sell-limit resting.** 10 sh @ 192.43, Mon close ~187.5 (-$49 /
  -2.5%). Fri close 189.67 < Thu 192.59 and Mon ~187.5 < Fri = TWO consecutive lower
  closes -> s6a exit. GTC sell-limit 10 @ 186.00 rests (`bcd33779`, placed 22:01Z) to fill
  at Tuesday's open; if it has NOT filled by the Tuesday planning leg (gap below 186),
  sell at market at the open per the governing rule (stop 182.94 still live).
- **CRWD** 3 sh @ 231.22, Mon close ~259.4 (+$84 / +12.2%). Target 264.13 resting
  (`9bfc5894`, +1.8% away), stop 219.15, time_stop 2026-10-03. next_earnings 2026-12-01.
- **TXG** 15 sh @ 75.64, Mon close 88.52 (+$193 / +17.0%). s6a-governed, stop 64.73, no
  target. Mon close 88.52 > Fri 85.71 - UP day, lower-close streak stays 0.
  next_earnings 2026-11-05.

## Ranked - Monday hunt

1. **Manage the book first** (stops vs 5m bars - watcher silent-miss issue; CRWD target
   resting; TXG/PLTR close-pattern at 15:00 CT).
2. **MSFT - best fit; WAIT, no order.** Mon close 509.22 (gap +3.4% Friday faded, -1.3%
   on the day; inside bar, 5m morning star + bearish engulfing at resistance 509.95) >
   EMA9 503.16 > EMA21 497.70 > EMA50 470.77 (passes 3c on the EMA order; ta.py tag
   "range/mixed"). RSI14 58.7, rs_vs_spy -0.62pp (L9 clean), vol 0.90x, spread 0.12%,
   $10.0B traded, ATR14 11.91. Friday's `--check` bucket read: neutral_45-60 RSI (10 of
   20 wins, suggestive). No hard dated catalyst. **Trigger:** do NOT chase. (a) a
   pullback that HOLDS EMA9 ~503 / support 493.81 on stabilising 5m bars, buy the
   reclaim (confirmation_trigger, re-anchor stop/target to the fill); (b) s6a: rising
   closes with the EMA stack intact, enter the next open. Planned: probe, ~$100 risk,
   stop under 491.2, target 519.4 (prior-day high) then 530. Grade C/B. Kill: close
   below EMA21 497.7 / 491. next_earnings 2026-10-28. Not staged as a resting limit:
   anticipatory limits (-$99/trade, 1/5 wins, s7a/W5) and C-grade probes (2/14, W6) are
   the desk's measured losers.
2b. **STX - WAIT, no order.** Close 921.51 > EMA9 890.41 > EMA21 867.71 > EMA50 856.57
   (passes 3c on the EMA order; ta.py tag "range/mixed"). RSI14 59.2, 98.5% of 20d range,
   rs_vs_spy +1.34pp (not L9), vol 0.91x, spread 0.05%, $3.09B traded, ATR14 50.25
   (5.5% - wide stops = small share count). Monday: gap -3.5%, hammer defended 870.38,
   ran to 932.87, closed under resistance 921.78 in a string of 5m dojis. **Trigger:**
   a daily close above 925.44/926 with the EMA stack intact, or 5m reclaim of 932.87
   with volume >1.2x (confirmation_trigger, re-anchor stop/target). Planned: probe, stop
   under 903.5 (prior-day low), target 936.49 then ~975. Kill: close below EMA21 868.
   next_earnings 2026-10-27 (ta.py now shows it).
3. **QCOM - L9 blocked.** Uptrend, close 201.97 > EMA21 183.44 > EMA50 176.06, RSI
   68.1, +4.3% on Snapdragon 8 Elite rollout + extended Apple patent agreement
   (Benzinga 09-25). `--check`: **leader_10pp+ (+18.5pp, SIGNIFICANT, 0/16)** and
   RSI 60-70 (W4, 0/10). Any thesis must cite L9 with a reason; none exists yet.
   Revisit only after a base that cuts RS below +10pp. next_earnings 2026-11-04.
4. **BE - L9 blocked.** Close 288.70 > EMA21 258.90 > EMA50 240.97, +8.4% rebound
   after Thursday's -6% Oracle force-majeure hit (Project Jupiter). `--check`:
   **leader_10pp+ (+22.1pp)**, ATR 6.9% (huge stop distance), 7.3% run from the open,
   no resistance overhead but Friday's close was a doji/marubozu at the highs.
   next_earnings 2026-10-27. Watch only.
5. **RBRK 90.15 / ZS 160.75 / SMTC 146.91** - resting GTC rungs (unfilled since
   09-16/17), thesis-of-record unchanged. ZS single-touch level (L8 caution).
   next_earnings RBRK 12-03, ZS 11-24, SMTC 11-23.
6. **TWLO / OKTA / DDOG** - still the only momentum_scan hits (TWLO 5.19% risk, OKTA
   5.15% risk). All L9 leaders (+31pp / +53.6pp / +12.7pp); DDOG fails 3c (EMA21 <
   EMA50). Carry as watch; enter only with a written L9 exception.

## Watch only / rejects

**09-28 evening vets (screen.py smallcap explore, StockTwits trending, momentum_scan;
not on prior lists):** **P** (only clean momentum_scan large hit; $591M traded, spread
0.50%, 5m shooting star + dojis at resistance 131.41): passes 3c (close 129.4 > EMA9
115.51 > EMA21 107.83 > EMA50 97.48, uptrend) but `--check 129.4` = **leader_10pp+
(rs +26.9pp, SIGNIFICANT 0/16)**, RSI 71 (overbought_70+), 3.33 ATR extension
(extended_2.5atr+: 2/13 wins) - three losing buckets stacked, ATR 5.6%; WATCH for a base
that cuts RS below +10pp. **APLD** (StockTwits): close 24.53 < EMA9 26.38 < EMA21 26.64 <
EMA50 27.66, -5.6% day, structure range/mixed, 3c FAIL (5m morning star at support 24.03
not a trend). **NVTS**: close 11.73 vs EMA21 11.79 < EMA50 12.14, +9.5% day off -4.1% gap,
range/mixed, 3c FAIL. **APP**: close 308.24 < EMA21 320.71 < EMA50 355.56, RSI 40.2, 3c
FAIL. **SMMT**: downtrend (lower highs/lows), EMA9 16.42 > EMA21 16.25 > EMA50 15.25 but
structure explicit downtrend, +17.6% intraday spike faded from 19.48 to 15.48, 3c FAIL.
**KOD** (+178% day, $3.46B, rel vol 35x): binary biotech gap event, not worked up beyond
the scan row; no base to define a stop. momentum_scan smallcaps GLND/YDES/ABLV/ZSQR/CD:
stop distance 24-43% disqualifies at probe size; WCT (3.38% risk, $1.1M traded) too thin
to size. Explore-lens SMJF/SLBT/BNKK/TANH/CANG/FLX all under $17M traded, none given a
thesis. None made the list.

**Fresh names vetted tonight (duty 1b; screen.py explore lens `smallcap`, social.py
trending, scan `big_leaders`):** MSFT (ranked #2 above; social.py trending #3 by
watchlist count, Reddit rank +13, StockTwits 9 bull / 3 bear), QCOM and BE (L9-blocked
above), **SHMD** (+20.7% scan / +33% day on $54.8M, rel vol 24.6x, spread 0.62%
TRADABLE): close 4.37 vs EMA9 3.70 / EMA21 3.68 / EMA50 4.06 - one-day spike from a
3.62 close, EMA21 < EMA50, `structure` range/mixed -> rule 3c FAIL; three 5m shooting
stars at 4.71-4.86. A gap-day spike, not a trend. Watch for a base above EMA50 4.06.
**09-26 vets:** JD (StockTwits trending) - close 26.51 < EMA9 27.00 < EMA21 27.54 <
EMA50 28.73, RSI 34.3, structure downtrend, 3c FAIL. TOST - close 30.60 < EMA21 31.74 <
EMA50 32.01, RSI 39.7, downtrend, spread 1.64% (TIGHT_SIZE), 3c FAIL. relvol-lens names
FTXH/GTOS/AKAL are funds with flat prices (FTXH +0.25% on 90x rel vol, no trend to
trade); IPST (+21.6% day but -45.1% 1m) not worked up. **momentum_scan smallcaps** ZKIN 2.35 (risk 31.2% to stop 1.62), SRFM 1.11 (23.8%),
IFBD 1.13 (27.5%): stop distance alone disqualifies at probe size. Dropped from the
watchlist: FSLY/IONQ/INOD (stale 3 sessions, no fresh evidence; FSLY L9, IONQ 3c).

**09-26 evening vets (turnover lens):** AKAM (+3.2% on 7.67x rel vol, $3.8B, spread 0.08%): close 113.94 vs EMA9 112.11 / EMA21 110.93 / EMA50 113.96 - EMA21 < EMA50, range/mixed, doji at resistance 122.79 earlier in week -> 3c FAIL; watch a close > 118.0 (prior-day high) with EMA21 crossing EMA50. MCHP (+5.4%, spread 0.42%): close 78.69 > EMA9 74.88 > EMA21 74.47 but EMA50 77.02 > EMA21 -> 3c FAIL (EMA21 still under EMA50; RSI 59.4, at 20d high, 5.4% gap). ON (+5.5%, spread 0.59%): close 77.20 vs EMA21 73.52 < EMA50 78.71 -> 3c FAIL. Semis are rebounding as a group (MCHP/ON/NXPI/CRDO +3-8%); revisit MCHP/ON only after EMA21 crosses above EMA50. next_earnings null in ta.py for all three - verify before any entry.

**09-26 late vets (gainers lens + StockTwits trending):** CELH - close 27.99 < EMA9 28.53 < EMA21 29.09 < EMA50 29.47, RSI 43.0, spread 0.04%, $182.6M, 3c FAIL (repeated rejection at 28.88-30.17). SEDG - close 32.68 < EMA21 34.46 < EMA50 38.29, RSI 43.7, spread 0.88%, vol 0.59x, 3c FAIL. F - downtrend, close 12.71 < EMA21 13.46 < EMA50 13.80, RSI 35.8, 3c FAIL. SUIL (+24% day, +108% 1m) - spread 22.5% UNTRADABLE ($8.3M traded, bid 13.37 / ask 16.76). None made the list; headlines not checked (MCPs unavailable).

**09-27 vets (StockTwits trending + Reddit rank-climbers + momentum_scan):** AMBA - close 72.68, EMA9 68.47 < EMA21 68.58 (EMA9/21 essentially flat, structure tag "uptrend" but EMA21 68.58 < EMA50 71.33) -> 3c FAIL on the literal EMA-order text despite the tag; MORNING STAR at support 63.65 09-24, watch for EMA21 to reclaim EMA50. BYD (Reddit rank +70, Boyd Gaming) - spread 4.33% UNTRADABLE, also downtrend (RSI 22.5, EMA21 75.44 < EMA50 80.25) - double reject. XPEV (StockTwits trending) - downtrend, close 10.12 < EMA21 10.74 < EMA50 11.61, RSI 34.0, 3c FAIL. NCPL (momentum_scan hit, 3d +40.2%) - spread 2.90% UNTRADABLE (playbook s7b), same reject basis as prior microcap momentum hits; APUS/GLND (also momentum_scan hits, 3d +292%/+121%) unchanged rejects on stop distance alone (36.4%/42.4% risk to launch-low stop). None made the list; headlines not checked (MCPs unavailable this session).

**09-27 evening vets (Reddit rank-climbers + StockTwits trending, 2nd leg):** MU - only
name tonight to PASS rule 3c (close 1082.28 > EMA9 1042.0 > EMA21 1003.63 > EMA50
959.32, explicit uptrend structure, RSI 63.3, TV strong_buy). `--check`: rel_strength_20d
+15.67pp -> **leader_10pp+ SIGNIFICANT (L9, 0/16)** + RSI strong_60-70 (W4, 0/10) -
both blocking buckets stack. **HARD earnings block on top: next_earnings shows null in
ta.py but Benzinga confirms Micron reports 2026-09-30 (Tue)** - inside the 2-day window
from Monday's open (playbook s5). WATCH ONLY - revisit post-print (Oct 1+) once the gap
risk clears and L9/RSI buckets can be re-checked against the new price. Reddit rank +63
(mentions 9), #1 Reddit overall. VST (Vistra, Reddit rank +269) - close 138.46 < EMA9
140.22 < EMA21 141.92 < EMA50 145.97, RSI 42.8, range/mixed -> 3c FAIL; hammer at support
134.9 on 09-25 not yet confirmed/reclaimed. Watch for a reclaim of EMA9. DASH (StockTwits
trending #2 by count) - close 193.36 < EMA9 194.23 < EMA21 201.2 ~= EMA50 201.19, RSI
39.4, range/mixed, TV strong_sell -> 3c FAIL. News sweep on book/resting-rung symbols
(CRWD/PLTR/TXG/RBRK/ZS/SMTC) since Friday close: CRWD - DOJ closed its CrowdStrike deals
investigation (positive, overhang removed) but shares dipped Friday on Akamai's $11.6B
Anthropic cloud deal (competitive-share-loss read for cybersecurity peers); PLTR - Thiel
says US corporate AI sales "accelerated tremendously" (positive); ZS - two analyst PT
raises (RBC to $236, Mizuho to $220) since Friday. Nothing invalidates any resting
thesis or book position.

**09-27 late vets (screen.py turnover-lens explore + Reddit rank-climbers, 3rd leg):**
CRDO (+7.65% on turnover) - close 210.97 > EMA9 188.74 but EMA9 < EMA21 190.15 and
EMA21 < EMA50 209.18 -> 3c FAIL on the literal EMA-order text despite an "uptrend"
structure tag (same AMBA-type tag-vs-EMA conflict). SMCI (+4.22%, StockTwits trending
#8 too) - close 43.26 > EMA9 40.77 > EMA21 39.09 > EMA50 34.99 (EMA order clean) but
`structure` explicitly "range/mixed" -> 3c FAIL on the structure text (same conflict
direction as QCOM's prior rejection); RSI 64.1 also sits in the W4 strong_60-70 losing
bucket. HUM (+4.63%, rel vol 2.09x) - spread 4.26% UNTRADABLE, also daily downtrend -
double reject. OPEN (Reddit rank +556, biggest climb tonight) - close 2.57 < EMA9 2.65
< EMA21 2.87 < EMA50 3.42, RSI 32.3, range/mixed, TV strong_sell -> 3c FAIL; a pure
hype/sentiment mismatch with the chart (playbook s11 - crowd rank is not a thesis).
NBIS (Reddit rank +23) - close 237.33 > EMA9 230.35 > EMA21 225.22 > EMA50 216.38 (EMA
order clean) but `structure` "range/mixed" -> 3c FAIL, same conflict type as SMCI.
News check (get_news): no fresh PLTR headlines since Friday close - nothing invalidates
the one-lower-close watch above. None of tonight's 5 made the list.

**Repeat rejects, unchanged reasons:** XOM (close < EMA21), UPST (bearish 3/13 sentiment
sample, not worked up), VKTX, SOFI, MSTR/CRCL, RIOT/CLSK/HOOD/MARA, SNDK/AVGO/LRCX/NVDA/
INTC, IREN - carry forward; no fresh catalyst on screen. Reddit rank-climbers
GLND (+45 ranks), TSLA (+10) noted; not vetted beyond scan lens (GLND on the `leaders`
lens, rel vol 2.43x).

## Macro calendar

- Earnings, book + candidates (all clear of any 2-day window): CRWD 12-01, PLTR 11-02,
  TXG 11-05, RBRK 12-03, ZS 11-24, SMTC 11-23, MSFT 10-28, BE 10-27, QCOM 11-04.
- Macro: 10Y near a multi-year high (09-23); no Fed/CPI date flagged inside 24h from
  what is on screen. Policy headlines on AI (FTC, OpenAI incident reviews) are noise
  for the stack unless price confirms.

## Next session (Tuesday 2026-09-29, PLANNING leg pre-market)

Set the day's loss budget; re-check `consent.expires_at` fresh (2026-10-12 as of 09-28);
cross-check every stop AND the CRWD target vs 5m bars (watcher silent-miss); review every
resting rung against overnight news; confirm PLTR sell-limit `bcd33779` filled at the open
(else market-sell at the open per s6a) and stamp the ledger; work MSFT/STX per their
triggers. MU reports 09-30 (Tue AH) - no entry before the print. Scoring debt
(`unscored_closed`) carries to the next weekly-review session.
