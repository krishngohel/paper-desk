# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-14 ~17:10 CT (research session, market closed - Monday evening,
post-close homework after today's full trading day: 4 legs continuous + preclose +
weekly-review). Full rewrite - prior version (09-09) referenced a book (COIN/IOT/
LITE/SMMT, staged HOOD/MSTR) that no longer exists; today's mandate-renewal, a
sector-rotation trading day, and the weekly review have superseded all of it.

**Regime (`ta.py --market`, 17:05 CT):** SPY 760.88 (vs_ema21 -0.47%, RSI14 47.2),
QQQ 709.18 (vs_ema21 -0.65%, RSI14 46.4) - both **range/mixed**, essentially flat to
slightly weaker than this morning. **Dominant story today: a sector-wide rotation OUT
of AI/chip names and INTO cybersecurity**, triggered by OpenAI/Anthropic publicly
calling for an AI development slowdown plus Microsoft's new AI-safety rules
(Benzinga, multiple stories 06:25-19:32 UTC). Cybersecurity (CRWD, PANW, ZS, S, SAIL,
RBRK, TENB, NET, OKTA) rallied hard (S/SentinelOne had its 2nd-biggest day ever,
+16%); AI/chip/optics names (GLW, TER, MXL, MU, INTC, AMD, COHR) sold off hard in the
same tape. Two added macro headwinds confirmed tonight: **the 10-year yield briefly
touched 5%**, and **Brent crude is above $102/barrel** (US-Iran tension, running
since 09-09) - both bearish-for-equities pressures layered on top of Tuesday/
Wednesday's FOMC decision (see macro calendar). This is a genuine, multi-source,
dated catalyst (not crowd hype) - it is the reason today's desk entries (BWIN
unrelated momentum trade, CRWD/RBRK/ZS same-cluster trades) leaned into cybersecurity.

## Mandate & quota status

**Mandate renewed 2026-09-14, `consent.expires_at` 2026-09-28T17:58:50Z - good for
2 more weeks, no urgency.**

**Standing-order quota: 5 live conditional entries across 3 distinct symbols (RBRK
x2 armed triggers @100.10/101.50, CRWD resting buy @232.00, HOOD x2 resting rungs
@108.85/100.70) - BELOW the >=6-across->=3 target, carried over as a FAILED LEG from
today's 14:35 CT preclose leg (ZS's trigger fired, consuming 1 without a same-leg
replacement because the leg was consumed by a gate-fault investigation).** This
research session hunted hard for a 6th replacement (duty 1b + quota refill): vetted
VEEA, VNCE, NTSK, RUM, ELMT fresh off tonight's explore-lens scan and news movers,
plus re-checked SAIL/RBRK/ZS/CRWD structure tags directly - **none independently
qualify** (see Watch-only section). Did NOT force an order to hit the number (rule 6:
"a forbidden setup is never how you satisfy... the standing-order quota"). Tomorrow's
planning leg inherits this shortfall; RBRK's two triggers also expire tomorrow
2026-09-15T15:00 CT if unfired, which would drop the count further to 3/2 - refilling
is the first priority next session regardless of whether a 6th name is found tonight.

**Process note for the next review (not a lesson - flagging only):** tonight's fresh
`ta.py` pulls show RBRK, ZS, and CRWD *all* carry a `structure: "range/mixed"` tag
identical to TENB/QLYS/S/SAIL, which today's 13:31 CT continuous leg rejected
explicitly *because* of that same tag ("range/mixed does not qualify" per SOP s3c).
The same leg's own text calls RBRK/ZS/CRWD "the 3 names that DID pass structurally" -
but the structure tag itself doesn't actually distinguish them from the rejected
group; only the raw EMA numeric order does. Worth the next review resolving whether
SOP s3c means "structure tag must read uptrend" (stricter, would have blocked
today's RBRK/ZS/CRWD trades too) or "EMA order passes AND structure isn't tagged
downtrend" (looser, what today's trades actually followed). Not re-litigating today's
already-placed trades here - just flagging the ambiguity so it doesn't recur silently.

## Book (4 positions)

- **ANGX** 68 sh @ avg 5.39, last 5.57 (+3.3% ROI). Stop 5.05 (9.3% clear), target
  5.95 resting (4cb979aa). **time_stop 2026-09-17** (extended today from 09-12 per
  L7, uptrend intact, RSI14 was 72.7 extended - caution flag). next_earnings
  2026-11-03 (safe, checked today).
- **BWIN** 75 sh @ avg 31.89, last 32.00 (+0.03% ROI). Stop 28.82 (9.6% clear,
  watcher-enforced), **no target - governing exit is 2 CONSECUTIVE lower daily
  closes** (playbook s6a momentum archetype, the desk's only significance-cleared
  edge). Only today's entry-day close exists so far - nothing to evaluate yet; check
  every session once a second daily close prints. time_stop 2026-10-13 (outer
  backstop only). next_earnings 2026-11-03 (safe).
- **IOT** 75 sh @ avg 37.971733, last 42.835 (+12.8% ROI, ~+2.9R). Stop 38.68
  (trailed up from 36.31 today, 9.7% clear), target 44.68 resting (c07abd8f).
  **time_stop 2026-09-15 - TOMORROW.** Next trading-capable session MUST re-decide
  extend-vs-cancel fresh: position remains well clear of both levels and deep in
  profit, so per L7 elapsed time alone is not cause to force-close, but this is due
  for an active decision, not a default rollover. next_earnings 2026-12-03 (safe).
- **ZS** 17 sh @ avg 193.12, last 192.10 (-0.5% ROI). Stop 188.15 (2.1% clear -
  tightest in the book), target 208.03 **now resting** (order 489b3ab4, fixed this
  session - the `pending_action_unresolved` gate marker that blocked it since 14:35
  CT self-cleared; retried once this leg per the established cadence and it went
  through cleanly). time_stop 2026-09-19. next_earnings 2026-11-24 (safe). Same
  sector-rotation thesis as RBRK below; watch stop clearance closely, it's the
  tightest position in the book.

## Staged / armed for next session - ranked

- **RBRK** (Rubrik) - 2 confirmation triggers still live, both **expire tomorrow
  2026-09-15T15:00 CT**: trg-20260914-001 buy>=100.10 qty29, trg-20260914-002
  buy>=101.50 qty19 (rung2). Same dated sector-rotation catalyst as ZS (Benzinga,
  multiple stories today). Fresh check tonight: last 100.20, bid 99.55/ask 100 -
  still just below rung1, multiple dojis at the 100 level this evening (unresolved
  fight, not yet confirmed). EMA9 92.46>EMA21 92.33>EMA50 86.82 (numeric pass),
  structure tagged "range/mixed" (see process note above). next_earnings 2026-12-03
  (safe). TV strong_buy/strong_buy/neutral. Grade B, probe, unchanged from arming.
  Kill: triggers expire unfired tomorrow 15:00 CT, or a close back below 90.15.
- **CRWD** - resting GTC buy-limit 232.00 (order 4bab1e47) unfilled, pullback-to-VWAP
  entry on the same catalyst cluster. Last 235.38, bid/ask has ranged 226-240 all day
  without touching the limit. Structure "range/mixed" (same caveat as RBRK). TV
  summary neutral tonight per fresh check; social sentiment (StockTwits, tonight)
  reads 2 bullish/6 bearish - genuinely two-sided crowd read, consistent with the
  unresolved-fight framing, not a reason to change the order (idea source only).
  next_earnings unchanged safe (checked prior sessions). Grade B, unchanged. Kill:
  a confirmed breakdown below 219 before it fills, or the sector rotation reverses.
- **HOOD** - 2 resting GTC buy-limit rungs, still unfilled: 15sh@108.85 (stop 102.24,
  target 125.38) + 12sh@100.70 (stop 94.09, target 117.23), staged since 2026-09-08.
  Fresh check tonight (duty: stale-staged-order review): last 114.33, well above
  both rungs - support levels (108.81, 100.68) still line up almost exactly with the
  resting prices, genuinely defended, not stale/invalidated. Structure "range/mixed"
  but EMA order clean bullish (113.31>109.02>105.46), TV strong_buy/strong_buy/buy,
  daily candle tonight a BULLISH ENGULFING off Thu/Fri's selling. next_earnings
  2026-11-04 (safe). Grade B, probe, unchanged. Kill: close below 96.59 (the 3rd
  support level) before either rung fills, invalidating the whole pullback thesis.

## Watch only (fails trend gate, tradability, or data quality tonight - do not stage)

- **VEEA** - explore-lens new name (+133.97% day, huge but see caveats). **Reject:
  data quality** - `ta.py` flags "No earnings dates found, symbol may be delisted";
  **and fails trend gate outright** - EMA9 1.88 < EMA21 2.16 < EMA50 3.06, a clean
  inverted/downtrend stack despite today's huge pop, structure "range/mixed". A
  speculative low-float pump, not a qualifying setup. Not worth re-checking absent a
  data-quality fix.
- **VNCE** (Vince Holding) - explore-lens new name (+44.27% day, $25.4M $vol).
  **Reject: fails trend gate AND structure** - EMA9 6.33 < EMA21 6.37 < EMA50 6.46
  (inverted), `key_levels.structure` explicitly "downtrend (lower highs + lower
  lows)". pos_in_20d_range 94.2% (extended). Erratic 5m tape tonight (marubozu
  buying/selling alternating every 5-10 min) - thin, choppy after-hours action, not
  tradable structure regardless of the gate. next_earnings 2026-12-08 (safe if it
  ever qualifies).
- **NTSK** (Netstreit or similar - liquid $227.8M $vol mover, +16.67% day) - EMA
  order cleanly bullish (EMA9 15.03>EMA21 14.62>EMA50 13.53), TV strong_buy/
  strong_buy/buy, next_earnings 2026-12-10 safe - **closest of tonight's new names
  to qualifying**, but `key_levels.structure` still tagged "range/mixed" and
  pos_in_20d_range 100% (fully extended, no room). Reject on structure per SOP s3c's
  strict reading (see process note above); re-check if structure flips to "uptrend"
  on a pullback-and-hold rather than a straight-line extension.
- **RUM** (Rumble, +10.88% day, $212.9M $vol) - **Reject: structure "range/mixed"**
  plus a fresh bearish signal - tonight's daily candle is a shooting star (sellers
  rejected 8.65) AT RESISTANCE 8.55, the exact opposite of a breakout confirmation.
  EMA stack not cleanly ordered either (EMA21 8.10 > EMA9 8.04). TV buy/buy/neutral.
  next_earnings 2026-11-09 (safe). Not a qualifying setup tonight.
- **ELMT** (Elmet Group, +36.5% day on confirmed $450M DoD funding news - a real,
  dated catalyst, not noise) - checked seriously given the genuine catalyst, but
  **fails on extension + structure**: pos_in_20d_range 100%, gap_pct 43.3% (already
  gapped huge before today's further move), structure "range/mixed", 5m tape
  whipsawing hard (buying/selling marubozus alternating). A real story, badly
  overextended for entry tonight. next_earnings 2026-11-16. Worth a fresh look only
  on a multi-day pullback-and-hold, not chased here.
- **SAIL / S / QLYS / TENB** - the broader cyber-rotation cluster beyond RBRK/ZS/
  CRWD, re-confirmed fresh tonight: SAIL structure "range/mixed" despite EMA9
  18.51>EMA21 18.45>EMA50 17.07 (numeric pass, same ambiguity as RBRK - see process
  note); TENB structure explicit "downtrend", fails outright; QLYS/S both "range/
  mixed" per today's continuous-leg checks, not re-run fresh tonight (no material
  time elapsed). None staged - already well covered by the RBRK/ZS/CRWD exposure the
  book already carries; adding more same-catalyst names would concentrate risk
  further into one macro story rather than diversify it.

## Macro calendar

- **2026-09-15/16 (Tue/Wed): FOMC rate decision** - the week's dominant scheduled
  event. Layered on top of two live cross-currents: the AI-slowdown/cybersecurity
  rotation (see regime note) and **the 10-year yield briefly touching 5% today** plus
  **Brent crude above $102/barrel** (both fresh bearish-for-equities pressure,
  confirmed via tonight's news sweep). Expect elevated volatility into and through
  the decision; size new risk with that in mind.
- **IOT time_stop 2026-09-15 (tomorrow)** - operational date, not macro, but the
  single most time-sensitive item for tomorrow's planning leg alongside FOMC.
  RBRK's 2 armed triggers also expire tomorrow 15:00 CT if unfired.
- No book or staged-name earnings fall within the next 30 days (ANGX/BWIN 11-03, IOT
  12-03, ZS 11-24, RBRK 12-03, HOOD 11-04) - the earnings sweep this session found
  no near-term conflicts.

## Pruned (no fresh catalyst/edge, or fully explained above)

COIN/MSTR/LITE/SMMT (all closed since the 09-09 version of this file - COIN unlucky
-$27.99, LITE unlucky -$209.13, SMMT right +$298.38, all scored in the 09-14 weekly
review; MSTR's staged rung was cancelled/expired, no fill, no thesis to carry
forward). BAND/JILL/AEO/ROIV/CRWV/SNDK/MU/ALAB/CSR (09-09 rejects, not re-checked
tonight - no fresh catalyst surfaced for any of them in tonight's news sweep; full
reasoning in `journal/archive/`). AEO reappeared tonight as a Reddit rank-climber
(136->7) - per playbook s11 crowd hype alone is not a reason to re-open a name that
crashed -11.6% on its own earnings 5 days ago with no new information since; not
re-added. SPCX (SpaceX) - tonight's #1 Reddit rank-climber (355->30) - not a
tradable US equity/ETF on this broker to my knowledge and not independently
verified tonight; noted, not pursued.

Next session (Tuesday 2026-09-15, the PLANNING leg pre-market): **(1) IOT time_stop
lands today** - re-decide extend-vs-cancel fresh using overnight/pre-market price
action, it's deep in profit (+12.8%/+2.9R) with stop already well clear, so L7
counsels against a reflexive close, but this needs an active decision. **(2) RBRK's
2 armed triggers expire today 15:00 CT** - if still unfired by then, the standing-
order count drops from 5 to 3 across 2 symbols, well below quota; have a replacement
candidate ready or accept the shortfall with reasoning. **(3) Standing-order quota is
5/3, already below target even before RBRK's possible expiry** - refill priority.
**(4) FOMC decision this week (09-15/16)** - expect volatility, size accordingly.
**(5) BWIN's governing 2-consecutive-lower-close exit is not yet evaluable (1 close
old)** - check again once tomorrow's close prints. **(6) Resolve or continue flagging
the SOP s3c structure-tag ambiguity** noted above if it recurs on a new candidate.
