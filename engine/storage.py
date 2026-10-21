import sqlite3, time, json
from pathlib import Path
DB=Path("stock_ai.db")
def connect(): return sqlite3.connect(DB)
def init_db():
    c=connect(); c.execute("""CREATE TABLE IF NOT EXISTS scans(id INTEGER PRIMARY KEY AUTOINCREMENT,ts REAL NOT NULL,symbol TEXT NOT NULL,price REAL,technical_score REAL,peak_score REAL,rsi REAL,volume_ratio REAL,momentum_20d REAL,signal TEXT,payload TEXT NOT NULL)"""); c.commit(); c.close()
def save_scan(r):
    init_db(); c=connect(); c.execute("INSERT INTO scans(ts,symbol,price,technical_score,peak_score,rsi,volume_ratio,momentum_20d,signal,payload) VALUES(?,?,?,?,?,?,?,?,?,?)",(time.time(),r["symbol"],r["price"],r["technical_score"],r["peak_score"],r["rsi"],r["volume_ratio"],r["momentum_20d"],r["signal"],json.dumps(r))); c.commit(); c.close()
def latest(limit=50):
    init_db(); c=connect(); rows=c.execute("SELECT symbol,price,technical_score,peak_score,rsi,volume_ratio,momentum_20d,signal,ts FROM scans ORDER BY ts DESC LIMIT ?",(limit,)).fetchall(); c.close(); keys=["symbol","price","technical_score","peak_score","rsi","volume_ratio","momentum_20d","signal","ts"]; return [dict(zip(keys,r)) for r in rows]
