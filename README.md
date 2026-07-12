# 감정평가 노트

상속·경매·전세까지, 부동산 감정평가 실무 노트.

**사이트:** [https://appraisal-note.inposa.net/](https://appraisal-note.inposa.net/)

[Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod) · GitHub Pages

**주제:** 감정평가 기초 · 서류·권리 · 상속·절세 · 경매·전세

## 콘텐츠 관리

발행 계획·글 작성·검수는 `content-engine/` 폴더에서 관리합니다.

- **발행 목록:** `content-engine/content-plan.csv`
- **시작 가이드:** `content-engine/README.md`

## 로컬 미리보기

```bash
hugo server -D
```

`baseURL`이 프로덕션 도메인으로 설정되어 있으므로, 로컬에서는 [http://localhost:1313/](http://localhost:1313/) 로 접속합니다.

## 사이트 빌드

```bash
hugo --minify
```

빌드 결과는 `public/` 폴더에 생성됩니다.

## 테마 업데이트

```bash
git submodule update --remote --merge themes/PaperMod
```

## 도메인

- **프로덕션:** `appraisal-note.inposa.net` (`static/CNAME`)
- DNS: `appraisal-note` CNAME → `inposamaster.github.io`
- GitHub Pages → Settings → Custom domain → Enforce HTTPS

내부 링크·이미지는 루트 상대경로(`/posts/…`, `/images/…`)를 사용합니다.
