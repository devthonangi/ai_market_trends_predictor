# **AI Market Trends Predictor** 
A **machine learning-driven stock price prediction system** utilizing **FastAPI, Prophet, and Streamlit** for real-time forecasting and interactive visualization.

---

##  **Project Overview**  
The **AI Market Trends Predictor** is designed to process **historical stock market data**, store it in a structured database, and generate **future stock price predictions** using **Facebook Prophet**. The system is built with **FastAPI** for API-based backend services and **Streamlit** for an interactive **frontend dashboard**.

- **Data Pipeline:** Stock data is ingested from structured CSV files and stored in a relational database using **SQLAlchemy**.  
- **Model Training:** Prophet is used to identify trends and patterns, forecasting **30 days into the future**.  
- **Visualization:** Interactive **Plotly-based charts** display both **historical** and **predicted** prices in a Streamlit UI.  
- **Deployment:** The backend is deployed using **Uvicorn**, serving API endpoints for data retrieval and prediction.  

---

##  **System Architecture**  
The system is designed with a modular architecture to ensure scalability and maintainability:

1️⃣ **Data Collection & Storage**  
   - Raw stock data is ingested from **CSV files** or **external APIs** (e.g., **Yahoo Finance**, **Alpha Vantage**).  
   - **SQLAlchemy ORM** is used to store structured stock data in an **SQLite database**.  
   - API endpoints enable real-time **data insertion and retrieval**.  

2️⃣ **Machine Learning Model**  
   - **Prophet** is trained on past stock prices using **time-series forecasting techniques**.  
   - The model learns **seasonal trends, daily fluctuations, and external factors** affecting stock prices.  
   - Predictions include **confidence intervals** (`yhat_lower`, `yhat_upper`) for uncertainty estimation.  

3️⃣ **API Development (FastAPI)**  
   - Provides a RESTful interface to interact with the **database and ML model**.  
   - Endpoints for **data retrieval, stock insertion, and predictions**.  
   - **CORS enabled** for seamless frontend-backend communication.  

4️⃣ **Frontend Visualization (Streamlit)**  
   - Connects to the **FastAPI backend** to fetch real-time predictions.  
   - Displays **interactive line charts** comparing **actual stock prices** (past data) and **predicted values**.  
   - Enables users to trigger **prediction generation on demand**.  

---

##  **Data Flow in the System**  

1️⃣ **Data Ingestion:** Historical stock data is fetched via **CSV or API** → Stored in the **database**.  
2️⃣ **Training & Prediction:** Prophet learns from **past trends** → Forecasts **future prices**.  
3️⃣ **API Exposure:** Predictions are made accessible via **FastAPI endpoints**.  
4️⃣ **Visualization:** The **frontend** fetches predictions → Renders **stock price trends** in an **interactive chart**.  

---

##  **Tech Stack**  

- **Backend:** FastAPI, SQLAlchemy, Uvicorn  
- **Frontend:** Streamlit, Plotly, Requests  
- **Machine Learning:** Facebook Prophet  
- **Database:** SQLite (extensible to PostgreSQL or MySQL)  
- **Data Source:** Structured CSV files (extendable to APIs)  

---

##  **Data Source & Processing**  

- The model currently trains on **historical stock data** stored in **CSV format** (`data/AAPL_stock_data_cleaned.csv`).  
- CSV structure:
  ```
  Date, Open, High, Low, Close, Volume
  2025-01-31, 246.91, 246.91, 233.18, 235.74, 101075100
  ```
- Columns are mapped as follows:
  - **`ds` (Date):** Used as the time index for predictions.  
  - **`y` (Close Price):** The target variable for forecasting.  
- Data preprocessing includes **missing value handling**, **date parsing**, and **formatting for Prophet**.  

---

##  **Machine Learning Model (Prophet)**  

- Prophet is used for **time-series forecasting**, trained on **historical stock prices**.  
- The model learns from:
  - **Daily & seasonal variations**
  - **Trend shifts & anomalies**
  - **Market fluctuations**  
- Forecasting output:
  - **`yhat`** → Predicted stock price.  
  - **`yhat_lower`, `yhat_upper`** → Confidence intervals.  

---

##  **Stock Price Prediction Workflow**  

1️⃣ **Data Cleaning**: Preprocess and structure data from CSV/API.  
2️⃣ **Model Training**: Fit Prophet to **historical price trends**.  
3️⃣ **Forecasting**: Predict stock movement for the next **30 days**.  
4️⃣ **Visualization**: Streamlit UI displays results in an interactive **time-series graph**.  

---

## 📡 **Backend API (FastAPI)**  

The backend exposes REST API endpoints for **data storage, retrieval, and prediction execution**.

| **Method**  | **Endpoint**        | **Description** |
|-------------|---------------------|----------------|
| **POST**    | `/insert_data/`      | Inserts new stock data into the database |
| **GET**     | `/fetch_data/`       | Retrieves stored stock data |
| **POST**    | `/predict/`          | Generates and returns 30-day stock predictions |

---

## 📊 **Frontend (Streamlit Dashboard)**  

- **UI Components**:
  - **Button to Fetch Predictions** (Triggers API call)
  - **Interactive Line Chart** (Actual vs Predicted)
---

##  **Key Features & Scalability**  

 **Dynamic Data Ingestion** (Extendable to real-time APIs)  
 **Scalable Database Integration** (SQLite → PostgreSQL/MySQL)  
 **Time-Series Forecasting** (Accurate stock price prediction)  
 **Interactive Dashboard** (Streamlit & Plotly for visualization)  
 **REST API-Driven** (Seamless backend-frontend communication)  

---

##  **Future Enhancements**  

- **Enhance API Data Sources** (Connect to **Yahoo Finance** & **Real-Time Stock Feeds**)  
- **Cloud Deployment** (Deploy on **AWS, GCP, or Heroku**)  
- **Improve Forecast Accuracy** (Fine-tune Prophet with **market indicators**)  
- **Add Multiple Stock Support** (Enable predictions for various stocks)  

---

##  **Conclusion**  
The **AI Market Trends Predictor** integrates **machine learning forecasting** with a **scalable API-driven system**, allowing users to retrieve, analyze, and predict stock prices efficiently. The **modular architecture** ensures flexibility for **future enhancements**, making it suitable for both **individual traders and financial analysts**.

---

##  **Author & Contribution**  

 **Developed by**: **Dev Thonangi**  

 **Contributions** are welcome! If you have ideas to improve the project, feel free to **submit a pull request**.

---

##  **License**  
 **MIT License** - Free to use and modify for commercial & personal projects.
