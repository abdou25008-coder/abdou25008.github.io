@echo off
chcp 65001 >nul
echo ======================================================
echo    جاري رفع التحديثات الجديدة إلى GitHub مباشرة...
echo ======================================================
cd /d "%~dp0"
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" add .
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" commit -m "Update website with latest features"
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" push origin main
echo.
echo ======================================================
echo    تم التحديث بنجاح! تفضل بزيارة موقعك على GitHub Pages.
echo ======================================================
pause
