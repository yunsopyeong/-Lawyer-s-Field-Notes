from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

import fitz  # PyMuPDF


@dataclass
class PDFPageText:
    page_number: int
    text: str


@dataclass
class PDFDocumentText:
    path: Path
    pages: List[PDFPageText]

    @property
    def full_text(self) -> str:
        return "\n".join(p.text for p in self.pages)


def extract_text_from_pdf(pdf_path: Path) -> PDFDocumentText:
    pdf_path = Path(pdf_path)
    pages: List[PDFPageText] = []

    with fitz.open(pdf_path) as doc:
        for i, page in enumerate(doc, start=1):
            text = page.get_text("text") or ""
            pages.append(PDFPageText(page_number=i, text=text.strip()))

    return PDFDocumentText(path=pdf_path, pages=pages)


def collect_pdf_files(input_dir: Path) -> List[Path]:
    input_dir = Path(input_dir)
    return sorted(p for p in input_dir.glob("*.pdf") if p.is_file())
