import flask

flask_app = flask.Flask(__name__)

from app import routes, custom_filters

import jinja2

env = jinja2.Environment()

#env.filters['to_upper'] = custom_filters.to_upper
#why it does not work ?

jinja2.filters.FILTERS['to_upper'] = custom_filters.to_upper
#why this solution viewed on internet works ?


