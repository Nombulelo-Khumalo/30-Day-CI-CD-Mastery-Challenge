# day02/project/app/main.py

from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, CI/CD World!"

#main.py update