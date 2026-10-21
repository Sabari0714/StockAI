from .scanner import scan
from .storage import save_scan

def rank(symbols):
    out=[]
    for s in symbols:
        try:
            r=scan(s); save_scan(r); out.append(r)
        except Exception as e: out.append({"symbol":s,"error":str(e)})
    valid=[x for x in out if "error" not in x]
    return {"bullish":sorted(valid,key=lambda x:x["technical_score"],reverse=True)[:20],"peak_risk":sorted(valid,key=lambda x:x["peak_score"],reverse=True)[:20],"bearish":sorted(valid,key=lambda x:x["technical_score"])[:20],"all":valid}
