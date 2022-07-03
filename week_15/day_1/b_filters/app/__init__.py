import flask

flask_app = flask.Flask(__name__)

from app import routes, custom_filters

import jinja2

#env = jinja2.Environment()

flask_app.jinja_env.filters['to_upper'] = custom_filters.to_upper

#solution found on stackoverflow that I don't understand
#jinja2.filters.FILTERS['to_upper'] = custom_filters.to_upper




