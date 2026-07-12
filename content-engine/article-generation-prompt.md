# 글 생성 프롬프트 (금형)

`content-plan.csv` 한 행 → `content/posts/{target_slug}.md` 초안.  
품질 울타리: `quality-standard.md` · 골격: `article-template.md` · 시각: `visual-elements.md`

## 사용 방법

1. `content-plan.csv`에서 이번 행 선택
2. 아래 프롬프트 `{...}` 채우기
3. Cursor Agent 실행 → `draft: true` 확인
4. `article-ai-review-prompt.md` 1회 실행
5. (필요 시) `article-visual-enhance-prompt.md` 시각 2차 패스
6. `reviews/{slug}-review.md` **Claim Log** 작성·출처 대조
7. `quality-checklist.md` 사람 검수

---

## 프롬프트 (복사용)

~~~~
감정평가 노트 블로그용 글 초안을 마크다운으로 작성해줘.

## 페르소나 (독자-facing)

감정평가 사무소에서 일하며 부동산·감정평가를 공부하는 사람이 쓰는 **정보 블로그 글**.
- 검색자의 질문에 답하는 톤. 독자에게 유용한 비교·기준·절차를 준다.
- 감정평가사·세무사 면허는 없지만, **글에서 그 사실을 광고하거나 고백하지 마라.**
- 「작성자가 잘 몰라서~」「이 글만으로 판단 불가」「이 글의 한계」 등 **자기 고백형 문장 금지.**
- 검수 노트·내부 파일 경로를 본문에 넣지 마라.

## 입력값 (content-plan.csv 행)

- suggested_title: {suggested_title}
- seed_keyword: {seed_keyword}
- keyword: {keyword}
- search_intent: {search_intent}
- content_type: {content_type}
- target_slug: {target_slug}
- category: {category}
- memo: {memo}

## 출력

- 파일: content/posts/{target_slug}.md
- 기존 글 수정 금지 (what-is-real-estate-appraisal.md 등)
- draft: 반드시 true

## 구조 규칙

1. Hugo front matter: title, date(오늘 ISO8601 +09:00), draft:true, description, categories(1개, taxonomy.md), tags
2. # 제목 (suggested_title)
3. 서론: 두괄식. 첫 문장에서 검색자 질문에 답. 예고형 서론 금지.
4. 핵심 요약: 인용 블록 3~5줄 (`visual-elements.md` 요약 박스)
5. H2: 4~6개, 질문 형태. article-template.md의 content_type 가이드 따름.
6. 시각 요소 (`visual-elements.md` 분량 가이드):
   - 표 **1~2개** (비교·정리)
   - 주의 박스 **0~1개** (본문 중간, 해당 시)
   - 절차·분기가 헷갈리면 **Mermaid 흐름도 1개** + PNG 교체용 HTML 주석(alt·경로 초안) + 캡션 1줄
   - PNG 이미지 파일은 생성하지 마라 (Mermaid만)
7. FAQ 3개 (롱테일, 본문 근거)
8. 짧은 마무리 + YMYL 공통 고지문 (article-template.md)

## 검색 의도·content_type

- 정보형: 언제·왜 검토하는지 중심
- 비교형: 판단 기준·비교 표 중심
- 실행형: 절차·체크리스트 중심

## 중복·얇은 콘텐츠

- {keyword}에만 정면 답한다. 기초 개념은 what-is-real-estate-appraisal 링크.
- memo 구분점 준수. 80% 겹치는 일반론 금지.
- 글자 수 목표 없음. 빈 단락·반복 금지.

## YMYL

- 세율·한도·비용·기간 단정 금지 → "~일 수 있습니다"
- 기준일: YYYY년 M월
- 출처: 국세청·법령 등 (필요 시)
- 사무소 CTA·과장 표현 금지
- 허구 경험·가명 사례 금지

## 톤·알맹이

- 「세무사에게 확인」만 반복하지 마라. **구체 정보**(평가 순서, 유형별 표, 상황별 갈림)가 본문에 있어야 한다.
- **현장 관찰** 1곳 이상: 접수·의뢰 맥락에서 반복되는 질문·지연 (가명 인물 금지).
- **가상 상황** 2곳 이상: 「이해를 돕기 위한 가상 상황」으로 유형별 walkthrough.
- 문장은 짧게. 서론 도입은 글마다 다르게.
- **강조 + 「」:** `**「…」**`는 Goldmark에서 볼드가 **깨짐** → `<strong>「…」</strong>` 사용 (hugo.toml `unsafe=true` 설정됨). 또는 `** 「…」 **`(앞뒤 공백).
~~~~

---

## 입력값 예시 (priority 1)

| 항목 | 값 |
|---|---|
| suggested_title | 상속 감정평가, 공시가격으로 신고해도 괜찮을까? |
| seed_keyword | 상속 감정평가 |
| keyword | 공시가격 상속세 신고 |
| search_intent | 비교형 |
| content_type | 비교정리 |
| target_slug | official-price-inheritance-tax-filing |
| category | 상속·절세 |
| memo | priority14와 혼동 금지. 공시가격 신고·감정평가 검토 판단만 |

## 생성 후 (발행 주체)

- [ ] `article-ai-review-prompt.md`
- [ ] (필요 시) `article-visual-enhance-prompt.md`
- [ ] `reviews/{slug}-review.md` 사실 확인
- [ ] `quality-checklist.md` (D. 시각 요소 포함)
- [ ] Mermaid → PNG 교체 (`static/images/`, 발행 직전)
- [ ] `content-plan.csv` → `drafted`
