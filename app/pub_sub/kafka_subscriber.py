import json
from typing import Iterator

from kafka import KafkaConsumer

from app.interfaces.pub_sub.subsriber_interface import SubscriberInterface
from app.utilities.singleton import singleton


@singleton
class KafkaSubscriber(SubscriberInterface):
    def __init__(self, topic: str):
        self._topic = topic
        self._subscriber = KafkaConsumer(
            self._topic,
            bootstrap_servers=['kafka'],
            auto_offset_reset='smallest',
            key_deserializer=lambda k: k.decode('utf-8'),
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

    def subscribe(self) -> Iterator:
        for message in self._subscriber:
            yield message
