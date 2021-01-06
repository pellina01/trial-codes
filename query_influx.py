from influxdb import InfluxDBClient

client = InfluxDBClient(host='ec2.IP', port=8086,
                        username='fishpond', password='thesis')
client.switch_database('fishpond')

res = client.query(
    'SELECT * FROM ph WHERE time > now() - 4d GROUP BY "unit"')
points = res.get_points(tags={'unit': 'ph'})

r = list(res.get_points(measurement='ph'))

for lists in r:
    print(lists["value"])
