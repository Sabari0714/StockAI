import os
class KiteProvider:
    def __init__(self):
        self.api_key=os.getenv("KITE_API_KEY"); self.access_token=os.getenv("KITE_ACCESS_TOKEN")
        if not self.api_key or not self.access_token: raise RuntimeError("Kite credentials are missing on backend")
        from kiteconnect import KiteConnect
        self.client=KiteConnect(api_key=self.api_key); self.client.set_access_token(self.access_token)
    def history(self,instrument_token,from_date,to_date,interval="day"):
        return self.client.historical_data(instrument_token,from_date,to_date,interval)
