import { buildConsultPrompt } from "@/lib/prompts";
import { getOpenAIClient } from "@/lib/openai";

function fallbackResult(input: any) {
  const caseGuess =
    input.clientType === "corporate"
      ? input.incomeStatus.includes("낮") || input.incomeStatus.includes("중단")
        ? "법인파산 쪽 검토가 먼저 필요해 보입니다."
        : "법인회생 가능성부터 검토해 볼 여지가 있습니다."
      : input.incomeStatus.includes("있")
      ? "개인회생 가능성부터 검토해 볼 여지가 있습니다."
      : "개인파산 방향 검토가 먼저 필요해 보입니다.";

  return {
    title: "상담 1차 분석 결과",
    analysis: [
      "정보 수집",
      `- 의뢰인 유형: ${input.clientType === "corporate" ? "법인/대표이사" : "개인 채무자"}`,
      `- 소득 또는 영업 지속 여부: ${input.incomeStatus}`,
      `- 최근 채무 증가 여부: ${input.debtGrowth}`,
      `- 상담 요약: ${input.summary}`,
      "",
      "분석",
      `- ${caseGuess}`,
      "- 제출자료와 사실관계에 따라 결론이 달라질 수 있습니다.",
      "- 최근 채무 발생 경위, 재산 보유 현황, 압류·독촉 여부를 함께 봐야 합니다.",
      "",
      "결론",
      "- 지금 단계에서는 혼자 절차를 단정하기보다 자료를 먼저 정리하는 것이 안전합니다."
    ].join("\n"),
    nextSteps: [
      "최근 대출·카드 사용 내역 정리",
      "재산·보증금·연대보증 여부 확인",
      "채권자 독촉 또는 압류 진행 여부 확인"
    ],
    warning: "이 결과는 변호사 검토 전 임시 초안입니다. 자동 생성 결과만으로 최종 법률판단을 확정하지 않습니다.",
    kakaoUrl: process.env.KAKAO_CHAT_URL || "#"
  };
}

export async function POST(req: Request) {
  const input = await req.json();

  try {
    const client = getOpenAIClient();
    const prompt = buildConsultPrompt(input);

    const response = await client.responses.create({
      model: "gpt-4.1-mini",
      input: prompt
    });

    const result = fallbackResult(input);
    if (response.output_text && response.output_text.trim()) {
      result.analysis = response.output_text.trim();
    }
    return Response.json(result);
  } catch {
    return Response.json(fallbackResult(input));
  }
}
