# Watchlist - Monday battle plan

Maintained by `research` sessions (evenings/weekends). Each name: draft thesis, the
EXACT numeric trigger that turns it into a trade, planned size/stop/target/grade, and
the kill condition. Monday's pre-market planning leg reads this FIRST.

Built 2026-08-28 18:45 CT (Friday research session). Regime: SPY range/mixed (769.28,
+0.58% vs EMA21, RSI14 55.9), QQQ range/mixed (716.44, +0.34% vs EMA21, RSI14 51.4) - no
broad tailwind, trade levels per playbook s1. Source: `journal/universe_scan.json`
(17:53 CT shortlist, 1500 liquid names screened). **Caveat carried into every name
below: alpaca-paper/vibe-research MCP tools (news, screeners, fundamentals) were
unavailable this session (10+ consecutive sessions now) - every mover's CATALYST is
unconfirmed. Monday's planning leg should get_news check anything here before trusting
the technical read, especially the two staged orders below.**

## Ranked candidates

1. **MRVL** (STAGED - see below) - semiconductor, -10.48% day on 1.95x volume, TradingView
   sell/sell, but structure range/mixed (not downtrend) with support 211.13 tested 4x on
   5m bars into the close and holding. Range-bounce probe staged below Friday's close
   (216.55). Trigger already live via resting GTC limit at 211.50. If it does NOT fill:
   watch for a reclaim above opening_range_low 220.20 on volume as an alternate,
   stronger-confirmation entry (would upgrade grade). Kill: close below 202.00 (stop) or
   below 201.83 support with no bounce - stand aside, downtrend confirmed. next_earnings
   2026-12-01 (safe).

2. **PCG** (STAGED - see below) - utility, -7.54% day on 4.65x volume (real catalyst
   likely, unconfirmed), TradingView strong_sell throughout, but a hammer reversal tell
   AT support 16.53 printed at 19:55 CT after 3 prior tests held. Small conservative
   range-bounce probe staged below Friday's close (16.61) at 16.45. Kill: close below
   16.00 (stop) - if TradingView's bearish read is right and this is catalyst-driven,
   expect a gap through the stop, not a clean stop-out; Monday's open print is the first
   real test. next_earnings 2026-10-22 (safe).

3. **TENB** - cybersecurity, flat day but healthiest structure seen this scan: EMA9>EMA21>
   EMA50 (uptrend), TradingView buy/strong_buy, THREE separate 5m hammers (buyers defended
   37.98, 38.15, 37.24) despite one selling marubozu - repeated dip-buying all session.
   No genuine support close enough to Friday's close (37.65) to stage conservatively
   (nearest named support 34.62 is 8% away). WATCH, no order staged. Trigger: a pullback
   to the 36.00-36.50 VWAP/EMA21 zone that holds with a 5m higher low, OR a clean break
   above today's high 38.26 on rel_volume >= 1.5 - either would be a B-grade entry (real
   structure, not a level bet). Planned stop ~35.50 (under the defended 37.24 print isn't
   right for a fresh pullback entry - use whatever low actually holds, minus ~0.5xATR
   1.1), target 39.30 (first resistance). Kill: close below 34.62 (structure breaks).
   next_earnings 2026-10-28 (safe).

4. **AFRM** - BNPL, gapped +11.1% then faded hard to flat (day high 90.36 -> close 77.76),
   pos_in_20d_range 84.7%, repeated seller rejections AT resistance 78.69/80.65 in the
   last hour (shooting stars, bearish engulfing, doji) - a failed gap-and-go, exactly the
   playbook s9 "fade" pattern, not the "go" pattern. TradingView still strong_buy (lagging
   the fade). WATCH, no order staged - no clean level close enough to Friday's close in
   either direction to stage a probe without chasing or guessing the gap-fill depth.
   Two possible Monday triggers: (a) reclaim above 78.69-80.65 resistance on volume =
   gap-continuation long, stop below 74.51; or (b) a hold at support 74.51-72.97 on a
   pullback = bounce long, stop below 71.75. Either is a C-grade probe given the failed
   first attempt. next_earnings 2026-11-05 (safe).

5. **PYPL** - fintech, -12.68% day (gap -12.52%), RSI14 35.1, pos_in_20d_range 0% (at the
   day/range low), TradingView strong_sell, a 19:45 CT hammer+bullish-engulfing bounce
   attempt was immediately killed by a bearish engulfing at 19:50 - sellers still in
   firm control, no confirmed higher low. Classic falling-knife per playbook s2 (a watch
   item, not a buy, until structure turns). WATCH ONLY, no order staged - nearest support
   (43.74) is 18% below, far too deep to stage a probe against. Trigger: only a confirmed
   HIGHER LOW on daily/5m bars above the 52.73 day-low, not a bounce off it intraday.
   next_earnings 2026-10-27 (safe).

6. **ESTC** - already traded this week (t-2026-08-28-001, C-probe, closed flat/-0.26% on
   its own time-stop). Now extremely extended: RSI14 77.3, pos_in_20d_range 100%, gap_pct
   25.1% off Wednesday's close, zero resistance_above levels (broke through everything),
   and the last hour of 5m bars turned distinctly bearish into the close (shooting stars
   at 100.81/100.92, a marubozu sell, a bearish engulfing, four dojis) - momentum fading
   after the gap. WATCH ONLY, no order staged - too extended to buy and no fresh base has
   formed yet. Trigger: a genuine pullback to a NEW base (watch where 5m bars stop making
   new lows Monday) followed by a reclaim, not a chase of Friday's highs. Per L5 (this
   week's own lesson): if a ladder is used again here, weight whichever rung actually
   fills, not the one hoped for. next_earnings 2026-11-19 (safe).

7. **RBRK** - continued weakness, -13.11% day, closed AT the day low (93.02) after a week
   of grinding down from a post-earnings spike. Only one bullish 5m print (a 19:05
   marubozu) in an otherwise weak tape; TradingView mixed (moving_averages buy, oscillators
   sell) - no clean read. WATCH ONLY. Trigger: a confirmed higher low above 93.02 with a
   reclaim of 99.92 (first resistance) - until then this is a knife, not a bounce, per
   playbook s2. next_earnings 2026-12-03 (safe).

8. **IREN** - bitcoin miner, -12.6% day, key_levels structure explicitly "downtrend
   (lower highs + lower lows)" despite a late-session bullish attempt (bullish engulfing +
   two buying marubozu 19:00-19:20 CT, then compression). TradingView strong_sell.
   WATCH ONLY per playbook s2 (downtrend names are watch items until structure turns, no
   counter-trend catch). Trigger: a confirmed higher low forming above 34.81 (today's
   low) on a 5m/daily basis - not yet present. next_earnings 2026-11-05 (safe).

9. **GAP** (Gap Inc.) - retailer, gapped +13.23% on 2.23x volume, EMA9>EMA21>EMA50 uptrend
   stack, TradingView strong_buy/buy. Added 2026-08-29 (Saturday research session) - a
   liquid mover missed by Friday's initial pass (dollar_volume $619.5M, mkt cap $8.45B,
   both well above the liquidity bar). Extended like ESTC's setup: RSI14 71.5,
   pos_in_20d_range 100%, zero resistance_above (broke through everything - price
   discovery), and the last hour of 5m bars faded (buying marubozu + hammer defended
   23.63 at 19:00-19:05, then two selling marubozu into the close at 19:30/19:40) -
   momentum stalling after the gap, same as ESTC's late-session tell. Nearest support
   21.09 is ~10% below Friday's close (23.48), too far to stage a conservative probe
   without chasing. WATCH ONLY, no order staged. Trigger: a genuine pullback to a NEW
   base (watch where 5m bars stop making new lows Monday) followed by a reclaim, OR a
   clean continuation break above today's high 23.82 on rel_volume >= 1.5 - either is a
   C/B-grade probe given the single-day move has no track record yet. Kill: a close back
   below prior-day's close (20.82) would erase the entire gap and invalidate the thesis
   outright. next_earnings 2026-11-19 (safe).

10. **WDAY** - enterprise software, added 2026-08-29 (fourth research session, `screen.py`
    explore turnover lens - a heavily-traded name moving 3%+ that the liquid shortlist
    alone didn't surface). Real Q2 earnings beat 2026-08-28: AI products >25% of new
    contract value, accelerating subscription growth, 10+ same-day analyst PT changes
    ($160-240 range, mostly above the 204.72 close - RBC $240, Bernstein $238, BMO $230,
    Barclays $224, Wells Fargo $225 vs Stifel $160/TD Cowen $210 as low outliers) despite
    a trimmed FY2027 revenue guide and one downgrade to Hold (Freedom Broker, PT $200).
    Structure uptrend (EMA9>EMA21>EMA50), TradingView strong_buy/strong_buy, RSI14 65.6.
    Gapped from Thursday's 193.57 close, printed Friday's low 189.25 (bullish engulfing
    AT the 188.38 support level) before ripping to a 207.84 high and closing 204.72 -
    a genuine earnings-day mover that held up despite the SAME Warsh rate-hike selloff
    that hit MRVL/AFRM/ESTC/RBRK/IREN/PYPL/GAP that afternoon (WDAY is named in the same
    Benzinga "Nasdaq 100 falls" piece) - real relative strength. Caveat: pos_in_20d_range
    94.8pct, same extended-post-gap character as ESTC/GAP - nearest support 188.38 is
    ~7.9% below, too far to stage a conservative probe without chasing. WATCH ONLY, no
    order staged. Trigger: (a) a pullback to a NEW intraday base Monday (watch where 5m
    bars stop making new lows) followed by a reclaim, or (b) a clean continuation break
    above Friday's 207.84 high on rel_volume >= 1.5 - either is a B-grade entry given the
    real catalyst + confirmed relative strength. Stop below whichever base actually holds
    (or below 188.38 if trading the base itself), target the 226.53 first resistance.
    Kill: a close back below 193.57 (Thursday's pre-earnings close) would erase the
    reaction entirely. next_earnings 2026-12-01 (safe).
11. **DKNG** - sports betting, added 2026-08-29 (fourth research session, same turnover
    lens). Real idiosyncratic catalyst: Ninth Circuit Court of Appeals ruled 3-0 against
    Kalshi's prediction-market sports offerings 2026-08-28, a competitive-moat positive
    for DraftKings' core sportsbook business (Benzinga, confirmed via `get_news`) - not
    a macro/sympathy move. But the reaction faded hard: opened 24.28, ran to a 26.58
    intraday high (+9.5% off the open) on the ruling, then gave back roughly half the
    pop to close 25.26 (+4.29% day) - the AFRM playbook-s9 "fade" pattern, not a clean
    "go." Structure range/mixed, RSI14 52.1 (neutral, not extended), TradingView
    buy/strong_buy. Support 25.14/24.43/23.96 sit close to the current price (25.14 is
    just ~0.4% below), resistance 26.4/26.45/26.62 close to Friday's 26.58 high - a
    genuinely tight range, unlike most of this scan's extended gap names. WATCH ONLY, no
    order staged (the intraday fade means Friday's close isn't confirmed support yet).
    Trigger: (a) a hold at 24.43-25.14 on a 5m higher low = range-bounce long, stop below
    23.96, target 26.4 (first resistance, ~1.3:1 R:R from a 25.0 entry - probe-grade C
    only), or (b) a reclaim of 26.58 (Friday's high) on rel_volume >= 1.5 = confirmed
    continuation, stop below 25.14, target measured off the range (~28) - B-grade.
    next_earnings 2026-11-05 (safe).

12. **SOLS** (STAGED - see below) - Solstice Advanced Materials, added 2026-08-30 (Sunday
    research session, `screen.py --mode relvol`/`--mode gainers` explore passes - a liquid
    large-cap mover ($10.09B mkt cap, $1046.5M dollar volume) that Friday's initial pass had
    bucketed into the generic "pruned, sub-$3B/no structure" list without individual
    vetting - that prune was wrong for this name and is corrected here. +12.76% Friday on
    11.95x 20d-avg volume, confirmed via `get_news`: (1) 2026-08-27 20:59 CT trading halt,
    resumed on news SOLS and Element Solutions mutually terminated their pending merger
    (removed merger-arb overhang), (2) same session, board authorized a $500M share
    repurchase AND affirmed Q3/FY2026 guidance - real capital-return signal. TradingView
    summary/moving_averages/oscillators all buy, RSI14 57.4 - NOT extended (the one name
    in this whole scan without the ESTC/GAP/WDAY/PD extended-chase problem). Structure
    range/mixed, EMA50 66.01 above price (recovering from a longer downtrend, not a fresh
    high), sitting almost exactly at resistance 63.66/63.79/64.67 (Friday close 63.53) with
    a clean support cluster at 60.01/59.77 (EMA21 59.7 confluence) below. Staged a
    conservative probe buy-limit 50sh @ 60.10 GTC (order `4f6baa26-0ea9-4b97-a700-f4a334cc758a`),
    stop 58.30, target 63.66 (R:R ~1.98:1), C-probe. Ledger `t-2026-08-30-001`. Caveat:
    MACD still net-negative (-1.922, pre-catalyst downtrend momentum not yet confirmed
    reversed) and the catalyst is only 2 trading days old - no confirmed base yet. Kill:
    a close back below 56.20 (next support down) would suggest the catalyst pop is fully
    round-tripping. next_earnings 2026-10-29 (safe).

13. **PD** (PagerDuty) - vetted 2026-08-30 (Sunday research session), WATCH ONLY, no order
    staged. Real Q2 catalyst 2026-08-27: EPS/sales beat, raised FY2027 guidance, BUT also
    cut headcount ~15% same day (mixed signal) and Morgan Stanley maintained UNDERWEIGHT
    (PT raised to only $10, below the 13.80 close) while Canaccord's Buy PT is $15 (~9%
    upside only) - analyst targets cluster AT OR BELOW the current price despite
    TradingView's strong_buy/strong_buy read, a real divergence worth flagging. RSI14 75.0,
    pos_in_20d_range 100pct, zero resistance_above (broke through everything) - the exact
    same extended-chase problem as ESTC/GAP/WDAY, and here it's compounded by analyst
    skepticism rather than offset by it. Structure uptrend (EMA9>EMA21>EMA50). No level
    close enough to stage a conservative probe without chasing. Trigger: a genuine pullback
    to a new base (watch where 5m bars stop making new lows Monday) followed by a reclaim -
    not a chase of Friday's highs. next_earnings 2026-11-24 (safe).

**Vetted and passed:** LULU (turnover lens, +5.05% Friday on 1.44x volume, marubozu
buying candle) - `get_news` found NO same-day catalyst explaining the pop (only stale
2026-08-25 negative sympathy coverage tied to Dick's Sporting Goods' soft apparel-market
commentary); structure range/mixed, RSI14 51.7 unremarkable. More importantly,
next_earnings is 2026-09-03 - only 3 trading days from Monday's open and inside the
playbook s5 2-day pre-earnings window by mid-week - any thesis staged now would need to
be flattened before Wednesday regardless of technicals. Passed: no catalyst to trade and
a closing earnings window that kills it almost immediately. Not added to the ranked list.

Pruned from consideration entirely (no tradable structure): VISN/IRE/MVLL/LPTH/BRUN/AEMD/
MSTX/SLS/CONL/SOLS/AXTI/XHLD/SOLT/SHAZ/CRML/LABU/AEHR/INFQ/LABD - sub-$3B or unrated
market cap, illiquid/gappy microcaps, or single-print volume spikes (GIGL/SPTB/PULS/IAUM/
PALL/ZSL/SCHP/EWJ/ACM/AIA/SUNB/ESI/LABD) with no repeatable level structure worth a
numeric trigger. Smallcap-lens names surfaced by an earlier pass today (SWVL/TJGC/JELD/
CABO/PD/SSTK/SMPL/STRT) were sub-$1.1B cap with rel_volume mostly under 1.6x - screened
but not deep-vetted, superseded by the higher-quality turnover-lens names (WDAY/DKNG/LULU)
found this pass.

## Staged orders

- **MRVL** buy-limit 10 sh @ 211.50 GTC (order `5d4f1e58-3616-4a04-a3ba-c24fd633d2e1`),
  staged 2026-08-28 18:45 CT. Ledger: `t-2026-08-28-002` (pending_entry). Stop 202.00,
  target 222.64, time_stop 2026-09-03. **Confirmed still resting as of the 2026-08-29
  later research session; catalyst now resolved bullish - see below.**
- ~~PCG buy-limit 100 sh @ 16.45 GTC~~ **CANCELLED 2026-08-29 later research session**
  (order `cc6fe7f6-edcc-401a-a501-3e579b29b6e9` cancelled via `trade_cli.py`; ledger
  `t-2026-08-28-003` marked `aborted`). Confirmed negative catalyst below.

- **SOLS** buy-limit 50 sh @ 60.10 GTC (order `4f6baa26-0ea9-4b97-a700-f4a334cc758a`),
  staged 2026-08-30 11:04 CT. Ledger: `t-2026-08-30-001` (pending_entry). Stop 58.30,
  target 63.66, time_stop 2026-09-03.

Monday's planning leg (phase 0-1 of the `open`/first `continuous` session): re-check
`orders` for the MRVL and SOLS fills, re-verify PCG stays cancelled (do not re-stage
without a new thesis), and treat the catalyst notes below as current going into the open.

## Macro calendar - CONFIRMED (2026-08-29 later research session, via web_search)

Resolves the "unverified, from memory" macro flag repeated in the two earlier sessions
today. Confirmed via web search (financecalendar.com, tradersquant.com, polymarkettrader.com):
- **2026-09-04 (Fri) 8:30am ET: NFP jobs report** (Employment Situation) - confirmed, as
  flagged. This IS the last trading day of the active-training directive (SOP rule 6) and
  MRVL's time_stop (2026-09-03) sits one session before it - expect elevated volatility
  risk on 09-04 specifically for anything still open into that date.
- **2026-09-11 (Fri) 8:30am ET: CPI report** - falls after the training window closes,
  not an immediate concern for currently-staged probes but relevant to any position
  carried past 2026-09-04.
- **2026-09-15/16 (Tue/Wed): FOMC meeting**, decision 2:00pm ET on the 16th - ALSO after
  the training window closes. Correction to the earlier flag: there is no FOMC date inside
  the 2026-08-31 to 2026-09-04 window, only the NFP print on the 4th itself.
- No US market holiday in the 2026-08-31 to 2026-09-05 window (confirmed previously;
  Labor Day 2026-09-07 falls after training window close).
Net: only ONE scheduled macro event (NFP, 09-04) falls inside the remaining training
window, and it lands on the window's own last day - not a mid-week whipsaw risk, but
worth treating 09-04 itself as reduced-size/manage-tighter per playbook s5 if anything
is still open that morning.

## Catalyst confirmation (2026-08-29 later session - alpaca-paper MCP finally restored)

After 11+ consecutive sessions with `get_news` unavailable (root-caused and fixed by
the operator 2026-08-29 11:35 CT per the operator-note in the journal - MCP servers
were registered outside the session's config home), this session ran `get_news` on
every mover with an unconfirmed catalyst. Major finding: nearly the ENTIRE Friday
loser list (MRVL, AFRM, IREN, RBRK, ESTC) was swept down by ONE shared macro catalyst
- Fed's Kevin Warsh reviving September rate-hike odds to 60%, hitting growth/tech
broadly (Benzinga "Warsh Sparks Rate-Hike Bets... Nasdaq 100 Falls", 2026-08-28
16:46-20:00 CT, explicitly naming AFRM/AMKR/ESTC/GAP/IREN/MRVL/PYPL/RBRK among others)
- while several of these names had genuinely GOOD same-day company news getting
overrun by the macro fear:
- **MRVL**: -10.48% day was macro-driven, NOT fundamental - same-day news was strongly
  bullish (Google AI chip deal called a "monster number" by the CEO, 5 separate analyst
  price-target raises to $245-325, all 15-55% above the 211-216 zone the selloff left
  it in). Upgrades confidence that 211.13 support holding Monday is a macro-dip-in-a-
  strengthening-name, not a broken thesis. Staged probe left unchanged (already
  conservative); Monday's live workup can decide whether to add on confirmation.
- **PCG**: -7.54% day IS catalyst-driven and it's a genuine structural negative:
  California lawmakers blocked Newsom's push to shield utilities from wildfire-liability
  lawsuits (Benzinga, 2026-08-28 17:07-18:39 CT). This is exactly the "if catalyst-driven,
  expect a gap through the stop" scenario the original thesis flagged as its own kill
  condition - probe CANCELLED, not carried into Monday's gap risk.
- **AFRM**: strong Q4 beat + raised FY2027 guidance, 35% GMV growth, Shopify expansion -
  genuinely bullish (analyst targets $90-124 vs Friday's 77.76 close). The intraday fade
  from +11% to flat was the same macro rate-fear hitting Nasdaq that afternoon, not a
  failed gap-and-go on the fundamentals. Existing WATCH-only plan (triggers unchanged)
  stands, with more confidence than a pure technical fade would warrant.
- **RBRK**: also a Q2 beat + raised guidance with SIX analyst price-target raises to
  $114-130 (vs ~93 close) - the stock's weakness is post-earnings-pop giveback compounded
  by the macro selloff, not a broken story. Technicals still show no confirmed higher low
  (closed at the day low) - WATCH-only plan unchanged, but the fundamental backdrop is
  more supportive than the chart alone suggests.
- **IREN**: also strongly positive same-day news (new multi-year AI cloud contract,
  $2.8B in deals targeting $4B ARR, a $2.4B Blue Owl debt deal to buy Nvidia chips, 2026
  capacity "sold out", BTIG reiterating Buy/$80 PT vs ~34.81 close) swept down by the
  same macro selloff. WATCH-only plan unchanged (downtrend structure, no higher low yet
  per playbook s2), but the fundamental catalyst is a genuine positive, not a red flag.
- **PYPL**: the one name with a real, idiosyncratic NEGATIVE catalyst distinct from the
  macro selloff - Stripe/Advent abandoned their takeover bid, pulling the rug out from
  under a deal-premium David Einhorn had just bought into. This is a fundamental
  de-rating, not tape noise - reinforces the existing "falling knife, watch only"
  treatment; no reason to get more constructive here even if it bounces technically.
- **GAP**: independently confirmed the +12.94% gap was a real earnings beat + raised
  guidance (multiple analyst PT raises $23-42), not speculative - still extended
  (RSI14 71.5, 100% of 20d range) with no fresh base, WATCH-only plan unchanged.

Net effect: the regime read (SPY/QQQ range/mixed, no broad tailwind) stands, but the
READ on individual names shifts from "several unconfirmed, possibly broken theses" to
"one real macro wobble (rate-hike fear) sweeping over a batch of names with mostly-
strong underlying fundamentals, plus two genuine idiosyncratic risks (PCG legal,
PYPL deal-collapse) correctly separated out and treated with more caution."

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
