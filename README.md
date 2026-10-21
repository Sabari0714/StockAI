# StockAI

Android-first stock research and market-scanning project for Indian and global equities.

The source bundle contains technical indicators, ML probability scoring, walk-forward validation, peak/overextension detection, paper portfolio logic, FastAPI backend, Kivy UI, and an Android Buildozer configuration.

**Important:** this is a research/risk-analysis tool. It does not guarantee profit and does not execute real-money orders. Production market data and provider credentials must be configured separately and must never be embedded in the APK.

The GitHub Actions workflow extracts `StockAI_FINAL_SOURCE.zip`, validates the Python modules, and builds a debug APK with Buildozer.
