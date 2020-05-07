from abc import abstractmethod, ABC
from datetime import datetime
from typing import Dict, Optional

from app.constants import EventType
from app.interfaces.models.cache_interface import CacheInterface
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.interfaces.models.event_interface import EventInterface


class CacheFactoryInterface(ABC):
    @abstractmethod
    def create_cache(self) -> CacheInterface: pass

    @abstractmethod
    def create_cache_item(
        self, key: str, value: Dict, expires_at: Optional[datetime] = None) -> CacheItemInterface: pass

    @abstractmethod
    def create_cache_event(self, type: EventType, cache_item: CacheItemInterface) -> EventInterface: pass
