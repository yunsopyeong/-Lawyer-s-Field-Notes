import os
from utils.generator import generate_content


def read_input() -> str:
    """읽기 입력 파일을 읽어 사용자 입력을 반환합니다."""
    input_path = os.path.join("data", "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def save_output(folder: str, filename: str, content: str) -> None:
    """생성된 콘텐츠를 지정된 폴더와 파일명으로 저장합니다."""
    path = os.path.join("outputs", folder, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    """콘텐츠 생성의 메인 진입점."""
    user_input = read_input()

    # 프롬프트 파일 위치
    blog_prompt_path = os.path.join("prompts", "blog_prompt.txt")
    youtube_prompt_path = os.path.join("prompts", "youtube_prompt.txt")
    thumbnail_prompt_path = os.path.join("prompts", "thumbnail_prompt.txt")

    # 콘텐츠 생성
    blog = generate_content(blog_prompt_path, user_input)
    youtube = generate_content(youtube_prompt_path, user_input)
    thumbnail = generate_content(thumbnail_prompt_path, user_input)

    # 생성된 콘텐츠 저장
    save_output("blog", "blog_post.txt", blog)
    save_output("youtube", "youtube_script.txt", youtube)
    save_output("thumbnail", "thumbnail.txt", thumbnail)

    print("✅ 콘텐츠 생성 완료!")


if __name__ == "__main__":
    main()