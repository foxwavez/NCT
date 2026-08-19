import requests

from toss.auth import get_access_token

BUYING_POWER_URL = "https://openapi.tossinvest.com/api/v1/buying-power"


def get_buying_power(account_seq: int, currency: str) -> dict:
    token = get_access_token()
    response = requests.get(
        BUYING_POWER_URL,
        params={"currency": currency},
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
    print(get_buying_power(account_seq, "USD"))
