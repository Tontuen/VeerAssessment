import requests
from flask import request
from flask import Flask
import json

app = Flask(__name__)


@app.route('/checkAuth')
def check_authorization():
    # Looks for the 'Authorization' header
    # If found, returns a boolean which determines whether or not the user is authorized to navigate between pages
    try:
        auth = request.headers['Authorization']
        if auth == 'Authorized':
            return json.dumps(True)
        else:
            return json.dumps(False)
    except:
        return json.dumps(False)


# 3. Create another REST API endpoint that will fetch a result from any public API and save the response as a file.
@app.route('/saveResponse')
def saveAPIResponse():
    try:
        api_url = request.args['url']
        path = request.args['path'] + '/'
    except KeyError:
        return 'You need a "url" and "path" parameter.'
    response = requests.get(api_url).json()

    # Save the API response to 'apiresponse.json' in the path given
    with open(path + 'apiresponse.json', 'w') as outfile:
        json.dump(response, outfile)

    return 'Data Saved to ' + path + 'apiresponse.json'