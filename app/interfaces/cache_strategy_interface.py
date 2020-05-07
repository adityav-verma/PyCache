from abc import ABC

from app.interfaces.models.cache_interface import CacheInterface


class CacheStrategyInterface(ABC):
    def get(self, key: str) -> CacheInterface: pass
