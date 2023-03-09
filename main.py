from flask import Flask, request
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/heatmap', methods=['POST'])
def heatmap():
    data = request.json
    producer.send('heatmap-demo', data.encode('utf-8'))
    print('send successss')
    return 'Data sent to Kafka'

if __name__ == '__main__':
    app.run(debug=True)