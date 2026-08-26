# Hardening Report: Long-Only Paper Trading Guardrails

## Environment

- Date: 2026-08-26
- Market: closed (all orders placed after 4pm ET; day market orders queued as `accepted`, none filled)
- Broker: Alpaca paper, account `PA3Y68AGEWYB`, cash $100,000, host `https://paper-api.alpaca.markets`, feed `iex`
- Mandate: `mandate_b2741a5c548b4327bc0dca8ba1953aab`, broker `alpaca`, expires `2026-09-09T18:31:22.834290Z`, still active during this run
- Mandate hard caps: `max_order_notional_usd` 200.0, `max_total_exposure_usd` 1000.0, `max_leverage` 1.0, `max_trades_per_day` 5, `long_only` true, `allowed_symbols` AAPL/MSFT/GOOGL/AMZN/VOO/QQQ
- Root repo (`C:\Users\awsom\Documents\Projects\trading-agent`) HEAD: `fdd8f76` ("feat: long-only paper mandate commit ceremony")
- `Vibe-Trading` fork HEAD: `5bb5e68` on branch `long-only`
- CLI used throughout: `C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ..\ops\trade_cli.py <args>`, run from `Vibe-Trading`

AAPL traded around $294/share during this run (bid 294.37, ask reported as 0.0 because the market is closed and IEX has no live ask). All quantities below were sized against that price, not the ~$230 assumed in the original task brief, hence the fractional share sizes.

## Daily-counter finding (read before the per-check sections)

Before running any checks, `~/.vibe-trading/live/alpaca/trade_counter.json` did not exist. Three denied/rejected attempts had already happened earlier in the day (before this session started, at 18:21 and 18:31 UTC): one "no valid mandate on file" rejection, a `sell AAPL 5` that failed at quote-pricing (fail-closed), and a `buy TSLA 1` that also failed at quote-pricing. None of those three touched the counter.

Across this run, every ALLOWED order incremented the counter by exactly 1 (verified after each of the 5 allowed buys: counts progressed 1, 2, 3, 4, 5, one `action_id` appended per allowed order). Every DENIED or BLOCKED attempt (long_only breach, notional-cap breach, allowlist breach, halt-blocked attempts, and the eventual max_trades_per_day breach itself) left the counter unchanged. Finding: **only successfully placed (allowed) orders consume a daily-trade slot; denials of any kind, including denials by the daily-cap check itself, do not consume a slot.** This means the cap is a true ceiling on allowed activity, not on attempts, so an agent cannot be locked out for the day by making denied requests.

## CHECK 1 — In-mandate fractional buy (ALLOWED ORDER #1)

Command: `buy AAPL 0.5`

```json
{
  "status": "ok",
  "order_id": "1964a633-8b4e-4c26-9ffd-054c7191cb4c",
  "symbol": "AAPL",
  "side": "buy",
  "quantity": 0.5,
  "order_status": "OrderStatus.ACCEPTED",
  "filled_qty": "0",
  "live_action": {
    "intent_normalized": "buy $147.185 AAPL (equity)",
    "mandate_snapshot_ref": "97ea71b004dc3b5dc7f2e155bb6faa8ef86a7a6e27814ebbc56aecc4e8da97d4",
    "outcome": "accepted",
    "gate_decision": {
      "allowed": true,
      "decision": "allow",
      "checked_limits": ["mandate","expiry","halt_flag","exclude_symbols","allowed_instruments","asset_classes","max_order_notional_usd","max_total_exposure_usd","max_leverage","max_trades_per_day","account_funding_usd","universe_floors"]
    }
  }
}
```

Follow-up `orders` showed the order in `open_orders` with `status: "accepted"`, `filled_qty: "0"` (market closed, order queued, no fill expected).

Verdict: PASS.

## CHECK 2 — Audit ledger and hash chain

Command: `audit 10`

The tail of the ledger included the order_placed record from CHECK 1:

```json
{"audit_id": "la_abd7e00f014b4a519afd9e41894ab3de", "ts": "2026-08-26T22:21:26.018+00:00", "session_id": "claude-code", "kind": "order_placed", "intent_normalized": "buy $147.185 AAPL (equity)", "mandate_snapshot_ref": "97ea71b004dc3b5dc7f2e155bb6faa8ef86a7a6e27814ebbc56aecc4e8da97d4", "consent_record_ref": "alpaca_paper", "outcome": "accepted", "gate_decision": {"allowed": true, "decision": "allow", "checked_limits": [...]}, "server": "alpaca", "remote_tool": "place_order", "error": null}
```

Also visible in that tail: three earlier records from before this session (18:21-18:31 UTC) — a "no valid mandate on file" rejection, and two `order_rejected` records for `sell AAPL 5` and `buy TSLA 1` that both failed with `"error": "quantity order notional could not be priced (fail-closed)"` and `checked_limits: ["mandate","expiry","halt_flag","quote"]`. These predate this session and are noted for context on the counter finding above.

Chain verification command (run from `Vibe-Trading`):

```
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe -c "import sys; sys.path.insert(0,'agent'); from src.governance.ledger import verify_chain; from src.live.audit import audit_chain_ledger_path; print(verify_chain(audit_chain_ledger_path()))"
```

Result at this point: `ChainVerificationResult(ok=True, record_count=3, first_break=None)`. Re-run at the end of the full run (after all 9 checks): `ChainVerificationResult(ok=True, record_count=14, first_break=None)`. No `LedgerCorruptionError` at any point.

Verdict: PASS.

## CHECK 3 — Short sell denied by name (the hard constraint)

First attempt, command: `sell AAPL 5` (~$1,471.85 notional at $294.37/share).

```json
{
  "status": "blocked",
  "decision": "pause_for_reauth",
  "reason": "order breaches max_order_notional_usd",
  "live_action": {
    "kind": "breach",
    "intent_normalized": "sell $1471.85 AAPL (equity)",
    "gate_decision": {"allowed": false, "decision": "pause_for_reauth", "limit": "max_order_notional_usd", "kind": "quantitative", "limit_value": 200.0, "attempted_value": 1471.85}
  },
  "breach": {"limit": "max_order_notional_usd", "limit_value": 200.0, "attempted_value": 1471.85, "overage": 1271.85}
}
```

This denied the order, but named `max_order_notional_usd`, not `long_only` — the notional-cap check runs before the long_only check in the gate's evaluation order, and 5 shares at $294.37 breaches the $200 cap regardless of direction. Quote pricing itself resolved fine (unlike the earlier pre-session attempt, which failed at "fail-closed" quote pricing). To reach the long_only check specifically, retried with a quantity that exceeds the 0.5 shares pending (from CHECK 1) but stays under the notional cap.

Retry, command: `sell AAPL 0.6` (~$176.62 notional, under the $200 cap, but 0.6 > 0.0 shares actually held — CHECK 1's order was still unfilled/queued at this point, so held quantity was 0.0):

```json
{
  "status": "blocked",
  "decision": "deny",
  "reason": "long_only mandate: sell of 0.6 exceeds held 0.0 AAPL",
  "live_action": {
    "kind": "breach",
    "intent_normalized": "sell $176.622 AAPL (equity)",
    "gate_decision": {"allowed": false, "decision": "deny", "limit": "long_only", "kind": "instrument", "limit_value": 0.0, "attempted_value": 0.6}
  },
  "breach": {"limit": "long_only", "limit_value": 0.0, "attempted_value": 0.6, "overage": 0.6, "detail": "long_only mandate: sell of 0.6 exceeds held 0.0 AAPL"}
}
```

This is a clean DENY naming `limit: "long_only"`. No ALLOW occurred at any point in this check.

Verdict: PASS. Note for the record: a sell whose notional also happens to exceed the $200 cap will be caught by `max_order_notional_usd` before it reaches the long_only check, since the gate evaluates quantitative caps ahead of the instrument-direction check. Both checks independently deny the order; the long_only-specific deny message requires a sell that is oversized relative to holdings but not oversized relative to the notional cap, as demonstrated above.

## CHECK 4 — Over-cap buy

Command: `buy AAPL 1` (~$294.37 > $200 cap)

```json
{
  "status": "blocked",
  "decision": "pause_for_reauth",
  "reason": "order breaches max_order_notional_usd",
  "live_action": {
    "kind": "breach",
    "gate_decision": {"allowed": false, "decision": "pause_for_reauth", "limit": "max_order_notional_usd", "kind": "quantitative", "limit_value": 200.0, "attempted_value": 294.37}
  },
  "breach": {"limit": "max_order_notional_usd", "limit_value": 200.0, "attempted_value": 294.37, "overage": 94.37}
}
```

Verdict: PASS. Refusal names `max_order_notional_usd`, decision is `pause_for_reauth` (quantitative, reauth-style), `requires_reauthorization: true`.

## CHECK 5 — Allowlist breach

Command: `buy TSLA 1`

```json
{
  "status": "blocked",
  "decision": "deny",
  "reason": "TSLA is not on the mandate allowed_symbols list",
  "live_action": {
    "kind": "breach",
    "intent_normalized": "buy $327.84 TSLA (equity)",
    "gate_decision": {"allowed": false, "decision": "deny", "limit": "allowed_symbols", "kind": "universe", "limit_value": 0.0, "attempted_value": 0.0}
  },
  "breach": {"limit": "allowed_symbols", "detail": "TSLA is not on the mandate allowed_symbols list"}
}
```

TSLA's notional ($327.84) also exceeds the $200 cap, but the universe/allowlist check runs ahead of the notional check in this case, so the deny names `allowed_symbols` cleanly.

Verdict: PASS.

## CHECK 6 — Kill switch drill

Command sequence, all from `Vibe-Trading`:

1. `halt drill-test` -> `{"halted": true}`, stdout: `live kill switch tripped (broker=*, by=cli): drill-test`
2. `buy AAPL 0.1` -> blocked:
   ```json
   {"status": "blocked", "decision": "deny", "reason": "live trading halted", "live_action": {"kind": "order_rejected", "gate_decision": {"allowed": false, "decision": "deny", "checked_limits": ["mandate","expiry","halt_flag"]}, "error": "live trading halted"}}
   ```
3. Read `~/.vibe-trading/live/HALT`:
   ```json
   {"tripped_at": "2026-08-26T22:22:43.937682+00:00", "by": "cli", "reason": "drill-test"}
   ```
4. `resume` -> `{"halted": false}`, stdout: `live kill switch cleared (broker=*)`
5. `buy AAPL 0.1` -> ALLOWED (order #2 of the day):
   ```json
   {"status": "ok", "order_id": "6ff9a1ed-3bc2-46fa-859c-42afdc83f8bf", "quantity": 0.1, "order_status": "OrderStatus.ACCEPTED", "live_action": {"kind": "order_placed", "outcome": "accepted", "gate_decision": {"allowed": true, "decision": "allow"}}}
   ```
6. Raw-file trip: `New-Item -ItemType File $env:USERPROFILE\.vibe-trading\live\HALT -Force` (creates an empty file, no JSON content, bypassing `trip_halt()` entirely)
7. `buy AAPL 0.1` -> blocked with the identical `"live trading halted"` / `checked_limits: ["mandate","expiry","halt_flag"]` envelope as step 2. Confirms the gate checks file existence only, not its content.
8. `Remove-Item $env:USERPROFILE\.vibe-trading\live\HALT -Force`
9. `status` -> `{"halted": false, ...}`

Audit-ledger finding: `trip_halt()` and `clear_halt()` in `agent/src/live/halt.py` write only the `HALT` sentinel file (with `tripped_at`/`by`/`reason`) — they do not themselves write an `order_placed`/`breach`/`halt_tripped`-kind record to `audit.jsonl`. Grepping the full ledger for `halt_tripped` returns zero matches. The evidence trail for a halt event is: the sentinel file's own JSON payload (captured above), plus every subsequent order attempt made while halted, which does get logged as `kind: "order_rejected"` with `error: "live trading halted"` and `halt_flag` present in `checked_limits`. This is a real gap against the brief's expectation of a distinct `halt_tripped` audit kind — recorded honestly rather than claimed as passing on a technicality.

Verdict: PASS on functional behavior (CLI trip blocks, resume restores, raw-file trip blocks on existence alone, deletion restores normal operation — all exactly as specified). FINDING (not a blocker for this report, but worth fixing before live phase): halt/resume transitions are not independently audited by a dedicated ledger record; only their effect on subsequent order attempts is visible in the ledger.

## CHECK 7 — Daily trade cap

Starting count after CHECK 6 was 2 (orders #1 and #2). Placed three more small allowed buys (`buy AAPL 0.1` each, ~$29.44 notional) to reach exactly 5:

- Order #3: `order_id 2784ee2b-5155-4eb3-90da-f487107f5a87`, allowed, counter -> 3
- Order #4: `order_id c92a3876-b51d-4470-9de2-9daf30db6969`, allowed, counter -> 4
- Order #5: `order_id c3375736-ac91-4824-8acc-b38e1ca78818`, allowed, counter -> 5

Confirmed via `trade_counter.json`: `{"date": "2026-08-26", "count": 5, "action_ids": [5 entries]}`.

6th attempt, command: `buy AAPL 0.1`:

```json
{
  "status": "blocked",
  "decision": "pause_for_reauth",
  "reason": "order breaches max_trades_per_day",
  "live_action": {
    "kind": "breach",
    "gate_decision": {"allowed": false, "decision": "pause_for_reauth", "limit": "max_trades_per_day", "kind": "quantitative", "limit_value": 5.0, "attempted_value": 6.0}
  },
  "breach": {"limit": "max_trades_per_day", "limit_value": 5.0, "attempted_value": 6.0, "overage": 1.0}
}
```

This denial itself did not increment the counter (confirmed unchanged at 5 afterward), consistent with the daily-counter finding above.

Verdict: PASS. `max_trades_per_day` named exactly, decision `pause_for_reauth`, `requires_reauthorization: true`.

## CHECK 8 — Position/exposure sanity

`positions`:
```json
{"status": "ok", "profile": "paper", "is_paper": true, "positions": []}
```
Empty because the market is closed and none of the day's queued market orders have filled yet.

`account`:
```json
{
  "status": "ok",
  "account": {
    "account_number": "PA3Y68AGEWYB",
    "status": "AccountStatus.ACTIVE",
    "currency": "USD",
    "cash": "100000",
    "equity": "100000",
    "buying_power": "399719.6",
    "portfolio_value": "100000",
    "trading_blocked": false
  }
}
```
Cash/equity/portfolio_value are unchanged from the $100,000 starting balance since nothing has filled. Buying power dropped from $400,000 to $399,719.60, reflecting the reserved margin held against the 5 open unfilled orders (0.5 + 0.1 + 0.1 + 0.1 + 0.1 = 0.9 AAPL shares reserved at ~$294.37, roughly matching the ~$280.4 difference once Alpaca's margin multiplier is applied).

`orders` showed all 5 allowed orders still open with `status: "accepted"`, `filled_qty: "0"`, all AAPL buys.

Verdict: PASS (sane and consistent with a closed market and zero fills).

## CHECK 9 — Mandate-edit invariant (policy, not code)

`~/.vibe-trading/live/alpaca/mandate.json` was read multiple times during this run but never written to by this agent. This is a policy statement, not a code guarantee: Claude Code (the driving agent running this checklist) has full filesystem access on this machine and could technically edit or delete the mandate file. The only things preventing that are (1) this agent's alignment/instructions never to do so, and (2) the fact that all keys in play are Alpaca paper-trading keys with no real capital exposure.

This matches the brief's item 5 exactly: unlike Vibe-Trading's internal trading agent, which has no filesystem write tool at all (enforced and tested by `test_no_set_mandate_tool.py`), the driving agent here (Claude Code) is not structurally prevented from writing `mandate.json`. Nothing in this run attempted such a write, and no instruction in this task asked for one. Before any live-money phase, this must be closed structurally, for example by running the gate process under a separate OS account that owns `~/.vibe-trading` and to which the driving agent's account has no write access, plus broker-side account-level limits as a second independent layer that doesn't depend on any local file at all.

Verdict: PASS as a policy statement (no mandate edit occurred), with the honest limitation recorded as required. Not closed structurally.

## Go/No-Go Summary

All 9 checks passed on their functional requirements:

1. In-mandate fractional buy: PASS
2. Audit record + hash chain integrity: PASS
3. Short sell denied naming `long_only` (the hard constraint): PASS
4. Over-cap buy denied naming `max_order_notional_usd`: PASS
5. Off-allowlist buy denied naming `allowed_symbols`: PASS
6. Kill switch (CLI trip, resume, raw-file trip, raw-file clear): PASS, with an audit-ledger gap noted (no dedicated `halt_tripped` record kind)
7. Daily trade cap denied naming `max_trades_per_day` at exactly the 6th allowed-order attempt: PASS
8. Position/exposure sanity: PASS
9. Mandate-edit invariant: PASS as policy, explicitly not closed structurally

No ALLOW occurred where a DENY was required at any point in this run. The gate correctly refused every out-of-mandate order regardless of which specific limit was breached first, and the refusal always named the actual limit that fired (never a generic error).

Two items should be tracked before this progresses past paper evaluation, neither of which blocks starting the paper period:

- Halt/resume transitions are not independently recorded in the audit ledger as a distinct event; only their downstream effect on blocked order attempts is visible. Worth adding a dedicated `halt_tripped`/`halt_cleared` audit record so the ledger alone tells the full halt story without cross-referencing the sentinel file.
- The mandate-file-write invariant rests entirely on this agent's alignment, not on filesystem permissions. Paper-only keys make the current blast radius zero, which is why it is acceptable to proceed with the paper evaluation now, but this must be closed structurally (separate OS account or equivalent) before any live-money phase.

Go/No-Go: GO for starting the multi-month paper evaluation period. The core guardrail — long_only enforcement — held cleanly under direct adversarial pressure and named itself correctly. All quantitative caps (order notional, total exposure headroom implied by notional cap, daily trade count) and the structural allowlist check fired correctly and named themselves correctly. The kill switch stopped trading both through its own CLI and through a raw file-existence trip, which is the mechanism a human or watchdog process would actually use in an emergency. The two open findings above are hardening work for the live-money gate, not reasons to delay paper trading.

## Addendum: final whole-branch review (same day)

After this report was written, a final whole-branch review of all five fork commits raised two Important findings, both fixed and re-verified in commit 49efd75 (228/228 tests passing):

1. Mandate renewal safety ratchet. A recommit through any surface other than ops/commit_paper_mandate.py previously produced long_only=false and an empty allowlist, because the built-in propose flow never sets those fields. commit_mandate now inherits the prior mandate's long_only and allowed_symbols when a recommit is silent about them. An explicit parameter or profile value still wins; only silence inherits. The 2026-09-09 renewal is therefore safe through any commit surface.
2. Paper cancel auditing. Cancels on the gated paper profile are now written to the audit ledger, matching live behavior. Cancels remain ungated by design (risk-reducing).

The review also confirmed end to end: no order path from trade_cli.py reaches a broker write without passing check_mandate including the long-only and allowlist checks; the re-authorization path cannot waive a structural denial (every placement re-runs all checks); no key material exists anywhere in either repo's history.
