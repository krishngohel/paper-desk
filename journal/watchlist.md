# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede - never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-25 evening (research session, market closed, Friday after the close).
Full in-place rewrite. Monday 09-28 is the LAST mandate day.

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
**momentum_scan smallcaps** ZKIN 2.35 (risk 31.2% to stop 1.62), SRFM 1.11 (23.8%),
IFBD 1.13 (27.5%): stop distance alone disqualifies at probe size. Dropped from the
watchlist: FSLY/IONQ/INOD (stale 3 sessions, no fresh evidence; FSLY L9, IONQ 3c).

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
