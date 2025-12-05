import requests

BINANCE_BASE = "https://api.binance.com"


def get_price(symbol: str) -> float:
    """
    Lấy giá hiện tại của symbol, ví dụ: 'BTCUSDT', 'ETHUSDT', 'LINKUSDT'.
    """
    url = f"{BINANCE_BASE}/api/v3/ticker/price"
    r = requests.get(url, params={"symbol": symbol}, timeout=5)
    data = r.json()
    return float(data["price"])


def get_24h_stats(symbol: str) -> dict:
    """
    Lấy thống kê 24h: high, low, volume, priceChangePercent,...
    """
    url = f"{BINANCE_BASE}/api/v3/ticker/24hr"
    r = requests.get(url, params={"symbol": symbol}, timeout=5)
    return r.json()
