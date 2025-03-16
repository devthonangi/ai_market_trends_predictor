from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

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
