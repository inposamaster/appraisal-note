# 콘텐츠 제작 워크플로

## 전체 흐름

```
seed keyword 선정
    ↓
AI로 롱테일 후보 생성
    ↓
사람이 무료 도구로 검증
    ↓
keywords.csv에 기록
    ↓
priority 상위 3개만 초안 생성
    ↓
content/posts에 draft = true 저장
    ↓
quality-checklist로 사람이 검수
    ↓
표·요약 박스·이미지 자리표시자 추가
    ↓
검수 완료 후 draft = false
    ↓
git commit → GitHub Pages 배포 확인
    ↓
Search Console 데이터 축적 후 제목·글 개선
```

---

## 단계별 상세

### 1. seed keyword 선정

감정평가 블로그 씨앗 키워드 예시:

- 감정평가, 상속 감정평가, 증여 감정평가, 경매 감정평가
- 부동산 공부, 토지이용계획확인서, 등기사항전부증명서
- 건축물대장, 공시지가, 부동산 시세

`keywords.csv`의 `seed_keyword` 열에 기록한다.

### 2. AI로 롱테일 후보 생성

Cursor에게 씨앗 키워드 기반 롱테일 후보를 요청할 수 있다.

- AI 제안은 **후보**일 뿐이다.
- 검색량·단가를 숫자로 단정하지 않는다.
- 후보는 `keywords.csv`에 `validation_status: 후보`로 추가한다.

### 3. 사람이 무료 도구로 검증

`keyword-research-guide.md` 참고.

- Google 자동완성, 관련 검색어
- Google Keyword Planner
- 네이버 데이터랩
- 검색 결과 1페이지 경쟁도 관찰

### 4. keywords.csv에 기록

| 업데이트 항목 | 내용 |
|---|---|
| validation_status | 검증중 → 검증완료 (또는 보류) |
| source_hint | 확인한 도구 |
| competition_note | 1페이지 관찰 메모 |
| cpc_note | 단가 가능성 질적 메모 |

### 5. priority 상위 3개만 초안 생성

v0.1 테스트 배치 규칙:

- `priority` 1, 2, 3만 초안 생성 대상
- `validation_status`가 **검증완료**인 것만 진행
- 한 번에 1개씩 생성·검수·발행하는 것을 권장

### 6. 초안 저장

- `article-generation-prompt.md` 프롬프트를 Cursor에 붙여넣기
- 출력: `content/posts/{target_slug}.md`
- **반드시 `draft: true`**
- `keywords.csv`의 `status`를 `drafted`로 변경

### 7. 품질 검수

`quality-checklist.md`를 인쇄하거나 복사해 항목별로 검수한다.

- 보완 필요 항목은 글을 수정
- 모든 항목 통과 시 발행 승인

### 8. 시각 요소 보강

`visual-elements-guide.md` 참고.

- 비교 표, 요약 박스, 체크리스트 추가
- 이미지 자리표시자 + alt/caption 초안

### 9. 발행

1. `draft: false`로 변경
2. `keywords.csv`의 `status`를 `published`로 변경
3. `git add` → `git commit` → `git push`
4. GitHub Actions 배포 완료 확인
5. 라이브 URL에서 최종 확인

### 10. 사후 개선

Search Console 연동 후 (추후):

- 노출·클릭 데이터 확인
- 제목·description·본문 첫 문단 개선
- `keywords.csv`의 `memo`에 개선 이력 기록

---

## 상태값 정리

### keywords.csv — validation_status

| 값 | 의미 |
|---|---|
| 후보 | AI 또는 아이디어 단계 |
| 검증중 | 사람이 도구로 확인 중 |
| 검증완료 | 초안 생성 가능 |
| 보류 | 당분간 작성 안 함 |

### keywords.csv — status

| 값 | 의미 |
|---|---|
| planned | 계획만 됨 |
| drafted | 초안 생성됨 (draft = true) |
| reviewed | 검수 완료, 발행 대기 |
| published | 발행됨 (draft = false) |
| skipped | 작성 안 함 |

---

## v0.1에서 하지 않는 것

- 대량 글 자동 생성
- 자동 발행 GitHub Actions
- 이미지 자동 생성
- 검색량·단가 숫자 단정

---

## 관련 파일

| 파일 | 용도 |
|---|---|
| `README.md` | 엔진 개요 |
| `keywords.csv` | 키워드 관리 |
| `keyword-research-guide.md` | 키워드 검증 |
| `article-generation-prompt.md` | 초안 생성 |
| `quality-checklist.md` | 발행 전 검수 |
| `visual-elements-guide.md` | 시각 요소 |
