import streamlit as st
import pandas as pd
import warnings
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objs as go

# Suppress ARIMA frequency warnings
warnings.filterwarnings("ignore", message="No frequency information was provided")

# Load data
df = pd.read_csv("processed_weather_data.csv", parse_dates=["DATE"])
st.title("📈 ARIMA Forecast Viewer")

# City selection
city = st.selectbox("🏙️ Select City", sorted(df["city"].unique()))

# Filter and prepare time series
city_df = df[df["city"] == city].sort_values("DATE")
series = city_df.set_index("DATE")["T2M_MAX"].dropna()
series = series.asfreq('D')  # Set explicit daily frequency to avoid warnings

try:
    with st.spinner("🔄 Fitting ARIMA model..."):
        model_arima = ARIMA(series, order=(5, 1, 0)).fit()
        forecast = model_arima.forecast(steps=7)

        last_date = series.index[-1]
        forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7, freq='D')

    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=series.index[-60:], y=series[-60:], mode='lines+markers',
        name='Historical T2M_MAX', line=dict(color='#d1495b')
    ))
    fig.add_trace(go.Scatter(
        x=forecast_dates, y=forecast, mode='lines+markers',
        name='Forecasted T2M_MAX', line=dict(color='#1f77b4', dash='dash')
    ))

    fig.update_layout(
        title=f"📊 7-Day Max Temperature Forecast for {city}",
        xaxis_title="Date",
        yaxis_title="T2M_MAX (°C)",
        hovermode='x unified',
        template="plotly_white",
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)

    # Forecast Data Table
    forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecasted T2M_MAX": forecast.round(2)})
    st.dataframe(forecast_df.style.set_table_styles([
        {'selector': 'thead', 'props': [('background-color', '#d1495b'), ('color', 'white')]},
        {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
    ]))

except Exception as e:
    st.error(f"❌ ARIMA model failed: {e}")
