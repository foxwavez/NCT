import requests

from toss.auth import get_access_token

HOLDINGS_URL = "https://openapi.tossinvest.com/api/v1/holdings"


def get_holdings(account_seq: int, symbol: str | None = None) -> dict:
    token = get_access_token()
    params = {"symbol": symbol} if symbol else {}
    response = requests.get(
        HOLDINGS_URL,
        params=params,
        headers={
            "Authorization": f"Bearer {token}",
            "X-Tossinvest-Account": str(account_seq),
        },
    )
    response.raise_for_status()
    return response.json()["result"]


if __name__ == "__main__":
    from toss.accounts import get_accounts

    account_seq = get_accounts()[0]["accountSeq"]
    print(get_holdings(account_seq))
