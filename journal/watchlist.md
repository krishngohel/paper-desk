# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-27 (Sunday research session, market closed; folds tonight's AMBA/BYD/
XPEV/NCPL vets into rejects, no changes to ranked leads). Monday 09-28 is the LAST
mandate day.

**Regime (`ta.py --market`, fresh):** SPY 771.35, +0.73% vs EMA21, RSI14 55.9,
structure **range/mixed**. QQQ 744.50, +2.72% vs EMA21, RSI14 64.8, **uptrend**.
Tech led Friday (MSFT +4%, QCOM +4.3%, BE +8.4%); 10Y-yield/rate-shock is still the live
tail risk for the growth-tilted book. No reason to chase size.

## Mandate & quota status

**Mandate `consent.expires_at` 2026-09-28T17:58:50Z - Monday is the last full day;
re-check `consent` fresh Monday pre-market.** Not halted (`status` fresh 09-25 evening).

**Standing-order quota: MET - 6 live resting buy-limits across 5 symbols, 0 armed
triggers:** CRWD 204.30 (`a1d8b66a`, 14sh) and CRWD 232.00 remainder (`4bab1e47`, 3sh
left), TXG 58.70 (`7f98e743`), SMTC 146.91 (`41354f13`), ZS 160.75 (`4b0ad29d`), RBRK
90.15 (`4e8ee047`). No order placed or touched this session. Most rungs sit 15-25%
below market (far from any near-term fill) - Monday's planning leg should decide
whether to re-price the ones whose thesis still holds.

## Book (3 positions, target 3-6 - one below the low end)

- **CRWD** 3 sh @ 231.22, now ~252.30 (+$63 / +9.1%). Target 264.13 resting
  (`9bfc5894`, +4.7%), stop 219.15, time_stop 2026-10-03. next_earnings 2026-12-01.
- **PLTR** 10 sh @ 192.43, now ~189.62 (-$28 / -1.5%). s6a-governed, stop 182.94, no
  target. Exit only on two consecutive lower closes. next_earnings 2026-11-02.
- **TXG** 15 sh @ 75.64, now ~85.72 (+$151 / +13.3%). s6a-governed, stop 64.73, no
  target. Exit only after two consecutive lower closes below 84.14 (09-25 close was
  above it - no lower close counted). next_earnings 2026-11-05.

## Ranked - Monday hunt

1. **Manage the book first** (stops vs 5m bars - watcher silent-miss issue; CRWD target
   resting; TXG/PLTR close-pattern at 15:00 CT).
2. **MSFT - best fit found tonight; WAIT, no order.** Close 516.17 > EMA9 501.64 >
   EMA21 496.65 > EMA50 469.02 (passes 3c on the EMA order; ta.py tag reads
   "range/mixed"). `trade_context --check 517.9`: rel_strength_20d **+0.17pp** (NOT
   leader_10pp+ -> L9 clean), RSI14 54.4 (neutral_45-60 bucket: 10 of 20 wins = 50%,
   suggestive), 2.06 ATR extension (moderate), gap +3.4% on Copilot relaunch + tech
   leadership - no hard dated catalyst. Vol 1.78x, spread 0.03%, $19.6B traded.
   Friday closed as a 5m shooting star + marubozu selling at resistance 517.78.
   **Trigger:** do NOT chase the gap. Two ways in - (a) pullback that HOLDS the
   gap-fill zone 498.9 (prior-day high) / EMA9 ~501 on stabilising 5m bars, buy the
   reclaim (confirmation_trigger, re-anchor stop/target to the fill); (b) s6a: a
   3rd/4th rising close with EMA stack intact, enter the next open. Planned: probe,
   ~$100 risk, stop under 491.2 (prior-day low), target 517.8 then 530. Grade C/B.
   Kill: close below EMA21 496.65 / gap fully filled below 491. next_earnings 2026-10-28.
   Not staged as a resting limit tonight: anticipatory limits (-$99/trade, 1/5 wins,
   s7a/W5) and C-grade probes (2/14, W6) are the desk's measured losers.
2b. **STX - new 09-26, WAIT, no order.** Close 916.83 > EMA9 882.64 > EMA21 862.29 >
   EMA50 852.96 (passes 3c on the EMA order; ta.py tag "range/mixed"). RSI14 58.8,
   `--check 922`: rel_strength_20d **+8.19pp** (outperforming_0-10pp, not L9), ext 1.19
   ATR, RSI neutral_45-60. Three straight daily inside bars 09-23..09-25 (compression
   under prior-day high 926.01), vol 0.72x, spread 0.30%, $2.56B traded, ATR14 49.3
   (5.4% - wide stops mean small share count). 5m dojis at resistance 921.78 into the
   close. **Trigger:** s6a-style upside break - a daily close above 926.01 with the EMA
   stack intact, or reclaim of 921.78 with volume >1.2x (confirmation_trigger,
   re-anchor stop/target to the fill). Planned: probe, stop under 898.8 (prior-day low),
   target 936.49 then ~975. Kill: close below EMA21 862. next_earnings unavailable in
   ta.py (null) - verify before any entry. Headlines not checked (news MCP timed out).
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

## Next session (Monday 2026-09-28, PLANNING leg pre-market)

Set the day's loss budget; verify `consent.expires_at` fresh (last mandate day - if
expired, journal MANDATE EXPIRED and stop); cross-check every stop AND the CRWD target vs
5m bars (watcher silent-miss); review every resting rung against weekend news; work MSFT
per its trigger; TXG/PLTR two-lower-closes check at the close.
