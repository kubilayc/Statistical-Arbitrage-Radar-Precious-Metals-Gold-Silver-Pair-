import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def commodity_arbitrage_radar(asset1, asset2, asset1_name, asset2_name, start_date):
    print(f"📡 Scanning Correlation: {asset1_name} vs {asset2_name}...")
    
    # 1. Fetching Commodity Data (Gold and Silver Futures)
    # GC=F is Gold, SI=F is Silver on Yahoo Finance
    data = yf.download([asset1, asset2], start=start_date, threads=False, progress=False, auto_adjust=True)['Close']
    data.dropna(inplace=True)

    # 2. Calculating Daily Returns and Statistical Correlation
    returns = np.log(data / data.shift(1)).dropna()
    current_corr = returns[asset1].corr(returns[asset2])
    
    # 3. Z-Score Spread Analysis
    # We normalize the prices because Gold is ~$2000+ and Silver is ~$20-30
    normalized = (data - data.mean()) / data.std()
    spread = normalized[asset1] - normalized[asset2]
    z_score = (spread - spread.mean()) / spread.std()

    # 4. Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

    # Top Plot: Normalized Gold & Silver Prices
    ax1.plot(normalized.index, normalized[asset1], label=f'{asset1_name} (Normalized)', color='#d4af37', lw=1.8)
    ax1.plot(normalized.index, normalized[asset2], label=f'{asset2_name} (Normalized)', color='#aaa9ad', lw=1.8)
    ax1.set_title(f"Precious Metals Arbitrage Radar | Correlation: {current_corr:.2f}", fontsize=14)
    ax1.legend()
    ax1.grid(alpha=0.2)

    # Bottom Plot: The Arbitrage Signal (Z-Score)
    ax2.plot(z_score.index, z_score, color='purple', label='Spread Z-Score')
    ax2.axhline(2, color='red', linestyle='--', label='Gold Overvalued / Silver Undervalued')
    ax2.axhline(-2, color='green', linestyle='--', label='Gold Undervalued / Silver Overvalued')
    ax2.axhline(0, color='black', lw=1)
    
    # Fill signal areas when Z-Score exceeds 2 standard deviations
    ax2.fill_between(z_score.index, 2, z_score, where=(z_score >= 2), color='red', alpha=0.3)
    ax2.fill_between(z_score.index, -2, z_score, where=(z_score <= -2), color='green', alpha=0.3)
    
    ax2.set_ylabel('Z-Score')
    ax2.set_title("Statistical Divergence Signal", fontsize=12)
    ax2.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

    # Final Technical Report
    last_z = z_score.iloc[-1]
    print(f"\n--- PRECIOUS METALS RADAR REPORT ---")
    if last_z > 2:
        print(f"⚠️ SIGNAL: Gold is significantly OVERVALUED relative to Silver (Z-Score: {last_z:.2f})")
        print("Strategy: Consider Short Gold / Long Silver")
    elif last_z < -2:
        print(f"⚠️ SIGNAL: Silver is significantly OVERVALUED relative to Gold (Z-Score: {last_z:.2f})")
        print("Strategy: Consider Long Gold / Short Silver")
    else:
        print(f"✅ STABLE: Gold and Silver are moving in sync (Z-Score: {last_z:.2f})")

if __name__ == "__main__":
    # GC=F: Gold Futures, SI=F: Silver Futures
    commodity_arbitrage_radar('GC=F', 'SI=F', 'GOLD', 'SILVER', '2024-01-01')