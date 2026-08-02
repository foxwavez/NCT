import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_URL = "https://openapi.tossinvest.com/oauth2/token"


def get_access_token() -> str:
    client_id = os.environ["TOSS_CLIENT_ID"]
    client_secret = os.environ["TOSS_CLIENT_SECRET"]

    response = requests.post(
        TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


if __name__ == "__main__":
    print(get_access_token())
