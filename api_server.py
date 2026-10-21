from fastapi import FastAPI,HTTPException
from engine.scanner import scan
from engine.ml import train,predict
from engine.backtest import run
from engine.ranker import rank
from engine.storage import latest,init_db
import json
from pathlib import Path
app=FastAPI(title="Stock AI",version="1.2.0"); init_db()
def universe(): return json.loads(Path("config/universe.json").read_text())
@app.get("/health")
def health(): return {"status":"ok","engine":"stock-ai","version":"1.2.0"}
@app.get("/scan/{symbol}")
def scan_api(symbol:str):
    try:return scan(symbol.upper())
    except Exception as e: raise HTTPException(500,str(e))
@app.get("/train/{symbol}")
def train_api(symbol:str):
    try:return train(symbol.upper())
    except Exception as e: raise HTTPException(500,str(e))
@app.get("/predict/{symbol}")
def predict_api(symbol:str):
    try:return predict(symbol.upper())
    except Exception as e: raise HTTPException(500,str(e))
@app.get("/backtest/{symbol}")
def backtest_api(symbol:str):
    try:return run(symbol.upper())
    except Exception as e: raise HTTPException(500,str(e))
@app.get("/universe")
def universe_api(): return universe()
@app.get("/rank")
def rank_api():
    u=universe(); return rank(u.get("india",[])+u.get("usa",[]))
@app.get("/history")
def history_api(limit:int=50): return latest(min(limit,500))
