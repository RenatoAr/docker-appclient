docker build -t docker-appclient .
docker run -p 5000:5000 -it --name docker-appclient docker-appclient
