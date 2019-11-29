from flask import Flask, render_template
import requests
import config
import json

app = Flask(__name__)

user = {
	'name': 'Maulana',
	'gatau': 'idk dude'
}

@app.route('/')
@app.route('/home')
def home():
	try:
		region = "Jakarta"
		weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&appid=' + config.WEATHER_TOKEN)
		news = requests.get('https://newsapi.org/v2/top-headlines?country=id&apiKey=' + config.NEWS_TOKEN)
		facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + region)
		return render_template('home.html', title = 'Home', weather = weather, news = news.articles, facts = facts, user = user)
	except Exception as e:
		raise e

@app.route('/<region>')
def kota(region):
	try:
		weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&appid=' + config.WEATHER_TOKEN)
		news = requests.get('https://newsapi.org/v2/everything?q=' + region + '&apiKey=' + config.NEWS_TOKEN)
		facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + region)
		return render_template('home.html', title = 'Home', weather = weather, news = news, facts = facts, user = user)
	except Exception as e:
		raise e

@app.route('/facts/<region>')
def facts(region):
	try:
		facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + region)
		facts = json.loads(facts.text)
		facts = facts['articles']
		return fa[0]
		""" return render_template('home.html', title = 'Facts: ' + region , facts = facts, user = user) """
	except Exception as e:
		raise e

@app.route('/weather/<region>')
def weather(region):
	try:
		weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&&appid=' + config.WEATHER_TOKEN)
		weather = json.loads(weather.text)
		weather = weather['weather'][0]
		return weather
		""" return render_template('home.html', title = 'Weather: ' + region, weather = weather, news = news, facts = facts, user = user) """
	except Exception as e:
		raise e

@app.route('/news/<region>')
def news(region):
	try:
		news = requests.get('https://newsapi.org/v2/everything?q=' + region + '&apiKey=' + config.NEWS_TOKEN)
		news = json.loads(news.text)
		news = news['articles']
		return news[0]
		""" return render_template('home.html', title = 'News: ' + region , news = news, user = user) """
	except Exception as e:
		raise e

if __name__ == '__main__':
	print('Server is running on ' + str(config.PORT))
	app.run(port = config.PORT, debug = True)