# 비전문가 사실 확인 가이드

**발행 주체(나)** 용 내부 절차. 공개 글(`content/posts/`)에는 쓰지 않는다.

발행 주체가 전문가가 아니어도, **검증 절차를 강화**하면 발행 품질을 지킬 수 있다.  
글 톤을 「잘 몰라서」로 바꾸는 것이 아니라, **아래 절차를 통과한 글만** `draft: false`로 올린다.

**전체 순서 SSOT:** `PIPELINE.md`

---

## 발행 전 절차 (필수)

```
1. AI 초안 생성 (draft: true)                    ← PIPELINE §2
2. article-ai-review-prompt.md — AI 1차 점검     ← §3
3. article-visual-enhance-prompt.md — PNG 3장   ← §4
4. reviews/{slug}-review.md — Claim Log         ← §5  ← 핵심
5. quality-checklist.md — 사람 검수              ← §6
6. 전부 통과 시 draft: false · published         ← §7
```

**4번(Claim Log)을 건너뛰지 않는다.** 전문 지식이 없을수록 Claim Log가 중요하다.

---

## Claim Log란

본문에서 **사실처럼 읽히는 문장**을 한 줄씩 뽑아, 공식 출처와 대조하는 표다.

| 결과 | 의미 | 조치 |
|---|---|---|
| O | 출처와 맞거나 완화 표현으로 안전 | 통과 |
| X | 틀림 | 본문 수정 후 재검 |
| 수정 | 애매 | 완화·삭제·출처 각주 |

템플릿: `reviews/_template.md`  
글별 예시: `reviews/official-price-inheritance-tax-filing-review.md`

---

## 전문가가 아닐 때 할 수 있는 것

| 할 수 있음 | 하지 말 것 |
|---|---|
| 국세청·법령 URL과 본문 대조 | 확신 없는 요건·수치 그대로 발행 |
| Claim Log에 확인일·URL 기록 | 허구 경험·사례로 알맹이 채우기 |
| SERP 1페이지와 차별점 비교 | 검수 생략하고 양산 발행 |
| 세무사·감정평가사 **2차 검수** (권장) | 글에 「작성자 한계」 고백 |

**보류는 실패가 아니다.** Claim Log에 X가 남으면 `draft: true` 유지.

---

## 2차 검수 (권장)

Claim Log를 **세무사 또는 감정평가사**에게 보내 「이 표현 틀린 부분 있나」만 물어도 된다.  
전문가가 본문 전체를 쓸 필요는 없다.

---

## 공식 출처 (감정평가 노트)

| 주제 | 1차 출처 |
|---|---|
| 상속·증여 재산 평가 | [국세청 cntntsId=7723](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7723&mi=2330) |
| 법령 | [국가법령정보센터](https://www.law.go.kr) 상속세 및 증여세법 |
| 공시가격 조회 | 부동산공시가격 알리미, 국세청 재산평가정보 |

---

## 관련 문서

- `PIPELINE.md`
- `reviews/_template.md`
- `quality-checklist.md`
- `quality-standard.md` § 발행 글 vs 검수
