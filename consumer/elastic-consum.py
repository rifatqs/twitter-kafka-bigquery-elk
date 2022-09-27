from kafka import KafkaConsumer
from json import loads
from time import sleep

from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")


consumer = KafkaConsumer(
    'twitter',
    bootstrap_servers=['35.240.249.157:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='euy',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    data = event.value 
    res = es.index(index='investasi', body=data)
   # output = {"date":event.date} 
    print(res)
