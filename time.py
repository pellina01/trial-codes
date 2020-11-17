import requests
import json
import time

# url = "http://worldtimeapi.org/api/timezone/Asia/Manila"

while True:
    try:
        url = "http://worldtimeapi.org/api/timezone/Asia/Manila"
        r = requests.get(url=url)
        data = r.json()
        print(data["datetime"])
        time.sleep(1)
    except:
        print("no internet")
        time.sleep(1)
