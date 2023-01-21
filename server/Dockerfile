FROM python:3.12-rc-alpine
WORKDIR /usr/src/server

RUN pip install flask==2.2.2 
COPY . .

CMD [ "python", "server.py" ] 