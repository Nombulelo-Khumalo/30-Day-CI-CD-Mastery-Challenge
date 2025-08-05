#day03/docker-flask-app/app/main.py
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "🚀 Dockerized CI/CD App Running!"
