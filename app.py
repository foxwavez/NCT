from flask import Flask, render_template

from toss.accounts import get_accounts
from toss.exchange_rate import get_exchange_rate
from toss.holdings import get_holdings

app = Flask(__name__)


def to_both_currencies(amount: str, currency: str, usd_krw_rate: float) -> dict:
    value = float(amount)
    if currency == "KRW":
        return {"krw": value, "usd": value / usd_krw_rate}
    return {"krw": value * usd_krw_rate, "usd": value}


@app.route("/")
def index():
    account_seq = get_accounts()[0]["accountSeq"]
    holdings = get_holdings(account_seq)
    usd_krw_rate = float(get_exchange_rate("USD", "KRW")["rate"])

    items = []
    total_purchase = {"krw": 0.0, "usd": 0.0}
    total_market_value = {"krw": 0.0, "usd": 0.0}

    for item in holdings["items"]:
        last_price = to_both_currencies(item["lastPrice"], item["currency"], usd_krw_rate)
        avg_purchase_price = to_both_currencies(
            item["averagePurchasePrice"], item["currency"], usd_krw_rate
        )
        market_value = to_both_currencies(
            item["marketValue"]["amount"], item["currency"], usd_krw_rate
        )
        purchase_amount = to_both_currencies(
            item["marketValue"]["purchaseAmount"], item["currency"], usd_krw_rate
        )

        total_purchase["krw"] += purchase_amount["krw"]
        total_purchase["usd"] += purchase_amount["usd"]
        total_market_value["krw"] += market_value["krw"]
        total_market_value["usd"] += market_value["usd"]

        items.append(
            {
                "name": item["name"],
                "symbol": item["symbol"],
                "marketCountry": item["marketCountry"],
                "quantity": item["quantity"],
                "profitLossRate": item["profitLoss"]["rate"],
                "lastPrice": last_price,
                "averagePurchasePrice": avg_purchase_price,
                "marketValue": market_value,
            }
        )

    total_profit_loss = {
        "krw": total_market_value["krw"] - total_purchase["krw"],
        "usd": total_market_value["usd"] - total_purchase["usd"],
    }
    total_profit_loss_rate = (
        total_profit_loss["krw"] / total_purchase["krw"] if total_purchase["krw"] else 0
    )

    return render_template(
        "index.html",
        items=items,
        total_purchase=total_purchase,
        total_market_value=total_market_value,
        total_profit_loss=total_profit_loss,
        total_profit_loss_rate=total_profit_loss_rate,
        usd_krw_rate=usd_krw_rate,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
