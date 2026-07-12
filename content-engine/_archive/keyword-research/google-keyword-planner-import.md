# Google Keyword Planner — CSV Import

## 목적

월간 검색량 **범위**, 광고 경쟁도, 입찰가 관련 지표를 **참고용**으로 확보한다.

## v0.1 방식: 수동 CSV Export

API 연동 전까지 CSV 다운로드만 사용한다.

### 절차

1. [Google Ads](https://ads.google.com) 계정에 로그인한다.
2. **도구 및 설정 → 키워드 플래너** (또는 계획 → 키워드 플래너)를 연다.
3. **새 키워드 검색** 또는 **키워드 아이디어 검색**을 선택한다.
4. `keywords.csv`의 `seed_keyword`를 입력한다.
   - 예: 상속 감정평가, 증여 부동산 감정평가
5. 지역·언어를 설정한다. (한국, 한국어)
6. 결과에서 유망 키워드를 확인한다.
7. **다운로드 → CSV**로 저장한다.
8. 파일을 `raw-data/google-keyword-planner/`에 저장한다.

### 파일명 규칙

    YYYY-MM-DD-seed-{seed_keyword}.csv

예: `2026-07-01-seed-상속감정평가.csv`

## CSV에서 볼 항목 (참고용)

| 항목 | 활용 |
|---|---|
| 평균 월간 검색량 (범위) | 수요 있음/없음 **참고** |
| 경쟁도 (낮음/중간/높음) | **광고** 경쟁 참고 |
| 상단·하단 입찰가 범위 | CPC 가능성 **참고** |

## 중요한 구분

**광고 경쟁도 ≠ SEO 경쟁도**

- Keyword Planner 경쟁도는 **광고주** 간 경쟁이다.
- SEO 1페이지 경쟁은 `manual-google-related-search.md`로 별도 관찰한다.
- 두 데이터를 혼동하지 않는다.

## keywords.csv 반영

- `google_keyword_planner_checked`: Y (확장 열 적용 시)
- `estimated_search_demand`: 높음 / 중간 / 낮음 (범위 기반 **질적** 판단)
- `cpc_note`: "입찰가 범위 참고, 단가 가능성 ○○" (숫자 단정 금지)
- 숫자를 그대로 CSV에 복사하기보다 **해석 메모**를 남긴다.

## 추후: Google Ads API

연동 검토 시 참고 사항:

- Google Ads API는 OAuth 2.0 인증이 필요하다.
- 개발자 토큰, 클라이언트 ID, 클라이언트 시크릿, 리프레시 토큰이 필요할 수 있다.
- 모든 인증 정보는 **`.env`에 보관**하고 Git에 커밋하지 않는다.
- `.env.example`에 변수 **이름만** 문서화한다.

### .env 예시 (값은 비워 둠)

    GOOGLE_ADS_DEVELOPER_TOKEN=
    GOOGLE_ADS_CLIENT_ID=
    GOOGLE_ADS_CLIENT_SECRET=
    GOOGLE_ADS_REFRESH_TOKEN=
    GOOGLE_ADS_CUSTOMER_ID=

v0.1에서는 위 연동 코드를 **작성하지 않는다.**

## 하지 말 것

- API 없이 대량 키워드를 자동 조회하는 스크립트
- CSV의 검색량 숫자를 절대값처럼 keywords.csv에 기록
