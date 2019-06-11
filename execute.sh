#!bin/bash

#Destroi container docker-appclient se exisir
sudo docker rm docker-appclient
#Destroi imagem docker-appclient se exitir
sudo docker image rm docker-appclient
#Controi a imagem docker-appclient
sudo docker build -t docker-appclient .
#Roda container com docker.sock montado
sudo docker run -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock --name docker-appclient docker-appclient
