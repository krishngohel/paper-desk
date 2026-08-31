@echo off
rem Freshness snapshot: data script + dashboard publish. Cheap model, few turns.
rem Run as the operator's Max-plan account (pranavjajapur). Without this the
rem default config home (~/.claude) is used, which is signed in as a DIFFERENT
rem account with its own, much smaller usage budget - the cause of the
rem 2026-08-31 all-day usage lockout. Do not remove.
set CLAUDE_CONFIG_DIR=C:\Users\awsom\.claude-work
cd /d C:\Users\awsom\Documents\Projects\trading-agent
echo ==== %DATE% %TIME% snapshot ==== >> ops\logs\snapshots.log
call claude -p "Run exactly this with the Bash tool: C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe C:\Users\awsom\Documents\Projects\trading-agent\ops\snapshot.py -- then read journal\DASHBOARD_URL.txt and publish ops\dashboard.html to that artifact url with the Artifact tool (favicon chart-increasing emoji). Do nothing else; if the script errors, stop." --model haiku --max-turns 15 >> ops\logs\snapshots.log 2>&1
echo ---- exit %ERRORLEVEL% ---- >> ops\logs\snapshots.log
