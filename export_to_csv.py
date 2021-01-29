from influxdb import InfluxDBClient
import pandas as pd

query = 'select * from temp_aggregated'
influxClient = InfluxDBClient(
    influxHost, influxPort, username, password)
influxClient.switch_database('aggregated')
points = influxClient.query(
    query, chunked=True).get_points(tags={'unit': 'Celsius'})

dfs = pd.DataFrame(points)

dfs.to_csv("temp_aggregated.csv", index=False)
