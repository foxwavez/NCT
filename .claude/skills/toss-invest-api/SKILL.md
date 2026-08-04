---
name: toss-invest-api
description: Use when working with the Toss Securities (토스증권) Open API in this repo — issuing OAuth2 access tokens, calling quote/account/holdings/exchange-rate endpoints, or extending the Flask holdings dashboard.
---

# Toss Securities Open API Client

## Overview

`toss/` wraps the Toss Securities Open API (base URL `https://openapi.tossinvest.com`, OAuth2 Client Credentials Grant). `app.py` + `templates/index.html` is a Flask dashboard that renders holdings with a KRW/USD switch.

## Prerequisites

- `.env` (gitignored, never commit) with `TOSS_CLIENT_ID` / `TOSS_CLIENT_SECRET` from WTS 설정 > Open API.
- The caller's public IP must be registered under 허용 IP 관리 in WTS, or every request 400s with `invalid_client`.
- Client secrets are shown once at issuance — if lost, revoke and reissue rather than guessing.

## Quick Reference

| Module | Function | Endpoint |
|---|---|---|
| `toss/auth.py` | `get_access_token()` | `POST /oauth2/token` |
| `toss/quotes.py` | `get_stock(symbol)` | `GET /api/v1/stocks` |
| `toss/accounts.py` | `get_accounts()` | `GET /api/v1/accounts` |
| `toss/holdings.py` | `get_holdings(account_seq, symbol=None)` | `GET /api/v1/holdings` |
| `toss/exchange_rate.py` | `get_exchange_rate(base, quote)` | `GET /api/v1/exchange-rate` |

Endpoints requiring account context (holdings, orders, buying-power, etc.) need the `X-Tossinvest-Account: {accountSeq}` header — get `accountSeq` from `get_accounts()` first.

## Pattern for Adding a New Endpoint Client

Every client function follows the same shape as `toss/quotes.py`:

```python
import requests
from toss.auth import get_access_token

SOME_URL = "https://openapi.tossinvest.com/api/v1/..."

def get_something(...) -> dict:
    token = get_access_token()
    response = requests.get(
        SOME_URL,
        params={...},
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["result"]
```

Add `"X-Tossinvest-Account": str(account_seq)` to headers if the endpoint needs account context.

## Token Handling

`get_access_token()` issues a fresh token on every call rather than caching — intentional per project decision, since the API only allows one valid token per client at a time (reissuing invalidates the previous one) and manual reissue was judged sufficient over building expiry-tracking cache logic.

## Common Mistakes

- **Jinja2 `holdings.items`**: dicts have a built-in `.items()` method, so `{% for item in holdings.items %}` silently resolves to the method object, not the `"items"` key, raising `TypeError: 'builtin_function_or_method' object is not iterable`. Use `holdings['items']` in templates.
- **`<label>` + manual `.click()`**: don't add an `onclick="...click()"` handler on an element inside a `<label>` wrapping a checkbox — the label's native toggle plus the manual `.click()` fire twice and cancel out, making the control look unresponsive.
- **Amounts are per-item-currency by default**: `holdings.items[].currency` is native (KRW or USD); converting to a single display currency requires fetching `get_exchange_rate("USD", "KRW")` and converting each item server-side (see `app.py`'s `to_both_currencies`).
