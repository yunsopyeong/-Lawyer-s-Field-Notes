"""법인회생/법인파산 콘텐츠 초안 생성기.

저장소 템플릿(정보 수집 → 분석 → 결론)을 기준으로,
주제와 매체 유형에 맞는 Markdown 초안을 자동 생성합니다.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def build_title(topic: str, media: str) -> str:
    if media == "blog":
        return f"{topic}, 어떤 기준으로 판단해야 할까요"
    if media == "youtube":
        return f"{topic} 핵심 체크포인트"
    return f"{topic} 실무 가이드 초안"


def build_template(topic: str, audience: str, media: str) -> str:
    title = build_title(topic, media)

    intro = {
        "blog": "상담을 하다 보면 대표이사분들이 가장 먼저 묻는 질문이 있습니다.",
        "youtube": "오늘은 대표이사 입장에서 꼭 헷갈리는 지점을 짧게 정리해 보겠습니다.",
        "premium": "실무에서 바로 점검할 수 있도록 체크포인트 중심으로 정리합니다.",
    }[media]

    return f"""# {title}

## 정보 수집
- 질문 핵심: {topic} 진행 전 어떤 기준과 자료를 먼저 확인해야 하는지
- 독자 유형: {audience}
- 먼저 확인할 사실관계:
  - 현재 영업 지속 가능성
  - 최근 6개월 자금흐름
  - 연체·압류·체불임금·세금 현황
  - 대표이사 개인 연대보증 여부
- 필요한 법령/판례/공식자료:
  - 채무자 회생 및 파산에 관한 법률(최신 확인 필요)
  - 법원 실무준칙(법원별 운영 차이 확인 필요)
- 지금 가장 중요한 쟁점:
  - 회사 절차(회생/파산)와 대표이사 개인문제를 분리해서 볼 것인지

> {intro}

## 분석
### 1. 적용되는 제도 또는 법률
- 법인회생은 계속기업가치, 수행 가능성, 자금흐름을 중심으로 판단합니다.
- 법인파산은 청산가치와 채권자 배당 가능성, 자료 정리 수준이 중요합니다.
- 사안에 따라 달라질 수 있으므로 서류 확인 전 단정은 어렵습니다.

### 2. 핵심 판단 기준
- 계속 영업 가능성
- 채권자 조정 가능성
- 대표이사 협조 가능성(자료 제출, 통장 흐름 소명 등)
- 세금·체불임금·편파변제 리스크

### 3. 실무상 자주 오해하는 부분
1) 폐업신고와 법인파산을 같은 것으로 보는 오해
2) 법인 절차를 하면 대표이사 개인채무도 자동 정리된다고 보는 오해
3) 자료 준비 없이 먼저 신청하면 된다고 생각하는 오해

### 4. 예외 또는 주의사항
- 법원별 운영 방식 차이가 있을 수 있어 최신 실무기준 확인이 필요합니다.
- 최근 자산 처분이나 특정 채권자 우선변제가 있으면 별도 검토가 필요합니다.
- 형사 이슈와 연결될 가능성은 사실관계에 따라 달라질 수 있습니다.

## 결론
- 핵심 정리: {topic}는 절차명보다 사실관계와 자료 정리가 먼저입니다.
- 지금 확인할 체크포인트:
  1) 최근 1년 회계·통장 자료
  2) 세금·체불임금·연대보증 현황
  3) 주요 채권자 리스트와 대응 이력
- 다음 행동:
  - 내부 자료 목록표부터 만들고 누락 서류를 보완합니다.
  - 회생/파산을 나누기 전에 "계속 영업 가능성"을 먼저 점검합니다.

## FAQ 초안
- Q1. 폐업만 하면 회사 채무 문제가 끝나나요?
- Q2. 법인파산을 하면 대표이사 개인보증도 같이 정리되나요?
- Q3. 회생과 파산 중 무엇을 먼저 검토해야 하나요?

## 내부 링크 후보
- 법인회생 준비서류 체크리스트
- 법인파산 절차와 기간 정리
- 대표이사 개인책임(연대보증, 세금, 체불임금) 점검 포인트
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="법인회생/파산 콘텐츠 마크다운 초안을 생성합니다."
    )
    parser.add_argument("topic", help="예: 법인파산 준비서류, 기업회생 신청 기준")
    parser.add_argument(
        "--audience",
        default="대표이사/사업주",
        help="예상 독자 유형 (기본값: 대표이사/사업주)",
    )
    parser.add_argument(
        "--media",
        choices=["blog", "youtube", "premium"],
        default="blog",
        help="출력 매체 유형 (기본값: blog)",
    )
    parser.add_argument(
        "--output",
        default="",
        help="저장할 파일 경로. 생략하면 표준출력으로만 보여줍니다.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    markdown = build_template(args.topic, args.audience, args.media)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        print(f"초안을 저장했습니다: {output_path}")
        return

    print(markdown)


if __name__ == "__main__":
    main()
