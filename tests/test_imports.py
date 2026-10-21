def test_core_imports():
    from engine import indicators, scoring, data, scanner, ml, backtest, storage, ranker
    from engine.walkforward import walk_forward
    from engine.regime import classify_regime
    from engine.portfolio import PaperPortfolio
    from engine.alerts import build_alert
