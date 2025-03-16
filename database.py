from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session
import os

# Updated import for SQLAlchemy 2.0 compatibility
Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'
    
    id = Column(Integer, primary_key=True, index=True)
    ds = Column(String, index=True)   # 'ds' is for the Date
    open = Column(Float)              # 'open' is for the opening price
    high = Column(Float)              # 'high' is for the highest price
    low = Column(Float)               # 'low' is for the lowest price
    y = Column(Float)                 # 'y' is the closing price, as per the insert_data.py script
    volume = Column(Integer)          # 'volume' is for the volume of stock traded

# Database connection
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables (if not already created)
Base.metadata.create_all(bind=engine)

# Create a SessionLocal instance to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to insert stock data into the database
def insert_data(db: Session):
    # Load the cleaned CSV file
    df = pd.read_csv("data/AAPL_stock_data_cleaned.csv")

    # Check if 'Close' exists, and rename it to 'y' if so
    if 'Close' in df.columns:
        df.rename(columns={'Close': 'y'}, inplace=True)

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

# Function to fetch stock data
def fetch_data(db: Session, limit: int = 10):
    return db.query(StockData).limit(limit).all()
