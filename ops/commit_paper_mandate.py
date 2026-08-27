"""Propose+commit the conservative long-only Alpaca paper mandate (v1 numbers).

Run from VT root with the venv active: python ..\\ops\\commit_paper_mandate.py
"""
import json
import sys
import uuid

sys.path.insert(0, "agent")

from src.live.mandate.commit import commit_mandate, save_proposal
from src.live.mandate.store import load_mandate

BROKER = "alpaca"
# v4 (user-authorized 2026-08-27): full training freedom on the paper account.
# No allowlist, no practical daily-order cap, and order/exposure limits opened to
# the full $100k paper account - position sizing is entirely the model's decision.
# What remains, by the project's definition rather than as tuning: LONG-ONLY
# (never bet against a stock) and no leverage (deploy the account, not margin).
ALLOWED = []
LIMITS = {
    "account_funding_usd": 100000.0,
    "max_order_usd": 100000.0,
    "max_total_exposure_usd": 100000.0,
    "daily_trade_cap": 100000,
    "leverage": "none",
    "instruments": ["equity", "etf"],
}
PROFILE = {
    "ordinal": 1,
    "label": "long-only-paper-v4-training",
    **LIMITS,
    "asset_classes": ["us_equity", "us_etf"],
    "min_market_cap_usd": None,
    "min_avg_daily_volume_usd": None,
    "exclude_symbols": [],
    "allowed_symbols": ALLOWED,
    "long_only": True,
    "flatten_on_halt": True,
}

proposal_id = "mp_" + uuid.uuid4().hex
save_proposal(
    {
        "type": "mandate.proposal",
        "proposal_id": proposal_id,
        "account": {"broker": BROKER, "type": "cash", "funded_by": "user"},
        "ceilings_ref": "paper_caps_v1",
        "ceilings": dict(LIMITS),
        "profiles": [PROFILE],
    }
)
result = commit_mandate(
    proposal_id=proposal_id,
    ordinal=1,
    adjustments=None,
    consent_ack=True,
    broker=BROKER,
    account_ref="alpaca_paper",
    lifetime_days=14,
    flatten_on_halt=True,
    long_only=True,
    allowed_symbols=ALLOWED,
)

m = load_mandate(BROKER)
assert m is not None, "mandate did not load back"
assert m.long_only is True
assert m.universe.allowed_symbols == tuple(ALLOWED)
assert m.hard_caps.max_order_notional_usd == 100000.0
assert m.hard_caps.max_total_exposure_usd == 100000.0
assert m.hard_caps.max_leverage == 1.0
assert m.hard_caps.max_trades_per_day == 100000
assert m.flatten_on_halt is True
print("MANDATE ACTIVE:", json.dumps(result, indent=2, default=str))
