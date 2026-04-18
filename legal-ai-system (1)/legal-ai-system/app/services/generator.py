from openai import OpenAI

client = OpenAI()


def generate_blog(text: str, category: str = "기타") -> str:
    prompt = f"""
아래 내용을 대한민국 변호사가 설명하는 블로그 글로 작성해 주세요.

구조:
- 정보 수집
- 분석
- 결론

조건:
- 상담형 도입부
- 실무상 오해 포인트 2개 이상
- 단정 표현 지양
- 분야: {category}

내용:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "당신은 대한민국 법률 콘텐츠를 작성하는 보조 도구입니다."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content or ""
