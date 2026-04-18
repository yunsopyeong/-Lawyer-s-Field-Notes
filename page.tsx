* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; font-family: Arial, sans-serif; background: #fafafa; color: #111; }
.wrap { max-width: 920px; margin: 0 auto; padding: 40px 20px; }
.card { background: white; border-radius: 18px; padding: 24px; box-shadow: 0 8px 24px rgba(0,0,0,.06); margin-bottom: 20px; }
.title { font-size: 28px; font-weight: 700; margin-bottom: 8px; }
.muted { color: #555; line-height: 1.6; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.field { display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px; }
.field input, .field select, .field textarea { border: 1px solid #d0d0d0; border-radius: 10px; padding: 12px; font-size: 14px; }
.field textarea { min-height: 180px; resize: vertical; }
.btns { display: flex; gap: 12px; flex-wrap: wrap; }
.btn { border: 0; border-radius: 12px; padding: 12px 18px; cursor: pointer; font-weight: 700; text-decoration: none; }
.primary { background: #111; color: white; }
.secondary { background: #fee500; color: #111; display: inline-flex; align-items: center; }
.result { white-space: pre-wrap; line-height: 1.7; }
.warning { font-size: 13px; color: #7a2f2f; background: #fff3f3; padding: 12px; border-radius: 10px; }
@media (max-width: 700px) { .grid { grid-template-columns: 1fr; } }
