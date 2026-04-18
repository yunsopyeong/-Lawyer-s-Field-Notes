# Legal AI Content System

이 프로젝트는 법률 상담, 키워드, 자료를 기반으로 블로그 및 유튜브 콘텐츠를 자동 생성하고 관리하는 시스템입니다.

## 핵심 기능

- 상담 → 콘텐츠 자동 변환
- 블로그 자동 초안 생성
- 유튜브 대본 자동 생성
- 법률 근거 보강
- 승인 기반 발행 시스템

## 기본 구조

입력 → 분석 → 생성 → 검수 → 승인 → 발행

## 폴더 구조

```text
legal-ai-system/
├── README.md
├── requirements.txt
├── main.py
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── generator.py
│   │   ├── sanitizer.py
│   │   └── classifier.py
│   ├── models/
│   │   └── schemas.py
│   └── db/
│       └── database.py
├── data/
│   ├── intake/
│   ├── drafts/
│   ├── approved/
│   └── published/
├── prompts/
│   ├── blog.txt
│   └── youtube.txt
├── dashboard/
│   └── wireframe.md
├── sql/
│   └── schema.sql
└── docs/
    └── github-save-guide.md
```

## 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate  # Windows는 .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 환경 변수

아래 환경 변수를 설정해 두는 것을 권장합니다.

- `OPENAI_API_KEY`: OpenAI API 키
- `DATABASE_URL`: PostgreSQL 접속 문자열

## 현재 상태

이 패키지는 MVP 스타터입니다. 실제 운영 전에는 아래를 추가로 붙이는 것이 좋습니다.

- WordPress 자동 발행 API
- YouTube 비공개 업로드 API
- 관리자 승인 화면
- 로그 및 예외처리
- 테스트 코드
