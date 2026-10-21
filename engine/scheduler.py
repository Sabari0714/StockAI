import json
from pathlib import Path
from .ranker import rank

def run_once():
    u=json.loads(Path("config/universe.json").read_text()); return rank(u.get("india",[])+u.get("usa",[]))
if __name__=="__main__":
    r=run_once(); print(json.dumps({"bullish":[x["symbol"] for x in r["bullish"][:10]],"peak_risk":[x["symbol"] for x in r["peak_risk"][:10]],"bearish":[x["symbol"] for x in r["bearish"][:10]]},indent=2))
