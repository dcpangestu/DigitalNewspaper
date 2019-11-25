from flask import Flask, render_template
import requests
import config

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/facts/<region>')
def facts(region):
	facts = requests.get('http://localhost:5000/region/' + region)
	return facts.text

@app.route('/weather/<region>')
def weather(region):
	weather = requests.get('https://openweathermap.org/data/2.5/weather?q=' + region + '&appid=' + config.WEATHER_TOKEN)
    return weather.text

@app.route('/news/<region>')
def news(region):
	news = requests.get('https://newsapi.org/v2/everything?q=' + region + '&apiKey=' + config.NEWS_TOKEN)
    return news.text

if __name__ == '__main__':
    app.run(port = config.PORT, debug = True)