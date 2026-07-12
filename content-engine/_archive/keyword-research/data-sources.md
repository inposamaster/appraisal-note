# 데이터 소스 구분

Keyword Research Lab에서 사용하는 데이터 소스와 수집 방식을 정리한다.

## 요약 표

| 소스 | 용도 | v0.1 방식 | 자동화 |
|---|---|---|---|
| Google 자동완성 | 키워드 후보 발견 | 사람이 직접 확인·기록 | **금지** (스크래핑) |
| Google 연관검색어 | 검색 의도 확장 | 사람이 직접 확인·기록 | **금지** (스크래핑) |
| Google Keyword Planner | 검색량 범위·광고 단가 참고 | CSV export | 추후 Google Ads API 검토 |
| Naver 자동완성/연관검색어 | 한국어 검색 의도 | 사람이 직접 확인·기록 | **금지** (스크래핑) |
| Naver DataLab | 키워드 추세 비교·검증 | 웹 화면 수동 기록 | 추후 공식 API |
| Naver Search Ad API | 연관 키워드·광고 지표 | 수동 기록 우선 | 추후 공식 API |
| Search Console | 발행 후 노출·클릭·CTR | 사후 검증 (추후 연동) | 공식 API |

---

## Google 자동완성

- **용도**: seed keyword에서 파생되는 롱테일 후보 발견
- **방식**: 시크릿 모드 등에서 사람이 직접 입력·확인
- **저장**: `raw-data/google-autocomplete/YYYY-MM-DD.md`
- **주의**: 자동 스크래핑·대량 쿼리 금지

## Google 연관검색어

- **용도**: 검색 의도 확장, 1페이지 경쟁 관찰
- **방식**: 검색 결과 하단·관련 검색어를 사람이 직접 기록
- **저장**: `raw-data/google-related-search/YYYY-MM-DD.md`
- **주의**: 자동 스크래핑 금지

## Google Keyword Planner

- **용도**: 월간 검색량 **범위**, 광고 경쟁도, 입찰가 **참고**
- **방식**: Google Ads 계정 → Keyword Planner → CSV 다운로드
- **저장**: `raw-data/google-keyword-planner/`
- **주의**: 광고 경쟁도 ≠ SEO 경쟁도. 숫자를 절대값처럼 쓰지 않는다.
- **추후**: Google Ads API 연동 검토 (`google-keyword-planner-import.md`)

## Naver 자동완성 / 연관검색어

- **용도**: 한국어 검색 의도, VIEW·블로그 노출 확인
- **방식**: 사람이 네이버 검색창·결과를 직접 확인
- **저장**: `raw-data/naver-related-search/YYYY-MM-DD.md`
- **주의**: 구글용·네이버용 콘텐츠 전략을 구분해 판단

## Naver DataLab

- **용도**: 여러 후보 키워드의 **상대적 추세 비교** (신규 발견보다 검증)
- **방식**: v0.1은 웹 화면 수동 확인 → `raw-data/naver-datalab/`
- **추후**: DataLab API (`naver-datalab-api.md`)

## Naver Search Ad API

- **용도**: 연관 키워드, 월간 검색수, 클릭률 등 광고 지표 참고
- **방식**: v0.1은 수동 기록·export 우선
- **추후**: API 연동 (`naver-searchad-api.md`)

## Search Console

- **용도**: **발행 후** 실제 노출·클릭·CTR·순위 사후 검증
- **방식**: 사이트 연동 후 대시보드 또는 API (추후)
- **위치**: 키워드 발굴 단계가 아닌 **콘텐츠 개선** 단계

---

## raw-data → keywords.csv 통합

1. 각 소스에서 확인한 내용을 `raw-data/`에 기록
2. `keyword-scoring-model.md`로 점수 산정
3. `keywords.csv`에 통합 (확장 열 제안: `keywords-csv-extension-proposal.md`)
4. Cursor는 raw-data를 읽고 keywords.csv 정리·통합을 **보조**한다

## 보안

- API 키, OAuth 토큰, secret key → `.env` (Git 제외)
- CSV에 계정 식별 정보가 포함되면 커밋 전 확인
