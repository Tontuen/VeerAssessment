# 1. Create a REST API endpoint (preferably using a Python backend, but can be Node as well) that will look for some
# parameter in the header of the request and deny access if that parameter's value is incorrect or missing
# (you can call the parameter whatever you like)
# 2. Create a React app that will have two pages, each with a button and a textbox:
# - switching between pages should not reload the browser (i.e. a single-page application)
# - the buttons should send a request with and without the required header to the endpoint above
# - the textbox is where you can display the response
# 3. Create another REST API endpoint that will fetch a result from any public API and save the response as a file.

import requests
from flask import request
from flask import Flask
import json

app = Flask(__name__)


@app.route('/checkAuth')
def check_authorization():
    # Looks for the 'Authorization' header
    # If found, returns a json message of whether or not the user is authorized to navigate between certain pages
    try:
        auth = request.headers['Authorization']
        if auth == 'Authorized':
            return {'authorization': 'Passed'}
        else:
            return {'authorization': 'You are not authorized'}
    except:
        return {'authorization': 'You are not authorized'}


@app.route('/totoro')
def getTotoroData():
    response = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49').json()

    # Change file location to wherever you want to save it
    # Currently saved to the flask-api directory
    with open('Totoro.json', 'w') as outfile:
        json.dump(response, outfile)

    return 'Data Saved to Totoro.json'