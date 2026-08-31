# Archived watchlist addenda — 2026-08
Superseded weekend/session addenda, moved out of the active watchlist to keep
session context small. Permanent record; the live plan is journal/watchlist.md.

## 2026-08-29 (Saturday) research session addendum

Re-verified from a cold read (not touched since Friday 18:45 CT): `status`/`account`/
`positions`/`orders` show the book unchanged - flat (0 positions), both MRVL and PCG
GTC buy-limits still resting/accepted, no fills possible (market closed all weekend).
`ta.py --market` and fresh `ta.py MRVL`/`ta.py PCG` pulls returned data identical to
Friday's close (no new bars can print over a weekend) - both staged theses, stops, and
targets stand unchanged, nothing to revise. Added GAP (#9 above) after finding it in
Friday's own `universe_scan.json` shortlist unresearched and unpruned - a liquid mover
that fell through the cracks; no order staged for it (too extended). Attempted WebSearch
to finally get real catalyst confirmation on the MRVL/PCG drops (10+ sessions now with
alpaca-paper/vibe-research MCP unavailable) - WebSearch itself is unauthorized in this
non-interactive session, so the catalyst gap remains unresolved; still flagging for the
human. Macro note (from memory, unverified - no calendar tool available): 2026-09-04 is
a first-Friday-of-month, historically nonfarm payrolls day, AND the last day of the
active-training directive (SOP rule 6) - expect elevated volatility into a session that
also marks the training-window boundary; no confirmed FOMC/CPI date found for the
2026-08-31 to 2026-09-04 window. No US market holiday falls in that window (Labor Day
2026 is 2026-09-07, the following Monday, after the training window closes).

## 2026-08-29 third research session addendum (evening pass)

Re-verified from a cold read: `status`/`account`/`positions`/`orders` unchanged since the
17:05 CT session - flat (0 positions), MRVL 10sh @ 211.50 GTC still `accepted`/unfilled,
PCG stays cancelled (no re-stage, no new thesis to justify one). `mcp__vibe-research__web_search`
is now reachable (unlike the two earlier sessions today, which got "permissions not granted") -
used it to finally close the macro-calendar gap flagged twice today; see the "Macro calendar -
CONFIRMED" section above for the resolved NFP/CPI/FOMC dates (net: only NFP on 09-04 falls
inside the training window, no FOMC/CPI collision). Ran a fresh `get_news` pass on MRVL
(the one open thesis) - two new Benzinga pieces from today (13:00 CT, 12:01 CT) are retail-
sentiment roundups ("stocks investors couldn't stop buzzing about") naming MRVL alongside
NVDA/CRM/CRWD/IREN, no new price-moving fact, nothing that changes the staged probe's thesis
or levels. No new candidates found beyond the 9 already ranked; TENB/AFRM/PYPL/ESTC/RBRK/
IREN/GAP remain WATCH ONLY for the same reason stated twice already today (no level close
enough to Friday's close to stage without chasing) - not re-litigating that call a third time
without new information. No new orders staged this session.

## 2026-08-30 (Sunday) research session

Re-verified from a cold read: `status`/`account`/`positions`/`orders` unchanged since Friday -
flat (0 positions), MRVL 10sh @ 211.50 GTC still `accepted`/unfilled, PCG stays cancelled.
Equity $99,999.99, no drift. Regime unchanged (weekend, no new bars): SPY/QQQ range/mixed.

Duty 1b (mandatory new-name hunt): forced `screen.py` through the two explore lenses not
yet used this weekend (`relvol`, `gainers`) since `turnover` had already run twice Saturday.
Both lenses mostly surfaced illiquid microcaps, bond/leveraged ETFs with ~$0 tracked market
cap, and repeat noise - but **PD** (PagerDuty, gainers lens, also present in Friday's
un-vetted smallcap-lens list) and **SOLS** (present in the main shortlist itself since
Friday but swept into a generic bulk-prune without individual review) stood out as legitimate
liquid names that had never gotten a real `ta.py` + `get_news` workup. Both deep-vetted this
session - see ranked items #12 (SOLS, STAGED) and #13 (PD, WATCH ONLY, passed on extension +
analyst-target skepticism) above. This corrects a process gap: Friday's bulk-prune list
("sub-$3B or unrated market cap...") swept in SOLS despite its $10.09B cap and $1046.5M
dollar volume - bulk-pruning without a per-name liquidity check risked discarding a real
candidate; SOLS is exactly that candidate.

Social sweep (`social.py`, full 13-name watchlist including PD/SOLS): nothing overrides the
existing technical/catalyst reads. SOLS did not return a StockTwits sentiment sample (low
message volume on the ticker, not a red flag - the get_news catalysts are already
dated/verifiable). Reddit rank-climbers (NB, FA, SGOV, VT, EU, ES, ON, VTI, BE, LULU) - none
carry a nameable level or fall inside the current watchlist; per doctrine (crowd hype is
never a thesis, a rank-climber with no structure is a pass) none warranted a separate workup
this pass.

Earnings/event calendar: SOLS next_earnings 2026-10-29 (safe), PD next_earnings 2026-11-24
(safe) - both clear of the playbook s5 window.

Watchlist turnover note: names #3-11 (TENB/AFRM/PYPL/ESTC/RBRK/IREN/GAP/WDAY/DKNG) have now
sat WATCH-only across three research sessions (Fri/Sat/Sun) with no fresh catalyst since
Friday - but this is a market-closed weekend, not stagnation: none of their numeric triggers
have had a live session to fire against yet. Deferring any prune decision to Monday's first
session, which will have real intraday price action to judge whether each trigger is still
live or has gone stale against fresh data - pruning now, before the market has even opened
once against these levels, would be premature per the letter of the turnover rule but not
its spirit (the rule targets names that went nowhere WITH live opportunity to move, not
names still waiting for the open).

No new information changes MRVL's staged order or the macro/catalyst sections above.

14. **FRNM** (Freenome) - vetted 2026-08-30 (Sunday afternoon research session, `screen.py --mode smallcap` explore lens - the one explore lens not yet forced this weekend). WATCH ONLY, no order staged. Recent IPO (ta.py's `next_earnings` returned "No earnings dates found, symbol may be delisted" - a data-quality artifact of a name too new to have an earnings history, not an actual delisting; treated as a caveat, not a blocker, since `get_news` confirms it trades normally with analyst coverage). Guggenheim initiated coverage 2026-08-20 with a Buy rating and $21 PT (~42% above the 14.77 close). Structure uptrend (EMA9>EMA21>EMA50), TradingView strong_buy/strong_buy, but RSI14 74.9 and pos_in_20d_range 100pct with zero resistance_above (broke through everything) - the identical extended-chase problem as ESTC/GAP/WDAY/PD this scan. Nearest support 13.41 is ~9.2% below last close, too far to stage a conservative probe without chasing. Trigger: a genuine pullback to a NEW base (watch where 5m bars stop making new lows Monday) followed by a reclaim - not a chase of Friday's highs. next_earnings: none on file (fresh IPO, no history) - treat any position here as inherently higher event-risk until a first earnings date is known.

15. **BBW** (Build-A-Bear Workshop) - vetted 2026-08-30 (Sunday afternoon research session, same smallcap lens pass). WATCH ONLY, no order staged - a real falling-knife per playbook s2, not a buy until structure turns. Confirmed via `get_news`: 2026-08-27 Q2 earnings miss (adj. EPS $0.70 in-line but sales $115.3M missed the $121.1M estimate), e-commerce demand down 15.6% amid broader sales pressure, and FY2026 sales guidance CUT from $530-550M to $500-525M - a genuine fundamental deterioration, not noise. DA Davidson maintained Buy but LOWERED its PT to $37 (still above the 29.78 close, but a cut signals eroding confidence, not a reason to buy the dip). Technicals confirm: RSI14 33.7, pos_in_20d_range 12.1pct (near the range low), TradingView sell/strong_sell (moving_averages), volume_vs_20d_avg 4.2x (the selloff is real, not thin). Structure range/mixed with an inside-bar compression candle printed 2026-08-28 (watch the break direction). Support 29.4 sits close to price (~1.3% below) but with NO confirmed higher low yet - per playbook s2, a downtrend/falling-knife name at support is a watch item, not a buy, until structure turns. Trigger: a confirmed higher low forming above the 27.52 post-earnings low, ideally with a reclaim of 31.68 (first resistance) on volume - until then this is a knife. next_earnings 2026-12-03 (safe, already reported this cycle).

## 2026-08-30 (Sunday afternoon) research session addendum

Re-verified from a cold read at 14:02 CT: `status`/`account`/`positions`/`orders` unchanged since the 11:04 CT session this morning - flat (0 positions), MRVL 10sh @ 211.50 GTC still `accepted`/unfilled, SOLS 50sh @ 60.10 GTC still `accepted`/unfilled, PCG stays cancelled. Equity $99,999.99, no drift. Cushion (rule 9): high-water mark $100,007.88, floor $10,000.79, distance to floor $89,999.20 - not in wounded mode. Regime unchanged (still Sunday, no new bars since this morning): SPY/QQQ range/mixed.

Duty 1b (mandatory new-name hunt): forced the `smallcap` lens (the one explore lens not yet used this weekend - `turnover` ran twice Saturday, `relvol`/`gainers` ran this morning). Surfaced mostly the same sub-$1.6B names as Friday's original smallcap pass (SWVL/TJGC/JELD/CABO/PD/SSTK/SMPL/STRT, already screened/passed or vetted) plus new ones this pass (RCKT/FMC/FRNM/NABL/WEN/MNRO/CMRC/FNKO/RMNI/MNTN/BBW/PTLO). Two cleared the bar for a full `ta.py` + `get_news` workup: **FRNM** (#14 above, WATCH ONLY - extended IPO, no genuine support close enough to stage) and **BBW** (#15 above, WATCH ONLY - confirmed real earnings-miss/guidance-cut catalyst, falling-knife structure, no higher low yet). Both are genuine liquid names ($25.4M and $65.2M dollar volume respectively) that the liquid shortlist itself didn't surface, satisfying the anti-tunnel-vision purpose of the explore lens.

Social sweep (`social.py`, full 14-name watchlist incl. FRNM/BBW): neither returned a StockTwits sentiment sample (low message volume, consistent with SOLS's same no-sample outcome two sessions ago - not a red flag). Reddit rank-climbers (NB, FA, SGOV, ON, BE, RR, ALL, LULU, VTI, VOO) unchanged from prior sessions' reads - none carry a nameable level inside the current watchlist; per doctrine, passed without a separate workup.

Earnings/event calendar: BBW next_earnings 2026-12-03 (safe, already reported). FRNM has no earnings history on file (fresh IPO) - flagged as an inherent event-risk unknown rather than a cleared date, distinct from every other watchlist name.

Watchlist turnover: still deferring the prune-vs-keep call on names #3-11 (WATCH-only across 4 sessions now with no fresh catalyst) to Monday's first live session, per the same reasoning as the 11:04 CT session - the market has not opened once against these levels yet, so "gone nowhere" reflects a closed market, not stale evidence. No new orders staged this session - neither FRNM nor BBW offers a level close enough to stage a conservative probe without either chasing (FRNM) or catching a falling knife (BBW).

No new information changes MRVL's or SOLS's staged orders or any earlier catalyst/macro-calendar sections above.

16. **FLUT** (Flutter Entertainment, FanDuel parent) - vetted 2026-08-30 (Sunday evening research session, `screen.py --mode turnover`). WATCH ONLY, no order staged. Real catalyst, confirmed via `get_news` and shared with DKNG (#11): the same 2026-08-28 Ninth Circuit ruling against Kalshi's prediction-market sports offerings (3-0, dissolving the injunction that let Kalshi operate) is a direct competitive-moat positive for FanDuel's core sportsbook - +7.13% day on 1.69x rel_volume, TradingView buy/buy/buy, RSI14 52.2 (neutral, not extended). But the technical setup does not clear the bar the way DKNG's did: price 101.87 sits in a genuinely narrow band between support 101.12 (0.7% below) and resistance 102.74 (0.9% above) - two daily candle tells (doji then shooting star, both AT 102.74) show sellers already rejecting that resistance twice. Ran the sizing math both ways: entry at support 101.12 with stop ~0.5xATR14 (2.36) below the next support 99.39 gives R:R well under 1:1 to the 102.74 target either way (~0.7-1.0:1) - the range is too tight for the reward side to clear even the probe floor. Trigger: a clean break above 102.74 on rel_volume >= 1.5 (B-grade breakout, stop below the breakout base) is the only setup here worth trading; a pullback to 99.39 would also improve the math if it comes. next_earnings 2026-11-12 (safe).

17. **HQY** (HealthEquity) - vetted 2026-08-30 (same session, turnover lens). WATCH ONLY, no order staged - passed, not a probe. Real Q2 beat-and-raise confirmed via `get_news` (2026-08-27: adj. EPS $1.24 vs $1.19 est, sales $350.7M vs $349.2M est, FY2027 guidance raised on both GAAP and adjusted EPS) and BTIG reiterated Buy with a $115 PT (~19.5% above the 96.24 close) - but Benzinga's own same-day market-summary piece explicitly lists HQY among stocks that "fell on earnings," confirmed by the chart: RSI14 39.8, pos_in_20d_range 21.4pct (near the range low), TradingView sell/sell/neutral. A beat-and-raise the market sold anyway is either a "sell the news"/guidance-not-enough overreaction (an eventual buy) or a signal the print had a soft spot get_news's headline-only feed didn't surface - can't tell which from here, and playbook s2 says a name at support without a confirmed higher low is a watch item, not a knife-catch. Support 93.7 sits ~2.6% below, resistance 98.3 ~2.1% above - a level exists to trade, just not yet. Trigger: a confirmed 5m/daily higher low above 93.7 with a reclaim of 98.3 on volume - not present yet. next_earnings 2026-12-02 (safe).

## 2026-08-30 (Sunday evening) research session addendum

Re-verified from a cold read at 19:31 CT: `status`/`account`/`positions`/`orders` unchanged since the 17:05 CT session - flat (0 positions), MRVL 10sh @ 211.50 GTC still `accepted`/unfilled, SOLS 50sh @ 60.10 GTC still `accepted`/unfilled, PCG stays cancelled. Equity $99,999.99, no drift. Cushion (rule 9): high-water mark $100,007.88, floor $10,000.79, distance to floor $89,999.20 - not in wounded mode. Regime unchanged (still Sunday, no new bars): SPY/QQQ range/mixed (identical to every prior pass this weekend).

Duty 1b (mandatory new-name hunt): re-ran `screen.py --mode turnover` (fresh pull, same lens Saturday used - deliberate, to catch any names that crossed the liquidity/move bar since then rather than force an untried lens again). Cross-checked the 20 explore names against everything already screened this weekend: EXPE, ADM, CHTR were repeats or sub-bar; **FLUT** and **HQY** were the two genuinely new, liquid ($307M and $217.8M dollar volume respectively), real-catalyst names not yet vetted - both got the full `ta.py` + `get_news` workup (items #16-17 above). Neither cleared the bar for a probe: FLUT's catalyst is real (shares DKNG's Kalshi-ruling tailwind) but its range is too tight for acceptable R:R at current levels; HQY's beat-and-raise was sold by the market and lacks a confirmed higher low.

Social sweep (`social.py`, full 16-name watchlist incl. FLUT/HQY): neither new name returned a StockTwits sentiment sample (consistent with FRNM/BBW/SOLS's earlier no-sample outcomes this weekend - low message volume, not a red flag). Reddit rank-climbers this pass (NB, FA, LULU, RDDT, ON, ASTS, AAPL, ALL, ES, AVGO) - LULU is already vetted-and-passed above, AAPL is a closed prior position, none of the rest carry a nameable level in the current watchlist; per doctrine, passed without a separate workup.

Earnings/event calendar: FLUT next_earnings 2026-11-12 (safe), HQY next_earnings 2026-12-02 (safe) - both clear of the playbook s5 window. All other watchlist/staged names unchanged from every prior session today.

Watchlist turnover: still deferring the prune-vs-keep call on names #3-11 (WATCH-only across 5 sessions now with no fresh catalyst since Friday) to Monday's first live session - eighth consecutive weekend pass making the same call for the same reason (market hasn't opened once against these levels yet). This is the last scheduled research pass before Monday's open; the planning leg should treat the prune decision as now overdue on live data, not defer it a further session once real intraday price action exists.

No new orders staged this session (17 ranked names total, 2 staged/resting unchanged: MRVL, SOLS). No new information changes MRVL's or SOLS's staged orders or any earlier catalyst/macro-calendar sections above.

