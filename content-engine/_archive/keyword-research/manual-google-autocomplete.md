# Google 자동완성 — 수동 확인 절차

## 목적

seed keyword에서 파생되는 롱테일 후보를 **사람이 직접** 발견하고 기록한다.

## 사전 준비

- 시크릿 모드(또는 개인화 영향을 줄인 브라우저) 사용
- VPN·지역 설정이 평소와 다르면 메모에 기록
- 템플릿: `raw-data/google-autocomplete/_template.md`

## 절차

### 1. seed keyword 선정

`keywords.csv`의 `seed_keyword` 또는 새 아이디어에서 1개를 고른다.

예: 상속 감정평가, 증여 감정평가, 경매 감정평가

### 2. Google 검색창에 입력

- seed keyword를 **한 글자씩** 또는 **완성형**으로 입력하며 자동완성 변화를 관찰
- 나타나는 표현을 **그대로** 기록 (띄어쓰기·조사·어미 포함)

### 3. 변형도 별도 기록

| 유형 | 예시 |
|---|---|
| 띄어쓰기 차이 | 상속감정평가 / 상속 감정평가 |
| 조사·어미 | ~하는 법, ~비용, ~필요한 경우 |
| 순서 변경 | 감정평가 상속 |

### 4. 검색 상황 추정

각 후보에 대해 메모한다.

- 검색자가 어떤 **상황**인가 (상속 준비, 세금 신고, 비용 비교 등)
- **정보형 / 비교형 / 실행형** 중 어디에 가까운가

### 5. 파일 저장

- 경로: `raw-data/google-autocomplete/YYYY-MM-DD.md`
- seed가 여러 개면 같은 파일에 섹션을 나누거나, seed별 파일 분리

### 6. keywords.csv 반영

- 유망 후보 → `keyword` 열에 추가 또는 기존 행 `memo` 업데이트
- `source_hint`에 "Google 자동완성 YYYY-MM-DD" 기록
- `validation_status`는 **후보** 유지 (연관검색어·경쟁 관찰 전)

## 하지 말 것

- 자동완성 API·스크래핑 도구 사용
- 짧은 시간에 수십 개 seed를 연속 자동 입력
- AI가 제안한 키워드를 자동완성 확인 없이 검증완료 처리

## 다음 단계

- `manual-google-related-search.md`로 1페이지 경쟁 관찰
- `manual-naver-related-search.md`로 한국어 의도 교차 확인
