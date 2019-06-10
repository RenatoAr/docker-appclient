sudo docker build -t docker-appclient .
sudo docker run -d -p 5000:5000 --name docker-appclient docker-appclient

#rodar container
sudo docker run -p 5000:5000 --name docker-appclient docker-appclient

#Abrir bash de um container rodando
sudo docker exec -it docker-appclient sh

#rodar container com docker.sock montado
sudo docker run -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock --name docker-appclient docker-appclient

#Instalar docker dentro do container
apk add docker