from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

db = []

@app.route('/currentWeather', methods=['POST'])
def currentWeather():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    city_name = request.form['city']

    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=d15352b0bff4d2c3b60fafed5288cc85')
    json_object = r.json()
    sky = json_object["weather"][0]["description"]

    db.append({'name' : city_name, 'current weather':sky, 'current time' : current_time})
    return render_template('output.html', weather=sky, city=city_name)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/currentWeather/all')
def allWeather():
    return jsonify(db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
