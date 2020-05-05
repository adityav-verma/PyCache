from datetime import datetime
from typing import Dict, Optional

from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.models.in_memory_cache import InMemoryCache
from app.models.in_memory_cache_item import InMemoryCacheItem


class InMemoryCacheFactory(CacheFactoryInterface):
    def create_cache(self) -> CacheInterface:
        return InMemoryCache(self)

    def create_cache_item(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        return InMemoryCacheItem(key, value, expires_at)
