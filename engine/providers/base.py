from abc import ABC, abstractmethod
class MarketDataProvider(ABC):
    @abstractmethod
    def history(self,symbol,period="2y",interval="1d"): raise NotImplementedError
