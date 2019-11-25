from flask import Flask, render_template
import requests
import config

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	try:
    	return render_template("home.html")
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
		weather = requests.get('https://openweathermap.org/data/2.5/weather?q=' + region + '&appid=' + config.WEATHER_TOKEN)
    	return weather.text
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
    app.run(port = config.PORT, debug = True)