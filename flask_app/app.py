import time
from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello world!!'

@server.route('/app')
def hello_mark():
    return 'Hello Mark!!'

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=8000)