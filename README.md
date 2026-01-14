# 🪙 Precious Metals Arbitrage Radar (Gold & Silver)

![Project Preview](preview.png)

This tool tracks the statistical relationship between **Gold (GC=F)** and **Silver (SI=F)**. By analyzing the price spread through **Z-Score normalization**, it identifies moments when one metal is significantly overvalued or undervalued relative to the other.

## 🚀 Key Features
* **Real-time Data:** Fetches latest futures data via Yahoo Finance API.
* **Statistical Analysis:** Calculates rolling correlation and Z-Score spread.
* **Visual Signals:** Generates professional-grade charts with buy/sell divergence zones.
* **Market Neutral Strategy:** Focuses on the relative value between two highly correlated assets.

## 📈 How It Works
1.  **Normalization:** Since Gold is priced much higher than Silver, the bot scales both prices to a comparable range.
2.  **Spread Calculation:** It measures the distance between the two normalized prices.
3.  **Thresholds:** When the Z-Score hits **±2**, it signals a statistical anomaly, suggesting that the prices are likely to converge again.

## 🛠️ Installation
```bash
pip install yfinance pandas matplotlib numpy

## Project Preview

![Market Radar Chart](preview.png)


