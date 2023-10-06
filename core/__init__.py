from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

from core.views import core

app.register_blueprint(core)