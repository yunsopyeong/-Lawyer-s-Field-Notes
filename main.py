"""
네이버 블로그 자동 업로드 스크립트.

이 스크립트는 Selenium을 사용하여 네이버 블로그에 로그인한 뒤
`outputs/blog/blog_post.txt`에 저장된 글을 새로운 포스트로 게시합니다.
네이버는 공식적인 블로그 글쓰기 API를 제공하지 않으므로 브라우저 자동화를
사용해야 하며, 실행 중 캡차나 OTP 입력이 요구될 수 있습니다.

사용 전 준비:
1. `requirements.txt`에 명시된 `selenium`과 `webdriver-manager` 패키지를 설치합니다.
2. `.env` 파일에 NAVER_ID, NAVER_PASSWORD 환경변수를 설정합니다.
3. Chrome 브라우저가 설치되어 있어야 합니다. 필요 시 Chromedriver가 자동 다운로드됩니다.

참고: 셀렉터와 페이지 구조는 네이버 업데이트에 따라 변경될 수 있습니다. 동작하지 않을 경우
네이버 블로그 글쓰기 페이지의 요소 ID나 클래스명을 확인 후 수정해야 합니다.
"""

import os
import time
from typing import Tuple

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def read_blog_post() -> Tuple[str, str]:
    """blog_post.txt 파일을 읽어 제목과 본문을 분리하여 반환한다.

    제목은 첫 번째 줄로 간주하고, 본문은 두 번째 줄부터 끝까지 합친다.

    Returns:
        Tuple[str, str]: (title, body)
    """
    path = os.path.join("outputs", "blog", "blog_post.txt")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        raise ValueError("blog_post.txt 파일에 내용이 없습니다.")

    title = lines[0].strip()
    body = "".join(lines[1:]).strip()
    return title, body


def upload_post():
    """네이버 블로그에 게시물을 업로드한다."""
    load_dotenv()
    naver_id = os.getenv("NAVER_ID")
    naver_pw = os.getenv("NAVER_PASSWORD")

    if not naver_id or not naver_pw:
        raise EnvironmentError("NAVER_ID 또는 NAVER_PASSWORD 환경변수가 설정되지 않았습니다.")

    title, body = read_blog_post()

    # Selenium WebDriver 설정
    options = webdriver.ChromeOptions()
    # 필요한 경우 headless 모드 활성화: GUI 없이 실행
    # options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 네이버 로그인 페이지로 이동
        driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(2)

        # 아이디와 비밀번호 입력
        id_input = driver.find_element(By.ID, "id")
        pw_input = driver.find_element(By.ID, "pw")

        id_input.send_keys(naver_id)
        pw_input.send_keys(naver_pw)
        pw_input.send_keys(Keys.RETURN)

        # 로그인 처리 대기
        time.sleep(3)

        # 블로그 글쓰기 페이지로 이동
        driver.get("https://blog.naver.com/PostWriteForm.naver")
        time.sleep(5)

        # 제목 입력 (네이버 블로그 글쓰기 페이지에서 제목 입력 필드의 ID는 subject)
        title_input = driver.find_element(By.ID, "subject")
        title_input.clear()
        title_input.send_keys(title)

        # 본문 편집기 iframe 내부로 이동
        # 구버전 스마트에디터2 기준 iframe id는 "se2_iframe"
        # 신버전은 #editorFrame 또는 #se2_ifr 같은 구조를 사용한다. 필요에 따라 수정.
        try:
            editor_frame = driver.find_element(By.ID, "se2_iframe")
        except Exception:
            try:
                editor_frame = driver.find_element(By.CSS_SELECTOR, "iframe[id*='se2_']")
            except Exception:
                # 새 에디터의 경우 editorFrame
                editor_frame = driver.find_element(By.ID, "editorFrame")

        driver.switch_to.frame(editor_frame)
        time.sleep(2)

        # 본문 입력 (iframe 내부 body 클릭 후 send_keys)
        body_area = driver.find_element(By.CSS_SELECTOR, "body")
        body_area.click()
        # Ctrl+A 후 삭제하여 빈 상태를 보장
        body_area.send_keys(Keys.CONTROL, 'a')
        body_area.send_keys(Keys.DELETE)
        body_area.send_keys(body)

        # 기본 프레임으로 복귀
        driver.switch_to.default_content()

        # 발행 버튼 클릭
        # 구버전: writeSubmitBtn 또는 btn_register
        try:
            publish_btn = driver.find_element(By.ID, "btn_publish")
        except Exception:
            try:
                publish_btn = driver.find_element(By.ID, "writeSubmit")
            except Exception:
                # 클래스명이 있을 경우
                publish_btn = driver.find_element(By.CSS_SELECTOR, "button.btn_register")
        publish_btn.click()

        print("✅ 블로그 업로드 완료!")

        # 게시 완료 확인 대기
        time.sleep(5)

    finally:
        driver.quit()


if __name__ == "__main__":
    upload_post()