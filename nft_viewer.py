import requests

def fetch_recent_sales(limit=10):
    url = "https://api.opensea.io/api/v2/events"
    headers = {
        "accept": "application/json",
    }
    params = {
        "event_type": "sale",
        "limit": limit,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        events = response.json().get("asset_events", [])

        if not events:
            print("Нет свежих продаж NFT.")
            return

        print(f"\n🖼 Последние {limit} продаж NFT на OpenSea:\n")
        for event in events:
            nft = event.get("nft", {})
            name = nft.get("name", "Без названия")
            collection = nft.get("collection", {}).get("name", "Неизвестная коллекция")
            permalink = nft.get("opensea_url", "")
            price_info = event.get("payment", {})
            price = float(price_info.get("quantity", "0")) / 10 ** int(price_info.get("decimals", 0))
            symbol = price_info.get("symbol", "ETH")

            print(f"🔹 {name} из коллекции {collection} → {price:.4f} {symbol}")
            print(f"   {permalink}\n")

    except Exception as e:
        print(f"❌ Ошибка при получении данных: {e}")

if __name__ == "__main__":
    fetch_recent_sales()
