FROM python:3.12-rc-alpine
WORKDIR /usr/src/client

RUN pip install requests==2.28.2
COPY . .

CMD [ "python", "client.py" ] 