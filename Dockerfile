FROM python:3.7-alpine
ADD ./src/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
RUN apk add docker
ADD ./src /opt/src/
WORKDIR /opt/src
EXPOSE 5000
CMD ["python", "appclient.py"]
