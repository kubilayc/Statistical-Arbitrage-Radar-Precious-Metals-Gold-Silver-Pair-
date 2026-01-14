# Statistical Arbitrage Radar: Precious Metals (Gold/Silver Pair) 📈💰

This project implements a **Statistical Arbitrage** strategy focusing on the correlation and cointegration between **Gold (GC=F)** and **Silver (SI=F)**. It uses the "Pairs Trading" logic to identify overbought and oversold conditions in the price ratio.

## 🎯 Project Overview
Statistical Arbitrage is a quantitative strategy that exploits price inefficiencies between two correlated assets. This tool:
* Monitors the **Gold/Silver Ratio** in real-time.
* Calculates the **Z-Score** to detect statistical deviations from the historical mean.
* Visualizes entry and exit points for mean-reversion trading.

## 🛠️ Tech Stack
* **Python:** Core logic.
* **yfinance:** Financial data extraction.
* **Pandas & NumPy:** Time-series analysis and Z-Score calculations.
* **Matplotlib:** Data visualization.

## 📊 Visual Analysis

> **IMPORTANT:** Ensure that your image files are named exactly as below and uploaded to the root folder of this repository for them to appear.

### 1. Gold vs. Silver Price Correlation
Shows how both assets move together over time.

![Price Analysis](gold_silver_prices.png)

### 2. Z-Score & Mean Reversion
The core of the strategy. When the Z-Score crosses the threshold (e.g., +2 or -2), it signals a potential trade.

![Z-Score Analysis](z_score_analysis.png)

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/Statistical-Arbitrage-Radar-Precious-Metals-Gold-Silver-Pair-.git](https://github.com/your-username/Statistical-Arbitrage-Radar-Precious-Metals-Gold-Silver-Pair-.git)
