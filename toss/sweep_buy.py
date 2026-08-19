"""SweepBuy (All-In Buy) -- DRY RUN ONLY.

Calculates what a conditional "buy with all available cash" order WOULD do
if `symbol` traded at `trigger_price`. This module intentionally does NOT
place any real order.

Do not add a real POST /api/v1/orders call here until the safety spec is
decided and documented: max order cap, re-trigger limit, and kill switch
are all still undefined. See docs/2026-08-19-sweepbuy-naming.md (issue #30)
before extending this into a live-executing feature.
"""

import math

from toss.accounts import get_accounts
from toss.buying_power import get_buying_power
from toss.quotes import get_stock


def plan_sweep_buy(symbol: str, trigger_price: float, currency: str = "USD") -> dict:
    """Return the DRY-RUN plan for a SweepBuy of `symbol` at `trigger_price`.

    quantity is floor(available_cash / trigger_price). No order is placed.
    """
    account_seq = get_accounts()[0]["accountSeq"]
    buying_power = float(get_buying_power(account_seq, currency)["cashBuyingPower"])
    quantity = math.floor(buying_power / trigger_price)
    stock = get_stock(symbol)

    return {
        "dry_run": True,
        "symbol": symbol,
        "name": stock["name"],
        "trigger_price": trigger_price,
        "currency": currency,
        "available_cash": buying_power,
        "quantity": quantity,
        "estimated_cost": round(quantity * trigger_price, 2),
    }


if __name__ == "__main__":
    import sys

    symbol = sys.argv[1] if len(sys.argv) > 1 else "NVDY"
    trigger_price = float(sys.argv[2]) if len(sys.argv) > 2 else 10.0
    print(plan_sweep_buy(symbol, trigger_price))
