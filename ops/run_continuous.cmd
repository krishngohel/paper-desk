@echo off
rem Continuous trading loop: relaunches think-act sessions back-to-back from
rem market open to close. Holds the session lock the whole day (slot tasks skip
rem while it lives; if it dies, the lock goes stale and the 15-min grid takes
rem over as fallback).
cd /d C:\Users\awsom\Documents\Projects\trading-agent
if not exist ops\logs mkdir ops\logs
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py acquire continuous >> ops\logs\sessions.log 2>&1
if errorlevel 1 exit /b 0
echo ==== %DATE% %TIME% CONTINUOUS LOOP START ==== >> ops\logs\sessions.log
:loop
for /f %%t in ('powershell -NoProfile -Command "Get-Date -Format HHmm"') do set NOW=%%t
if %NOW% GEQ 1456 goto done
rem Refresh the lock so it never goes stale while the loop lives.
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py acquire continuous >> ops\logs\sessions.log 2>&1
echo ---- %DATE% %TIME% continuous cycle ---- >> ops\logs\sessions.log
call claude -p "Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: continuous." --model sonnet --max-turns 200 >> ops\logs\sessions.log 2>&1
timeout /t 5 /nobreak > nul
goto loop
:done
echo ==== %DATE% %TIME% CONTINUOUS LOOP END ==== >> ops\logs\sessions.log
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py release >> ops\logs\sessions.log 2>&1
