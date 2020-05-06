import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from app.interfaces.models.event_interface import EventInterface
from app.interfaces.pub_sub.publisher_interface import PublisherInterface
from app.utilities.singleton import singleton


@singleton
class KafkaPublisher(PublisherInterface):
    def __init__(self, topic: str):
        self._topic = topic
        # TODO: move to config
        self._publisher = KafkaProducer(
            bootstrap_servers=['kafka'],
            key_serializer=lambda k: k.encode('utf-8'),
            value_serializer=lambda v: (json.dumps(v)).encode('utf-8')
        )

    def publish(self, event: EventInterface):
        print(self._topic)
        print(event.type.value)
        print(event.payload)
        x = self._publisher.send(self._topic, key=event.type.value, value=event.payload)
        self._publisher.flush()

        # Block for 'synchronous' sends
        try:
            record_metadata = x.get(timeout=10)
        except KafkaError as e:
            # Decide what to do if produce request failed...
            print(e)
