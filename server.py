#!/usr/bin/env python

# Import framework
from flask import Flask, request
from flask import jsonify
import datetime

# Instantiate the app
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify("Hello World")


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


