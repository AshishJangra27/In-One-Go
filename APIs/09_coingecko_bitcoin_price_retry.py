"""
09_coingecko_bitcoin_price_retry.py
----------------------------------
Fetches Bitcoin price from CoinGecko with retry logic.
"""

import time
import requests

coingecko_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
max_retries = 3
retry_delay = 2  # seconds

for attempt in range(1, max_retries + 1):
    try:
        print(f'Attempt {attempt}: Fetching Bitcoin price...')
        response = requests.get(coingecko_url, timeout=10)
        response.raise_for_status()
        price_data = response.json()
        bitcoin_price = price_data.get('bitcoin', {}).get('usd')
        print(f'Success! Current Bitcoin Price: ${bitcoin_price:,}')
        break  # Exit loop on success
    except Exception as e:
        print(f'Attempt {attempt} failed: {e}')
        if attempt < max_retries:
            print(f'Retrying in {retry_delay} seconds...')
            time.sleep(retry_delay)
        else:
            print('All retry attempts failed.')
