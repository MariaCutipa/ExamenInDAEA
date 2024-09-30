from flask import Flask, render_template, request, make_response, g, jsonify
from kafka import KafkaProducer, KafkaConsumer
from redis import Redis
import os
import socket
import random
import json
import logging

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

# Configurar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='3.86.34.96:9092',  # IP de tu broker Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Configurar Redis
redis = Redis(host="redis", db=0, socket_timeout=5)

@app.route("/", methods=['POST','GET'])
def hello():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        app.logger.info('Received vote for %s', vote)
        
        # Enviar el voto a Kafka
        data = {'voter_id': voter_id, 'vote': vote}
        producer.send('votes', value=data)
        producer.flush()

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp

@app.route("/redis_data", methods=['GET'])
def get_redis_data():
    votes = redis.lrange('votes', 0, -1)
    return jsonify([json.loads(vote) for vote in votes])

@app.route("/kafka_data", methods=['GET'])
def get_kafka_data():
    try:
        consumer = KafkaConsumer(
            'votes',
            bootstrap_servers='3.86.34.96:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        
        kafka_data = []
        for message in consumer:
            kafka_data.append(message.value)
            # Imprimir mensaje para depuración
            app.logger.info('Received message: %s', message.value)
        consumer.close()
        return jsonify(kafka_data)
    except Exception as e:
        app.logger.error('Error while consuming Kafka messages: %s', str(e))
        return jsonify({'error': 'Failed to fetch Kafka data'}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
