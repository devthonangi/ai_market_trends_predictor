!pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

API_URL = "http://127.0.0.1:8000/predict/"

st.title(" Stock Price Prediction")

if st.button("Get Stock Price Forecast"):
    response = requests.post(API_URL)

    if response.status_code == 200:
        data = response.json().get("predictions", [])

        if data:
            df = pd.DataFrame(data)

            # Rename columns for better clarity
            df.rename(columns={"ds": "Date", "yhat": "Stock Price"}, inplace=True)
            df["Date"] = pd.to_datetime(df["Date"])

            # Plot Actual vs Predicted Stock Prices
            fig = px.line(df, x="Date", y="Stock Price", color="type",
                          title="Stock Price Forecast",
                          labels={"Date": "Date", "Stock Price": "Stock Price ($)", "type": "Type"},
                          line_shape="linear")

            # Customize legend and colors
            fig.update_traces(marker=dict(size=4), line=dict(width=2))
            fig.update_layout(
                legend=dict(
                    title="Legend",
                    x=0.02, y=0.98,
                    bgcolor="rgba(255,255,255,0.5)"
                ),
                title_font_size=20
            )

            st.plotly_chart(fig)
        else:
            st.error("No prediction data available.")
    else:
        st.error("Error fetching predictions from API.") 
