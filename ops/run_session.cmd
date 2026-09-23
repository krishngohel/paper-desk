@echo off
rem Headless trading session launcher. Arg 1 = open ^| intraday ^| preclose ^| weekly-review ^| triggered
rem Run as the operator's Max-plan account (pranavjajapur). Without this the
rem default config home (~/.claude) is used, which is signed in as a DIFFERENT
rem account with its own, much smaller usage budget - the cause of the
rem 2026-08-31 all-day usage lockout. Do not remove.
set CLAUDE_CONFIG_DIR=C:\Users\awsom\.claude-work
set TYPE=%1
if "%TYPE%"=="" set TYPE=intraday
cd /d C:\Users\awsom\Documents\Projects\trading-agent
if not exist ops\logs mkdir ops\logs
rem One post-close review per day. The continuous loop chains it at the close
rem and the scheduled review tasks are fallbacks; whichever gets here second
rem sees today's stamp and skips (ops\review_due.py explains why).
if not "%TYPE%"=="weekly-review" goto locked
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\review_due.py >> ops\logs\sessions.log 2>&1
if errorlevel 1 exit /b 0
:locked
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py acquire >> ops\logs\sessions.log 2>&1
if errorlevel 1 exit /b 0
rem Every session type runs on Sonnet (user decision 2026-08-31). Never leave
rem this blank: an empty flag inherits the operator's interactive default
rem (Opus/Fable), which burns the subscription budget many times faster.
set MODELFLAG=--model sonnet
echo ==== %DATE% %TIME% %TYPE% ==== >> ops\logs\sessions.log
call claude -p "Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: %TYPE%." %MODELFLAG% --max-turns 160 >> ops\logs\sessions.log 2>&1
set RC=%ERRORLEVEL%
echo ---- exit %RC% ---- >> ops\logs\sessions.log
rem Stamp only a review that finished cleanly; a crashed or limit-killed one
rem leaves the day due so a fallback task retries it.
if "%TYPE%"=="weekly-review" if "%RC%"=="0" C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\review_due.py --mark
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py release >> ops\logs\sessions.log 2>&1
