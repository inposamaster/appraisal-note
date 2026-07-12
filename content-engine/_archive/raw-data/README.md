# Raw Data 저장소

키워드 리서치에서 사람이 직접 확인하거나, 공식 도구에서 export한 **원본 데이터**를 보관한다.

## 원칙

- 자동 스크래핑 데이터는 저장하지 않는다.
- API 키·OAuth 토큰·secret key는 이 폴더에 넣지 않는다. (`.env` 사용)
- 파일명에 날짜를 포함한다. 예: `2026-07-01.md`, `2026-07-01-seed-상속감정평가.csv`

## 폴더별 용도

| 폴더 | 내용 |
|---|---|
| `google-autocomplete/` | Google 자동완성 수동 기록 |
| `google-related-search/` | Google 연관검색어·1페이지 경쟁 관찰 |
| `google-keyword-planner/` | Keyword Planner CSV export |
| `naver-related-search/` | 네이버 자동완성·연관검색어·VIEW 관찰 |
| `naver-datalab/` | DataLab 웹 화면 확인 기록 |
| `naver-searchad/` | Search Ad 수동 기록·export |

## 통합

여러 출처의 데이터를 확인한 뒤 `keywords.csv`에 반영한다. 통합 방법은 `keyword-research/keyword-scoring-model.md`와 `keyword-research/keywords-csv-extension-proposal.md`를 참고한다.
