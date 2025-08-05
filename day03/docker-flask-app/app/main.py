#day03/docker-flask-app/app/main.py
#testing day 03 pipeline

from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "🚀 Dockerized CI/CD App Running!"
