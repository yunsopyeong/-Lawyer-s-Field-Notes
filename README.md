# 윤소평 변호사 법률 AI 에이전트 프로젝트

이 저장소는 윤소평 변호사 프로젝트를 기준으로  
대한민국 법률정보, 법률 콘텐츠, 프롬프트, 소스 자료, 운영 문서를 체계적으로 관리하기 위한 작업 저장소입니다.

회생·파산을 중심으로 하되,  
민사, 형사, 가사, 상속, 성년후견 등 관련 생활법률 콘텐츠까지 함께 다룹니다.

---

## 저장소 목적

- 법률 콘텐츠 초안과 최종본을 분리해 관리
- 네이버 블로그, 브런치, 네이버 프리미엄콘텐츠, 유튜브 대본을 주제별로 축적
- 커스텀 GPT용 프롬프트와 내부 운영 기준을 정리
- 법령, 판례, 공식자료, 실무준칙, 내부 요약본을 소스 형태로 관리
- 반복 가능한 법률 콘텐츠 생산 구조를 만드는 것

---

## 핵심 원칙

이 저장소의 모든 문서와 결과물은 아래 원칙을 기본으로 합니다.

- 대한민국 법령, 판례, 공식자료를 우선 반영합니다.
- 회생·파산 분야는 서울회생법원 실무준칙도 함께 고려합니다.
- 답변과 원고는 정보 수집 → 분석 → 결론 구조를 기본으로 합니다.
- 과장광고, 단정 표현, 공포 조장 문구는 사용하지 않습니다.
- 질문과 직접 관련 있을 때만 참고자료 링크를 연결합니다.
- 원고는 실제 상담을 해 본 변호사의 문장처럼 차분하고 쉽게 설명합니다.

---

## 저장소 구조 예시

```text
-Lawyer-s-Field-Notes/
├─ README.md
├─ AGENTS.md
├─ .gitignore
├─ .github/
│  ├─ pull_request_template.md
│  └─ ISSUE_TEMPLATE/
│     ├─ config.yml
│     ├─ blog-content-request.md
│     ├─ youtube-script-request.md
│     ├─ source-update.md
│     └─ hotfix.md
│
├─ 01_brand/
├─ 02_prompts/
├─ 03_templates/
├─ 04_topics/
├─ 05_sources/
└─ 06_operations/
   └─ codex/
      └─ codex-task-list.md
```

---

## 운영 문서

이 저장소는 아래 운영 문서를 기준으로 관리합니다.

- [코덱스 업무 정리 (Codex Task List)](./06_operations/codex/codex-task-list.md)

---

## 브랜치 운영 규칙

이 저장소는 `main` 브랜치를 최종본 보관용으로 사용합니다.  
초안, 수정, 실험 작업은 반드시 별도 브랜치에서 진행합니다.

### 기본 원칙
- `main`은 최종 승인된 문서만 반영합니다.
- 직접 `main`에서 작업하지 않습니다.
- 모든 수정은 작업 브랜치에서 진행한 뒤 Pull Request로 병합합니다.
- 작업이 끝난 브랜치는 병합 후 삭제합니다.

### 브랜치 이름 규칙
- `draft/blog-*` : 네이버 블로그 원고 작업
- `draft/youtube-*` : 유튜브 대본 작업
- `draft/prompt-*` : 프롬프트 수정
- `draft/source-*` : 소스 자료 정리
- `hotfix/*` : 긴급 수정

---

## AGENTS.md 운영 원칙

이 저장소는 Codex와 함께 작업할 수 있도록 프로젝트 전용 지침 파일인 `AGENTS.md`를 사용합니다.

`AGENTS.md`는 이 저장소에서 문서를 만들거나 수정할 때 따라야 하는 기본 기준을 정리한 파일입니다.  
쉽게 말하면, 사람에게는 운영 매뉴얼이고 Codex에게는 프로젝트별 작업 기준서에 가깝습니다.

---
# GitHub 자동저장 운영 매뉴얼
## 연결 제한이 있을 때도 가장 덜 번거로운 방식

## 1. 이 매뉴얼의 목적

이 매뉴얼은 ChatGPT 프로젝트에서 만든 결과물을
가장 적은 수작업으로 GitHub에 저장하고,
가능하면 Codex까지 연결해 자동화하는 운영 기준서이다.

핵심 원칙은 아래와 같다.

- 일반 ChatGPT의 GitHub 연결은 읽기·검색·분석 중심으로 사용한다.
- 실제 저장, 덮어쓰기, push는 Codex 또는 GitHub 업로드로 처리한다.
- 자동저장이 막히면 “업로드용 ZIP 1개” 방식으로 우회한다.
- 같은 작업을 반복하지 않도록 저장 경로와 파일명을 먼저 고정한다.

---

## 2. 가장 현실적인 운영 방식

### 기본 구조
1. ChatGPT에서 문서/코드 생성
2. 결과물을 ZIP 또는 파일 세트로 받음
3. GitHub 저장소에 업로드
4. Vercel 등 배포 도구가 자동 반영

### 원칙
- ChatGPT는 초안 생성기
- GitHub는 원본 저장소
- Codex는 push 가능한 자동화 도구
- Vercel은 배포 도구

즉,
문서 작성은 ChatGPT,
저장과 버전관리는 GitHub,
자동 반영은 Vercel로 나눈다.

---

## 3. 연결 제한이 있을 때 표준 절차

### A안. 가장 간단한 방식
- ChatGPT에게 “GitHub 업로드용 ZIP으로 만들어 달라”고 요청
- ZIP 다운로드
- GitHub에서 업로드
- 끝

이 방식은 가장 단순하고 실패가 적다.

### B안. Codex 연결 방식
- Codex에 저장소를 연결
- ChatGPT가 만든 파일 본문을 Codex에 전달
- Codex가 브랜치 생성 → 파일 생성/수정 → 커밋 → PR 생성
- 사용자는 GitHub에서 PR 확인 후 merge

이 방식이 진짜 자동저장에 가장 가깝다.

---

## 4. 내가 항상 써야 할 요청 문구

### 4-1. ChatGPT에 요청할 문구
아래 결과물을 GitHub 업로드용으로 만들어줘.

조건:
- 파일별로 분리
- 저장 경로 포함
- ZIP으로 묶기
- README 또는 운영 문서에 연결 문구 포함
- 바로 GitHub에 올릴 수 있게 만들기

### 4-2. Codex에 요청할 문구
아래 파일들을 내 GitHub 저장소에 반영해줘.

작업:
- 새 브랜치 생성
- 지정 경로에 파일 생성 또는 수정
- 커밋 메시지 작성
- PR 생성

기준:
- main 직접 수정 금지
- draft/ 또는 hotfix/ 브랜치 사용
- 한 PR에는 한 주제만
- README 링크까지 함께 반영

---

## 5. GitHub 저장소에 어디에 붙여넣는가

### 운영 문서
- `06_operations/workflow/`
- `06_operations/codex/`
- `06_operations/quality-control/`

### 프롬프트
- `02_prompts/blog/`
- `02_prompts/youtube/`
- `02_prompts/consultation/`

### 템플릿
- `03_templates/intake/`
- `03_templates/blog/`
- `03_templates/youtube/`
- `03_templates/legal-content/`

### 웹 서비스 코드
- `web/app/`
- `web/app/api/`
- `web/lib/`

### 자동화 도구
- `tools/`

### GitHub 설정 파일
- `.github/workflows/`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`

---

## 6. 파일별 복붙 위치

### README 전체 교체본
붙여넣는 곳:
- 저장소 루트 `README.md`

### AGENTS 기준서
붙여넣는 곳:
- 저장소 루트 `AGENTS.md`

### 상담 자동화 파이프라인 문서
붙여넣는 곳:
- `06_operations/workflow/consultation-pipeline.md`

### Codex 업무 문서
붙여넣는 곳:
- `06_operations/codex/codex-task-list.md`

### 상담폼 웹페이지
붙여넣는 곳:
- `web/app/page.tsx`

### 상담 API
붙여넣는 곳:
- `web/app/api/consult/route.ts`

### 프롬프트 로직
붙여넣는 곳:
- `web/lib/prompts.ts`

### OpenAI 연결 코드
붙여넣는 곳:
- `web/lib/openai.ts`

### 로컬 자동화 스크립트
붙여넣는 곳:
- `tools/build_content_bundle.py`

### 자동 배포 워크플로
붙여넣는 곳:
- `.github/workflows/vercel-check.yml`

---

## 7. GitHub에서 실제 업로드하는 순서

### 새 파일 업로드
1. 저장소 열기
2. Add file
3. Upload files
4. ZIP을 푼 파일들을 드래그
5. Commit changes

### 기존 파일 교체
1. 해당 파일 열기
2. Edit 버튼 클릭
3. 전체 삭제
4. 새 본문 붙여넣기
5. Commit changes

---

## 8. 커밋 메시지 규칙

금지:
- update
- fix
- 수정
- 변경

권장:
- `[운영] README 전체 교체`
- `[운영] AGENTS.md 추가`
- `[자동화] 상담폼 + AI 분석 구조 추가`
- `[배포] Vercel 자동배포 워크플로 추가`
- `[운영] 코덱스 업무 문서 추가`

---

## 9. 브랜치 규칙

- `main` = 최종본
- `draft/...` = 일반 작업
- `hotfix/...` = 긴급 수정

예시:
- `draft/readme-final`
- `draft/legal-ai-web`
- `draft/consultation-pipeline`
- `hotfix/kakao-link-fix`

---

## 10. Codex까지 붙일 때의 운영 방식

### 추천 흐름
1. ChatGPT에서 파일 초안 생성
2. 파일 세트를 ZIP 또는 본문으로 확보
3. Codex에 “이 파일들을 저장소에 반영” 요청
4. Codex가 브랜치 생성
5. Codex가 커밋
6. Codex가 PR 생성
7. GitHub에서 merge

### 장점
- 수동 복붙을 크게 줄일 수 있다
- 기존 파일 덮어쓰기에도 강하다
- PR 단위로 검토가 가능하다

---

## 11. 연결이 안 될 때 점검할 것

1. ChatGPT에서 Settings → Apps → GitHub 확인
2. 저장소 접근 권한이 맞는지 확인
3. 새 저장소라면 5분 정도 기다리기
4. GitHub에서 저장소 접근 범위 다시 선택
5. 그래도 안 되면 ZIP 업로드 방식으로 우회

---- [GitHub 자동저장 운영 매뉴얼](./06_operations/workflow/github-auto-save-manual.md)

## 12. 최종 원칙

- 일반 ChatGPT GitHub 연결은 읽기 중심으로 생각한다.
- 쓰기/푸시 자동화는 Codex 기준으로 설계한다.
- 연결 제한이 있으면 ZIP 1회 업로드 방식으로 우회한다.
- 저장 경로를 먼저 고정하고, 그 다음 본문을 만든다.

## 한 줄 정리

연결 제한이 있을 때 가장 덜 번거로운 방식은
“ChatGPT가 GitHub 업로드용 파일 세트 또는 ZIP 생성 → GitHub 업로드 또는 Codex로 PR 생성”
구조로 운영하는 것이다.
## 최종 한 줄 정리

이 저장소는  
윤소평 변호사 법률 콘텐츠 시스템의 기준 문서, 소스 자료, 프롬프트, 발행형 원고를  
안전하고 일관되게 관리하기 위한 운영 저장소입니다.
