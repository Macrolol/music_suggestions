from flask import Flask
from jinja2 import render_template

from data import Suggester



app = Flask(__name__)


@app.route('/')
def index():
    dummy_suggester = Suggester("michael", "email@email.com")

    return render_template('index.html', dummy_suggester)