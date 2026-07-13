# AdSense·SEO 운영 체크리스트

**1호 `appraisal-note` 전용.** 2호 이후는 인프라 복제 + 주제별 taxonomy 분리.

포트폴리오·2호 선정: `../../inposa-blog-system/BLOG_TOPIC_SELECTION_BRIEF.md`

---

## AdSense (inposa.net 계정)

| 항목 | 위치 | 상태 점검 |
|------|------|-----------|
| Publisher ID | `hugo.toml` params | `ca-pub-6632240269170834` |
| ads.txt | `static/ads.txt` | 라이브 `/ads.txt` 200 |
| 개인정보·쿠키 | `content/privacy.md` | AdSense 문구 포함 |
| 신뢰 페이지 | `about.md`, `contact.md` | 면책·문의 |
| 심사 전 | — | **가치 있는 글 수·내비·모바일** (`BLOG_TOPIC_SELECTION_BRIEF` §3) |

**심사 중:** 대시보드 갱신 지연 가능. ads.txt 정상이면 **대기**.

---

## Google SEO

| 항목 | 위치 |
|------|------|
| canonical·OG | `hugo.toml`, 테마 |
| sitemap | Hugo 자동 `/sitemap.xml` |
| Search Console | 도메인·URL 접두 검증 (`static/google*.html`) |
| 구조 | H1 1개, 내부링크, `description` front matter |

**발행 후:** Search Console URL 검사(선택), 색인 요청은 남용하지 않음.

---

## 네이버 SEO

| 항목 | 권장 |
|------|------|
| 서치어드바이저 | 사이트 등록·소유 확인 (별도 HTML 또는 메타) |
| 제목·본문 | 한국어 자연어, 키워드 스터핑 금지 |
| RSS | Hugo RSS 피드 활용 가능 |
| 중복 | 다른 블로그·네이버 블로그에 **동일 글** 미게시 |

네이버 API·심층 키워드: `content-engine/_archive/keyword-research/`

---

## 발행 직후 (글 1편)

- [ ] 라이브 URL 200
- [ ] `/images/*.png` 3장 200
- [ ] 메타 description·카테고리 1개 (`taxonomy.md`)
- [ ] 내부 링크 깨짐 없음

---

## 아직 설정 예정 (로드맵)

- 네이버 서치어드바이저 자동화·상태 문서화
- 구조화 데이터(JSON-LD) 정책 통일
- 멀티블로그 **keyword 레지스트리** (블로그 간 중복 방지 SSOT)
- Core Web Vitals·이미지 lazy 로드 점검 자동화

검증된 항목만 `inposa-blog-system`으로 승격한다.
