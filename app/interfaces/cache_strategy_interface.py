from abc import ABC


class CacheStrategyInterface(ABC):
    def get(self, key: str) -> CacheInterface:
