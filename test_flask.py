from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/.well-known/acme-challenge/DyW69SztQ4-bEsdIcBjdE-X619tfeW0PjDTxUPJDfYg',methods=['GET'])
def challenge():
    with open('/.well-known/acme-challenge/DyW69SztQ4-bEsdIcBjdE-X619tfeW0PjDTxUPJDfYg') as f:
        return f.read()

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80)
