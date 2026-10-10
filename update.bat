@echo off
echo ======================================================
echo    Uploading new updates to GitHub...
echo ======================================================
cd /d "%~dp0"
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" add .
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" commit -m "Update website with latest features"
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" push origin main
echo.
echo ======================================================
echo    Update Successful! Check your live website.
echo ======================================================
pause
