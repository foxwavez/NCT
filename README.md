# NCT — New Conditions Tech

🇰🇷 [한국어](#-한국어) · 🇬🇧 [English](#-english)

---

## 🇰🇷 한국어

토스증권(Toss Securities) Open API를 연동해서 실제 투자 데이터를 다루는 개인 프로젝트입니다.

### 🏦 토스증권 API 연동 워크플로우
OAuth2 토큰 발급부터 시세·계좌·보유종목·환율 조회, KRW⇄USD 통화 스위치가 달린 Flask 대시보드까지 구현했습니다.

- 📄 자세한 내용: [`docs/2026-08-04-toss-invest-workflow.md`](docs/2026-08-04-toss-invest-workflow.md)
- 🖼️ 요약 카드: [Artifact 보기](https://claude.ai/code/artifact/4b7c86b5-53ce-40cb-b579-d1aeab6fedd2)

### 🎯 SweepBuy (All-In Buy) — 진행 중
조건주문에서 파생된, 지정가에 도달하면 **계좌 가용잔고 전액**으로 자동 매수 수량을 계산하는 기능입니다. 실제 자산이 걸린 기능이라, 1회 최대 매수 상한선·재실행 제한·킬 스위치 같은 안전 스펙이 정해지기 전까지는 **드라이런(모의 계산)만** 지원합니다.

- 📄 네이밍·안전 원칙: [`docs/2026-08-19-sweepbuy-naming.md`](docs/2026-08-19-sweepbuy-naming.md)
- 🖼️ 요약 카드: [Artifact 보기](https://claude.ai/code/artifact/74b7e22d-8799-47df-b157-151928b39ae4)

### 📚 그 외 문서

| 문서 | 비고 |
|---|---|
| [`claude-code-shortcuts.md`](docs/2026-08-09-claude-code-shortcuts.md) | 클로드 코드 CLI 단축키 레퍼런스 ([Artifact](https://claude.ai/code/artifact/46264f3b-4aba-4bae-b989-676a35ede6e7)) |

---

## 🇬🇧 English

A personal project integrating the Toss Securities Open API to work with real investment data.

### 🏦 Toss Securities API Workflow
Implemented everything from OAuth2 token issuance to quote / account / holdings / exchange-rate lookups, plus a Flask dashboard with a KRW⇄USD currency switch.

- 📄 Full write-up: [`docs/2026-08-04-toss-invest-workflow.md`](docs/2026-08-04-toss-invest-workflow.md) *(Korean)*
- 🖼️ Summary card: [View Artifact](https://claude.ai/code/artifact/4b7c86b5-53ce-40cb-b579-d1aeab6fedd2)

### 🎯 SweepBuy (All-In Buy) — In Progress
A conditional-order variant: when a stock hits a target price, automatically buy as many shares as the account's **full available cash** allows. Because real money is on the line, only a **dry-run (calculation-only, no live orders)** is implemented until the safety spec — max order cap, re-trigger limit, kill switch — is defined.

- 📄 Naming & safety principles: [`docs/2026-08-19-sweepbuy-naming.md`](docs/2026-08-19-sweepbuy-naming.md) *(Korean)*
- 🖼️ Summary card: [View Artifact](https://claude.ai/code/artifact/74b7e22d-8799-47df-b157-151928b39ae4)

### 📚 Other Docs

| Doc | Note |
|---|---|
| [`claude-code-shortcuts.md`](docs/2026-08-09-claude-code-shortcuts.md) | Claude Code CLI keyboard shortcuts reference *(Korean)* ([Artifact](https://claude.ai/code/artifact/46264f3b-4aba-4bae-b989-676a35ede6e7)) |
