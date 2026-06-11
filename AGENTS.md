# AGENTS.md

## 커밋 규칙

### 형식
```
<type>: <문제이름>
```

- 한국어로 작성
- 문제이름은 띄어쓰기 없이 붙여쓰기
- 문제 하나당 커밋 하나 (여러 문제는 각각 분리)
- Co-Authored-By, Generated with Codex 등 서명 추가 금지

### Type

| Type | 사용 상황 |
|----------|----------|
| feat | 문제를 완벽히 풀어서 제출 |
| wip | 풀이 중인 코드 중간 저장 |
| fix | 이미 올린 코드의 오류 수정 |
| refactor | 기능 변화 없이 코드 개선 |
| docs | README 등 문서만 수정 |
| rename | 파일/폴더명 변경 |
| remove | 불필요한 파일 삭제 |

### 예시
```
feat: 로또의최고순위와최저순위
fix: 설탕배달
refactor: 완주하지못한선수
```

## 브랜치 규칙
```
feat/<github사용자명소문자>-<yyMMdd>
```
예: `feat/jexists-260420`

## 파일/폴더 규칙
- 폴더: `yyMMdd_<BJ|PMS>_<문제이름>` (예: `260420_PMS_로또의최고순위와최저순위`)
- 파일: `<이름>_<문제이름>.py` (예: `jexists_로또의최고순위와최저순위.py`)
- 폴더가 없으면 생성, 있으면 그대로 사용 (발제자든 풀이자든 먼저 필요한 사람이 생성)

## Issue 규칙 (발제자)
- 제목: `[yyMMdd] 문제이름`
- 본문 템플릿:
  ```
  - 일시:
  - 레벨:
  - 정답률:
  - 링크:
  ```
- `gh issue create` 사용
- 문제 여러 개면 Issue도 여러 개 (문제당 1개)

## PR 규칙
- 제목: `Related to #N` 형식 (문제가 여러 개면 `Related to #N, #M`)
- 본문에 **`Related to #N`** 포함 (`Closes`, `Fixes`, `Resolves` 금지)
- 이유: 팀원 모두 머지 전에 Issue가 자동으로 닫히면 안 됨
- `gh pr create` 사용
- 브랜치는 날짜당 1개, PR도 날짜당 1개 (여러 문제도 한 PR에 커밋 여러 개로 처리)
- **발제자가 아닌 경우**: PR 생성 후 즉시 머지하고 브랜치 삭제
  - `gh pr merge <PR번호> --merge` 로 머지
  - `git branch -d <브랜치명>` 으로 로컬 브랜치 삭제
  - `git push origin --delete <브랜치명>` 으로 원격 브랜치 삭제

## Issue close
- 모든 팀원의 PR이 머지된 뒤, 발제자가 수동으로 close (`gh issue close N`)

## 세션 시작 시 자동 확인

대화 세션이 시작되면 아래를 자동으로 실행하고 결과를 요약 보고한다:

1. `git fetch origin` — 원격 커밋 확인
2. 로컬 main과 origin/main 차이 확인 — 새 커밋 있으면 `git pull` 실행
3. pull로 받아온 커밋 목록을 표로 표시 (merge 커밋 제외, 실제 작업 커밋만)
4. `gh issue list --state open` — 오늘 날짜(yyMMdd) 기준 풀어야 할 문제 있으면 알림

새로운 게 없으면 조용히 넘어간다 (불필요한 보고 금지).

## 기본 동작

사용자 지시가 짧아도 아래 기본 동작을 수행합니다. 중간에 애매한 부분(Issue 번호 등)만 물어봅니다.

### 발제자 동작
트리거: "Issue 만들어줘", "발제 준비해줘", "오늘 발제자야"

1. 문제 정보 확인 (레벨, 정답률, 링크) — 누락 시 사용자에게 물어봄
2. `gh issue create` — 제목 `[yyMMdd] 문제이름`, 본문 템플릿 채워서 생성
3. 문제가 여러 개면 Issue도 여러 개 생성

세션 후 트리거: "Issue close 해줘", "마무리해줘"
- `gh issue close N` 실행 (번호는 사용자가 지정하거나 열려있는 Issue 목록에서 선택)

### 풀이자 동작
트리거: "커밋해줘", "푼 문제 올려줘", "PR 만들어줘"

1. `git status`로 변경된 파일 확인
2. `git checkout main && git pull origin main` — 최신 상태 동기화
3. 현재 브랜치가 `feat/<이름>-<yyMMdd>` 형식이 아니면 새로 생성
4. 파일별로 개별 staging + 커밋 (문제 하나 = 커밋 하나)
   - 커밋 메시지: `feat: <문제이름>` (파일명에서 추출)
5. `git push origin <브랜치>`
6. Issue 번호를 사용자에게 물어본 후 `gh pr create` 실행
   - 제목: `Related to #N` (문제가 여러 개면 `Related to #N, #M`)
   - 본문: `Related to #N` (문제가 여러 개면 각 줄에 하나씩)
7. PR 생성 후 즉시 머지 및 브랜치 삭제
   - `gh pr merge <PR번호> --merge`
   - `git branch -d <브랜치명>` (로컬)
   - `git push origin --delete <브랜치명>` (원격)
8. 작업 요약을 사용자에게 보여줌 (어떤 커밋이 생겼고 어떤 PR이 만들어졌는지)

### 공통 규칙
- 작업 시작 전 현재 git 상태를 먼저 확인하고 요약 보고
- 파괴적 명령(force push, reset --hard 등)은 실행 전 사용자 확인
- `git add .` 또는 `git add -A` 사용 금지 (파일 명시)
- 커밋 메시지에 Co-Authored-By, Generated with Codex 등 서명 절대 추가 금지

## 스마트 동작 (gh 조회 후 판단)

### 풀이자: Issue 번호 자동 매칭
커밋/PR 트리거 시 사용자에게 Issue 번호를 묻기 전에:
1. `gh issue list --state open` 실행
2. 작업한 파일명(문제이름)과 Issue 제목 매칭 시도
3. 매칭되면 "Issue #N과 연결할까요?" 제안 (번호 물어보지 않음)
4. 매칭 안 되거나 여러 개면 사용자에게 확인 요청

### 풀이자: 파일/폴더명 자동 정리
커밋 트리거 시, 파일/폴더가 규칙에 안 맞으면 자동으로 정리:

1. 파일 내용 확인 (주석, 문제 링크 등)하여 어떤 문제인지 파악
2. `gh issue list`로 열린 Issue와 매칭하여 정확한 문제이름 확정
3. 아래 형식과 다르면 rename/이동:
   - 폴더: `<yyMMdd>_<BJ|PMS>_<문제이름>/`
   - 파일: `<github사용자명소문자>_<문제이름>.py`
4. 사용자 이름은 `git config user.name` (소문자 변환)
5. 플랫폼은 Issue 본문의 링크로 판단:
   - `acmicpc.net` → `BJ`
   - `programmers.co.kr` → `PMS`
6. 변경 전 사용자에게 확인: "`lotto.py` → `jexists_로또의최고순위와최저순위.py`로 이동할게요"
7. 확인 후 `git mv`로 이동 (feat 커밋에 포함, 별도 rename 커밋 불필요)

### 발제자: Issue 생성 전 중복 체크
"Issue 만들어줘" 트리거 시:
1. `gh issue list --state open` 로 오늘 날짜(yyMMdd)의 Issue 먼저 확인
2. 같은 문제 Issue가 이미 있으면 사용자에게 알림
3. 없으면 문제 정보(레벨, 정답률, 링크) 질문 후 생성

### 발제자: 마무리 자동 검증
"마무리해줘" / "Issue close 해줘" 트리거 시:
1. `gh issue list --state open` 로 열린 Issue 확인
2. 각 Issue에 대해 연결된 PR 상태 확인 (`gh pr list --search "#N"`)
3. **모든 PR이 머지된 Issue만** close 후보로 제안
4. 미머지 PR이 있으면 경고 후 close 보류 ("PR #5가 아직 머지 안 됨")

### 상태 조회 질문
사용자가 "오늘 뭐 해야 해?", "내 PR 상태 봐줘" 같은 질문을 하면:
- 오늘 날짜(yyMMdd) 포함한 열린 Issue 목록 조회
- 내 브랜치(`feat/<이름>-<오늘날짜>`) 존재 여부 확인
- 내가 만든 PR의 상태 확인 (`gh pr list --author @me`)
- 다음에 할 액션 제안

## Imported Claude Cowork project instructions
