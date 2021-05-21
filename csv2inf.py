import csv
from datetime import datetime
from influxdb import InfluxDBClient

host = '34.203.207.77'
port = 8086
username = 'fishpond'
pw = 'thesis'
influxdb_client = InfluxDBClient(host, port, username, pw)

with open('tb.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    measurement_name = "tb"
    data = []
    for row in csv_reader:
        line_count += 1
        if line_count == 1:
            continue
        try:
        	d = datetime.strptime(row[0],'%Y-%m-%dT%H:%M:%S.%fZ')
        except:
        	d = datetime.strptime(row[0],'%Y-%m-%dT%H:%M:%SZ')
        data.append("{measurement},unit={unit} value={value} {timestamp}".format(measurement=measurement_name,unit=row[1],value=float(row[2]),timestamp=int(datetime.timestamp(d)*1000)))

    influxdb_client.write_points(data, database='fishpond', time_precision='u',batch_size=line_count, protocol='line')
    print("ok")
	