from typing import Dict

import requests

from app.constants import EventType, CacheOperation


class ReplicationManager:
    def __init__(self):
        self._host = 'http://localhost'
        self._sync_api_path = '/cache/sync/'

    def replicate(self, key: str, value: Dict, event_type: EventType):
        payload = {'key': key, 'value': value}
        if event_type == EventType.CACHE_SET.value:
            payload['operation'] = CacheOperation.SET.value
        elif event_type == EventType.CACHE_EXPIRE.value:
            payload['operation'] = CacheOperation.EXPIRE.value
        requests.post('http://localhost/api/cache/sync/', json=payload)
