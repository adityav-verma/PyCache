from abc import ABC, abstractmethod

from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface


class EvictionPolicyInterface(ABC):
    @abstractmethod
    def evict(self, cache: CacheInterface) -> CacheItemInterface: pass
