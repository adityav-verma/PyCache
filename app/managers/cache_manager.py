from datetime import datetime
from typing import Optional, Dict

from app.constants import CacheOperation, EventType
from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.models.event_queue import EventQueue


class CacheManager:
    def __init__(self, factory: CacheFactoryInterface):
        self._factory = factory
        self._cache = factory.create_cache()
        self._event_queue = EventQueue()

    def _publish_event(self, type: EventType, cache_item: CacheItemInterface):
        event = self._factory.create_cache_event(type, cache_item)
        self._event_queue.publish(event)

    def set(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        cache_item = self._cache.set(key, value, expires_at)
        self._publish_event(EventType.CACHE_SET, cache_item)
        return cache_item

    def get(self, key: str) -> Optional[CacheItemInterface]:
        return self._cache.get(key)

    def expire(self, key: str) -> bool:
        cache_item = self.get(key)
        response = self._cache.expire(key)
        if cache_item:
            self._publish_event(EventType.CACHE_EXPIRE, cache_item)
        return response

    def sync(self, key: str, value: Dict, operation: CacheOperation):
        if operation == CacheOperation.SET.value:
            # TODO: Handle expire
            self._cache.set(key, value)
        elif operation == CacheOperation.EXPIRE.value:
            self._cache.expire(key)
        else:
            raise Exception(f'Invalid cache operation: {key}, {value}, {operation}')
