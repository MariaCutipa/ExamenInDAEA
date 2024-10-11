from kafka import KafkaConsumer
from redis import Redis
import json
import os

# Configurar Redis
redis = Redis(host='redis', db=0)

# Configurar Kafka Consumer
consumer = KafkaConsumer(
    'votes',
    bootstrap_servers='44.212.65.45:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    voter_id = data['voter_id']
    vote = data['vote']

    # Enviar a Redis
    redis.rpush('votes', json.dumps(data))
    print(f"Sent vote {vote} from {voter_id} to Redis")
