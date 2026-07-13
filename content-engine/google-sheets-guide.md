# Google 스프레드시트 연동

## 가져오기

1. [Google 스프레드시트](https://sheets.google.com) 새 문서
2. **파일 → 가져오기 → 업로드**
3. `content-engine/content-plan.csv` 선택
4. 구분 기호: **쉼표**

선택: `seed-priority.csv`를 두 번째 시트로 가져온다.

## 편집 후 레포 반영

1. **파일 → 다운로드 → CSV**
2. `content-plan.csv`로 교체
3. git commit

## 자주 쓰는 열

| 열 | 값 예시 |
|---|---|
| validation_status | 후보 / 검증완료 / 보류 |
| status | **planned** / **published** (`drafted` 사용 안 함 — `GLOSSARY.md`) |
| competition_note | 1페이지 블로그 2개 |
| memo | 검증일, 수정 메모 |

## 필터

- `month = 4` → Phase 2 (4개월차)만
- `status ≠ published` → 미발행 글만

## content-plan.csv 열 설명

| 열 | 설명 |
|---|---|
| month | 1~3 = Phase 1 · **4** = Phase 2 (4개월차) |
| priority | 발행 순서 **1~42** |
| suggested_title | 글 제목 (H1) |
| seed_keyword | 주제 묶음 |
| keyword | 핵심 검색어 |
| search_intent | 정보형 / 비교형 / 실행형 |
| content_type | 개념설명 / 절차안내 등 |
| validation_status | 키워드 검증 상태 |
| status | 작성·발행 상태 |
| target_slug | 파일명 (영문) |
