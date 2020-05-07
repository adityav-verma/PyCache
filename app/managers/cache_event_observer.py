from app.constants import CacheEventTopic
from app.models.event import Event
from app.models.event_queue import EventQueue
from app.pub_sub.kafka_publisher import KafkaPublisher
from app.utilities.singleton import singleton


@singleton
class CacheEventObserver:
    def __init__(self):
        EventQueue().subscribe(self.handle)
        self._publisher = KafkaPublisher(CacheEventTopic.NAME)

    def handle(self, event: Event):
        self._publisher.publish(event)