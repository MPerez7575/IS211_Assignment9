# Source: https://finance.yahoo.com/quote/AAPL/history?p=AAPL

import requests
import json
from datetime import datetime

SYMBOL = "AAPL"        
RANGE = "3mo"          
INTERVAL = "1d"        

# URL
URL = f"https://query1.finance.yahoo.com/v8/finance/chart/{SYMBOL}?range={RANGE}&interval={INTERVAL}"

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
data = response.json()

timestamps = data["chart"]["result"][0]["timestamp"]
closes = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]

print(f"{'Date':<15} {'Close Price':>15}")
print("-" * 35)

for ts, close in zip(timestamps, closes):
    if close is not None:
        date = datetime.fromtimestamp(ts).strftime("%b %d, %Y")
        print(f"{date:<15} {close:>15.2f}")
