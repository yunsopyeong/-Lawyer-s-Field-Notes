# 윤소평 변호사 법률 콘텐츠 시스템

이 저장소는 윤소평 변호사 프로젝트를 기준으로  
대한민국 법률정보, 법률 콘텐츠, 프롬프트, 소스 자료, 운영 문서를 체계적으로 관리하기 위한 작업 저장소입니다.

회생·파산을 중심으로 하되,  
민사, 형사, 가사, 상속, 성년후견 등 관련 생활법률 콘텐츠까지 함께 다룹니다.

---

## 저장소 목적

이 저장소의 목적은 아래와 같습니다.

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
ysp-legal-content-system/
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
│  └─ messaging/
│     ├─ tone-and-style.md
│     └─ prohibited-expressions.md
│
├─ 02_prompts/
│  ├─ blog/
│  │  └─ naver-blog-main-prompt.md
│  └─ youtube/
│     └─ youtube-script-main-prompt.md
│
├─ 03_templates/
│  └─ legal-content/
│     └─ info-analysis-conclusion-template.md
│
├─ 04_topics/
│  └─ rehabilitation-bankruptcy/
│     └─ corporate-bankruptcy/
│        └─ overview.md
│
├─ 05_sources/
│  └─ court-practice/
│     └─ seoul-bankruptcy-court-guidelines.md
│
└─ 06_operations/
   └─ quality-control/
      └─ final-review-checklist.md
위 프롬프트를 해당 깃허브에 저장해 줘