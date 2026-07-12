# 콘텐츠 엔진

감정평가 노트 블로그의 **발행 계획 · 글 작성 · 검수**를 관리하는 폴더입니다.

## 핵심 원칙

**AI는 초안을 만들고, 사람은 최종 책임을 진다.**

- 초안은 `draft: true`
- 검수 후에만 `draft: false` → commit → 배포

## 워크플로

```
1. content-plan.csv에서 글 고르기
2. article-generation-prompt.md로 초안 생성 (표·박스·Mermaid 포함)
3. article-ai-review-prompt.md로 AI 1차 점검
4. (필요 시) article-visual-enhance-prompt.md 시각 2차 패스
5. reviews/{slug}-review.md Claim Log·출처 대조
6. quality-checklist.md로 사람 검수 (D. 시각 요소)
7. Mermaid → static/images/ PNG 교체 (발행 직전)
8. draft: false → 발행
```

자세한 설명: `keyword-workflow-simple.md`  
품질 기준선: `quality-standard.md`

## 파일 구성

| 파일 | 역할 |
|---|---|
| **quality-standard.md** | 품질 기준선 (다른 블로그 확장 시에도 공통) |
| **content-plan.csv** | 발행 글 **30편** 로드맵 (애드센스 목표) |
| **seed-priority.csv** | 핵심 시드 키워드 Top 15 |
| **article-template.md** | 글 본문 골격 |
| **article-generation-prompt.md** | Cursor 초안 생성 금형 |
| **article-visual-enhance-prompt.md** | 시각 요소 2차 패스 (표·박스·Mermaid) |
| **taxonomy.md** | 카테고리·태그·메뉴 규칙 |
| **visual-elements.md** | 시각 요소 규칙 (Mermaid → PNG 교체) |
| **article-ai-review-prompt.md** | AI 1차 셀프 리뷰 |
| **quality-checklist.md** | 사람 발행 게이트 (7+1 + 시각) |
| **fact-check-guide.md** | 비전문가 검증 5단계 (Claim Log) |
| **reviews/** | 글별 검수 노트·Claim Log |
| keyword-workflow-simple.md | 단순 워크플로 |
| google-sheets-guide.md | 스프레드시트 연동 |

## 시작하기

1. `content-plan.csv`에서 이번 글 1편 (권장: priority 1~3)
2. `article-generation-prompt.md`로 초안
3. `article-ai-review-prompt.md` 실행
4. `quality-checklist.md` 검수
5. `content-plan.csv` → `status: published`

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
| `static/images/` | 발행용 PNG (Mermaid 교체본) |
| `layouts/_markup/` | Mermaid 렌더 훅 |
| `hugo.toml` | 사이트 설정 |
