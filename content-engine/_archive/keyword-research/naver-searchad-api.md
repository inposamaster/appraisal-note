# Naver Search Ad API — 연동 가능성

## 역할 정의

네이버 검색광고 API는 다음 용도로 **검토**한다.

- **연관 키워드** 후보 확장
- 월간 검색수, 클릭률 등 **광고 지표** 참고
- CPC·경쟁 관련 **질적** 판단 보조

SEO 1페이지 경쟁은 별도로 `manual-google-related-search.md`로 관찰한다.

## v0.1: 수동 우선

API 연동 전:

- 검색광고 관리 화면에서 연관 키워드를 **수동**으로 확인
- 필요 시 export 파일을 `raw-data/naver-searchad/`에 저장
- 수동 메모 템플릿은 필요 시 `raw-data/naver-searchad/YYYY-MM-DD.md`로 작성

## 사전 요구사항 (API 연동 시)

1. [네이버 검색광고](https://searchad.naver.com) 계정
2. API License 발급 (광고주 센터 → 도구 → API 사용 관리)
3. 다음 인증 정보:
   - API Key (Access License)
   - Secret Key
   - Customer ID

## .env 보관 (Git 제외)

    NAVER_SEARCHAD_API_KEY=
    NAVER_SEARCHAD_SECRET_KEY=
    NAVER_SEARCHAD_CUSTOMER_ID=

`.env.example`에 변수 이름만 두고, 실제 값은 커밋하지 않는다.

## 추후 자동화 가능 범위

| 가능 (공식 API) | 불가/금지 |
|---|---|
| 연관 키워드 목록 조회 | 네이버 검색결과 스크래핑 |
| 광고 지표 참고용 export | 대량 자동 쿼리 |
| keywords.csv 통합 스크립트 | API 키를 코드·Git에 포함 |

### 통합 흐름 (추후)

1. API로 연관 키워드 조회
2. 사람이 유망 후보만 선별
3. `keywords.csv`에 행 추가
4. SEO 경쟁은 여전히 수동 SERP 관찰

v0.1에서는 **연동 코드를 작성하지 않는다.**

## keywords.csv 반영

- `naver_searchad_checked`: Y (확장 열 적용 시)
- `cpc_note`에 질적 메모만 (숫자 단정 금지)

## 보안

- Secret Key 유출 시 즉시 재발급
- 스크립트는 환경변수에서만 키 로드
- CI/CD에 키를 plaintext로 넣지 않음 (추후 GitHub Secrets 사용)
