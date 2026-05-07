@echo off
chcp 65001 >nul
python main.py
if errorlevel 1 (
  echo 실행 중 오류가 발생했습니다.
) else (
  echo 정상 완료되었습니다.
)
echo 창을 닫으려면 아무 키나 누르세요.
pause
