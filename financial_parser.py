from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
import re
from typing import List


@dataclass
class FinancialRecord:
    year: int
    company_name: str
    document_type: str
    account_name: str
    amount: float
    major_category: str
    sub_category: str
    is_total: bool


AMOUNT_PATTERN = re.compile(r"(-?\d{1,3}(?:,\d{3})*(?:\.\d+)?)")


def parse_financial_statements(text: str, year_hint: int | None) -> List[FinancialRecord]:
    records: List[FinancialRecord] = []
    year = year_hint or 0
    doc_type = "결산보고서"
    company = "미상"

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if "주식회사" in line or "유한회사" in line:
            company = line

        if "재무상태표" in line:
            current_section = "재무상태표"
            continue
        if "손익계산서" in line:
            current_section = "손익계산서"
            continue

        m = AMOUNT_PATTERN.search(line)
        if not m:
            continue

        amount = float(m.group(1).replace(",", ""))
        account = line[: m.start()].strip(" :\t") or "미상계정"
        is_total = "합계" in account or "총계" in account
        records.append(
            FinancialRecord(
                year=year,
                company_name=company,
                document_type=doc_type,
                account_name=account,
                amount=amount,
                major_category=locals().get("current_section", "기타"),
                sub_category="",
                is_total=is_total,
            )
        )

    return records


def write_records_json_csv(records: List[FinancialRecord], output_dir: Path) -> tuple[Path, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "parsed_financials.json"
    csv_path = output_dir / "parsed_financials.csv"

    data = [asdict(r) for r in records]
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()) if data else [
            "year", "company_name", "document_type", "account_name", "amount", "major_category", "sub_category", "is_total"
        ])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return json_path, csv_path
