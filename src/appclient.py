import os

import docker
client = docker.from_env()

from flask import Flask, request
app = Flask(__name__)

dados = 'Hello World\n'

@app.route('/GET_INFO', methods=['GET'])
def getinfo():
    global dados
    dados = client.containers.get('docker-appclient')
    return dados

@app.route('/POST_INFO', methods=['POST'])
def postinfo():
    global dados
    dados = request.form['nome']
    return dados

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
