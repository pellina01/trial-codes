#!/usr/bin/env python3

import time
import paho.mqtt.client as mqtt
import json
# This is the Publisher


topic = "topic/ph"
url = "ec2-18-206-177-119.compute-1.amazonaws.com"


client = mqtt.Client()
client.will_set(topic, payload=json.dumps(
    {"status": "disconnected"}), qos=0, retain=False)

connected = False
printed = False
while connected is False:
    try:
        client.connect(url, 1883, 60)
        connected = True
    except:
        if not printed:
            print(
                "failed to establish connection with %s,reconnecting..." % url)
            printed = True

print("connecting.......")
client.publish(topic, json.dumps({"status": "connected"}))

client.loop_start()
# client.disconnect()


while True:
    myvar = input("enter message: ")
    client.publish(topic, json.dumps(
        {"status": "connected", "message": myvar}), retain=False)
    time.sleep(2)


# sample_string = input("enter a string")
# if sample_string.find("Oscar") >= 0:
#     print("the given string contains Oscar")
# else:
#     print("the given string does not contain Oscar")
