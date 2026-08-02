import requests

from toss.auth import get_access_token

EXCHANGE_RATE_URL = "https://openapi.tossinvest.com/api/v1/exchange-rate"


def get_exchange_rate(base_currency: str, quote_currency: str) -> dict:
    token = get_access_token()
    response = requests.get(
        EXCHANGE_RATE_URL,
        params={"baseCurrency": base_currency, "quoteCurrency": quote_currency},
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["result"]


if __name__ == "__main__":
    print(get_exchange_rate("USD", "KRW"))
