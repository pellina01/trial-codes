import i2c_arduino_mod as i2c
import time
import json
import unixtime_api as clock
from mqtt import mqtt
from config import config
import datetime
import temp as w1temp

ph = config.topic
mqtt_url = config.mqtt_url
time_url = config.time_url
list_name = config.list_name
tb = "topic/tb"
temp = "topic/temp"

tb_mqtt = mqtt(tb, mqtt_url)
ph_mqtt = mqtt(ph, mqtt_url)
temp_mqtt = mqtt(temp, mqtt_url)
#sensor type 1 fpr ph, 2 for turbidity
while True:
    ph_value = str(i2c.read_arduino(11, 1))
    tb_value = str(i2c.read_arduino(11, 2))
    temp_value = str(w1temp.read_value())
    current_time = str(clock.getnow(time_url, list_name))
    ph_data = {"time": current_time, "value": ph_value}
    tb_data = {"time": current_time, "value": tb_value}
    temp_data = {"time": current_time, "value": temp_value}
    temp_mqtt.send(json.dumps(temp_data))
    ph_mqtt.send(json.dumps(ph_data))
    tb_mqtt.send(json.dumps(tb_data))
    time.sleep(2)

while True:
    try:
        ph_value = str(i2c.read_arduino(11, 1))
        tb_value = str(i2c.read_arduino(11, 2))
        temp_value = temp.read_value()
        current_time = str(clock.getnow(time_url, list_name))
        ph_data = {"time": current_time, "value": ph_value}
        tb_data = {"time": current_time, "value": tb_value}
        temp_data = {"time": current_time, "value": temp_value}
        temp_mqtt.send(json.dumps(temp_data))
        ph_mqtt.send(json.dumps(ph_data))
        tb_mqtt.send(json.dumps(tb_data))
        time.sleep(2)
    except Exception as e:
        print("error occured: ")
        print(e)
        time.sleep(2)
        
        
