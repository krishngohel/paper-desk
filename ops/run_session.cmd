@echo off
rem Headless trading session launcher. Arg 1 = open ^| intraday ^| preclose ^| weekly-review ^| triggered
set TYPE=%1
if "%TYPE%"=="" set TYPE=intraday
cd /d C:\Users\awsom\Documents\Projects\trading-agent
if not exist ops\logs mkdir ops\logs
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py acquire >> ops\logs\sessions.log 2>&1
if errorlevel 1 exit /b 0
echo ==== %DATE% %TIME% %TYPE% ==== >> ops\logs\sessions.log
call claude -p "Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: %TYPE%." --model sonnet --max-turns 160 >> ops\logs\sessions.log 2>&1
echo ---- exit %ERRORLEVEL% ---- >> ops\logs\sessions.log
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py release >> ops\logs\sessions.log 2>&1
