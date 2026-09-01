@echo off
rem Cloudflare quick tunnel: exposes the LOCAL ops console (localhost:8321) at a
rem public https URL so it can be viewed from another machine. Read-only by
rem construction (console.py has no order path), and remote requests must carry
rem the token in ops\logs\console_token.txt - localhost stays open.
rem
rem Quick tunnels get a NEW random hostname every start. The full viewing URL
rem (host + token) is written to ops\logs\tunnel_url.txt after startup.
cd /d C:\Users\awsom\Documents\Projects\trading-agent
if not exist ops\logs mkdir ops\logs
del /q ops\logs\tunnel.log 2>nul
start "" /B ops\tools\cloudflared.exe tunnel --url http://localhost:8321 --logfile ops\logs\tunnel.log
rem give cloudflared time to register and print its hostname
timeout /t 25 /nobreak > nul
C:\Users\awsom\Documents\Projects\trading-agent\.venv\Scripts\python.exe ops\tunnel_url.py
