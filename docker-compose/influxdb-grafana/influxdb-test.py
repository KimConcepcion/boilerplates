import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
# token = os.environ.get("Meei4izC5YJju-cE8SEGYxB-RgQVLarXaUdfz9EUqR88zE7CuNOBETC5u5QZD8CIGCfhEiXphom9x0YvFlhgDg==")
org = "my-org"
url = "http://0.0.0.0:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="kim-bucket"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="my-org", record=point)
  time.sleep(1) # separate points by 1 second

query_api = client.query_api()

query = """from(bucket: "kim-bucket")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="my-org")

for table in tables:
  for record in table.records:
    print(record)

query_api = client.query_api()

query = """from(bucket: "kim-bucket")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="my-org")

for table in tables:
    for record in table.records:
        print(record)
