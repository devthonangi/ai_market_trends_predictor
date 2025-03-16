from sqlalchemy.orm import Session
from database import SessionLocal, StockData

# Function to fetch data from the database
def fetch_data():
    db = SessionLocal()  # Create a session to the database
    try:
        # Query all stock data from the table
        data = db.query(StockData).all()
        
        # Display the data
        for record in data:
            print(f"Date: {record.ds}, Open: {record.open}, High: {record.high}, Low: {record.low}, Close: {record.y}, Volume: {record.volume}")
    finally:
        db.close()  # Close the session

# Call the fetch_data function
if __name__ == "__main__":
    fetch_data()
