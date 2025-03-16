import pandas as pd
from database import SessionLocal, StockData

def insert_data():
    # Load the cleaned CSV file
    df = pd.read_csv("data/AAPL_stock_data_cleaned.csv")

    # Check if 'Close' exists, and rename it to 'y' if so
    if 'Close' in df.columns:
        df.rename(columns={'Close': 'y'}, inplace=True)

    # Create a new session to interact with the database
    db = SessionLocal()

    for index, row in df.iterrows():
        try:
            # Insert the row into the stock_data table
            stock_data = StockData(
                ds=row["Datetime"],  # 'Datetime' is the column name from the CSV
                open=row["Open"],
                high=row["High"],
                low=row["Low"],
                y=row["y"],  # 'y' now corresponds to 'Close' column
                volume=row["Volume"]
            )
            db.add(stock_data)
            db.commit()
            print(f"Inserted row {index}")
        except Exception as e:
            print(f"❌ Error inserting row {index}: {e}")
            db.rollback()

    print("✅ Data insertion complete.")

# Call the function to start the data insertion process
insert_data()
