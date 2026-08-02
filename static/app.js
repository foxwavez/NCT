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
