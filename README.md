# Legal Content Automation

이 저장소는 키워드 또는 상담 내용을 입력하면 네이버 블로그 글과 유튜브 대본, 썸네일 문구를 자동으로 생성하고 저장하는 시스템의 기본 엔진을 제공합니다. 또한 옵션에 따라 생성된 블로그 글을 네이버 블로그에 자동으로 업로드할 수 있는 스크립트도 포함하고 있습니다.

## 기능

1. **콘텐츠 생성**
   - `data/input.txt` 파일에 입력된 키워드 또는 상담 내용을 바탕으로 GPT‑모델을 호출하여 네이버 블로그 글, 유튜브 대본, 썸네일 문구를 생성합니다.
   - 생성된 결과는 `outputs/` 폴더 아래에 각각 `blog_post.txt`, `youtube_script.txt`, `thumbnail.txt`로 저장됩니다.

2. **네이버 블로그 자동 업로드**
   - `utils/blog_uploader.py` 스크립트는 Selenium을 사용하여 네이버에 로그인하고 생성된 블로그 글을 자동으로 게시합니다.
   - 사용자는 환경변수로 네이버 로그인 정보를 제공해야 하며, 게시 전에 크롬 드라이버가 설치되어 있어야 합니다.

## 실행 방법

### 1. 가상환경 생성 및 패키지 설치

```sh
pip install -r requirements.txt
```

### 2. 환경변수 설정 (.env)

아래와 같이 `.env` 파일을 생성하거나 운영 체제 환경변수에 추가합니다. GPT API 키와 네이버 계정 정보가 필요합니다.

```env
OPENAI_API_KEY=your_openai_api_key
NAVER_ID=your_naver_id
NAVER_PASSWORD=your_naver_password
```

> **주의:** 네이버는 자동화 로그인 시 CAPTCHA가 발생할 수 있습니다. 스크립트 실행 중 캡차가 나타나면 수동으로 해결해야 합니다.

### 3. 콘텐츠 생성 실행

`data/input.txt` 파일에 키워드 또는 상담 내용을 입력한 다음 아래 명령을 실행합니다.

```sh
python main.py
```

실행 후 `outputs/` 폴더에 결과가 저장되며, 커맨드라인에는 `✅ 콘텐츠 생성 완료!` 메시지가 출력됩니다.

### 4. 네이버 블로그 업로드 (선택 사항)

콘텐츠를 생성한 후 `utils/blog_uploader.py` 스크립트를 실행하면 `outputs/blog/blog_post.txt` 파일의 제목과 내용을 이용해 네이버 블로그에 글을 올립니다.

```sh
python utils/blog_uploader.py
```

스크립트는 네이버 로그인 후 블로그 작성 페이지로 이동하여 제목과 본문을 입력하고 발행합니다. 환경에 따라 버튼 위치나 요소 ID가 달라질 수 있으므로 필요에 따라 셀렉터를 조정해야 합니다.

## 프로젝트 구조

```
legal-content-automation/
│
├── README.md                # 설명서
├── requirements.txt         # Python 패키지 목록
├── main.py                 # 콘텐츠 생성 메인 실행 파일
│
├── data/
│   └── input.txt            # 입력 키워드/상담 내용
│
├── outputs/
│   ├── blog/
│   │   └── blog_post.txt    # 생성된 블로그 글
│   ├── youtube/
│   │   └── youtube_script.txt # 생성된 유튜브 대본
│   └── thumbnail/
│       └── thumbnail.txt    # 생성된 썸네일 문구
│
├── prompts/
│   ├── blog_prompt.txt       # 블로그 글 생성 프롬프트
│   ├── youtube_prompt.txt    # 유튜브 대본 생성 프롬프트
│   └── thumbnail_prompt.txt  # 썸네일 문구 생성 프롬프트
│
└── utils/
    ├── generator.py          # GPT를 호출하여 콘텐츠 생성
    └── blog_uploader.py      # Selenium을 통한 네이버 블로그 자동 업로드
```

## 확장 아이디어

이 기본 엔진을 바탕으로 다음과 같이 확장할 수 있습니다.

- 키워드 목록을 CSV로 받아 연속적으로 여러 개의 콘텐츠를 생성
- 워드/HTML/PDF 파일로 변환해 저장
- 썸네일 이미지를 생성하는 API와 연동 (예: Canva API)
- 네이버 블로그 외에 다른 플랫폼(티스토리, 워드프레스 등)에도 자동 업로드
- 상담 내용을 분석하여 자동으로 법률 서면 초안을 작성하는 기능

실제 업무에 적용 시 자동화에 따른 계정 사용 정책을 반드시 준수하시기 바랍니다.