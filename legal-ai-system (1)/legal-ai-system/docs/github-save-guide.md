# GitHub 반자동 저장 가이드

## 1. 새 저장소 만들기
GitHub에서 새 저장소를 만든 뒤, 아래 명령으로 연결합니다.

```bash
git init
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
```

## 2. 파일 업로드
이 폴더를 저장소 루트에 복사한 뒤 아래를 실행합니다.

```bash
git add .
git commit -m "legal ai system starter package 추가"
git push -u origin main
```

## 3. 권장 다음 작업
- `.env.example` 추가
- `.gitignore` 추가
- WordPress 발행 모듈 추가
- YouTube 업로드 모듈 추가
- 테스트 코드 추가
