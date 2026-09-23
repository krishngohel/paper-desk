# Watchlist - battle plan

> **Maintenance rule:** this file is the CURRENT battle plan, not a log. Fold new
> findings INTO the ranked entries above and delete what they supersede — never append
> a dated addendum section. History belongs in `journal/YYYY-MM.md`.

Maintained by `research` sessions. Each name: draft thesis, the EXACT numeric trigger
that turns it into a trade, planned size/stop/target/grade, and the kill condition.
The next planning leg reads this FIRST.

Updated 2026-09-23 ~17:05 CT (research session, market closed - Wednesday evening,
after the 09-23 close). Full in-place rewrite: MDB moved from "staged" to "held"
(entered 09-23 13:33Z); the FSLY/IONQ vettings below replace last night's
VKTX/INOD/BB/SOFI names.

**Regime (`ta.py --market`, fresh):** SPY 767.81, +0.36% vs EMA21, RSI14 53.0,
structure **range/mixed** (down from 773.38 last night). QQQ 741.21, +2.8% vs EMA21,
RSI14 62.8, **uptrend**. Benzinga 09-23: 10Y Treasury yield at a 19-year high on
blowout PMI, Nasdaq 100 slipped, cybersecurity bucked the selloff. Rate shock is the
live tail risk for the ARTY/MDB/TXG growth-tilted book - no reason to chase size.

## Mandate & quota status

**Mandate `consent.expires_at` 2026-09-28T17:58:50Z - 5 days runway; a human renewal
decision is needed by then.** Not halted (verified fresh via `status`).

**Standing-order quota: MET - 6 live resting buy-limits across 5 distinct symbols,
0 armed triggers:** CRWD 204.30 (`a1d8b66a`, 14sh) and CRWD 232.00 remainder
(`4bab1e47`, 3sh left of 6), TXG 58.70 (`7f98e743`), SMTC 146.91 (`41354f13`), ZS
160.75 (`4b0ad29d`), RBRK 90.15 (`4e8ee047`). No triggers live (TWLO/FIVN both
retired). No order touched this session.

## Book (4 positions, target 3-6 - inside range)

- **ARTY** 47 sh @ 79.67, now 78.67 (-$47.00 / -1.26%). s6a-governed, stop 77.05
  (2.1% below), no target, time_stop 2026-10-22. **09-23 closed 78.67 vs 79.81 - the
  FIRST lower close.** A second consecutive lower close (09-24 close below the 09-23
  official close, 78.71 per the handoff; ta.py last print 78.67) = SELL per s6a; an
  up-close resets the count. Spread 1.89% -
  TRADABLE_TIGHT_SIZE, so exit via limit near bid in the final cycle, not a sweep.
- **CRWD** 3 sh @ 231.22, now 261.66 (+$91.32 / +13.2%). Target 264.13 resting
  (`9bfc5894`, 0.9% away), stop 219.15, time_stop 2026-10-03. next_earnings 2026-12-01.
- **MDB** 2 sh @ 431.49 (entered 09-23 13:33Z, s6a), now 428.40 (-$6.18 / -0.72%).
  Stop 378.50 (11.7% below), no target, time_stop 2026-10-23. 09-23 close 428.36 vs
  427.69 prior = UP close, no lower-close count. Spread 1.84% (TIGHT_SIZE).
  `ta.py` structure tag reads "range/mixed" though EMA order passes (close 428.36 >
  EMA9 402.05 > EMA21 397.18 > EMA50 380.90); volume 0.59x 20d avg = thin (W3
  watch: thin-volume s6a entry). next_earnings 2026-12-01.
- **TXG** 15 sh @ 75.64, now 75.69 (+$0.79 / +0.07%). s6a-governed, stop 64.73,
  no target, time_stop 2026-10-15. Carries ONE lower close (per 09-23 handoff; a 2nd
  at 09-24's close below the 09-23 close = SELL). next_earnings 2026-11-05.

## Staged / armed for next session - ranked

1. **Manage the book first.** ARTY and TXG each sit one lower close from the s6a exit;
   CRWD is 0.9% under its resting target; MDB is a fresh s6a hold. Nothing new is
   worth chasing before those four are resolved at tomorrow's close.
2. **RBRK** - resting GTC buy-limit 90.15 (`4e8ee047`), unfilled since 09-16. Deep
   pullback into an old multi-touch cluster; no current holding. Kill: cybersecurity
   rotation thesis fully unwinds. next_earnings 2026-12-03.
3. **ZS** - resting GTC buy-limit 160.75 (`4b0ad29d`), unfilled since 09-16. Single-
   touch level (L8 caution). next_earnings 2026-11-24.
4. **SMTC** - resting GTC buy-limit 146.91 (`41354f13`), unfilled since 09-17, at the
   09-16 morning-star base. next_earnings 2026-11-23.
5. **Arm no above-market triggers overnight** (research stages below-market limits
   only). Tomorrow's planning leg: arm fresh triggers only for names passing rule 3c AND
   a `trade_context.py --check` that does NOT read `leader_10pp+` (L9). OKTA/PANW from
   the 09-23 handoff remain candidates subject to that check.

## Watch only (fails trend gate, L9, or lacks catalyst)

**Fresh names hunted tonight (duty 1b - screen.py relvol lens + social.py, full
`ta.py` + news workups):**
- **FSLY** (Fastly, +13.69% on $889M, rel vol 3.81x/5.16x 20d avg, spread 0.03%
  TRADABLE) - structure uptrend, close 29.65 > EMA21 24.48 > EMA50 23.31, RSI14 65.9,
  pos 100% of 20d range, next_earnings 2026-11-04 (safe). **REJECTED under L9:**
  `trade_context.py --check` reads `rel_strength_20d.leader_10pp+` (+12.39pp) -
  SIGNIFICANT, 0 wins in 16, -$1,688.53 - and its RSI 65.9 falls in the W4 60-70
  losing bucket. Catalyst is weak on the page: the move follows an investor-day and an
  X-post about Meta Muse agent traffic share (Fastly 29.3% vs Cloudflare 37.0%), while
  the only two analyst notes (DA Davidson Neutral PT $23; BofA Underperform PT $22)
  sit BELOW the 29.65 price. 5m tape ended in dojis/shooting stars under resistance
  30.69. Revisit only after a reset to a base with RS under +10pp.
- **IONQ** (momentum_scan hit, +3.83% on $3.1B, gap +7.64%, spread 0.12%) - momentum
  scan passes 3-rising-closes + close 42.55 > EMA9 39.92 > EMA21 39.77, BUT the literal
  EMA order fails rule 3c: **EMA50 40.17 > EMA21 39.77**, and `structure` reads
  "range/mixed". Catalyst is real (first on-premise quantum deployment at NVIDIA
  Research Center; real-time error-correction decoder, Benzinga 09-23) but the entry
  would be a gap-day chase into resistance 42.94 (5m shooting star + doji there) with
  risk 6.29% to the launch-low stop. Rejected on rule 3c. Revisit if close > EMA50 AND
  EMA21 > EMA50 after a base.
- **INOD** (momentum_scan hit, 3d +22.8%, risk 18.09% to launch-low stop 57.31) -
  already rejected 09-22 on rule 3c (EMA21 < EMA50); the scan flag is a scan artifact,
  not a fresh pass. Stop distance alone (18%) is disqualifying at probe scale.
- Reddit/StockTwits rank-climbers (APP/U/HIMS/TTD/VKTX/MCD/NVO/NLST, mega-cap MU/META/
  AMD/GOOGL/NVDA at top ranks) - crowd chatter, no fresh single-name structure vetted
  tonight beyond FSLY/IONQ; playbook s11: crowd hype is never a thesis.
- Relvol-lens extremes (HVII -50.9%, BLDX, GCTK, KIDZ, INNV -15.5%, NNBR +14.5% on
  $37M) - HVII/INNV are large down-gaps (no long thesis), the rest are sub-$50M-dollar-
  volume or ETF-flow relvol artifacts with no catalyst on screen; not worked up.

**Repeat rejects, unchanged reasons:** VKTX (downtrend gap day), BB (earnings
2026-09-24 event window), SOFI (range, TV strong_sell), RIOT/WDC/AAOI/CLSK/HOOD/MARA/
BMNR/ALMR/BIAF/NCI/GEMI/SOLT/BSOL/HALO/BTDR, SNDK/MUU/AVGO/LRCX/STX/COHR/AMAT/MTSI/
NVDA/INTC/CIFR, CYPH/HUT/PSIX/ADPT, DSP/ABTC/WOLF/GLOO/AKAN, MSTR/CRCL/XENE, IREN/FPS,
TWLO - carry forward; none produced a fresh catalyst tonight.

## Macro calendar

- Earnings, book + staged (all clear of any 2-day window): ARTY none (ETF), CRWD
  12-01, MDB 12-01, TXG 11-05, RBRK 12-03, ZS 11-24, SMTC 11-23. BB reports 09-24
  (not held). FSLY 11-04, IONQ 11-04 (not held).
- Macro: 10Y at a 19-year high on strong PMI - rate-shock risk to long-duration
  growth names; no scheduled Fed/CPI date flagged inside 24h from what is on screen.

## Pruned this rewrite

VKTX/INOD/BB/SOFI/COIN-type one-day-gap rejects folded into the reject list above;
MDB promoted out of "staged" (now held); TWLO retired (trigger expired unfired 09-22).

Next session (Thursday 2026-09-24, PLANNING leg pre-market): set the day's loss
budget; **(1)** ARTY/TXG second-lower-close check at tomorrow's close (ARTY < 78.71,
TXG < 75.58, the 09-23 closes per the handoff) - sell per s6a if both conditions hit; **(2)** CRWD
target 264.13 resting (0.9% above), verify a watcher miss did not skip it; **(3)**
manually cross-check every stop AND armed trigger vs 5m bars (watcher silent-miss issue);
**(4)** OKTA/PANW open-hunt candidates subject to L9 `--check`; **(5)** mandate
expires 2026-09-28T17:58Z.
