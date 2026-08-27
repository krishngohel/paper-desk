@echo off
rem Headless trading session launcher. Arg 1 = open ^| intraday ^| preclose ^| weekly-review
set TYPE=%1
if "%TYPE%"=="" set TYPE=intraday
cd /d C:\Users\awsom\Documents\Projects\trading-agent
if not exist ops\logs mkdir ops\logs
echo ==== %DATE% %TIME% %TYPE% ==== >> ops\logs\sessions.log
call claude -p "Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: %TYPE%." --max-turns 100 >> ops\logs\sessions.log 2>&1
echo ---- exit %ERRORLEVEL% ---- >> ops\logs\sessions.log
