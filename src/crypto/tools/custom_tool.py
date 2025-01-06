from crewai_tools import BaseTool
from typing import Any
import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException
import os
from dotenv import load_dotenv
load_dotenv()



class MyCryptoTool(BaseTool):
    name: str = "get_position_with_highest_value"
    description: str = "This tool returns the ticker symbol of the asset with the highest value in the private portfolio."

    def _run(self, **kwargs: Any) -> str:
        # Implementation goes here
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        try:
            client = Client(api_key, api_secret)
        except BinanceAPIException as e:
            return f"Binance API Exception: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

        try:
            account = client.get_account()
        except BinanceAPIException as e:
            return f"Binance API Exception: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
        df = pd.DataFrame(account["balances"])
        df.free = pd.to_numeric(df.free, errors="coerce")
        current_assets = df.loc[df.free > 0]

        try:
            # Fetch balances with more than zero balance
            balances = {}
            try:
                balances = {asset['asset']: float(asset['free']) + float(asset['locked'])
                            for asset in client.get_account()['balances'] if float(asset['free']) + float(asset['locked']) > 0}
            except BinanceAPIException as e:
                return f"Binance API Exception: {e}"
            except Exception as e:
                return f"An unexpected error occurred: {e}"

            prices = {}
            try:
                prices = {price['symbol']: float(price['price']) for price in client.get_all_tickers()}
            except BinanceAPIException as e:
                return f"Binance API Exception: {e}"
            except Exception as e:
                return f"An unexpected error occurred: {e}"

            # Estimate the USDT value of each asset
            estimated_values = {}
            for asset, balance in balances.items():
                if asset == 'USDT':
                    estimated_values[asset] = balance
                elif f"{asset}USDT" in prices:
                    estimated_values[asset] = balance * prices[f"{asset}USDT"]
                elif f"USDT{asset}" in prices:  # Handle reverse pairs
                    estimated_values[asset] = balance / prices[f"USDT{asset}"]

            # Determine the asset with the highest estimated USDT value
            most_valuable_symbol = max(estimated_values, key=estimated_values.get) if estimated_values else "No Transaction"

            return most_valuable_symbol

        except BinanceAPIException as e:
            return f"Binance API Exception: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"