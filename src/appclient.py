import os
import datetime
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/GET_INFO', methods=['GET'])
def getinfo():
    dados = requests.get('http://192.168.50.10:5000/GET_INFO').content
    return dados

@app.route('/POST_INFO', methods=['POST'])
def postinfo():
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%c")
    nomecontainer = 'docker stats --no-stream --format "{{.Name}}"'
    nomecontainer = os.popen(nomecontainer).read()
    idcontainer = 'docker stats --no-stream --format "{{.ID}}"'
    idcontainer = os.popen(idcontainer).read()
    imageid = 'docker images --filter=reference=docker-appclient --format "{{.ID}}"'
    imageid = os.popen(imageid).read()
    usocpu = 'docker stats --no-stream --format "{{.CPUPerc}}"'
    usocpu = os.popen(usocpu).read()
    usomem = 'docker stats --no-stream --format "{{.MemUsage}}"'
    usomem = os.popen(usomem).read()
    r = requests.post('http://192.168.50.10:5000/POST_INFO', data=[('timestamp',timestamp), ('nomecontainer',nomecontainer), ('idcontainer',idcontainer), ('imageid',imageid), ('usocpu',usocpu), ('usomem',usomem)])
    return 'Docker Stats enviado!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
