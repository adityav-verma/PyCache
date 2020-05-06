from datetime import datetime
from typing import Optional, Dict

from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.utilities.singleton import singleton


@singleton
class InMemoryCache(CacheInterface):
    def __init__(self, cache_factory: CacheFactoryInterface):
        self._cache_factory = cache_factory
        self._items: Dict[str, CacheItemInterface] = {}

    def set(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        if key in self._items:
            cache_item = self._items[key]
            cache_item.value = value
            cache_item.expires_at = expires_at
        else:
            cache_item = self._cache_factory.create_cache_item(key, value, expires_at)
            self._items[key] = cache_item
        return cache_item

    def get(self, key: str) -> Optional[CacheItemInterface]:
        if key not in self._items:
            return None
        cache_item = self._items[key]

        # TODO: Maybe move this to command or something

        if cache_item.expires_at and str(cache_item.expires_at) < str(datetime.utcnow()):
            self._items.pop(key)
            return None
        return cache_item

    def expire(self, key: str) -> bool:
        if key not in self._items:
            return False
        cache_item = self._items[key]
        cache_item.expires_at = datetime.utcnow()
        self._items[key] = cache_item
