from binance.client import Client
from dotenv import load_dotenv
import os
import numpy as np

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# For testnet
client = Client(api_key, api_secret, testnet=True)

# Get market depth
depth = client.futures_order_book(symbol='ETHUSDT')
# print(depth)


# Get historical candle data
candles = client.futures_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_1MINUTE)

# Extract the closing price
closing_prices = [float(candle[4]) for candle in candles]

# Calculate moving averages
short_rolling = np.mean(closing_prices[-5:])
long_rolling = np.mean(closing_prices[-10:])

# Simple trading logic
if short_rolling > long_rolling:
    print("Buy signal")
elif short_rolling < long_rolling:
    print("Sell signal")
