import yfinance as yf
import pandas as pd
import os

# ✅ Ensure the 'data' folder exists
os.makedirs("data", exist_ok=True)

# ✅ Define the stock ticker
ticker = "AAPL"
file_path = f"data/{ticker}_stock_data.csv"

print(f"⏳ Fetching stock data for {ticker}...")

try:
    # ✅ Fetch historical stock data (Auto-adjust to fix column mismatch)
    stock_data = yf.download(ticker, period="30d", interval="1d", auto_adjust=True)

    # ✅ Check if data is empty
    if stock_data.empty:
        raise ValueError("❌ ERROR: No data returned from Yahoo Finance!")

    # ✅ Reset index to move Date from index to column
    stock_data.reset_index(inplace=True)

    # ✅ Rename & ensure correct column order
    stock_data = stock_data[["Date", "Open", "High", "Low", "Close", "Volume"]]
    stock_data.rename(columns={"Date": "Datetime"}, inplace=True)

    # ✅ Remove any incorrect extra row (e.g., "AAPL, AAPL, AAPL...")
    if stock_data.iloc[0, 0] == "AAPL":
        stock_data = stock_data.iloc[1:]

    # ✅ Save cleaned data to CSV
    stock_data.to_csv(file_path, index=False)

    print(f"✅ Cleaned stock data for {ticker} saved successfully at {file_path}!")

except Exception as e:
    print(f"❌ Error fetching stock data: {e}")
