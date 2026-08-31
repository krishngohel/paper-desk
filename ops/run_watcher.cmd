@echo off
rem Run as the operator's Max-plan account (pranavjajapur). Without this the
rem default config home (~/.claude) is used, which is signed in as a DIFFERENT
rem account with its own, much smaller usage budget - the cause of the
rem 2026-08-31 all-day usage lockout. Do not remove.
set CLAUDE_CONFIG_DIR=C:\Users\awsom\.claude-work
cd /d C:\Users\awsom\Documents\Projects\trading-agent
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\watcher.py >> ops\logs\watcher_stdout.log 2>&1
