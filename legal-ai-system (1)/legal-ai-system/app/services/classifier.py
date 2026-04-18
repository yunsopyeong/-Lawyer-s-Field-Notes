def classify(text: str) -> str:
    if "법인파산" in text or "기업파산" in text or "파산" in text:
        return "법인파산/개인파산"
    if "법인회생" in text or "기업회생" in text or "간이회생" in text or "일반회생" in text or "개인회생" in text or "회생" in text:
        return "회생"
    if "상속" in text or "한정승인" in text:
        return "상속"
    if "음주운전" in text:
        return "음주운전"
    return "기타"
