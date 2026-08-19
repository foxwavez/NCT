function formatKrw(value) {
  return Math.round(value).toLocaleString("ko-KR") + "원";
}

function formatUsd(value) {
  return "$" + value.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function render(showUsd) {
  document.querySelectorAll(".amount").forEach((el) => {
    const value = parseFloat(showUsd ? el.dataset.usd : el.dataset.krw);
    let text = showUsd ? formatUsd(value) : formatKrw(value);
    if (el.dataset.rate !== undefined) {
      text += ` (${el.dataset.rate}%)`;
    }
    el.textContent = text;
  });
}

const toggle = document.getElementById("currency-toggle");
toggle.addEventListener("change", () => render(toggle.checked));
render(toggle.checked);

// --- Language switch ---
// NOTE: the Toss API only returns stock names in Korean (name) and English
// (englishName) - there is no Chinese name field. In "zh" mode, stock names
// fall back to the English name; only the surrounding UI labels are Chinese.
const I18N = {
  ko: {
    pageTitle: "토스증권 보유 종목",
    heading: "보유 종목",
    totalPurchase: "매입금액",
    marketValue: "평가금액",
    profitLoss: "손익",
    colSymbol: "종목",
    colMarket: "시장",
    colQty: "수량",
    colPrice: "현재가",
    colAvgPrice: "평균매입가",
    colMarketValue: "평가금액",
    colReturn: "손익률",
  },
  en: {
    pageTitle: "Toss Securities Holdings",
    heading: "Holdings",
    totalPurchase: "Cost Basis",
    marketValue: "Market Value",
    profitLoss: "P/L",
    colSymbol: "Symbol",
    colMarket: "Market",
    colQty: "Qty",
    colPrice: "Price",
    colAvgPrice: "Avg. Cost",
    colMarketValue: "Market Value",
    colReturn: "Return",
  },
  zh: {
    pageTitle: "토스증권 持仓",
    heading: "持仓明细",
    totalPurchase: "买入金额",
    marketValue: "评估金额",
    profitLoss: "盈亏",
    colSymbol: "股票",
    colMarket: "市场",
    colQty: "数量",
    colPrice: "现价",
    colAvgPrice: "平均买入价",
    colMarketValue: "评估金额",
    colReturn: "收益率",
  },
};

function applyLanguage(lang) {
  document.documentElement.lang = lang;

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.dataset.i18n;
    el.textContent = I18N[lang][key];
  });

  document.querySelectorAll(".stock-name").forEach((el) => {
    el.textContent = lang === "ko" ? el.dataset.ko : el.dataset.en;
  });

  document.querySelectorAll("#lang-switch button").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
  });

  localStorage.setItem("lang", lang);
}

document.querySelectorAll("#lang-switch button").forEach((btn) => {
  btn.addEventListener("click", () => applyLanguage(btn.dataset.lang));
});

applyLanguage(localStorage.getItem("lang") || "ko");
