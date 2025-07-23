"""
Global Inflation Time Series Analysis
---------------------------------------
Simulates time series analysis on global inflation rates.
Reads from CSV-like structure and performs:
- line plot visualization
- moving average smoothing

Skills:
- pandas data manipulation
- matplotlib for plotting
- time series smoothing (rolling mean)

Data Source:
Simulated IMF/WB-like inflation data
"""

import pandas as pd
import matplotlib.pyplot as plt

# Simulated CSV data: Inflation rates by year for three countries
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'USA': [0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8.0],
    'Germany': [0.3, 0.5, 1.7, 1.9, 1.4, 0.5, 3.2, 7.9],
    'Turkey': [7.7, 8.5, 11.1, 20.3, 15.2, 12.3, 36.1, 64.3]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set Year as index
df.set_index('Year', inplace=True)

# Plotting
plt.figure(figsize=(10, 6))
for country in df.columns:
    plt.plot(df.index, df[country], label=country, linewidth=2)

plt.title("Global Inflation Trends (Simulated Data)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Moving average (3-year window)
df_ma = df.rolling(window=3).mean()

# Plot smoothed graph
plt.figure(figsize=(10, 6))
for country in df.columns:
    plt.plot(df_ma.index, df_ma[country], label=country + " (3yr MA)", linestyle='--')

plt.title("3-Year Moving Average of Inflation", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
