from datetime import datetime
from typing import Optional, Dict

from app.constants import CacheOperation
from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface


class CacheManager:
    def __init__(self, factory: CacheFactoryInterface):
        self._factory = factory
        self._cache = factory.create_cache()

    def set(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        return self._cache.set(key, value, expires_at)

    def get(self, key: str) -> Optional[Dict]:
        return self._cache.get(key)

    def expire(self, key: str) -> bool:
        return self._cache.expire(key)

    def sync(self, key: str, value: Dict, operation: CacheOperation):
        if operation == CacheOperation.SET.value:
            # TODO: Handle expire
            self._cache.set(key, value)
        elif operation == CacheOperation.EXPIRE.value:
            self._cache.expire(key)
        else:
            raise Exception(f'Invalid cache operation: {key}, {value}, {operation}')
