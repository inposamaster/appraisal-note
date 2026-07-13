# 콘텐츠 엔진

감정평가 노트 블로그의 **발행 계획 · 글 작성 · 검수**를 관리하는 폴더입니다.

## SSOT (먼저 읽을 것)

| 문서 | 역할 |
|------|------|
| **`PIPELINE.md`** | 생산 0~7단계 **단일 순서** |
| **`GLOSSARY.md`** | 용어·status·Phase 정의 |
| **`content-plan.csv`** | 발행 큐 (priority·status) |

2호 이후 포트폴리오: `../inposa-blog-system/BLOG_TOPIC_SELECTION_BRIEF.md`

## 핵심 원칙

**AI는 초안을 만들고, 사람은 최종 책임을 진다.**

- 초안: `content/posts/*.md` → `draft: true`
- 발행 게이트 통과 후만 `draft: false` → commit → 배포
- CSV `status`: `planned` → `published` (`drafted` **사용 안 함** — `GLOSSARY.md`)

## 워크플로 (요약)

`PIPELINE.md`와 동일:

```
0. 키워드 기획 — planning/
1. 글 선택 — content-plan.csv
2. 초안 생성 — article-generation-prompt.md
3. AI 1차 리뷰 — article-ai-review-prompt.md
4. 시각 2차 + PNG 3장 — article-visual-enhance-prompt.md
5. Claim Log — reviews/{slug}-review.md
6. 사람 검수 — quality-checklist.md
7. 발행 — draft: false, status: published
```

## 로드맵 단계

| Phase | priority | 상태 |
|-------|----------|------|
| **Phase 1** (1~3개월) | 1~30 | 발행 완료 |
| **Phase 2** (4개월차) | 31~42 | 진행 중 (31 발행) |

## 파일 구성

| 파일 | 역할 |
|---|---|
| **PIPELINE.md** | 워크플로 SSOT |
| **GLOSSARY.md** | 용어 사전 |
| **quality-standard.md** | 품질 기준선 (다블로그 확장 시 공통 후보) |
| **content-plan.csv** | 발행 큐 SSOT |
| **seed-priority.csv** | 핵심 시드 키워드 Top 21 |
| **planning/** | 0단계 스프린트·키워드 풀 |
| **publish-schedule.csv** | 발행일 기록 (Phase 1 완료 + Phase 2 예정) |
| **article-template.md** | 글 본문 골격 |
| **article-generation-prompt.md** | Cursor 초안 생성 금형 |
| **article-visual-enhance-prompt.md** | 시각 2차 패스 (PNG 3장) |
| **taxonomy.md** | 카테고리·태그·메뉴 규칙 |
| **visual-elements.md** | 시각 요소·PNG 네이밍 |
| **article-ai-review-prompt.md** | AI 1차 셀프 리뷰 |
| **quality-checklist.md** | 사람 발행 게이트 (7+1 + 시각) |
| **fact-check-guide.md** | Claim Log 절차 (비전문가용) |
| **OPS_ADSENSE_SEO.md** | AdSense·구글·네이버 운영 체크 |
| **reviews/** | 글별 검수 노트·Claim Log |
| keyword-workflow-simple.md | 파이프라인 요약본 |
| google-sheets-guide.md | 스프레드시트 연동 |

## 시작하기 (다음 글 1편)

1. `content-plan.csv`에서 `status: planned` 중 **가장 낮은 priority** (현재: **32**)
2. `PIPELINE.md` 2~7단계 순서대로 실행
3. 발행 후 CSV·`CONTENT_BACKLOG.md`·스프린트 md 동기화

## 스프레드시트

`content-plan.csv`를 Google 스프레드시트로 가져와 편집할 수 있다.  
방법: `google-sheets-guide.md`

## 심화 자료

키워드 API·수동 SERP 심층 검증 등은 `_archive/`에 보관.

## 블로그 저장소 구조 (참고)

| 경로 | 역할 |
|---|---|
| `content/posts/` | 발행 글 (Hugo) |
| `content-engine/` | 이 폴더 |
| `static/images/` | 발행용 PNG |
| `layouts/_markup/` | Mermaid 렌더 훅 |
| `hugo.toml` | 사이트 설정 |
