from flask import Flask, render_template, request
import joblib
import datetime
import requests

app = Flask(__name__)
model = joblib.load("weather_model.pkl")

API_KEY = "your_openweather_api_key"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    city = None

    if request.method == "POST":
        print("Form Data:", request.form)  # Debugging: Print form data
        if "city" in request.form and "date" in request.form:  # Ensure keys exist
            city = request.form["city"]
            date_str = request.form["date"]
            timestamp = int(datetime.datetime.strptime(date_str, "%Y-%m-%d").timestamp())

            # Fetch live temperature for the city (optional)
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                live_temp = response.json()["main"]["temp"]
            else:
                live_temp = None  # In case API fails

            # Predict temperature
            prediction = model.predict([[timestamp]])[0]
        else:
            print("Form missing city or date")

    return render_template("index.html", prediction=prediction, city=city)

if __name__ == "__main__":
    app.run(debug=True)
