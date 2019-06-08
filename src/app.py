import os

from flask import Flask, request
import docker

app = Flask(__name__)

dados = 'nada'
myCmd = 'ls'
# client = docker.from_env()
# container = client.containers.get('docker-flask')

@app.route('/', methods=['GET'])
def getinfo():
    global dados
    os.system(myCmd)
    # global container
    #return 'Hello '+ container
    return 'Hello '+ dados

@app.route('/', methods=['POST'])
def postinfo():
    global dados
    dados = request.form['nome']
    return 'hello' + dados

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
