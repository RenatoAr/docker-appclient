import os

from flask import Flask, request
import docker

app = Flask(__name__)

dados = 'nada'
# client = docker.from_env()
# container = client.containers.get('docker-flask')
client = docker.from_env()
objdocker = docker.Client(base_url="unix://var/run/docker.sock")
objdocker.stats_container = objdocker.stats('docker-appclient')
for stat in objdocker.stats_container:
print(stat)

@app.route('/', methods=['GET'])
def getinfo():
    global dados
    # global container
    #return 'Hello '+ container
    return 'Hello '+ dados

@app.route('/', methods=['POST'])
def postinfo():
    global dados
    dados = request.form['nome']
    return 'hello' + dados

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
