@echo off
rem Continuous trading loop: relaunches think-act sessions back-to-back from
rem market open to close. Holds the session lock the whole day (slot tasks skip
rem while it lives; if it dies, the lock goes stale and the 15-min grid takes
rem over as fallback).
rem Run as the operator's Max-plan account (pranavjajapur). Without this the
rem default config home (~/.claude) is used, which is signed in as a DIFFERENT
rem account with its own, much smaller usage budget - the cause of the
rem 2026-08-31 all-day usage lockout. Do not remove.
set CLAUDE_CONFIG_DIR=C:\Users\awsom\.claude-work
cd /d C:\Users\awsom\Documents\Projects\trading-agent
if not exist ops\logs mkdir ops\logs
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py acquire continuous >> ops\logs\sessions.log 2>&1
if errorlevel 1 exit /b 0
echo ==== %DATE% %TIME% CONTINUOUS LOOP START ==== >> ops\logs\sessions.log
:loop
rem Central time regardless of the system zone - the laptop has flipped to ET,
rem which ended the loop an hour early (14:56 ET = 13:56 CT).
for /f %%t in ('C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\review_due.py --ct') do set NOW=%%t
if %NOW% GEQ 1456 goto done
rem Refresh the lock so it never goes stale while the loop lives.
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py acquire continuous >> ops\logs\sessions.log 2>&1
echo ---- %DATE% %TIME% continuous cycle ---- >> ops\logs\sessions.log
for /f %%s in ('C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe -c "import time;print(int(time.time()))"') do set LEGT0=%%s
call claude -p "Read C:\Users\awsom\Documents\Projects\trading-agent\ops\SESSION_PROMPT.md and follow it exactly. Session type: continuous." --model sonnet --max-turns 200 > ops\logs\_cycle.txt 2>&1
type ops\logs\_cycle.txt >> ops\logs\sessions.log
rem Usage-limit backoff: a limit-blocked session dies in <1s, so a 5s sleep
rem spins the loop hundreds of times against a dead endpoint. Sleep 10 min
rem instead and let the reset arrive.
findstr /C:"hit your session limit" /C:"hit your monthly spend limit" /C:"usage limit" ops\logs\_cycle.txt > nul
if not errorlevel 1 (
  echo ---- %DATE% %TIME% usage limit detected - backing off 10 min ---- >> ops\logs\sessions.log
  timeout /t 600 /nobreak > nul
) else (
  rem Minimum 15 min between LEG STARTS. Back-to-back legs burned a 5-hour
  rem usage window in 40 minutes on 2026-08-31. The watcher still reacts to
  rem price in ~1s between legs, so reflexes are unaffected.
  rem NOTE: pace.py sleeps for up to 15 min. Its output must NOT be redirected
  rem into sessions.log - the redirect holds an exclusive handle for the whole
  rem sleep, and any other session (a review, a triggered leg) then fails with
  rem "the process cannot access the file because it is being used by another
  rem process". Its own file, and it appends a line to sessions.log after.
  C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\pace.py %LEGT0% 900 > ops\logs\pace.log 2>&1
  type ops\logs\pace.log >> ops\logs\sessions.log
)
goto loop
:done
echo ==== %DATE% %TIME% CONTINUOUS LOOP END ==== >> ops\logs\sessions.log
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\session_lock.py release >> ops\logs\sessions.log 2>&1
rem Post-close review, chained here so it no longer depends on a wall-clock
rem task landing after the loop: the zone flips moved that task into the loop's
rem lock and it was skipped (no review 2026-09-21/22). Wait out the 15:00 CT
rem close so the day's last exits are in the ledger. run_session.cmd skips it
rem if a fallback task already reviewed today.
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe -c "import time; time.sleep(900)"
call C:\Users\awsom\Documents\Projects\trading-agent\ops\run_session.cmd weekly-review
