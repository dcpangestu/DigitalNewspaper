from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    weather = requests.get('https://openweathermap.org/data/2.5/weather?q=London&appid=2d57d53ccc1e413e485d654921fd72e5')
    return weather.text
    #return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True)