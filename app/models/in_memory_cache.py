from datetime import datetime
from typing import Optional, Dict

from app.interfaces.eviction_policy_interface import EvictionPolicyInterface
from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.utilities.singleton import singleton


@singleton
class InMemoryCache(CacheInterface):

    def __init__(self, max_size, eviction_policy: EvictionPolicyInterface, cache_factory: CacheFactoryInterface):
        self._eviction_policy = eviction_policy
        self._cache_factory = cache_factory
        self._items: Dict[str, CacheItemInterface] = {}
        self._max_size = max_size
        self._size = 0

    @property
    def max_size(self) -> int:
        return self._max_size

    @property
    def size(self) -> int:
        return self._size

    @property
    def items(self) -> Dict[str, CacheItemInterface]:
        return self._items

    def set(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        if key in self._items:
            cache_item = self._items[key]
            cache_item.value = value
            cache_item.expires_at = expires_at
        else:
            # Check size to evict a key
            if self.size >= self.max_size:
                cache_item = self._eviction_policy.evict(self)
                self.expire(cache_item.key)
            cache_item = self._cache_factory.create_cache_item(key, value, expires_at)
            self._items[key] = cache_item
            self._size += 1
        return cache_item

    def get(self, key: str) -> Optional[CacheItemInterface]:
        if key not in self._items:
            return None
        cache_item = self._items[key]
        if cache_item.expires_at and cache_item.expires_at < datetime.utcnow():
            self._items.pop(key)
            return None
        return cache_item

    def expire(self, key: str) -> bool:
        if key not in self._items:
            return False
        self._items.pop(key)
        self._size -= 1
        return True
