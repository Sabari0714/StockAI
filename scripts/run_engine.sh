#!/data/data/com.termux/files/usr/bin/bash
set -e
python -m pip install -r requirements.txt
python -m uvicorn api_server:app --host 127.0.0.1 --port 8000
