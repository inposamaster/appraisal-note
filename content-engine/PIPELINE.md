# 콘텐츠 생산 파이프라인 (SSOT)

**이 문서가 워크플로의 단일 진실 원천이다.**  
다른 md가 순서를 다르게 적으면 **이 문서를 따른다.**

용어: `GLOSSARY.md`

---

## 전체 흐름

```
0. 키워드 기획
1. 글 선택 (content-plan.csv)
2. 초안 생성 (draft: true)
3. AI 1차 리뷰
4. 시각 2차 패스 + PNG 3장
5. Claim Log (reviews/)
6. 사람 검수 (quality-checklist.md)
7. 발행 (draft: false → published → commit → push)
```

---

## 0. 키워드 기획 (선행)

| 할 일 | 산출물 |
|-------|--------|
| 후보 브레인스토밍·중복 스캔 | `planning/keyword-pool.csv` |
| 스프린트 확정·주간 순서 | `planning/month-*-keyword-sprint-*.md` |
| 발행 큐 반영 | `content-plan.csv` 행 추가, `validation_status: 검증완료` |
| 시드 갱신 | `seed-priority.csv` (필요 시) |

**규칙:** Phase 1(1~30) 및 **다른 블로그**와 검색 의도 80% 중복 금지.

---

## 1. 글 선택

- `content-plan.csv`에서 `status: planned` 중 **다음 priority** 1편
- `memo`·`keyword`·기발행 slug와 구분점 확인
- 발행 직전 Google 1페이지 **30초 재확인** (스프린트 검증 보완)

---

## 2. 초안 생성

- 도구: `article-generation-prompt.md` + `article-template.md` + `visual-elements.md`
- 출력: `content/posts/{target_slug}.md`
- **필수:** `draft: true`, 핵심 요약 박스, 표 1~2, FAQ 3, YMYL 고지 초안
- **필수 사전 한 줄:** 「검색자가 가져갈 본체 = ___」(`quality-standard` §1-2). 없으면 생성 보류
- **Mermaid:** 절차·분기 헷갈리면 1개 (PNG 교체용 주석 포함)
- **하지 말 것:** PNG 파일 생성, `draft: false`, 형제 글 스킨 복제

---

## 3. AI 1차 리뷰

- 도구: `article-ai-review-prompt.md`
- AI 흔적·얇은 단락·과장·가명 사례 제거
- 사실·수치 **새로 지어내지 않음**

---

## 4. 시각 2차 패스 + PNG 3장

- 도구: `article-visual-enhance-prompt.md`
- **본문 사실관계는 바꾸지 않음**
- `static/images/`에 PNG **3장** (흐름·비교·상황)
- 본문 삽입 + alt + 이탤릭 캡션 (기준일)
- Mermaid가 있으면 **흐름도 PNG로 교체**
- 파일명: `GLOSSARY.md`·`visual-elements.md` § PNG 네이밍

---

## 5. Claim Log

- 파일: `reviews/{slug}-review.md` (`reviews/_template.md` 복사)
- 본문 주장 ↔ 국세청·법령 등 출처 대조
- SERP 거름망 (+1) 기록
- **X = 0** 전까지 발행 금지

---

## 6. 사람 검수

- 도구: `quality-checklist.md` (A·B·D·C)
- PNG 한글·화살표·본문 일치 **눈으로** 확인
- `hugo server -D`에서 글·이미지 URL 확인

보조: `fact-check-guide.md` (Claim Log 절차 상세)

---

## 7. 발행

| 순서 | 작업 |
|------|------|
| 1 | `draft: false` |
| 2 | `content-plan.csv` → `status: published` |
| 3 | `publish-schedule.csv` 날짜 기록 (선택·권장) |
| 4 | git commit (`inposamaster`) → push → 라이브 URL 확인 |
| 5 | `CONTENT_BACKLOG.md`·스프린트 md 진행 상태 갱신 |

**한 글당 주 1편 리듬 권장** (4개월차: 주 3편 = 월·수·금).

---

## status 전이 (content-plan.csv)

```
planned ──(7. 발행 완료)──► published
```

- 초안 작성 중에도 CSV는 **`planned`**
- `draft: true` / `false`는 **글 front matter**만 사용

---

## 블로그 확장 시

1호에서 **실제로 통과한** 단계만 `inposa-blog-system`으로 복사한다.  
블로그마다 `content-plan.csv`·`taxonomy.md`·도메인은 **별도 SSOT**.

---

## 문서 맵

| 단계 | 문서 |
|------|------|
| 0 | `planning/README.md`, 스프린트 md |
| 2 | `article-generation-prompt.md` |
| 3 | `article-ai-review-prompt.md` |
| 4 | `article-visual-enhance-prompt.md`, `visual-elements.md` |
| 5 | `reviews/_template.md`, `fact-check-guide.md` |
| 6 | `quality-checklist.md`, `quality-standard.md` |
| 7 | `publish-schedule.csv`, `OPS_ADSENSE_SEO.md` |
