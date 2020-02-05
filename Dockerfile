FROM python:3.6-alpine

WORKDIR /digitalnewspaper

COPY requirements.txt requirements.txt
COPY templates templates
COPY main.py config.py ./

RUN pip install -r requirements.txt

ENV FLASK_APP main.py

EXPOSE 5000
CMD flask run