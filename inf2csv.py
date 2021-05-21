  
from influxdb import InfluxDBClient
import pandas as pd

# query = 'select * from do where time > 1615343254000'
query = 'select * from temp'
influxClient = InfluxDBClient(
    '54.167.184.7', '8086', 'fishpond', 'thesis')
influxClient.switch_database('fishpond')
points = influxClient.query(
    query, chunked=True).get_points(tags={'unit': 'Celsius'})

dfs = pd.DataFrame(points)

dfs.to_csv("temp.csv", index=False)