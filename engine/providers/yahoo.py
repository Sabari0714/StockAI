import pandas as pd
class YahooProvider:
    def history(self,symbol,period="2y",interval="1d"):
        import yfinance as yf
        df=yf.download(symbol,period=period,interval=interval,auto_adjust=False,progress=False)
        if isinstance(df.columns,pd.MultiIndex): df.columns=[c[0] for c in df.columns]
        return df.dropna()
