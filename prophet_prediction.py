import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

print("🔍 Checking data directory...")
# ✅ Ensure data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# ✅ Use the updated, fully cleaned stock data file path
file_path = "data/AAPL_stock_data_cleaned.csv"

print(f"📂 Loading cleaned stock data from: {file_path}")
df = pd.read_csv(file_path)

# ✅ Step 1: Remove Any Rows Containing Non-Numeric Values in 'y' Column (Close Price)
df = df[pd.to_numeric(df["Close"], errors="coerce").notna()]
df.dropna(inplace=True)  # Drop any row with missing values after filtering

# ✅ Step 2: Rename Columns for Prophet Format
df.columns = ["ds", "Open", "High", "Low", "y", "Volume"]

# ✅ Step 3: Convert 'ds' to DateTime Format (Force Correct Dates)
df["ds"] = pd.to_datetime(df["ds"], errors="coerce")

# ✅ Step 4: Drop Any Rows Where 'ds' (Date) is Missing
df = df[df["ds"].notna()]

# ✅ Step 5: Convert Numeric Columns to Proper Format
numeric_columns = ["Open", "High", "Low", "y", "Volume"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ✅ Step 6: Drop Any Rows That Still Have Missing Data
df.dropna(inplace=True)

print("📊 Final Cleaned Data Preview:")
print(df.head())

# ✅ Step 7: Train AI Model (Prophet)
print("🧠 Training AI Model (Prophet)...")
model = Prophet()
model.fit(df[["ds", "y"]])  # Train only on Date and Close Price

# ✅ Step 8: Make Future Predictions
print("📈 Making future predictions...")
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# ✅ Step 9: Save Predictions
output_file = "data/AAPL_forecast.csv"
forecast.to_csv(output_file, index=False)
print(f"✅ AI model trained and forecast saved at: {output_file}")

# ✅ Step 10: Plot Results
plt.figure(figsize=(10, 5))
plt.plot(df["ds"], df["y"], label="Actual Prices", color="blue")
plt.plot(forecast["ds"], forecast["yhat"], label="Predicted Prices", color="red", linestyle="dashed")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Price Prediction for AAPL")
plt.legend()
plt.show()
