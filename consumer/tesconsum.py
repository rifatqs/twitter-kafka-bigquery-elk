from kafka import KafkaConsumer
from json import loads
from time import sleep
consumer = KafkaConsumer(
    'twitter',
    bootstrap_servers=['(broker):9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    
