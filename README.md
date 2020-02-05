# Digital Newspaper
A website that can display news, weather, and facts of cities in Indonesia\
Mata Kuliah II3160 - Teknologi Sistem Terintegrasi\
Deployed application: [https://digital-newspaper.herokuapp.com](https://digital-newspaper.herokuapp.com)\
\
**Group 5**:
1. Dwi Cahyo Pangestu - 18217029
2. Alfian Maulana Ibrahim - 18217038

**Used API**:
1. WikiRegionAPI - API tentang crawling fun facts dari Wikipedia dan API penyedia wilayah Indonesia (https://wiki-region-api.herokuapp.com/{routes}), repository: https://github.com/alfinm01/tst
2. NewsAPI - API penyedia berita di berbagai wilayah di dunia (newsapi.org)
3. OpenWeatherMap - API penyedia cuaca di berbagai wilayah di dunia (openweathermap.org)

## Clone setup (on Windows example)

``` bash
# install environments
$ py -3 -m venv venv
$ venv\Scripts\activate
(venv) $ pip install -r requirements.txt
```

## Running locally (on Windows example)

``` bash
# serve at default http://localhost:5000
$ venv\Scripts\activate
(venv) $ py main.py

# to leave venv
(venv) $ deactivate
```