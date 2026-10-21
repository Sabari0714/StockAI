from pathlib import Path
import pandas as pd
import yfinance as yf

DATA=Path("data"); DATA.mkdir(exist_ok=True)

def get_history(symbol,period="2y",interval="1d"):
    x=yf.download(symbol,period=period,interval=interval,auto_adjust=True,progress=False)
    if x is None or x.empty: raise ValueError("No market data: "+symbol)
    if hasattr(x.columns,"levels"): x.columns=[c[0] for c in x.columns]
    x=x.rename(columns=str.title); return x[["Open","High","Low","Close","Volume"]].dropna()

def cache(symbol,df):
    p=DATA/(symbol.replace(".","_")+".csv"); df.to_csv(p); return p
