# Keyword Research Lab v0.1

감정평가·부동산·상속·증여·경매 주제의 **롱테일 키워드를 안전하게 발굴·검증**하기 위한 연구 공간입니다.

## 목표

다음 조건에 가까운 키워드를 찾는다.

- 검색량이 **0은 아닌** 키워드
- SEO 경쟁이 **상대적으로 약한** 키워드
- 광고 단가가 **받쳐줄 가능성**이 있는 키워드
- 검색 **의도가 분명한** 롱테일 키워드

## 핵심 원칙

### 후보 생성과 검증을 분리한다

| 단계 | 담당 | 산출물 |
|---|---|---|
| 후보 생성 | AI 제안, 자동완성·연관검색어 관찰 | raw-data/, 아이디어 목록 |
| 검증 | 사람 (+ 공식 도구) | raw-data/ 기록, keywords.csv 업데이트 |

**AI가 제안한 키워드는 후보일 뿐이다.** 실제 검색 흔적은 사람이 직접 확인해야 한다.

### 안전한 수집

- Google·Naver 검색결과를 **무단 스크래핑하지 않는다.**
- 검색엔진에 **자동 쿼리를 대량으로 보내지 않는다.**
- API 키·OAuth·secret key는 **Git에 커밋하지 않는다.**

### 발전 순서

```
1단계: 수동 검증 (지금)
    ↓
2단계: CSV export 반자동 import
    ↓
3단계: 공식 API 연동 (문서화만 완료, 코드는 추후)
```

## 폴더 구성

| 경로 | 역할 |
|---|---|
| `keyword-research/` | 절차·API·점수 모델 문서 |
| `raw-data/` | 수동 기록·CSV export 원본 |
| `keywords.csv` | 검증 후 통합 키워드 관리 |

## 시작하기

1. `data-sources.md`에서 데이터 소스별 역할을 확인한다.
2. priority 1~3 seed keyword로 **수동 검증**을 시작한다.
   - `manual-google-autocomplete.md`
   - `manual-google-related-search.md`
   - `manual-naver-related-search.md`
3. 기록을 `raw-data/`에 저장한다.
4. `keyword-scoring-model.md`로 점수를 매기고 `keywords.csv`를 업데이트한다.
5. 검증완료 키워드만 글 초안 생성 단계로 넘긴다.

## 관련 문서

| 문서 | 내용 |
|---|---|
| `data-sources.md` | 데이터 소스별 구분 |
| `manual-google-autocomplete.md` | Google 자동완성 수동 절차 |
| `manual-google-related-search.md` | Google 연관검색어 수동 절차 |
| `manual-naver-related-search.md` | Naver 수동 절차 |
| `google-keyword-planner-import.md` | Keyword Planner CSV |
| `naver-datalab-api.md` | DataLab API·수동 기록 |
| `naver-searchad-api.md` | Search Ad API·수동 기록 |
| `keyword-scoring-model.md` | 우선순위 점수 |
| `keywords-csv-extension-proposal.md` | keywords.csv 확장 제안 |
