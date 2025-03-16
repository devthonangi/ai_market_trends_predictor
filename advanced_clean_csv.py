import pandas as pd
import os

print(" Checking data directory...")
#  Ensure data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

input_file = "data/AAPL_stock_data.csv"
output_file = "data/AAPL_stock_data_cleaned.csv"

print(f" Loading raw stock data from: {input_file}")
df = pd.read_csv(input_file)

# Step 1: Remove Any Rows Where ANY Column Contains "AAPL"
df = df[~df.astype(str).apply(lambda row: row.str.contains("AAPL", na=False)).any(axis=1)]
print("⚠️ Removed rows containing 'AAPL'.")

# Step 2: Reset Index
df.reset_index(drop=True, inplace=True)

#  Step 3: Rename Columns to Prophet Format
df.columns = ["Datetime", "Open", "High", "Low", "Close", "Volume"]

# Step 4: Convert 'Datetime' to DateTime Format
df["Datetime"] = pd.to_datetime(df["Datetime"], errors="coerce")

#  Step 5: Convert Numeric Columns
numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

#  Step 6: Drop Rows with Missing or Invalid Data
df.dropna(inplace=True)

print("📊 Final Cleaned Data Preview:")
print(df.head())

#  Step 7: Save Cleaned Data
df.to_csv(output_file, index=False)
print(f" Cleaned stock data saved at: {output_file}")
