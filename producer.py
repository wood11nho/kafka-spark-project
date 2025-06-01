from kafka import KafkaProducer
import json
import time
import random

# Inițializează producer Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# IP-uri simulate
ip_list = [f"192.168.1.{i}" for i in range(1, 6)]

print("Trimitere tranzacții către Kafka topic 'tranzactii'...")

while True:
    mesaj = {
        "timestamp": int(time.time() * 1000),
        "ip_address": random.choice(ip_list),
        "trx_amount": round(random.uniform(1, 1000), 2)
    }

    producer.send("tranzactii", mesaj)
    producer.flush()

    print("Trimis:", mesaj)
    time.sleep(3)  # 1 mesaj la 3 secunde