import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
df = pd.read_csv("weather_data.csv")

# Convert datetime to numerical values
df['datetime'] = pd.to_datetime(df['datetime'])
df['timestamp'] = df['datetime'].astype(int) // 10**9  # Convert to UNIX timestamp

# Define features & labels
X = df[['timestamp']]
y = df['temperature']

# Split into train & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}°C")

# Save model
joblib.dump(model, "weather_model.pkl")

# Plot results
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel("Timestamp")
plt.ylabel("Temperature")
plt.legend()
plt.show()
    