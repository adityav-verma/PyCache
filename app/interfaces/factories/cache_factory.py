from abc import abstractmethod, ABC
from datetime import datetime
from typing import Dict, Optional

from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface


class CacheFactoryInterface(ABC):
    @abstractmethod
    def create_cache(self) -> CacheInterface: pass

    @abstractmethod
    def create_cache_item(self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface: pass

