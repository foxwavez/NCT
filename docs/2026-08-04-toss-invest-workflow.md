# 🏦 토스증권 Open API 연동 워크플로우

📅 **작성일**: 2026-08-04
🧑‍💻 **작성**: Claude Code + foxwavez
🔖 **관련 이슈**: [#9](https://github.com/foxwavez/NCT/issues/9) · [#24](https://github.com/foxwavez/NCT/issues/24) · [#25](https://github.com/foxwavez/NCT/issues/25)

> 토스증권 Open API로 토큰을 발급받고, 내 계좌·보유 종목·시세를 가져와서, 눈에 보이는 대시보드로 확인하기까지의 전체 여정을 정리한 문서입니다.

---

## 🗺️ 한눈에 보는 아키텍처

```
🔐 .env (client_id/secret)
      │
      ▼
🔑 toss/auth.py  ──────────────►  POST /oauth2/token
      │  (access_token)
      ▼
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ 📈 quotes.py │ 💼 accounts.py │ 📊 holdings.py │ 💱 exchange_rate.py │
└─────────────┴─────────────┴─────────────┴─────────────┘
      │
      ▼
🖥️ app.py (Flask)  ──────────►  templates/index.html + static/app.js
      │
      ▼
🔀 KRW ⇄ USD 스위치가 달린 보유 종목 대시보드
```

---

## 🧩 기능 카탈로그

| 아이콘 | 기능 | 파일 | 설명 |
|:---:|---|---|---|
| 🔐 | 환경변수 관리 | `.env`, `.env.example` | client_id/secret을 코드와 분리, git에서 제외 |
| 🔑 | 토큰 발급 | `toss/auth.py` | OAuth2 Client Credentials Grant로 access_token 발급 |
| 📈 | 시세 조회 | `toss/quotes.py` | 종목 심볼로 기본 정보 조회 (예: 삼성전자, NVDA, NVDY) |
| 💼 | 계좌 조회 | `toss/accounts.py` | 보유 계좌 목록과 `accountSeq` 조회 |
| 📊 | 보유 종목 조회 | `toss/holdings.py` | 계좌 기준 보유 주식·평가금액·손익 조회 |
| 💱 | 환율 조회 | `toss/exchange_rate.py` | 실시간 USD ↔ KRW 환율 |
| 🖥️ | 대시보드 | `app.py`, `templates/index.html` | Flask + Jinja2로 렌더링되는 보유 종목 화면 |
| 🔀 | 통화 스위치 | `static/app.js` | 순수 JS 토글로 전체 금액을 KRW/USD 기준 전환 |
| 📘 | 재사용 스킬 | `.claude/skills/toss-invest-api/` | 다음에 이어서 개발할 때 AI가 참고하는 레퍼런스 문서 |

---

## 🗓️ 진행 타임라인

- [x] 🔑 **토큰 발급** — WTS에서 client_id/secret 발급 → `.env` 설정 → `/oauth2/token` 호출 성공
- [x] 📈 **시세 조회 클라이언트** — `get_stock()` 구현, NVDA/NVDY 실제 호출 검증
- [x] 💼 **계좌·자산 조회 클라이언트** — `get_accounts()`, `get_holdings()` 구현
- [x] 🖥️ **Flask 대시보드** — 보유 종목을 테이블로 시각화 (React 없이 순수 서버 렌더링)
- [x] 🔀 **KRW/USD 통화 스위치** — 실시간 환율로 전체 금액 환산 후 토글 UI 추가
- [x] 🎭 **Playwright Agent CLI 연동** — 브라우저 자동화/스크린샷 스킬 추가
- [x] 📟 **상태줄 컨텍스트 표시** — `🤖 모델명 · 📊 사용률%` 상시 표시
- [x] 📘 **스킬 문서화** — 오늘 만든 워크플로우를 재사용 가능한 스킬로 정리
- [ ] 🎯 **커스텀 조건주문** — 아래 "다음 단계" 참고

---

## 🚀 다음 단계 — 커스텀 조건주문 (아이디어 정리)

토스 앱의 기본 조건주문에는 없는, **"예수금 전액 기준 자동 수량 계산"** 매수 기능을 만들고 싶어함:

1. 🎯 **조건**: 지정가에 도달하면 매수
2. 💵 **수량**: 고정값이 아니라 그 시점 **계좌 예수금(USD) 전액**으로 살 수 있는 최대 주식 수(N)를 자동 계산
3. 🔁 **배경**: NVDY 배당이 매주 들어와서 계좌 달러 잔고가 매번 달라짐 → N을 손으로 계산하기 번거로움

> 💡 토스 Open API의 네이티브 조건주문(`POST /api/v1/conditional-orders`)은 `quantity`가 고정값 필수라, 이 기능은 별도의 **가격 감시 + 예수금 조회 + 즉시 주문 실행** 서비스를 직접 만들어야 함 (`GET /api/v1/buying-power` + `POST /api/v1/orders` 조합).

---

## 🔗 참고

- 이슈: [#9](https://github.com/foxwavez/NCT/issues/9) · [#11](https://github.com/foxwavez/NCT/issues/11) · [#13](https://github.com/foxwavez/NCT/issues/13) · [#16](https://github.com/foxwavez/NCT/issues/16) · [#18](https://github.com/foxwavez/NCT/issues/18) · [#20](https://github.com/foxwavez/NCT/issues/20) · [#22](https://github.com/foxwavez/NCT/issues/22) · [#24](https://github.com/foxwavez/NCT/issues/24)
- 스킬: [`.claude/skills/toss-invest-api/SKILL.md`](../.claude/skills/toss-invest-api/SKILL.md)
