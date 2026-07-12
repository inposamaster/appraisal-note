# keywords.csv 확장 제안

> **상태: 제안 (v0.1)** — 기존 CSV는 아직 변경하지 않았다.  
> Keyword Research Lab 검증이 1~2회 진행된 뒤 적용 여부를 결정한다.

## 배경

현재 `keywords.csv` 열:

    priority, seed_keyword, keyword, search_intent, content_type,
    competition_note, cpc_note, validation_status, source_hint,
    target_slug, status, memo

Keyword Research Lab에서 **소스별 검증 여부**와 **점수**를 추적하려면 열 추가가 유리하다.

## 제안 열

| 열 | 타입 | 설명 |
|---|---|---|
| google_autocomplete_found | Y / N | Google 자동완성에서 후보 발견 여부 |
| google_related_found | Y / N | Google 연관검색어·SERP 관찰 완료 |
| naver_related_found | Y / N | Naver 자동완성·연관검색어 관찰 완료 |
| naver_datalab_checked | Y / N | DataLab 추세 확인 (수동 또는 API) |
| google_keyword_planner_checked | Y / N | Keyword Planner CSV 확인 |
| naver_searchad_checked | Y / N | Search Ad 수동/API 확인 |
| estimated_search_demand | 낮음/중간/높음 | 질적 수요 추정 (숫자 금지) |
| seo_competition_level | 낮음/중간/높음 | SEO 1페이지 관찰 기반 |
| score_total | 숫자 | keyword-scoring-model 총점 |
| next_action | 텍스트 | 초안생성 / 재검증 / 보류 / skip |

## 기존 열과의 관계

| 기존 열 | 확장 열과의 관계 |
|---|---|
| validation_status | 소스별 Y/N이 쌓이면 → 검증완료 승격 |
| competition_note | seo_competition_level의 근거 메모 |
| cpc_note | google_keyword_planner·searchad 확인 후 보강 |
| source_hint | raw-data 파일 경로 참조 가능 (예: google-autocomplete/2026-07-01.md) |
| priority | score_total과 함께 참고, priority가 최종 결정권 |

## 통합 워크플로

```
raw-data/ (소스별 기록)
    ↓
사람이 검증·점수 산정
    ↓
keywords.csv 해당 행 업데이트
    ↓
validation_status = 검증완료
next_action = 초안생성
    ↓
article-generation-prompt.md로 초안
```

## Cursor 역할 (반자동)

- raw-data Markdown·CSV를 읽고 keywords.csv 행 **초안** 정리
- 점수 워크시트 표 채우기 **보조**
- 최종 승인·숫자 해석은 **사람**

## 적용 시점 제안

| 조건 | 행동 |
|---|---|
| 지금 (v0.1) | 기존 12열 유지, `memo`·`source_hint`에 상세 기록 |
| priority 1~3 수동 검증 1회 완료 후 | 확장 열 10개 추가 검토 |
| API 연동 시 | checked 열이 특히 유용 |

## 적용 시 주의

- 기존 10행 데이터에 빈 값으로 열 추가 (하위 호환)
- `score_total`은 AI가 임의로 채우지 않음
- `estimated_search_demand`에 Keyword Planner 숫자를 직접 넣지 않음

## 확장 후 헤더 예시 (참고)

    priority,seed_keyword,keyword,search_intent,content_type,competition_note,cpc_note,validation_status,source_hint,target_slug,status,memo,google_autocomplete_found,google_related_found,naver_related_found,naver_datalab_checked,google_keyword_planner_checked,naver_searchad_checked,estimated_search_demand,seo_competition_level,score_total,next_action

적용은 별도 커밋으로 진행한다.
