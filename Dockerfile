FROM python:3.7.4

WORKDIR .
COPY requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["py", "main.py"]