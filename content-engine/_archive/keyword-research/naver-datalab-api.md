# Naver DataLab — API 연동 가능성

## 역할 정의

DataLab은 **새 키워드 발견**보다 **추세 검증** 도구로 사용한다.

- 여러 후보 키워드의 **상대적 검색 추세** 비교
- 기간별 상승·유지·하락 확인
- PC/모바일, 성별, 연령 조건 (추후 세분화)

## v0.1: 웹 화면 수동 기록

API 연동 전에는 [네이버 데이터랩](https://datalab.naver.com)에서 직접 확인한다.

### 절차

1. 비교할 키워드 2~5개를 선정한다 (`keywords.csv` 후보).
2. 검색어 트렌드에서 키워드를 입력한다.
3. 기간을 설정한다. (예: 최근 3개월, 1년)
4. 상대적 추세를 관찰한다.
5. `raw-data/naver-datalab/_template.md` 형식으로 기록한다.

### 저장 위치

    raw-data/naver-datalab/YYYY-MM-DD.md

## keywords.csv 반영

- `naver_datalab_checked`: Y (확장 열 적용 시)
- `memo`에 "DataLab: A > B 추세" 형태로 **상대 비교**만 기록
- 절대 검색량 숫자 단정 금지

## 추후: DataLab API

공식 API 문서: [네이버 개발자센터 — 데이터랩](https://developers.naver.com/docs/serviceapi/datalab/search/datalab.md)

### 필요 정보

- 네이버 개발자센터 애플리케이션 등록
- Client ID, Client Secret

### .env 보관 (Git 제외)

    NAVER_DATALAB_CLIENT_ID=
    NAVER_DATALAB_CLIENT_SECRET=

### API로 할 수 있는 것 (추후)

- 키워드 그룹별 검색량 **비율** 추이 조회
- 기간·디바이스·성별·연령 조건 설정

### API로 하지 않을 것

- DataLab에 없는 임의 키워드 대량 발굴 자동화
- 네이버 검색결과 스크래핑 대체

v0.1에서는 **연동 코드를 작성하지 않는다.**

## 보안

- API 키는 `.env`에만 저장
- `.env`는 `.gitignore`에 포함
- 로그·에러 메시지에 키 노출 금지
