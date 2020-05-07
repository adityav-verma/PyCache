from app.constants import CacheEventTopic
from app.managers.replication_manager import ReplicationManager
from app.pub_sub.kafka_subscriber import KafkaSubscriber


class ReplicationWorker:
    def __init__(self):
        self._subscriber = KafkaSubscriber(CacheEventTopic.NAME)

    def process(self):
        print('Start consuming messages')
        for message in self._subscriber.subscribe():
            try:
                ReplicationManager().replicate(
                    message.value['key'], message.value['value'], message.key
                )
            except Exception as e:
                print(e)
