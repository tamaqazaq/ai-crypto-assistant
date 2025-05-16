import requests

def get_news(token):
    print("Calling CoinGecko for description...")
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{token.lower()}"
        data = requests.get(url, timeout=5).json()
        description = data.get("description", {}).get("en", "")
        result = "Description:\n" + description[:300] + "..."
        print("Got description from CoinGecko")
        return result
    except Exception as e:
        print(f"Failed to fetch description: {e}")
        return "Failed to fetch description"
