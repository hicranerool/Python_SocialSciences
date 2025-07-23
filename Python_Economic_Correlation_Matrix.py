"""
Correlation Matrix of Economic Indicators
------------------------------------------
Simulates economic data from World Bank-like indicators.
Calculates correlation matrix and visualizes it using a heatmap.

Skills:
- pandas data handling
- correlation analysis
- seaborn heatmap
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Simulated economic data (e.g. from World Bank)
data = {
    'GDP_per_capita': [42000, 38000, 15000, 12000, 5000, 3500, 3000],
    'Inflation_rate': [2.1, 1.9, 3.5, 4.2, 7.8, 10.1, 12.5],
    'Unemployment_rate': [4.0, 5.2, 6.3, 7.1, 10.5, 12.0, 14.3],
    'Interest_rate': [0.5, 0.25, 1.0, 1.5, 2.8, 4.2, 6.0],
    'Population_millions': [330, 80, 140, 60, 90, 110, 75]
}

# Convert to DataFrame
df = pd.DataFrame(data, index=[
    'USA', 'Germany', 'Brazil', 'Turkey', 'India', 'Nigeria', 'Pakistan'
])

# --- Correlation Matrix ---
corr_matrix = df.corr()

print("Correlation Matrix:\n")
print(corr_matrix)

# --- Heatmap ---
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Economic Indicators")
plt.tight_layout()
plt.show()
