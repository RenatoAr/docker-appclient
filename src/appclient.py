import os

from flask import Flask, request

cmd = 'docker ps -a'

app = Flask(__name__)

dados = 'Hello World\n'

@app.route('/GET_INFO', methods=['GET'])
def getinfo():
    global dados
    os.system(cmd)
    return dados

@app.route('/POST_INFO', methods=['POST'])
def postinfo():
    global dados
    dados = request.form['nome']
    return dados

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
