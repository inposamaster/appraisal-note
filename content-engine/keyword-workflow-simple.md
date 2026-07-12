# 콘텐츠 제작 — 단순 워크플로

## 3단계

### 1단계 — 글 고르기

`content-plan.csv`를 연다.

- 30편이 3개월 로드맵(카테고리 7+7+8+8)으로 정리되어 있음
- 이번에 쓸 글 1편만 고름 (권장: priority 1~3)
- Google 스프레드시트로 관리해도 됨 (`google-sheets-guide.md`)

### 2단계 — 초안 작성

1. `quality-standard.md`·`article-template.md`·`visual-elements.md` 확인
2. `article-generation-prompt.md`를 Cursor에 붙여넣기
3. `content/posts/{target_slug}.md` 생성 (`draft: true`, 표·박스·Mermaid 포함)
4. `article-ai-review-prompt.md`로 AI 1차 점검
5. (필요 시) `article-visual-enhance-prompt.md` 시각 2차 패스
6. `reviews/{target_slug}-review.md` Claim Log·출처 대조
7. `content-plan.csv`의 `status`를 `drafted`로 변경

### 3단계 — 검수·발행

1. `quality-checklist.md`로 사람 검수 (7+1 + D. 시각 요소)
2. Mermaid → `static/images/` PNG 교체 (발행 직전, 권장)
3. `draft: false` 변경
4. git commit → push → 라이브 URL 확인
5. `content-plan.csv`의 `status`를 `published`로 변경

---

## 키워드 검증은 언제 하나?

**매 글마다 하지 않는다.**

- `content-plan.csv` 30편 — 키워드는 발행 직전 가볍게 검증
- 이번 달 쓸 **3편만** Google에서 30초 검색해 보면 충분
- `validation_status`를 `검증완료`로 바꿀지 `보류`로 바꿀지만 기록

심층 키워드 조사가 필요하면 `_archive/keyword-research/` 참고.

---

## 제목 공식

    [핵심 키워드] + [상황] + [궁금증/해결]

예: 상속 감정평가, 공시가격으로 신고해도 괜찮을까?

---

## 이번 달 권장 순서 (1개월차)

| priority | 제목 |
|---|---|
| 1 | 상속 감정평가, 공시가격으로 신고해도 괜찮을까? |
| 2 | 상속 감정평가 비용은 어떻게 정해질까? |
| 3 | 증여 감정평가, 증여 전에 꼭 검토해야 할까? |

1편씩 발행한다. 3편을 한꺼번에 쓰지 않는다.
