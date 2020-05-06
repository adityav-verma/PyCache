from datetime import datetime
from typing import Optional, Dict

import requests

from app.constants import CacheOperation, EventType
from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.models.event_queue import EventQueue


class CacheManager:
    def __init__(self, factory: CacheFactoryInterface):
        self._factory = factory
        self._cache = factory.create_cache()

    def _publish_event(self, type: EventType, key: str, value: Optional[Dict]):
        event = self._factory.create_cache_event(type, key, value)
        EventQueue().publish(event)

    def set(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        response = self._cache.set(key, value, expires_at)
        self._publish_event(EventType.CACHE_SET, key, value)
        return response

    def get(self, key: str) -> Optional[Dict]:
        return self._cache.get(key)

    def expire(self, key: str) -> bool:
        cache_item = self.get(key)
        response = self._cache.expire(key)
        if cache_item:
            self._publish_event(EventType.CACHE_EXPIRE, key, cache_item.value)
        return response

    def sync(self, key: str, value: Dict, operation: CacheOperation):
        if operation == CacheOperation.SET.value:
            # TODO: Handle expire
            self._cache.set(key, value)
        elif operation == CacheOperation.EXPIRE.value:
            self._cache.expire(key)
        else:
            raise Exception(f'Invalid cache operation: {key}, {value}, {operation}')

    def replicate(self, key: str, value: Dict, event_type: EventType):
        payload = {'key': key, 'value': value}
        if event_type == EventType.CACHE_SET.value:
            payload['operation'] = CacheOperation.SET.value
        elif event_type == EventType.CACHE_EXPIRE.value:
            payload['operation'] = CacheOperation.EXPIRE.value
        requests.post('http://localhost/api/cache/sync/', json=payload)
