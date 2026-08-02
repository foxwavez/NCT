import requests

from toss.auth import get_access_token

ACCOUNTS_URL = "https://openapi.tossinvest.com/api/v1/accounts"


def get_accounts() -> list:
    token = get_access_token()
    response = requests.get(
        ACCOUNTS_URL,
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["result"]


if __name__ == "__main__":
    print(get_accounts())
