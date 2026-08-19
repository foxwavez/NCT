import requests

from toss.auth import get_access_token

STOCKS_URL = "https://openapi.tossinvest.com/api/v1/stocks"


def get_stock(symbol: str) -> dict:
    return get_stocks([symbol])[0]


def get_stocks(symbols: list) -> list:
    token = get_access_token()
    response = requests.get(
        STOCKS_URL,
        params={"symbols": ",".join(symbols)},
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["result"]


if __name__ == "__main__":
    import sys

    print(get_stock(sys.argv[1] if len(sys.argv) > 1 else "005930"))
