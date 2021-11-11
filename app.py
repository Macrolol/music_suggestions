from flask import Flask
from jinja2 import render_template

from classes.data import Suggester



app = Flask(__name__)


@app.route('/')
def index():
    dummy_suggester = Suggester("michael", "email@email.com")

    return render_template('index.html', dummy_suggester)

@app.route('/api/<int:suggester_id>/suggested_by')
def suggested_by(suggester_id):
    suggester = Suggester.query.get_or_404(suggester_id)
    return suggester.name

@app.route('/api/<int:suggester_id>/suggested_to')
def suggested_to(suggester_id):
    suggester = Suggester.query.get_or_404(suggester_id)
    return suggester.email

@app.route('/api/wants_suggestions/<int:limit>')
def wants_suggestions(limit):
    
