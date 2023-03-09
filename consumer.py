from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer('heatmap_demo', bootstrap_servers=['localhost:9092'], 
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
client = MongoClient("mongodb+srv://telemachosc:<pass>@cluster0.woidtmk.mongodb.net/?retryWrites=true&w=majority")
db = client['heatmap_demo']
collection = db['data']


if __name__ =='__main__':
    print('Consumer started...')

    for message in consumer:
        data = message.value
        collection.insert_one(data)
        print('sent one click! yey!')
