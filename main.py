from flask import Flask, render_template
import requests
import config

app = Flask(__name__)

user = {
	'name': 'Maulana',
	'gatau': 'idk dude'
}

@app.route('/')
@app.route('/home')
def index():
	try:
		return render_template('home.html', title = 'Home', user = user)
	except Exception as e:
		raise e

@app.route('/facts/<region>')
def facts(region):
	try:
		facts = requests.get('http://localhost:5000/region/' + region)
		return facts.text
	except Exception as e:
		raise e

@app.route('/weather/<region>')
def weather(region):
	try:
		weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + region + '&appid=' + config.WEATHER_TOKEN)
		return render_template('weather.html', title = 'Weather: ' + region , region = region, data = weather.text, user = user)
	except Exception as e:
		raise e

@app.route('/news/<region>')
def news(region):
	try:
		news = requests.get('https://newsapi.org/v2/everything?q=' + region + '&apiKey=' + config.NEWS_TOKEN)
		return news.text
	except Exception as e:
		raise e

if __name__ == '__main__':
	print('Server is running on ' + str(config.PORT))
	app.run(port = config.PORT, debug = True)