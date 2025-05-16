import requests

def get_market_data(token):
    url = f"https://api.coingecko.com/api/v3/coins/{token.lower()}"
    try:
        data = requests.get(url).json()
        market_cap = data['market_data']['market_cap']['usd']
        rank = data['market_cap_rank']
        return f"Market Cap: ${market_cap}, Rank: {rank}"
    except:
        return "Failed to fetch market data."
