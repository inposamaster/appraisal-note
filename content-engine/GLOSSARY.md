# 용어 사전 (GLOSSARY)

**목적:** `appraisal-note` 및 향후 2~10호 블로그에서 **같은 말이 같은 뜻**이 되도록 고정한다.  
**SSOT:** 이 문서. 충돌 시 `PIPELINE.md`·`content-plan.csv`가 우선.

---

## 블로그·포트폴리오

| 용어 | 정의 |
|------|------|
| **블로그 인스턴스** | Git 저장소 1개 + Hugo 사이트 1개 + 서브도메인 1개 (예: `appraisal-note`) |
| **1호 / 기준 블로그** | `appraisal-note` — 파이프라인·품질 게이트 실험장 |
| **포트폴리오** | `inposa-blogs/` 워크스페이스 안의 블로그·허브 전체 |
| **공통 엔진** | 여러 블로그에서 **검증된** 규칙만 승격하는 `inposa-blog-system/` (과조기 추출 금지) |
| **허브** | `www.inposa.net` — 블로그 간 탐색·신뢰·AdSense 루트 |

---

## 콘텐츠 계획

| 용어 | 정의 |
|------|------|
| **SSOT (발행 큐)** | `content-plan.csv` — priority·제목·keyword·status의 단일 진실 원천 |
| **Phase 1** | priority **1~30** (2026년 5~7월, **발행 완료**) |
| **Phase 2** | priority **31~42** (4개월차 스프린트, **진행 중**) |
| **month** (CSV 열) | 기획상 달 구분. Phase 1은 1~3, Phase 2는 **4** |
| **priority** | 발행·생산 **순서** (1이 가장 먼저) |
| **target_slug** | `content/posts/{slug}.md` 파일명·URL slug |
| **seed_keyword** | 주제 묶음(시드). `seed-priority.csv`와 연동 |
| **keyword** | 글 1편이 정면으로 답하는 **핵심 검색어** |
| **search_intent** | 정보형 / 비교형 / 실행형 |
| **content_type** | 비교정리 / 개념설명 / 절차안내 / 체크리스트 / 사례해설 등 |
| **validation_status** | 키워드 검증: `후보` → `검증완료` / `보류` |
| **memo** (CSV) | 구분점·중복 회피·생산 메모 (본문에 넣지 않음) |

---

## status (content-plan.csv)

| 값 | 의미 |
|----|------|
| **planned** | 행 확정·검증 완료. **아직 라이브 발행 전** (초안 유무와 무관) |
| **published** | `draft: false` + git push + 라이브 URL 확인 후 |

### 사용하지 않는 값 (레거시)

| 값 | 처리 |
|----|------|
| ~~**drafted**~~ | **폐기.** 초안 완료는 `content/posts/*.md`의 `draft: true`로 표현. CSV는 `planned` 유지 → 발행 시 `published` |

**초안 여부는 CSV가 아니라 글 front matter `draft`가 진실이다.**

---

## 파이프라인·품질

| 용어 | 정의 |
|------|------|
| **0단계** | 키워드 기획 — `planning/` 스프린트, `content-plan.csv` 행 추가 |
| **생산 파이프라인** | 초안 → AI 리뷰 → 시각 2차(PNG 3) → Claim Log → 사람 검수 → 발행 |
| **Claim Log** | `reviews/{slug}-review.md`의 사실 주장 대조표 |
| **발행 게이트** | `quality-checklist.md` (7+1 + D 시각) — **사람** 최종 |
| **PNG 3장** | 글당 필수: 흐름도·비교·상황/유형 (`visual-elements.md`) |
| **YMYL** | 금융·세무 등 — 단정·과장 금지, 기준일·면책 필수 |
| **SERP 거름망** | checklist 8번 / review — 1페이지 대비 차별 각도 |

---

## 파일·폴더

| 경로 | 역할 |
|------|------|
| `content/posts/` | Hugo **발행 글** (독자-facing) |
| `content-engine/` | 계획·프롬프트·검수·정책 (**비독자**) |
| `content-engine/planning/` | 스프린트·키워드 풀 (0단계 산출물) |
| `content-engine/reviews/` | 글별 Claim Log (**내부**, 본문 링크 금지) |
| `static/images/` | 발행용 PNG (`/images/...` URL) |
| `content-engine/CONTENT_BACKLOG.md` | 사람용 진행 요약 (**SSOT 아님** · **비공개**, CSV 동기화) |

---

## SEO·운영 (요약)

| 용어 | 정의 |
|------|------|
| **네이버 SEO** | 한국어 제목·본문·내부링크·카테고리 일관; 네이버 서치어드바이저 (설정은 `OPS_ADSENSE_SEO.md`) |
| **구글 SEO** | 구조화·canonical·sitemap·Search Console; `hugo.toml` 메타 |
| **크로스블로그 중복 금지** | 동일 keyword·동일 검색 의도를 **다른 블로그**에 복제하지 않음 (`quality-standard.md` §9) |

---

## 관련 문서

- `PIPELINE.md` — 단계별 작업 순서
- `README.md` — 이 폴더 허브
- `../inposa-blog-system/BLOG_TOPIC_SELECTION_BRIEF.md` — 2호 이후 주제 선정
