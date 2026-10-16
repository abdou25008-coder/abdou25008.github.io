@echo off
echo ======================================================
echo    Synchronizing and Uploading to GitHub...
echo ======================================================
cd /d "%~dp0"
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" add .
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" commit -m "Update portfolio website"
echo.
echo Pulling latest changes from GitHub...
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" pull origin main --rebase
echo.
echo Pushing updates to GitHub...
"C:\Users\LENOVO\.gemini\antigravity\scratch\mingit\cmd\git.exe" push origin main
echo.
echo ======================================================
echo    Update Finished! Check your live website.
echo ======================================================
pause
