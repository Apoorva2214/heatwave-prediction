import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import timedelta

monthly_means = pd.read_csv("monthly_means.csv")
df = pd.read_csv("processed_weather_data.csv", parse_dates=["DATE"])
scaler = joblib.load("scaler.pkl")
model = joblib.load("heatwave_model.pkl")

st.title("🔮 Heatwave Prediction")

city = st.selectbox("🏙️ Select City", sorted(monthly_means['city'].unique()))
date = st.date_input("📅 Select Prediction Start Date")

with st.expander("🧮 Enter Meteorological Inputs"):
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        T2M_MAX = st.number_input("🌡️ T2M_MAX (°C)", 20.0, 50.0, 42.0, help="Max temperature in Celsius")
        RH2M = st.number_input("💧 RH2M (%)", 0.0, 100.0, 40.0, help="Relative Humidity at 2 meters height")
    with col2:
        RH2M_7D = st.number_input("💧 RH2M_7D (%)", 0.0, 100.0, 42.0, help="7-day average RH2M")
        PRECTOTCORR_7D = st.number_input("🌧️ 7D Total Precip (mm)", 0.0, 100.0, 5.0, help="7-day total precipitation")

    T2M_MAX_7D = st.slider("📊 T2M_MAX_7D", 20.0, 50.0, 40.0)
    T2M_MAX_14D = st.slider("📊 T2M_MAX_14D", 20.0, 50.0, 38.5)

Heat_Index = 0.5 * (T2M_MAX + 61.0 + ((T2M_MAX - 68.0) * 1.2) + (RH2M * 0.094))
st.markdown(f"""
<div style="
    background: #ffdddd;
    border-left: 6px solid #d1495b;
    padding: 10px 15px;
    margin: 15px 0;
    font-weight: 700;
    font-size: 1.25rem;
    border-radius: 8px;
">
Calculated Heat Index: {Heat_Index:.2f} °C
</div>
""", unsafe_allow_html=True)

def temp_anomaly(city, date, val):
    m = pd.to_datetime(date).month
    base = monthly_means[(monthly_means['city'].str.lower() == city.lower()) & (monthly_means['Month'] == m)]
    return val - base['Monthly_Mean_T2M_MAX'].values[0] if not base.empty else 0

if st.button("🚀 Predict"):

    anomaly = temp_anomaly(city, date, T2M_MAX)
    input_vec = pd.DataFrame([[T2M_MAX_7D, T2M_MAX_14D, Heat_Index, RH2M, RH2M_7D, PRECTOTCORR_7D, anomaly]],
                             columns=["T2M_MAX_7D", "T2M_MAX_14D", "Heat_Index", "RH2M", "RH2M_7D", "PRECTOTCORR_7D", "Temp_Anomaly"])
    input_scaled = scaler.transform(input_vec)
    today_pred = model.predict(input_scaled)[0]

    st.subheader("📍 Prediction for Selected Date")
    if today_pred == 1:
        st.error("🔥 Heatwave predicted for today!")
    else:
        st.success("✅ No heatwave predicted today.")

    # ... (rest of your code)
