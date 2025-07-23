"""
Automated Survey Report Generator
---------------------------------------
Loads a survey Excel file, computes descriptive statistics,
and generates plots for each question.

Skills:
- Read Excel with pandas
- Summary statistics: mean, value_counts
- Visualization with matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# Simulated survey data (you would load from .xlsx in real case)
data = {
    'Satisfaction': [4, 5, 3, 4, 2, 5, 5, 4],
    'Recommend': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes'],
    'Age': [22, 34, 28, 45, 19, 23, 31, 37]
}

# Convert to DataFrame (in practice: pd.read_excel("survey.xlsx"))
df = pd.DataFrame(data)

# --- Summary Report ---
print("Survey Summary Report\n")
for column in df.columns:
    print(f"Question: {column}")
    if df[column].dtype == 'object':
        print(df[column].value_counts())
    else:
        print(df[column].describe())
    print()

# --- Plotting ---
for column in df.columns:
    plt.figure(figsize=(6, 4))
    if df[column].dtype == 'object':
        df[column].value_counts().plot(kind='bar', color='skyblue')
        plt.title(f"Distribution of {column}")
    else:
        plt.hist(df[column], bins=5, color='salmon', edgecolor='black')
        plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
