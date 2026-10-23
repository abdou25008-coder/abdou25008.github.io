@echo off
chcp 65001 >nul
echo ======================================================
echo    Uploading and Deploying Portfolio to GitHub & Cloudflare...
echo ======================================================
cd /d "%~dp0"

echo 1. Committing local changes...
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" add .
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" commit -m "Update portfolio website"

echo.
echo 2. Pushing to GitHub...
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" push origin main --force

echo.
echo 3. Deploying live to Cloudflare Pages (abdou-mousa.pages.dev)...
python deploy_cf_pages_final.py

echo.
echo ======================================================
echo    Deployment Finished!
echo    Live URL: https://abdou-mousa.pages.dev
echo ======================================================
pause
