from datetime import datetime
from typing import Dict, Optional

from app.constants import EventType
from app.interfaces.eviction_policy_interface import EvictionPolicyInterface
from app.interfaces.factories.cache_factory import CacheFactoryInterface
from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.interfaces.models.event_interface import EventInterface
from app.models.event import CacheEvent
from app.models.in_memory_cache import InMemoryCache
from app.models.in_memory_cache_item import InMemoryCacheItem
from app.utilities.singleton import singleton


@singleton
class InMemoryCacheFactory(CacheFactoryInterface):
    def create_cache_event(self, type: EventType, cache_item: CacheItemInterface) -> EventInterface:
        return CacheEvent(type, cache_item)

    def create_cache(self, max_size: int, eviction_policy: EvictionPolicyInterface) -> CacheInterface:
        return InMemoryCache(max_size, eviction_policy, self)

    def create_cache_item(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface:
        return InMemoryCacheItem(key, value, expires_at)
