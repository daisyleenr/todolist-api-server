FROM python:3

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 app:app

EXPOSE 5000