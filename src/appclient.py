import os
import statsToJSON

from flask import Flask, request
import docker

app = Flask(__name__)

dados = 'Hello World\n'

@app.route('/', methods=['GET'])
def getinfo():
    global dados
    return dados

@app.route('/', methods=['POST'])
def postinfo():
    global dados
    dados = request.form['nome']
    return dados

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug:True)
