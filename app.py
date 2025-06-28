from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler (make sure these are in the same folder)
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from form
    holiday = request.form['holiday']
    rain = float(request.form['rain'])
    snow = float(request.form['snow'])
    temp = float(request.form['temp'])
    weather = request.form['weather']
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    hours = int(request.form['hours'])
    minutes = int(request.form['minutes'])
    seconds = int(request.form['seconds'])

    # Encoding (same as model training)
    holiday_dict = {
        'None': 0, 'Labor Day': 1, 'Thanksgiving Day': 2,
        'Christmas Day': 3, 'New Year’s Day': 4,
        'Independence Day': 5, 'Diwali': 6, 'Eid': 7
    }
    weather_dict = {
        'Clear': 0, 'Clouds': 1, 'Fog': 2, 'Haze': 3,
        'Rain': 4, 'Snow': 5, 'Thunderstorm': 6
    }

    h = holiday_dict.get(holiday, 0)
    w = weather_dict.get(weather, 0)

    # Create input array
    input_data = np.array([[h, rain, snow, temp, w,
                            year, month, day, hours, minutes, seconds]])

    # Scale and predict
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]

    result = f"{round(prediction)} "
    print("Prediction:", result)  # for terminal debug

    return render_template('final.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
