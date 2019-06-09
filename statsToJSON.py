import json
import datetime
import os

def dockerStatsToJSON (path, filename, data):
	filePathNameWExt = './' + path + './' + filename + '.json'
	with open(filePathNameWExt, 'w') as fp:
		json.dump(data, fp)

path = './'
filename = 'dockerStats'
timestamp = datetime.datetime.now()
data = {}
#Data
data['timestamp'] = str(timestamp)
#ID da Imagem
data['imageID'] = os.popen('sudo docker images --filter=reference=docker-appclient --format "table {{.ID}}\t"').read()
#Dados do Container
data['containerStats'] = os.popen('sudo docker stats --no-stream --format "table {{.Name}}\t{{.ID}}\t{{.CPUPerc}}\t{{.MemUsage}}"').read()

dockerStatsToJSON (path, filename, data)