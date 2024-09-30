from kafka import KafkaConsumer
from redis import Redis
import json
import os
import logging

# Configurar Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configurar Redis
redis = Redis(host='redis', db=0)

# Configurar Kafka Consumer
consumer = KafkaConsumer(
    'votes',
    bootstrap_servers='44.201.78.41:9092',
    group_id='my-group2',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

logger.info("Kafka consumer iniciado y escuchando el tópico 'votes'...")

for message in consumer:
    data = message.value
    voter_id = data['voter_id']
    vote = data['vote']

    # Enviar a Redis
    redis.rpush('votes', json.dumps(data))
    print(f"Sent vote {vote} from {voter_id} to Redis")

