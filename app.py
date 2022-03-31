import json

import flask
import random

app = flask.Flask(__name__)

Base_url = "https://api.themoviedb.org/3/movie/"

parfait = {"api_key": os.getenv("key")}

response = requests.get(url=url, params=params)
data = response.json()


@app.route("/")
def index():
    return flask.render_template("index.html")

