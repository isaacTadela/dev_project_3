from flask import Flask, request
from db_connector import insert, select, update, delete
import os
import signal

app = Flask(__name__)


# Supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            if insert(user_id, user_name):
                return {'status': 'ok', 'user_added': user_name}, 200 # status code
            else:
                return {'status': 'error', 'reason': 'id already exists'}, 500
        except Exception as e:
            print(e)
            return {'status': 'error', 'reason': 'id already exists'}, 500
    elif request.method == 'GET':
        try:
            user_name = select(user_id)
            return {'status': 'ok', 'user_name': user_name}, 200  # status code
        except Exception as e:
            print(e)
            return {'status': 'error', 'reason': 'no such id'}, 500
    elif request.method == 'PUT':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            update(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        except Exception as e:
            print(e)
            return {'status': 'error', 'reason': 'no such id'}, 500
    elif request.method == 'DELETE':
        try:
            delete(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except Exception as e:
            print(e)
            return {'status': 'error', 'reason': 'no such id'}, 500


# Stop the server with http request
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


# Home page
@app.route('/')
def home():
    return 'Welcome to the flask server within docker, ' \
           'you can go to "/users/user_id" to search a user in database.'


app.run(host='0.0.0.0', debug=True, port=5000)