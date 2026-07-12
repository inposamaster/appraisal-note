# 감정평가 노트

상속·경매·전세까지, 부동산 감정평가 실무 노트.

[Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod) · [GitHub Pages](https://inposamaster.github.io/appraisal-note/)

**주제:** 감정평가 기초 · 서류·권리 · 상속·절세 · 경매·전세

## 콘텐츠 관리

발행 계획·글 작성·검수는 `content-engine/` 폴더에서 관리합니다.

- **발행 목록:** `content-engine/content-plan.csv`
- **시작 가이드:** `content-engine/README.md`

## 로컬 미리보기

```bash
cd appraisal-note
hugo server -D
```

브라우저에서 [http://localhost:1313/appraisal-note/](http://localhost:1313/appraisal-note/) 로 접속합니다.

## 사이트 빌드

```bash
hugo
```

빌드 결과는 `public/` 폴더에 생성됩니다.

## 테마 업데이트

```bash
git submodule update --remote --merge themes/PaperMod
```
