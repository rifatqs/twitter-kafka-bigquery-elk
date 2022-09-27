from google.cloud import bigquery
from kafka import KafkaConsumer
from json import loads
from time import sleep

consumer = KafkaConsumer(
    'twitter',
    bootstrap_servers=['(broker):9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='euyyyy',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

PROJECT_ID = "static-cirrus-354813"
DATASET_ID = "BIGPROJECT"
TABLE_ID = "twitter"

client = bigquery.Client()

rows_to_insert = []


for event in consumer:
    data = event.value
    rows_to_insert = []
    rows_to_insert.append(data)
    errors = client.insert_rows_json(
        f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}", rows_to_insert
    )     
    if errors == []:
        print("New rows have been added.")
        print(data)
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
