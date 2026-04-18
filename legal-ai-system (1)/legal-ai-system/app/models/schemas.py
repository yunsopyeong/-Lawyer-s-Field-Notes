from pydantic import BaseModel


class SourceBase(BaseModel):
    raw_text: str
    sanitized_text: str
    category: str
