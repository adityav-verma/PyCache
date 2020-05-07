from app.interfaces.eviction_policy_interface import EvictionPolicyInterface
from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface


class LRUEvictionPolicy(EvictionPolicyInterface):
    def evict(self, cache: CacheInterface) -> CacheItemInterface:
        items = [value for key, value in cache.items.items()]
        items.sort(key=lambda x: x.last_updated_at)
        return items[0]
