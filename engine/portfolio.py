from dataclasses import dataclass
from datetime import datetime,timezone
@dataclass
class Position:
    symbol:str; qty:float; entry:float; stop:float; target:float; opened_at:str
class PaperPortfolio:
    def __init__(self,cash:float=100000.0): self.cash=float(cash); self.positions={}
    def open(self,symbol,price,risk_pct=.01,stop_pct=.02,target_pct=.04):
        if symbol in self.positions or price<=0:return False
        risk_cash=self.cash*min(max(risk_pct,0),.02); qty=risk_cash/max(price*stop_pct,1e-9); cost=qty*price
        if cost>self.cash: qty=self.cash/price; cost=qty*price
        if qty<=0:return False
        self.cash-=cost; self.positions[symbol]=Position(symbol,qty,price,price*(1-stop_pct),price*(1+target_pct),datetime.now(timezone.utc).isoformat()); return True
    def mark(self,prices):
        equity=self.cash; rows=[]
        for s,p in self.positions.items():
            px=float(prices.get(s,p.entry)); equity+=p.qty*px; rows.append({"symbol":s,"qty":p.qty,"entry":p.entry,"price":px,"pnl":(px-p.entry)*p.qty,"stop":p.stop,"target":p.target})
        return {"cash":self.cash,"equity":equity,"positions":rows}
