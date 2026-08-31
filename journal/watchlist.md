# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-08-31 22:15 CT (second Monday-evening research leg, same session day - folded
forward, no re-append). Regime unchanged: SPY range/mixed (767.05, +0.26% vs EMA21, RSI14
54.1), QQQ range/mixed (716.76, +0.35% vs EMA21, RSI14 52.3), trade levels per playbook s1.
Source: `journal/universe_scan.json` (17:02 CT relvol + gainers explore lenses, re-screened
this leg) and `journal/social.json` (17:02 CT, re-screened this leg).

## Ranked candidates

1. **MRVL** (BOOK POSITION, 10 sh @ 211.472) - `t-2026-08-28-002`. Range/mixed structure
   intact, testing support 211.10 into the close (bearish engulfing AT SUPPORT 21:05 UTC -
   a rejection, not yet a breakdown; watch for a confirmed close below it). TradingView
   flipped to sell/strong_sell/sell (was neutral). Stop 202.00 (watcher-enforced, well
   clear), target 222.64 resting GTC across two orders (`9184e057...` 8sh + `7c26ff3e...`
   2sh). next_earnings 2026-12-01 (safe). No action - fully bracketed, let it work.

2. **CRWD** - cybersecurity, hit a NEW ALL-TIME HIGH today on FIVE separate same-day
   catalysts confirmed via `get_news`: Fal.Con 2026 conference product news (drove the
   ATH), Cognizant OT-cybersecurity partnership expansion, Snowflake Marketplace
   collaboration, Falcon-on-Google-Cloud, and a fresh AI Partner Specialization
   announcement (20:42 UTC, after today's own trigger trg-20260831-003 @ 234.00 was
   cancelled mid-morning on a volume fade - the thesis outlasted that cancellation).
   EMA9(211.00)>EMA21(206.37)>EMA50(195.13) uptrend, RSI14 63.0, rs_vs_spy_pp +5.38, no
   resistance_above (price discovery). **STAGED**: buy-limit 23 sh @ 225.50 GTC (order
   `760d71d9-ccef-4e66-bb39-474a5655cd52`), just above the defended opening_range_low
   225.07 - a pullback-into-today's-range probe, not a chase. Stop 218.91 (~0.5xATR14
   below the level), target 238.00 (~1xATR14), R:R 1.90:1. Ledger `t-2026-08-31-002`
   (B-probe). Kill: a close back below prior-day close 218.40 would erase today's gap
   entirely - cancel the resting order if that prints first. next_earnings 2026-12-01
   (safe).

3. **CRCL** - Circle (stablecoin issuer), +9.02% day on 1.34x volume, uptrend confirmed
   (bullish engulfing AT SUPPORT 84.25 today), EMA9>EMA21>EMA50 stack, TradingView
   strong_buy/strong_buy/buy. Today's own trigger (trg-20260831-004 @ 96.25) never fired
   in regular hours but the after-hours tape printed 96.40 - through the level - before
   fading to ~95.00, meaning the breakout is being actively contested, not rejected.
   `get_news` found NO company-specific catalyst (only a generic whale-options-activity
   mention) - this is a technical/momentum thesis, graded down accordingly (playbook
   s11 - the chart earns the grade, not a story). **STAGED**: buy-limit 70 sh @ 90.00 GTC
   (order `1562bf52-5664-4a07-909d-78acebc7e37f`), just above today's day_low/
   opening_range_low 88.30 (held all session). Stop 87.90, target 96.40 (the after-hours
   high this thesis is testing), R:R 3.05:1. Ledger `t-2026-08-31-003` (C-probe). Kill: a
   close back below 84.25 (today's engulfing base) invalidates the uptrend read.
   next_earnings 2026-11-11 (safe).

4. **ASND** (PENDING - see below) - Ascendis Pharma, +7.01% on a binding BioMarin patent
   settlement (removed litigation overhang) plus five sell-side Buy reiterations (targets
   15-30% above spot despite target trims). Ladder resting per below, unchanged thesis.
   Ledger `t-2026-08-31-001` (B-probe). next_earnings: unconfirmed (`ta.py` returned null)
   - flagged unknown-risk per playbook s5, not cleared.

5. **SOLS** (PENDING - see below) - Solstice Advanced Materials, merger-termination +
   $500M buyback catalyst from last week still intact. Chopping right at resistance
   63.68-64.74 (shooting stars AND a bullish engulfing both printed there today - genuinely
   undecided, not yet resolved either way). Resting probe unchanged below. Ledger
   `t-2026-08-30-001` (C-probe). next_earnings 2026-10-29 (safe).

6. **STDN** (PENDING - see below) - new name this leg, surfaced via `screen.py --mode
   gainers` explore lens (duty 1b hunt). +14.58% day_change, gap +5.74%, volume_vs_20d_avg
   2.44x (real participation). Structure confirmed UPTREND, EMA9>EMA21, MACD +1.77, RSI14
   66.6, TradingView strong_buy across the board, rs_vs_spy_pp +14.83 (strong outperform).
   `get_news` found only two generic "stocks moving" roundup mentions - no company-specific
   catalyst - graded C/probe per playbook s11 (chart earns the grade, not a story).
   pos_in_20d_range_pct 100% (fully extended, real chase risk) and resistance_above is
   empty (price discovery, no breakout level to size against). **STAGED**: buy-limit 100
   sh @ 14.85 GTC (order `784b6a0f-ed2f-4877-931e-be0a6fb53a58`), at today's own tested
   opening_range_low/day_low (14.85/14.83, held all session) - a pullback-into-range probe,
   not a chase. Stop 14.20, target 16.22 (today's day_high), R:R 2.11:1. Ledger
   `t-2026-08-31-005` (C-probe). Kill: a close back below 14.20 or fresh negative news.
   next_earnings 2026-11-16 (safe).

## Vetted this leg, no order placed

- **TITN** (Titan Machinery) - +15.17% day_change, real defended support (5 dojis all AT
  20.12 over the last hour, playbook s2b compression-at-a-level), TradingView strong_buy,
  but no company-specific catalyst found (generic Benzinga roundup mention only). Attempted
  a conservative probe (100 sh @ 20.12 GTC) - **REFUSED by the gate's PRICE_BAND fat-finger
  guard**: `{"status": "blocked", "code": "PRICE_BAND", "detail": "buy limit 20.12 is 15.1%
  through quote ref 17.48 (band 10.0%) - fat-finger guard"}`. Root cause: `trade_cli quote
  TITN` showed bid 17.48/ask 0.00 - an invalid two-sided market, below the entire day's real
  trading range (19.81-21.04 per bars), the same bad-tick/IEX-lag pattern flagged repeatedly
  today for ASND/TENB/CRWD. Declined to chase the broken quote by lowering the limit toward
  it (would violate the standing never-price-off-a-bad-tick discipline) - dropped, not
  forced; recorded aborted in `trades.jsonl` (`t-2026-08-31-004`), not counted as a trade.
  Re-examine next session once the broker quote refreshes past market reopen.

## Vetted and passed (playbook s2 - falling knives, no buy)

- **EIX / PCG** - California utility wildfire-liability crisis. Confirmed via `get_news`:
  California lawmakers left investor-owned utilities on the hook for wildfire liability
  (SB 492 failed to cap it) - Edison down 22.6% (worst day since 2001), PG&E down 19.3%,
  a WAVE of same-day analyst downgrades (Wells Fargo, Mizuho, BMO all cutting PT
  40-50%+: PG&E to $16-24, Edison to $70). RSI14 22/22, **no support_below levels at all**
  from `ta.py` (broken through everything), still printing selling marubozu into the
  close - a textbook falling knife, not a dip. PCG's prior staged probe (`t-2026-08-28-003`)
  was correctly cancelled 2026-08-29 on the first sign of this catalyst and stays
  cancelled. No trigger staged for either name - would need a confirmed higher low AFTER
  the legal situation stabilizes, which given uncapped liability exposure could be weeks
  away, not a same-week setup. SRE (Sempra) also named in the same downgrade wave but
  didn't clear today's shortlist - watch if it appears on a future scan.

- **HWM** (Howmet Aerospace) - -6.66% day, gap -6.2%, downtrend structure (lower highs +
  lower lows), RSI14 28.3, repeated rejections at support 243.68 (shooting star + bearish
  engulfing + two dojis, no confirmed hold). Two same-day catalysts found via `get_news`,
  net mixed-to-negative: broad macro headwind (oil spiking near $90 on new Iran strikes,
  10Y yield to a 19-month high, Dow -0.64%) PLUS a genuine competitive-threat headline -
  "SpaceX is building gas-turbine parts in Texas as Elon Musk targets a casting
  bottleneck" - i.e. Musk/SpaceX moving into the turbine-blade casting business that is
  core to Howmet's own forge/casting franchise, not simply a bullish "HWM benefits from
  AI power buildout" story as the headline framing first suggested. No earnings catalyst
  (next_earnings 2026-11-05, not until then). WATCH ONLY - no confirmed higher low yet;
  a reclaim of 249.28 (today's high) off a higher low above 243.68 would be the earliest
  bounce signal worth a probe.

## Pruned this session (no fresh catalyst today, absent from full-market/turnover/gainers
scans; each already had a full workup and/or a live armed-and-cancelled trigger across
Friday through today's 17-leg continuous relay - re-add only on new evidence)

TENB (index-inclusion thesis fizzled on collapsing volume, trg-20260831-001 cancelled),
IREN (bounce rejected at highs on thin volume, trg-20260831-002 cancelled), AFRM, PYPL,
ESTC, RBRK, GAP, WDAY, DKNG, PD - all quiet today, no new price action or catalyst to
re-rank against the five live names above.

## Macro calendar (confirmed 2026-08-29 via web_search, still current)

- **2026-09-04 (Fri) 8:30am ET: NFP jobs report** - last trading day of the active-training
  directive; elevated volatility risk for anything still open into that date.
- **2026-09-11 (Fri): CPI report** and **2026-09-15/16: FOMC** - both after the training
  window closes (2026-09-04), not an immediate concern for currently-staged probes.
- No US market holiday before 2026-09-05 (Labor Day 2026-09-07 falls after window close).
- New this session: oil near $90/bbl on fresh US-Iran strikes (2026-08-31) - a live macro
  thread worth tracking for energy-sector spillover, separate from the utility-sector
  wildfire-liability catalyst above.

## Staged orders (live as of this session)

- **ASND** 2-rung ladder: 25 sh @ 262.05 GTC (`194afe49-73a9-430e-9a11-95819cd8b263`) +
  15 sh @ 260.60 GTC (`6cdee89c-2d15-4a2c-95d9-98d5b0df3c77`). Stop 258.50, target 268.65,
  time_stop 2026-09-02. Ledger `t-2026-08-31-001`.
- **SOLS** 50 sh @ 60.10 GTC (`4f6baa26-0ea9-4b97-a700-f4a334cc758a`). Stop 58.30, target
  63.66, time_stop 2026-09-03. Ledger `t-2026-08-30-001`.
- **CRWD** 23 sh @ 225.50 GTC (`760d71d9-ccef-4e66-bb39-474a5655cd52`). Stop 218.91,
  target 238.00, time_stop 2026-09-02. Ledger `t-2026-08-31-002`.
- **CRCL** 70 sh @ 90.00 GTC (`1562bf52-5664-4a07-909d-78acebc7e37f`). Stop 87.90, target
  96.40, time_stop 2026-09-02. Ledger `t-2026-08-31-003`.
- **STDN** 100 sh @ 14.85 GTC (`784b6a0f-ed2f-4877-931e-be0a6fb53a58`). Stop 14.20, target
  16.22, time_stop 2026-09-03. Ledger `t-2026-08-31-005`.

Standing-order quota (binds `research` sessions too, SOP duty 3b): 6 live conditional
entries across 5 distinct symbols (ASND x2, SOLS, CRWD, CRCL, STDN) - quota met.

Next session (planning leg, pre-market 2026-09-01 or the next `open`/`continuous` slot):
re-check `orders` for fills on all five staged names against overnight news, re-verify
MRVL's 211.10 support didn't break, re-examine TITN once broker quotes refresh past market
reopen (aborted this leg only on a broken bid, not on thesis), and treat the EIX/PCG/HWM
pass-reasoning above as current unless a new catalyst appears.
