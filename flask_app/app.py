from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello world!!'

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0')