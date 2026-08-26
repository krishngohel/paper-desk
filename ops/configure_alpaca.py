"""Write ~/.vibe-trading/alpaca.json (0600) from paper-key env vars, then smoke-read.

Field names confirmed against agent/src/trading/connectors/alpaca/sdk.py
(AlpacaConfig / build_config / save_config): api_key, secret_key,
profile ("paper"/"live-readonly"/"live"), feed ("iex"/"sip"), timeout, readonly.

Run from VT root with the venv active:
    python ..\\ops\\configure_alpaca.py
"""
import os
import sys

sys.path.insert(0, "agent")

from src.trading.connectors.alpaca import sdk

key = os.environ["ALPACA_PAPER_KEY"]
secret = os.environ["ALPACA_PAPER_SECRET"]
if not key.startswith("PK"):
    sys.exit("REFUSING: key does not look like an Alpaca PAPER key (must start with 'PK').")

cfg = sdk.build_config(overrides={"api_key": key, "secret_key": secret, "profile": "paper"})
path = sdk.save_config(cfg)
print(f"wrote {path}")
print("status:", sdk.check_status())
print("account:", sdk.get_account_snapshot())
print("quote:", sdk.get_quote("AAPL"))
