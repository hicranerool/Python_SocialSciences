"""
Data Cleaning Assistant Script
------------------------------
Automatically cleans common data problems:
- Missing values
- Duplicate rows
- Data type inconsistencies

Skills demonstrated:
- Reading and writing Excel/CSV files
- DataFrame manipulation with pandas
- Basic data cleaning operations
"""

import pandas as pd

# Define file path (change to your data file)
file_path = "your_data.xlsx"  # Or "your_data.csv"

# Load data based on file extension
if file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
elif file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    raise ValueError("Unsupported file type. Please use .csv or .xlsx")

print("Original Data Overview:\n")
print(df.info())
print("\nFirst 5 rows:\n", df.head())

print("\nCleaning data...")

# 1. Display missing values count per column
print("\nMissing values per column:\n", df.isnull().sum())

# 2. Fill missing numeric values with column mean
for col in df.select_dtypes(include='number'):
    if df[col].isnull().any():
        df[col].fillna(df[col].mean(), inplace=True)

# 3. Fill missing categorical/text values with 'Unknown'
for col in df.select_dtypes(include='object'):
    if df[col].isnull().any():
        df[col].fillna('Unknown', inplace=True)

# 4. Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nData cleaning completed successfully.")

# 5. Save cleaned data to a new Excel file
output_file = "cleaned_data.xlsx"
df.to_excel(output_file, index=False)

print(f"\nCleaned data saved as: {output_file}")
