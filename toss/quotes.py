import requests

from toss.auth import get_access_token

STOCKS_URL = "https://openapi.tossinvest.com/api/v1/stocks"


def get_stock(symbol: str) -> dict:
    token = get_access_token()
    response = requests.get(
        STOCKS_URL,
        params={"symbols": symbol},
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["result"][0]


if __name__ == "__main__":
    import sys

    print(get_stock(sys.argv[1] if len(sys.argv) > 1 else "005930"))
