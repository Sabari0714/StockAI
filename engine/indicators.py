import numpy as np
import pandas as pd

FEATURES = ["RSI14","MACD","MACD_SIGNAL","ATR14","VOLUME_RATIO","MOM_20","MOM_60","DIST_52W_HIGH","EMA20_GAP","EMA50_GAP"]

def rsi(c, n=14):
    d=c.diff(); g=d.clip(lower=0).rolling(n).mean(); l=(-d.clip(upper=0)).rolling(n).mean(); rs=g/l.replace(0,np.nan); return 100-100/(1+rs)

def add_indicators(df):
    x=df.copy(); c=x["Close"]
    x["EMA20"]=c.ewm(span=20,adjust=False).mean(); x["EMA50"]=c.ewm(span=50,adjust=False).mean(); x["EMA200"]=c.ewm(span=200,adjust=False).mean()
    x["RSI14"]=rsi(c); e12=c.ewm(span=12,adjust=False).mean(); e26=c.ewm(span=26,adjust=False).mean(); x["MACD"]=e12-e26; x["MACD_SIGNAL"]=x["MACD"].ewm(span=9,adjust=False).mean()
    pc=c.shift(1); tr=pd.concat([(x.High-x.Low),(x.High-pc).abs(),(x.Low-pc).abs()],axis=1).max(axis=1); x["ATR14"]=tr.rolling(14).mean()
    x["VOLUME_RATIO"]=x.Volume/x.Volume.rolling(20).mean(); x["MOM_20"]=c.pct_change(20); x["MOM_60"]=c.pct_change(60)
    h=c.rolling(252,min_periods=60).max(); x["DIST_52W_HIGH"]=c/h-1; x["EMA20_GAP"]=c/x.EMA20-1; x["EMA50_GAP"]=c/x.EMA50-1
    return x.replace([np.inf,-np.inf],np.nan).dropna()
