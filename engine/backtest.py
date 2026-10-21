import pandas as pd
from .data import get_history
from .indicators import add_indicators
from .scoring import technical_score

def run(symbol,threshold=70,horizon=5,target=.02,stop=.02):
    d=add_indicators(get_history(symbol)).copy(); d["score"]=d.apply(technical_score,axis=1); trades=[]
    for i in range(len(d)-horizon):
        if d.score.iloc[i]<threshold: continue
        entry=float(d.Close.iloc[i]); future=d.Close.iloc[i+1:i+1+horizon]; ret=float(future.iloc[-1]/entry-1); peak=float(future.max()/entry-1); trough=float(future.min()/entry-1); win=peak>=target and trough>-stop
        trades.append({"date":str(d.index[i]),"return":ret,"peak":peak,"trough":trough,"win":win})
    t=pd.DataFrame(trades)
    if t.empty:return {"symbol":symbol,"trades":0}
    equity=(1+t["return"]).cumprod(); dd=(equity/equity.cummax()-1).min()
    return {"symbol":symbol,"trades":len(t),"win_rate":round(float(t.win.mean()*100),2),"avg_return_pct":round(float(t["return"].mean()*100),3),"max_drawdown_pct":round(float(dd*100),3)}
