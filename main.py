'''The main app module takes care to setup the routes for the REST API and 
calling the proper handler objects to process the request.
'''
from flask import Flask

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Apply CORS to this app
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World! This is the Disaster Resource Locator app.'


if __name__ == '__main__':
    app.run()
