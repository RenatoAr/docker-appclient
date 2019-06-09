docker build -t docker-appclient .
docker run -d -p 5000:5000 --name docker-appclient docker-appclient
