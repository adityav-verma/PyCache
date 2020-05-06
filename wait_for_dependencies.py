import time

from kafka import KafkaProducer


def connect_to_kafka():
    producer = KafkaProducer(bootstrap_servers=['kafka'])
    producer.close()


while True:
    try:
        print('Attempt connecting to Kafka')
        connect_to_kafka()
        break
    except Exception:
        print('Unable to connect to Kafka, sleeping for 1 sec..')
        time.sleep(1)
