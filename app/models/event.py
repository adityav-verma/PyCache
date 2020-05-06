from typing import Dict, Optional

from app.constants import EventType
from app.interfaces.models.event_interface import EventInterface


class Event(EventInterface):
    def __init__(self, type, payload):
        self._type = type
        self._payload = payload

    @property
    def type(self) -> EventType:
        return self._type

    @property
    def payload(self) -> Dict:
        return self._payload


class CacheEvent(Event):
    def __init__(self, type: EventType, key: str, value: Optional[Dict]):
        payload = {'key': key, 'value': value}
        super(CacheEvent, self).__init__(type, payload)
