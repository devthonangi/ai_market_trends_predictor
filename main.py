from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, get_db, insert_data, fetch_data
import pandas as pd
from prophet import Prophet
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Update this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the Stock Price Prediction API!"}

# Endpoint to insert stock data into the database
@app.post("/insert_data/")
def insert_data_route(db: Session = Depends(get_db)):
    insert_data(db)
    return {"message": "Stock data inserted successfully."}

#  Endpoint to fetch stock data from the database
@app.get("/fetch_data/")
def fetch_stock_data(db: Session = Depends(get_db)):
    stocks = fetch_data(db)
    return {"stocks": stocks}  # Return fetched data

#  Prediction Endpoint: Forecasts stock prices for the next 30 days
@app.post("/predict/")
def predict_stock_prices_route():
    """
    Predict stock prices for the next 30 days.
    Returns both actual past prices and future predictions.
    """
    try:
        # Load the cleaned stock data from CSV
        df = pd.read_csv("data/AAPL_stock_data_cleaned.csv")

        # Rename columns as required by Prophet
        if "Close" in df.columns:
            df.rename(columns={"Close": "y"}, inplace=True)

        df["ds"] = pd.to_datetime(df["Datetime"])
        df = df[["ds", "y"]]  # Keep only Date and Close Price

        #  Train Prophet Model
        model = Prophet()
        model.fit(df)

        #  Generate Predictions for the Next 30 Days
        future = model.make_future_dataframe(periods=30)  # Future dates
        forecast = model.predict(future)

        #  Label actual and predicted data
        df["type"] = "Actual"  # Historical data
        forecast["type"] = "Predicted"  # Future predictions

        #  Keep relevant columns
        forecast = forecast[["ds", "yhat", "type"]]
        df = df.rename(columns={"y": "yhat"})  # Rename actual price to match Prophet output
        combined_data = pd.concat([df, forecast])  # Merge both datasets

        return {"predictions": combined_data.to_dict(orient="records")}

    except Exception as e:
        return {"error": f"Error making predictions: {str(e)}"}

#  Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()