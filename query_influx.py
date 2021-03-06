from influxdb import InfluxDBClient
import time
import math

topic = 'ph'
client = InfluxDBClient(host='3.236.214.86', port=8086,
                        username='fishpond', password='thesis')
client.switch_database('fishpond')

query_result = client.query(
    'SELECT * FROM {} WHERE time > now() - 10d'.format(topic))

data_points = list(query_result.get_points(measurement=topic))
print(data_points)
aggregated_data = 0
n = 0
for lists in data_points:
    aggregated_data += lists["value"]
    n += 1
    print(aggregated_data)

aggregated_data /= n
print(aggregated_data)
json_body = [
    {
        "measurement": "{}_aggregated".format(topic),
        "tags": {
            "user": topic,
        },
        "time": math.trunc(time.time())-86400,
        "fields": {
            "value": aggregated_data
        }
    }]

client.write_points(json_body)
print('success')
