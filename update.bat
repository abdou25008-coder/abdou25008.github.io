@echo off
chcp 65001 >nul
echo ======================================================
echo    Uploading Portfolio Website to GitHub...
echo ======================================================
cd /d "%~dp0"

echo 1. Saving local files...
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" add .
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" commit -m "Update portfolio website with latest improvements"

echo.
echo 2. Pushing directly to GitHub (Force overwrite remote)...
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" push origin main --force

echo.
echo ======================================================
echo    Upload Complete! Check your live website.
echo ======================================================
pause
