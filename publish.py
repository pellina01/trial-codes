#!/usr/bin/env python3

import time
import paho.mqtt.client as mqtt
import json
# This is the Publisher


topic = "topic/tb"
url = " "


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
    clock = int(time.time())
    myvar = input("enter message: ")
    client.publish(topic, json.dumps(
        {"status": "sending", "time": clock, "value": myvar}), retain=False)
    time.sleep(2)


# sample_string = input("enter a string")
# if sample_string.find("Oscar") >= 0:
#     print("the given string contains Oscar")
# else:
#     print("the given string does not contain Oscar")
