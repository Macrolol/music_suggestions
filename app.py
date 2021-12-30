from flask import Flask, request
from classes.suggesters import Suggester
from flask_cors import CORS
import jsons;
#from classes.data import Suggester



app = Flask(__name__)
CORS(app)

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
    pass

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    print("login attempt: {}, {}".format(data['email_address'] , data['password']))
    user = Suggester.try_login(data['email_address'], data['password'])
   
    if user is None:
        return 'Invalid login credentials', 401
    return jsons.dump(user), 200
