# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-03 evening (research session, market closed). Regime: SPY uptrend
(773.17, +1.00% vs EMA21, RSI14 59.2), QQQ range/mixed (717.67, +0.56% vs EMA21,
RSI14 53.3) - both improved from yesterday's range/mixed. Today's whole-tape rally
(CRWD/SMMT/TSLA/HOOD/SNOW/MSTR/COIN all up big) traces to one wire: Fed Governor
Waller signaled a September rate-hold, sending bitcoin above $80,000 and lifting
risk assets broadly (Benzinga 2026-09-03 17:47 UTC) - a real macro catalyst, not
unrelated idiosyncratic pops.

**CRITICAL CARRYOVER - READ FIRST: the broker order-placement gate has been broken
since 2026-09-03T17:00:59 UTC** (`pending_action_unresolved`/"exact broker evidence
is missing or contradictory" on every attempt, ~20+ documented blocks). Retested once
this session (22:02 UTC) - still blocked. **TSLA's rung1 (8sh) stop was genuinely
touched today (day_low 375.23 vs stop 376.35) and the exit could NOT be executed** -
attempted repeatedly per rule 9, blocked every time; the ledger record stays open
since no sell has executed. SMMT (200sh) is also unbracketed on the sell side (no
resting target). **Tomorrow's PLANNING leg's first action must be retrying the TSLA
exit and re-resting SMMT's target before anything else**, and escalating to the
operator (a push notification was already sent) if the gate is still down - this is
a broker-side infrastructure fault, not something session-level retries can fix.

## Book (3 positions)

- **CRWD** 30 sh @ avg 211.382 (2 confirmation rungs, 210.834+211.93), last 214.97
  (+1.71% ROI). Stop 204.39/205.49 (both resting GTC), target 230.15/231.25 (both
  resting GTC). next_earnings 2026-12-01 (safe). Structure range/mixed but EMA stack
  bullish (EMA9 211.1>EMA21 207.56>EMA50 197.6).
- **SMMT** 200 sh @ avg 16.78 (confirmation entry), last 17.13 (+2.09% ROI). Stop
  16.295, target 18.24 **NOT resting** (gate-blocked since fill). next_earnings
  2026-10-19 (safe). RSI14 69.9, pos_in_20d_range 100% - fully extended after a
  Phase 3 survival-data catalyst (Akeso/ivonescimab vs Keytruda).
  Re-rest the target the moment the gate clears.
- **TSLA** 14 sh @ blended avg 382.132 (2 rungs: 8sh @376.35 stop, 6sh @373.45 stop),
  last 376.37/377.00 bid. **Rung1's stop (376.35) was touched today (day_low 375.23)
  and the exit is UNEXECUTED due to the gate lock** - see critical carryover above.
  Rung2 not breached (day_low 375.23 > stop 373.45). next_earnings 2026-10-21 (safe).

## Top candidates for tomorrow's planning leg (ranked)

Order-gate-blocked tonight - none of these were staged as broker orders; MSTR/HOOD/
COIN are armed as `triggers.jsonl` entries instead (unaffected by the broker gate,
since arming only writes a journal record - execution will still need the gate clear).

- **MSTR** (Strategy) - NEW name (duty 1b, screen.py shortlist, +17.44% on 1.72x
  volume/$6.2B mkt cap). Real catalyst: Fed-dovish/BTC>$80k macro tailwind + B. Riley
  PT raise to $175 (~21% above spot). Passes the trend gate (close>EMA21>EMA50).
  Social cross-check: Reddit rank-climber 148->17, StockTwits trending, 16 bull/4
  bear. Caveat: RSI14 67.9, pos_in_20d_range 100%, no resistance level - real chase
  risk since this is a bitcoin-price proxy, not an operating-business catalyst.
  Armed `trg-20260903-012/013` (2 rungs, 146.00/148.00, above today's 145.88 high).
  Kill: a BTC reversal or a fade back below today's high before either rung fires.
- **HOOD** - Real catalyst cluster (Scotiabank Sector Outperform init $136 PT, broad
  upgrades, Fed/BTC tailwind). Passes trend gate. Caveat: THREE separate shooting-star
  rejections at the highs this last hour (124.19/124.49/124.40) - persistent selling
  into strength, RSI14 69.1/100% range extension. Armed `trg-20260903-014` (125.10,
  above today's 125.00 high). Kill: continued rejection at the highs without a fresh
  push through 125.00.
- **COIN** - Genuine multi-touch support (3 separate defenses at 174.73 across three
  sessions, per L8 - stronger evidence than most names worked this week). Real
  catalyst: BTC rally + pending Senate crypto-vote + Coinbase board/product news.
  Passes trend gate, volume gate cleared. Armed `trg-20260903-015` (195.90, above
  today's 195.85 high). Kill: Senate vote disappoints or BTC reverses before the
  trigger fires.
- **SNOW** - Real earnings-beat catalyst (8+ analyst PT raises), but today's tape
  FADED hard off the highs: spiked to 384.56, closed ~355-356, well below vwap_today
  (364.73) - the same fading-breakout signature that killed TENB/CRWD/IREN triggers
  on 08-31 (playbook s7, volume is the lie detector). NOT re-armed tonight; needs a
  confirmed reclaim of vwap/today's range before treating as tradeable again.
- **CIFR** (bitcoin miner) - Strong social sentiment (19 bull/0 bear) and a real
  theme (crypto rally), but FAILS the binding trend gate: EMA21 (16.95) < EMA50
  (19.69) - still technically a downtrend by the s2a/s3c rule despite today's pop.
  WATCH ONLY, not staged. Needs the EMA stack to actually flip before qualifying.
- **HPE** - earnings-reaction reversal candidate from two nights ago (49.12 support,
  DELL-style whipsaw pattern) - never re-checked against a live open since. Stale;
  re-verify at tomorrow's open before treating the level as still valid.

## Macro calendar

- **2026-09-04 (Fri) 8:30am ET: NFP jobs report** - last trading day of the
  active-training directive (expires 2026-09-04); elevated volatility risk for
  anything open into it, especially the unresolved TSLA breach.
- **2026-09-11 (Fri): CPI report** and **2026-09-15/16: FOMC** - after the training
  window closes, not an immediate concern this week.
- No US market holiday before 2026-09-05 (Labor Day 2026-09-07 falls after window
  close).
- Mandate: check exact expiry wording at next planning leg (last review noted ~8
  days remaining as of 2026-09-01).

## Pruned (no fresh catalyst/edge, or fully explained above)

DUOL (closed +306.70, target hit, scored "right"), CHPT (closed -96.00, scored
unlucky), VRNS/TLYS (triggers expired/cancelled unfired, no fresh evidence),
TENB, IREN, AFRM, PYPL, ESTC, RBRK, GAP, WDAY, DKNG, PD, FROG, NTSK, FIGR, MMED,
FSLY, CRDO, AXON, ENOV, SN, WETO, KORU, EIX, PCG, HWM, TITN, FRVO, MRVL, MDB, PANW,
STDN, MRNA, PURR - quiet or no directional edge; re-add only on new evidence.

Next session (tomorrow's PLANNING leg, pre-market 2026-09-03... i.e. 2026-09-04):
FIRST resolve the TSLA breach + SMMT unbracketed target (see critical carryover),
THEN set a fresh daily loss budget per playbook s10, THEN re-check MSTR/HOOD/COIN/
SNOW/CIFR against the live opening tape - none of tonight's levels were tested by
real market liquidity, and NFP at 8:30am ET adds real volatility risk to the open.
