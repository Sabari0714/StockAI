from .data import get_history
from .indicators import add_indicators
from .scoring import technical_score,peak_score

def scan(symbol):
    d=add_indicators(get_history(symbol)); r=d.iloc[-1]; ts=technical_score(r); ps=peak_score(r)
    signal="BULLISH" if ts>=70 else ("BEARISH" if ts<=30 else "NEUTRAL")
    return {"symbol":symbol,"price":round(float(r.Close),2),"technical_score":round(ts,1),"peak_score":round(ps,1),"rsi":round(float(r.RSI14),1),"volume_ratio":round(float(r.VOLUME_RATIO),2),"momentum_20d":round(float(r.MOM_20)*100,2),"signal":signal}
