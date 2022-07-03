import flask
from app import flask_app


@flask_app.route('/say_hi')
def say_hi():
    return flask.render_template("say_hi.html")

