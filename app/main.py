from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import threading,requests,json
class StockAI(App):
    def build(self):
        root=BoxLayout(orientation="vertical",padding=12,spacing=8); root.add_widget(Label(text="STOCK AI  •  RESEARCH",font_size=26,size_hint_y=.09)); self.symbol=TextInput(text="RELIANCE.NS",multiline=False,size_hint_y=.08); root.add_widget(self.symbol)
        row=BoxLayout(size_hint_y=.09,spacing=6); b1=Button(text="SCAN"); b1.bind(on_press=self.scan); b2=Button(text="TOP RANK"); b2.bind(on_press=self.rank); row.add_widget(b1); row.add_widget(b2); root.add_widget(row)
        self.out=Label(text="Ready",halign="left",valign="top",size_hint_y=None); self.out.bind(texture_size=self.out.setter("size")); sv=ScrollView(); sv.add_widget(self.out); root.add_widget(sv); return root
    def scan(self,*_): self.out.text="Scanning..."; threading.Thread(target=self._scan,daemon=True).start()
    def _scan(self):
        try: self.out.text=json.dumps(requests.get("http://127.0.0.1:8000/scan/"+self.symbol.text.strip(),timeout=30).json(),indent=2)
        except Exception as e: self.out.text="Backend unavailable: "+str(e)
    def rank(self,*_): self.out.text="Ranking universe..."; threading.Thread(target=self._rank,daemon=True).start()
    def _rank(self):
        try:
            r=requests.get("http://127.0.0.1:8000/rank",timeout=180).json(); lines=["TOP BULLISH"]
            lines += [f'{i+1}. {x["symbol"]} score={x["technical_score"]} peak={x["peak_score"]}' for i,x in enumerate(r["bullish"][:10])]
            lines += ["","PEAK / OVEREXTENSION RISK"]; lines += [f'{i+1}. {x["symbol"]} peak={x["peak_score"]} RSI={x["rsi"]}' for i,x in enumerate(r["peak_risk"][:10])]
            lines += ["","BEARISH"]; lines += [f'{i+1}. {x["symbol"]} score={x["technical_score"]}' for i,x in enumerate(r["bearish"][:10])]; self.out.text="\n".join(lines)
        except Exception as e: self.out.text="Ranking failed: "+str(e)
if __name__=="__main__": StockAI().run()
