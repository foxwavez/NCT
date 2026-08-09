# ⌨️ 클로드 코드 CLI 단축키 레퍼런스

📅 **작성일**: 2026-08-09
🔖 **관련 이슈**: [#28](https://github.com/foxwavez/NCT/issues/28)

> Photoshop·Sketch·Figma처럼 단축키를 외워서 빠르게 작업하기 위한 클로드 코드 CLI 단축키 정리 문서입니다.

---

## 🔍 계기 — `/resume` 후 rename한 세션이 안 보이던 문제

`/rename`으로 세션 이름을 바꿨는데 `/resume` 목록에 안 보였던 이유: 피커는 기본적으로 **현재 프로젝트(레포)의 세션만** 보여줍니다. rename한 세션이 다른 프로젝트/worktree 경로에 있으면 범위를 넓혀야 보입니다.

| 키 | 동작 |
|---|---|
| 기본 | 현재 프로젝트의 세션만 표시 |
| `Ctrl+W` | 같은 레포의 다른 worktree까지 확장 |
| **`Ctrl+A`** | **머신의 전체 프로젝트 세션까지 확장** (다시 누르면 원복) |
| `Ctrl+B` | 현재 git 브랜치 기준으로만 필터 |

> ⚠️ `Ctrl+A`는 문맥에 따라 뜻이 다릅니다 — **세션 피커**에서는 "전체 프로젝트 보기", **입력창**에서는 "줄 맨 앞으로 이동"입니다.

---

## 🗂️ `/resume` 피커

| 키 | 동작 |
|---|---|
| `↑` `↓` | 세션 이동 |
| `→` `←` | 그룹 펼치기/접기 |
| `Enter` | 재개 |
| `Space` | 미리보기 |
| `Ctrl+R` | 이름 바꾸기 |
| 아무 문자 입력 | 검색/필터 모드 진입 |
| PR URL 붙여넣기 | 해당 PR을 만든 세션 바로 찾기 |

---

## ⌨️ 입력창 기본

| 키 | 동작 |
|---|---|
| `Esc` | 응답 중단 / 열린 다이얼로그 닫기 |
| `Esc` `Esc` (연속) | 입력 있으면 지우고 히스토리 저장, 없으면 되감기 메뉴 |
| `Ctrl+C` | 대기 중이면 1회=입력 지움, 2회=종료 |
| `Ctrl+D` | 종료 (0.8초 내 두 번) |
| `\` + `Enter` / `Ctrl+J` | 줄바꿈 (모든 터미널 지원) |
| `Shift+Enter` | 줄바꿈 (iTerm2 등 일부 터미널 기본 지원) |

---

## ✍️ 텍스트 편집 (readline 스타일)

| 키 | 동작 |
|---|---|
| `Ctrl+A` / `Ctrl+E` | 줄 맨 앞/끝으로 이동 |
| `Ctrl+K` / `Ctrl+U` | 커서~끝 삭제 / 커서~처음 삭제 |
| `Ctrl+W` | 앞 단어 삭제 |
| `Ctrl+Y` | 삭제한 텍스트 붙여넣기 |
| `Ctrl+R` | 입력 히스토리 역방향 검색 (다시 누르면 이전 매치로) |

---

## 🎛️ 모드 전환

| 키 | 동작 |
|---|---|
| `Shift+Tab` | 권한 모드 순환 (수동 → 편집 자동승인 → Plan → 완전자동) |
| `Option+P` | 모델 선택기 |
| `Option+T` | Extended thinking 토글 |
| `Option+O` | Fast mode 토글 |
| `Ctrl+O` | 트랜스크립트(상세 로그) 뷰어 토글 |
| `Ctrl+T` | 작업 체크리스트 토글 |
| `Ctrl+G` | 프롬프트를 외부 에디터($EDITOR)로 열기 |
| `Ctrl+B` | 현재 작업을 백그라운드로 |

---

## 💬 명령/파일 자동완성

| 키 | 동작 |
|---|---|
| `/` | 슬래시 명령/스킬 메뉴 (타이핑으로 필터) |
| `@` | 파일 경로 자동완성 |
| `Tab` / `↓` `↑` | 후보 순환, `Enter`/`Tab`으로 확정 |
| `!` | 셸 모드 진입 (결과가 컨텍스트에 포함됨) |

---

## 🖥️ Vim 모드

`/config`에서 Editor mode를 vim으로 켤 수 있음 — `h/j/k/l` 이동, `dd`/`yy`/`p` 등 표준 vim 편집·텍스트 오브젝트 대부분 지원. `~/.claude/settings.json`에서 `jj` → `<Esc>` 같은 인서트모드 리맵도 가능:

```json
{
  "editorMode": "vim",
  "vimInsertModeRemaps": { "jj": "<Esc>" }
}
```

---

## 🎨 커스터마이징

`/keybindings`로 `~/.claude/keybindings.json`을 열어서 단축키를 자유롭게 재바인딩할 수 있습니다.

---

## 🔗 참고

- 공식 문서: [keybindings](https://code.claude.com/docs/en/keybindings.md), [interactive-mode](https://code.claude.com/docs/en/interactive-mode.md)
