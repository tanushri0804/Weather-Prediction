import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key is missing. Make sure to set it in the .env file.")

city = input("Enter city name: ")  

URL = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
response = requests.get(URL)
data = response.json()

# Extract relevant data
weather_data = []
for entry in data['list']:
    weather_data.append({
        'datetime': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'weather': entry['weather'][0]['main']
    })

# Convert to DataFrame
df = pd.DataFrame(weather_data)
df.to_csv("weather_data.csv", index=False)
print(f"Weather data for {city} saved successfully!")
