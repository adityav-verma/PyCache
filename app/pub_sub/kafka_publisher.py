import json
from kafka import KafkaProducer

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
        self._publisher.send(self._topic, key=event.type.value, value=event.payload)
