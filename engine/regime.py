import pandas as pd

def classify_regime(df:pd.DataFrame)->str:
    if len(df)<200:return "UNKNOWN"
    c=df["Close"]; e50=c.ewm(span=50,adjust=False).mean().iloc[-1]; e200=c.ewm(span=200,adjust=False).mean().iloc[-1]; r20=c.pct_change(20).iloc[-1]; v20=c.pct_change().rolling(20).std().iloc[-1]
    if e50>e200 and r20>0:return "BULL"
    if e50<e200 and r20<0:return "BEAR"
    if v20>c.pct_change().rolling(60).std().median():return "HIGH_VOLATILITY"
    return "SIDEWAYS"
