from fastapi import APIRouter
from pydantic import BaseModel

from app.services.generator import generate_blog
from app.services.sanitizer import sanitize_text
from app.services.classifier import classify

router = APIRouter()


class ContentRequest(BaseModel):
    content: str


@router.post("/generate/blog")
def create_blog(payload: ContentRequest) -> dict:
    clean = sanitize_text(payload.content)
    category = classify(clean)
    result = generate_blog(clean, category=category)
    return {"category": category, "result": result}
