import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

# 전역 클라이언트 인스턴스 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_prompt(prompt_path: str) -> str:
    """프롬프트 파일을 읽어 문자열로 반환합니다."""
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def generate_content(prompt_path: str, user_input: str) -> str:
    """지정된 프롬프트 파일과 사용자 입력을 결합하여 GPT API로 콘텐츠를 생성합니다."""
    prompt = load_prompt(prompt_path)
    full_prompt = f"""
{prompt}

[사용자 입력]
{user_input}
"""

    response = client.chat.completions.create(
        model="gpt-5.3",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content