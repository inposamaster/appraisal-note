# 콘텐츠 제작 — 단순 워크플로

**상세 SSOT:** `PIPELINE.md` · **용어:** `GLOSSARY.md`

---

## 3단계 요약

### 1단계 — 글 고르기

`content-plan.csv`를 연다.

- **Phase 1** (priority 1~30): 발행 완료
- **Phase 2** (priority 31~42): 4개월차 — **현재 진행**
- 이번에 쓸 글 1편: `status: planned` 중 **가장 낮은 priority**
- Google 스프레드시트 관리: `google-sheets-guide.md`

### 2단계 — 생산 (초안 ~ Claim Log)

`PIPELINE.md` 2~5단계:

1. `article-generation-prompt.md` → `draft: true` 초안
2. `article-ai-review-prompt.md`
3. `article-visual-enhance-prompt.md` → **PNG 3장**
4. `reviews/{slug}-review.md` Claim Log

CSV는 **`planned` 유지** (초안 완료해도 `drafted`로 바꾸지 않음).

### 3단계 — 검수·발행

`PIPELINE.md` 6~7단계:

1. `quality-checklist.md` 사람 검수
2. `draft: false`
3. git commit → push → 라이브 확인
4. `content-plan.csv` → `status: published`

---

## 키워드 검증은 언제 하나?

**매 글마다 심층 조사하지 않는다.**

- 스프린트에서 `validation_status: 검증완료`로 올린 뒤
- **초안 직전** Google 1페이지 30초 재확인
- 이상 있으면 `보류` 또는 각도 수정

심층 키워드: `_archive/keyword-research/`

---

## 제목 공식

    [핵심 키워드] + [상황] + [궁금증/해결]

예: 감정평가 일정은 며칠 걸릴까—의뢰부터 보고서까지

---

## Phase 2 다음 순서 (1주차 잔여)

| priority | slug | 상태 |
|----------|------|------|
| 31 | appraisal-timeline-how-long | published |
| 32 | gift-appraisal-cost-how | published |
| 33 | burden-gift-appraisal-difference | planned ← **다음** |
| 33 | burden-gift-appraisal-difference | planned |

1편씩 발행. 주 3편은 `month-4-keyword-sprint-2026-07.md` §4 참고.
