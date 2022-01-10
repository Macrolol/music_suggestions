from flask import Flask, request,jsonify
from classes.suggesters import Suggester
from flask_cors import CORS
from datetime import datetime
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
    print(data) # debug
    print("login attempt: {}, {}".format(data['email_address'] , data['password']))
    user = Suggester.try_login(data['email_address'], data['password'])
    print(user) # debug 
    if not user:  
        return { 'error' : 'Invalid login credentials'}, 401
    return jsonify(user), 200


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data) # debug
    print("register attempt: {}, {}".format(data['email_address'] , data['password'], data['username']))
    id = Suggester.try_register(data['email_address'], data['password'], data['username'])
    print( id ) # debug
    if not id:
        return { 'message' : 'Invalid login credentials'}, 401
    return jsonify(id), 200