from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ClassifiedPDF:
    path: Path
    document_type: str
    year: int | None


DOC_KEYWORDS = {
    "결산보고서": ["재무상태표", "손익계산서", "결산보고서"],
    "부가가치세자료": ["부가가치세", "과세표준"],
    "납세증명서": ["납세증명서"],
    "4대보험자료": ["4대보험", "국민연금", "건강보험"],
}


def _find_year(text: str) -> int | None:
    for token in text.split():
        if token.endswith("년") and token[:-1].isdigit() and len(token[:-1]) == 4:
            return int(token[:-1])
    return None


def classify_document(path: Path, text: str) -> ClassifiedPDF:
    doc_type = "기타"
    for name, keys in DOC_KEYWORDS.items():
        if any(k in text for k in keys):
            doc_type = name
            break
    return ClassifiedPDF(path=path, document_type=doc_type, year=_find_year(text))
