import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Example: Load the same dataset you used in Colab
df = pd.read_csv("processed_weather_data.csv")  # Use actual CSV file used in Colab

# Select only the feature columns used for scaling
feature_columns = ["T2M_MAX_7D", "T2M_MAX_14D", "Heat_Index", "RH2M", "RH2M_7D", "PRECTOTCORR_7D", "Temp_Anomaly"]  # Modify if needed
X = df[feature_columns]

# Fit scaler
scaler = StandardScaler()
scaler.fit(X)

# Save it locally
joblib.dump(scaler, "scaler.pkl")

print("✅ Scaler saved locally.")
