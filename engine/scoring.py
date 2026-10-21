def clamp(v,a=0,b=100): return max(a,min(b,float(v)))

def technical_score(r):
    s=50; s += 6 if r.Close>r.EMA20 else -6; s += 7 if r.EMA20>r.EMA50 else -7; s += 7 if r.EMA50>r.EMA200 else -7
    s += clamp(r.MOM_20*40,-10,10); s += clamp(r.MOM_60*25,-8,8); s += 5 if r.MACD>r.MACD_SIGNAL else -5
    s += 6 if r.VOLUME_RATIO>=1.5 else (3 if r.VOLUME_RATIO>=1.15 else (-2 if r.VOLUME_RATIO<.7 else 0)); return clamp(s)

def peak_score(r):
    s=0; d=r.DIST_52W_HIGH; s += 30 if d>=-.02 else (22 if d>=-.05 else (12 if d>=-.10 else 0))
    q=r.RSI14; s += 30 if q>=75 else (22 if q>=70 else (10 if q>=65 else 0)); e=r.EMA20_GAP
    s += 25 if e>=.12 else (18 if e>=.08 else (8 if e>=.05 else 0)); s += 15 if r.VOLUME_RATIO>=2 else (8 if r.VOLUME_RATIO>=1.5 else 0); return clamp(s)
