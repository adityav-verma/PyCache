from datetime import datetime
from typing import Dict

from app.constants import EventType
from app.interfaces.models.cache_item_interface import CacheItemInterface
from app.interfaces.models.event_interface import EventInterface
from app.utilities.helpers import get_uid


class Event(EventInterface):

    def __init__(self, type, payload):
        self._type = type
        self._payload = payload
        self._source = get_uid()
        self._created_at = datetime.utcnow()

    @property
    def source(self) -> str:
        return self._source

    @property
    def type(self) -> EventType:
        return self._type

    @property
    def payload(self) -> Dict:
        return self._payload

    @property
    def created_at(self) -> datetime:
        return self._created_at


class CacheEvent(Event):
    def __init__(self, type: EventType, cache_item: CacheItemInterface):
        payload = {
            'key': cache_item.key, 'value': cache_item.value,
            'last_accessed_at': str(cache_item.last_accessed_at)
        }
        super(CacheEvent, self).__init__(type, payload)
