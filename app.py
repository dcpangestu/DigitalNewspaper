from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/weather/<region>')
def weather(region):
	weather = requests.get('https://openweathermap.org/data/2.5/weather?q=' +  +  '&appid=' + os.getenv("WEATHER_TOKEN"))
    return weather.text

if __name__ == '__main__':
    app.run(port = os.getenv("PORT"), debug = True)