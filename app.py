from flask import Flask, render_template

from toss.accounts import get_accounts
from toss.holdings import get_holdings

app = Flask(__name__)


@app.route("/")
def index():
    account_seq = get_accounts()[0]["accountSeq"]
    holdings = get_holdings(account_seq)
    return render_template("index.html", holdings=holdings)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
