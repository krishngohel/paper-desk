@echo off
rem Freshness snapshot: data script + dashboard publish. Cheap model, few turns.
cd /d C:\Users\awsom\Documents\Projects\trading-agent
echo ==== %DATE% %TIME% snapshot ==== >> ops\logs\snapshots.log
call claude -p "Run exactly this with the Bash tool: C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe C:\Users\awsom\Documents\Projects\trading-agent\ops\snapshot.py -- then read journal\DASHBOARD_URL.txt and publish ops\dashboard.html to that artifact url with the Artifact tool (favicon chart-increasing emoji). Do nothing else; if the script errors, stop." --model haiku --max-turns 15 >> ops\logs\snapshots.log 2>&1
echo ---- exit %ERRORLEVEL% ---- >> ops\logs\snapshots.log
