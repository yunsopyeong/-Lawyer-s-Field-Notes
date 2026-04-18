"use client";

import { useState } from "react";

type ApiResult = {
  title: string;
  analysis: string;
  nextSteps: string[];
  warning: string;
  kakaoUrl: string;
};

export default function Home() {
  const [clientType, setClientType] = useState<"corporate" | "personal">("corporate");
  const [incomeStatus, setIncomeStatus] = useState("");
  const [debtGrowth, setDebtGrowth] = useState("예");
  const [summary, setSummary] = useState("");
  const [result, setResult] = useState<ApiResult | null>(null);
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    setLoading(true);
    setResult(null);

    const res = await fetch("/api/consult", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ clientType, incomeStatus, debtGrowth, summary })
    });

    const json = await res.json();
    setResult(json);
    setLoading(false);
  };

  return (
    <main className="wrap">
      <section className="card">
        <div className="title">{process.env.NEXT_PUBLIC_SITE_NAME || "윤소평 변호사 법률 상담"}</div>
        <p className="muted">
          질문은 최대한 간단하게 받습니다. 먼저 상황을 짧게 정리한 뒤, AI가 1차 분석 초안을 보여주고
          바로 카카오 상담으로 연결합니다.
        </p>
      </section>

      <section className="card">
        <div className="grid">
          <div className="field">
            <label>의뢰인 유형</label>
            <select value={clientType} onChange={(e) => setClientType(e.target.value as "corporate" | "personal")}>
              <option value="corporate">법인 / 대표이사</option>
              <option value="personal">개인 채무자</option>
            </select>
          </div>

          <div className="field">
            <label>소득 또는 영업 지속 여부</label>
            <input
              value={incomeStatus}
              onChange={(e) => setIncomeStatus(e.target.value)}
              placeholder="예: 영업 지속이 어렵습니다 / 급여가 있습니다"
            />
          </div>
        </div>

        <div className="field">
          <label>최근 빚이 늘었나요?</label>
          <select value={debtGrowth} onChange={(e) => setDebtGrowth(e.target.value)}>
            <option>예</option>
            <option>아니오</option>
            <option>잘 모르겠습니다</option>
          </select>
        </div>

        <div className="field">
          <label>현재 상황을 한 줄 또는 몇 줄로 적어 주세요</label>
          <textarea
            value={summary}
            onChange={(e) => setSummary(e.target.value)}
            placeholder="예: 회사 매출이 급감했고 세금과 직원 급여가 밀렸습니다."
          />
        </div>

        <div className="btns">
          <button className="btn primary" onClick={submit} disabled={loading || !summary.trim()}>
            {loading ? "분석 중..." : "1차 분석 받기"}
          </button>
          <a className="btn secondary" href={process.env.NEXT_PUBLIC_KAKAO_CHAT_URL || "#"}>
            카카오 상담 바로가기
          </a>
        </div>
      </section>

      {result && (
        <>
          <section className="card">
            <div className="title">{result.title}</div>
            <div className="result">{result.analysis}</div>
          </section>

          <section className="card">
            <div className="title">지금 확인할 사항</div>
            <ul>
              {result.nextSteps.map((item, idx) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
            <p className="warning">{result.warning}</p>
            <div className="btns" style={{ marginTop: 16 }}>
              <a className="btn secondary" href={result.kakaoUrl}>
                카카오 상담 연결
              </a>
            </div>
          </section>
        </>
      )}
    </main>
  );
}
