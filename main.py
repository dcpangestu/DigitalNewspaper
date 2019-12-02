from flask import Flask, render_template, request
from datetime import datetime, timedelta
import requests
import json
import os

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
	try:
		req_weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + 'Jakarta' + '&units=metric&appid=' + os.environ['WEATHER_TOKEN'])
		req_news = requests.get('https://newsapi.org/v2/top-headlines?country=' + 'id' + '&apiKey=' + os.environ['NEWS_TOKEN'])
		req_facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + 'indonesia')
		weather = json.loads(req_weather.text)
		news = json.loads(req_news.text)
		facts = json.loads(req_facts.text)
		time = (datetime.now() + timedelta(hours = 7)).strftime('%d %B %Y, %H:%M:%S')
		return render_template('index.html', title = 'Home | Digital Newspaper', weather = weather, news = news, facts = facts, time = time, region = ['Indonesia', 'Jakarta'])
	except Exception as e:
		raise e

@app.route('/search')
def search():
	try:
		keyword = request.args.get('keyword').capitalize()
		req_weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + keyword + '&units=metric&appid=' + os.environ['WEATHER_TOKEN'])
		req_news = requests.get('https://newsapi.org/v2/everything?q=' + keyword + '&apiKey=' + os.environ['NEWS_TOKEN'])
		req_facts = requests.get('https://wiki-region-api.herokuapp.com/wiki?name=' + keyword)
		weather = json.loads(req_weather.text)
		news = json.loads(req_news.text)
		facts = json.loads(req_facts.text)
		time = (datetime.now() + timedelta(hours = 7)).strftime('%d %B %Y, %H:%M:%S')
		return render_template('index.html', title = keyword + ' | Digital Newspaper', weather = weather, news = news, facts = facts, time = time, region = [keyword, keyword], keyword = keyword)
	except Exception as e:
		raise e

## For sake of testing ##

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
		weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&units=metric&appid=' + os.environ['WEATHER_TOKEN'])
		weather = json.loads(weather.text)
		#weather = weather['weather']
		return weather
	except Exception as e:
		raise e

@app.route('/news/<region>')
def news(region):
	try:
		news = requests.get('https://newsapi.org/v2/top-headlines?country=' + region + '&apiKey=' + os.environ['NEWS_TOKEN'])
		news = json.loads(news.text)
		#news = news['articles']
		return news
	except Exception as e:
		raise e

if __name__ == '__main__':
	app.run(threaded = True, port = os.environ['PORT'])
	#app.run(port = os.environ['PORT'], debug = True)