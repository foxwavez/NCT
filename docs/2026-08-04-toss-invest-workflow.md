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

### 🔐 환경변수 관리 — `.env`, `.env.example`
client_id/secret을 코드에서 완전히 분리. `.env`는 `.gitignore`에 등록해 git 이력에 절대 남지 않도록 하고, 값이 비어있는 `.env.example`만 커밋해서 다른 환경에서도 어떤 값이 필요한지 알 수 있게 함.

### 🔑 토큰 발급 — `toss/auth.py`
`POST /oauth2/token`에 OAuth2 **Client Credentials Grant** 방식으로 요청. 발급된 access_token은 24시간 유효하며, client당 유효 토큰이 1개뿐이라 재발급 시 이전 토큰은 즉시 무효화됨. (자동 캐싱/재발급 로직은 검토했으나, "필요할 때 재발급" 방식으로 충분하다고 판단해 단순하게 유지하기로 결정 — 이슈 #15 참고)

### 📈 시세 조회 — `toss/quotes.py`
`GET /api/v1/stocks`로 종목 심볼 기반 기본 정보 조회. 삼성전자(005930), NVDA(엔비디아), NVDY(YieldMax NVDA Option Income Strategy ETF) 3개 종목으로 실제 호출 검증 완료.

### 💼 계좌 조회 — `toss/accounts.py`
`GET /api/v1/accounts`로 보유 계좌 목록 조회. 응답의 `accountSeq`가 이후 계좌 관련 API(보유종목, 주문 등)의 `X-Tossinvest-Account` 헤더 값으로 재사용되는 진입점 역할.

### 📊 보유 종목 조회 — `toss/holdings.py`
`GET /api/v1/holdings`로 계좌 기준 보유 주식·평가금액·손익 조회. 국내(KR) 4종목 + 해외(US) 6종목 실제 데이터로 검증 완료.

### 💱 환율 조회 — `toss/exchange_rate.py`
`GET /api/v1/exchange-rate`로 실시간 USD ↔ KRW 환율 조회 (1분 주기 갱신). 대시보드의 통화 스위치 기능이 이 환율로 전체 금액을 실시간 환산하는 데 사용.

### 🖥️ 대시보드 — `app.py`, `templates/index.html`
Flask + Jinja2 서버사이드 렌더링. React를 전혀 쓰지 않고 순수 HTML/CSS/JS로 구성 — "빠르게, 눈에 보이게" 확인하는 게 목표였기 때문에 빌드 과정이 필요 없는 방식을 택함.

### 🔀 통화 스위치 — `static/app.js`
매입금액/평가금액/손익 등 모든 금액을 KRW ⇄ USD 토글 하나로 전환. 달러 보유 비중이 큰 사용자(작성자 본인)를 위해 추가된 기능. 초기 버전에서 `<label>` + 중복 `onclick`으로 토글이 두 번 발생해 아무 반응이 없어 보이는 버그가 있었고, 원인을 찾아 수정함.

### 📘 재사용 스킬 — `.claude/skills/toss-invest-api/`
다음에 이 작업을 이어갈 때 AI(Claude Code)가 매번 새로 문서를 뒤지지 않고도 API 엔드포인트, 인증 흐름, 자주 발생하는 실수를 바로 참고할 수 있도록 정리한 레퍼런스. 사람이 읽는 이 문서와 달리, AI 세션 시작 시 필요할 때만 불러와지는 문서.

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

## 🔁 다시 시작할 때 체크리스트

이어서 개발할 때 매번 확인이 필요한 것들:

1. 🌐 **허용 IP 확인** — 네트워크가 바뀌면 (예: 카페, 다른 와이파이) WTS 설정 > Open API > 허용 IP 관리에서 현재 공인 IP를 새로 등록해야 함. 등록 안 된 IP에서 호출하면 `invalid_client`로 실패.
2. 🔑 **`.env` 값 확인** — client_secret은 발급 시 한 번만 표시되므로, 유실 시 재발급 후 반드시 `.env`에 즉시 저장.
3. 🐍 **가상환경 활성화** — `source .venv/bin/activate` 후 `pip install -r requirements.txt`.
4. 🖥️ **로컬 서버 실행** — `python app.py` → `http://127.0.0.1:5001/`.

## 🔗 참고

- 이슈: [#9](https://github.com/foxwavez/NCT/issues/9) · [#11](https://github.com/foxwavez/NCT/issues/11) · [#13](https://github.com/foxwavez/NCT/issues/13) · [#16](https://github.com/foxwavez/NCT/issues/16) · [#18](https://github.com/foxwavez/NCT/issues/18) · [#20](https://github.com/foxwavez/NCT/issues/20) · [#22](https://github.com/foxwavez/NCT/issues/22) · [#24](https://github.com/foxwavez/NCT/issues/24)
- 스킬: [`.claude/skills/toss-invest-api/SKILL.md`](../.claude/skills/toss-invest-api/SKILL.md)
