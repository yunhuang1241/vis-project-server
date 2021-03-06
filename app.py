from flask import Flask, request
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()