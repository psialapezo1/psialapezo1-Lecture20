import json

import flask
import random

app = flask.Flask(__name__)


bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)


@bp.route("/saved_review", method="POST")
def save_review():
    data = flask.request.get_json(data=True)


app.register_blueprint(bp)


@app.route("/review")
def review():
    Utilizer_search = flask.request.get_json()
    review_list = rating.query.filter_by(user=name.first())
    return flask.jsonify({"review": review_list})


app.run()
