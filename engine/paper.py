import sqlite3,time
DB="paper_trading.db"
def init():
    c=sqlite3.connect(DB); c.execute("CREATE TABLE IF NOT EXISTS trades(id INTEGER PRIMARY KEY,symbol TEXT,side TEXT,qty REAL,price REAL,ts REAL,status TEXT)"); c.commit(); c.close()
def add(symbol,side,qty,price,status="OPEN"):
    init(); c=sqlite3.connect(DB); c.execute("INSERT INTO trades(symbol,side,qty,price,ts,status) VALUES(?,?,?,?,?,?)",(symbol,side,qty,price,time.time(),status)); c.commit(); c.close()
