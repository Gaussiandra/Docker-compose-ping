import requests
import time

n_requests = 0
while True:
    try:
        answer = requests.get("http://server:5000/ping")
        n_requests += 1

        print(n_requests, answer.text, end='', flush=True)
    except Exception as e:
        print(e)

    time.sleep(3)