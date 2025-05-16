import requests

def get_price(token):
    mapping = {
        "Bitcoin": "BTCUSDT",
        "Ethereum": "ETHUSDT",
        "Solana": "SOLUSDT",
    }
    symbol = mapping.get(token, "BTCUSDT")
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        price = requests.get(url).json().get("price")
        return f"{symbol}: {price} USD"
    except:
        return "Failed to fetch price."
