from flask import Flask, render_template
import requests
import config
import json

app = Flask(__name__)


@app.route('/')
def index():
	try:
		region = "Jakarta"
		weather = json.loads(requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&units=celcius&appid=' + config.WEATHER_TOKEN).text)
		news = requests.get('https://newsapi.org/v2/top-headlines?country=id&apiKey=' + config.NEWS_TOKEN)
		facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + region)
		print(weather)
		return render_template('index.html', title = 'Home | Digital Newspaper', weather = weather, news = news, facts = facts)
	except Exception as e:
		raise e

# For sake of testing

@app.route('/facts/<region>')
def facts(region):
	try:
		facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + region)
		facts = json.loads(facts.text)
		#facts = facts['articles']
		return facts
	except Exception as e:
		raise e

@app.route('/weather/<region>')
def weather(region):
	try:
		weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&&appid=' + config.WEATHER_TOKEN)
		weather = json.loads(weather.text)
		#weather = weather['weather']
		return weather
	except Exception as e:
		raise e

@app.route('/news/<region>')
def news(region):
	try:
		news = requests.get('https://newsapi.org/v2/everything?q=' + region + '&apiKey=' + config.NEWS_TOKEN)
		news = json.loads(news.text)
		#news = news['articles']
		return news
	except Exception as e:
		raise e

if __name__ == '__main__':
	app.run(port = config.PORT, debug = True)