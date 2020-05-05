from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional

from app.interfaces.models.cache_item_interface import CacheItemInterface


class CacheInterface(ABC):
    @abstractmethod
    def set(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface: pass

    @abstractmethod
    def get(self, key: str) -> Optional[Dict]: pass

    @abstractmethod
    def expire(self, key: str) -> bool: pass
