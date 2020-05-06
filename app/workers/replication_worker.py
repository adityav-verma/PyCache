from app.constants import CacheEventTopic
from app.factories.in_memory_cache_factory import InMemoryCacheFactory
from app.managers.cache_manager import CacheManager
from app.pub_sub.kafka_subscriber import KafkaSubscriber


class ReplicationWorker:
    def __init__(self):
        self._subscriber = KafkaSubscriber(CacheEventTopic.NAME)

    def process(self):
        print('Start consuming messages')
        for message in self._subscriber.subscribe():
            # TODO: move logic to manager
            try:
                CacheManager(InMemoryCacheFactory()).replicate(
                    message.value['key'],
                    message.value['value'],
                    message.key
                )
            except Exception as e:
                print(e)
