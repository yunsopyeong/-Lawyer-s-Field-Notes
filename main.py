from __future__ import annotations

from datetime import datetime
from pathlib import Path

from excel_autofill import autofill_financials
from excel_template_analyzer import analyze_template
from financial_parser import parse_financial_statements, write_records_json_csv
from pdf_classifier import classify_document
from pdf_reader import collect_pdf_files, extract_text_from_pdf
from validation import validate_excel_errors


def run() -> None:
    base = Path.cwd()
    input_pdf_dir = base / "INPUT" / "PDF"
    template_path = base / "INPUT" / "template.xlsx"

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_root = base / "OUTPUT" / f"RESULT_{ts}"
    out_root.mkdir(parents=True, exist_ok=True)

    records = []
    for pdf in collect_pdf_files(input_pdf_dir):
        doc = extract_text_from_pdf(pdf)
        classified = classify_document(pdf, doc.full_text)
        if classified.document_type != "결산보고서":
            continue
        records.extend(parse_financial_statements(doc.full_text, classified.year))

    write_records_json_csv(records, out_root)

    analysis = analyze_template(template_path)
    autofill_financials(
        template_path=template_path,
        output_xlsx_path=out_root / "autofilled.xlsx",
        records=records,
        analysis=analysis,
        unmatched_log_path=out_root / "확인필요_미매칭항목.txt",
    )

    validate_excel_errors(out_root / "autofilled.xlsx", out_root / "오류검사결과.txt")
    print(f"완료: {out_root}")


if __name__ == "__main__":
    run()
