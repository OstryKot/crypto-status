import requests
import time

# Symbolami dla kryptowalut na Binance
CRYPTO_SYMBOLS = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "SOLUSDT", "BNBUSDT"]
OUTPUT_FILE = "/tmp/crypto_prices.txt"  # Plik używany przez bumblebee-status

# Kod Unicode dla ikon kryptowalut
ICON_MAP = {
    "BTC": "\uf15a",  # Bitcoin
    "ETH": "\uea99",  # Ethereum
    "XRP": "\uea9a",  # Ripple
    "SOL": "\uea91",  # Solana
}

def fetch_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    prices = {}
    try:
        for symbol in CRYPTO_SYMBOLS:
            response = requests.get(url, params={"symbol": symbol})
            response.raise_for_status()
            data = response.json()
            prices[symbol[:-4]] = float(data["price"])  # Usuwamy "USDT" z symbolu
    except Exception as e:
        print(f"Error fetching prices: {e}")
    return prices

def write_prices_to_file(prices):
    try:
        with open(OUTPUT_FILE, "w") as file:
            for symbol, price in prices.items():
                icon = ICON_MAP.get(symbol, symbol)
                file.write(f"{symbol}: {price:.2f} | ")
#                file.write(f"{icon}: {price:.2f} | ")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    while True:
        prices = fetch_prices()
        write_prices_to_file(prices)
        time.sleep(60)  # Aktualizacja co minutę

if __name__ == "__main__":
    main()

