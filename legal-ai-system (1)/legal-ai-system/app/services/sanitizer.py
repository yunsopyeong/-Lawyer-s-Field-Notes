import re


def sanitize_text(text: str) -> str:
    text = re.sub(r"\\d{2,3}-\\d{3,4}-\\d{4}", "[전화번호]", text)
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", "[이메일]", text)
    text = re.sub(r"\\b\\d{6}-\\d{7}\\b", "[주민등록번호]", text)
    return text
