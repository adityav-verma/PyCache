from datetime import datetime
from typing import Dict, Optional

from app.interfaces.models.cache_item_interface import CacheItemInterface


class InMemoryCacheItem(CacheItemInterface):

    def __init__(self, key: str, value: Dict, expires_at: Optional[datetime] = None):
        self._key = key
        self._value = value
        self._expires_at = expires_at
        self._last_updated_at = datetime.utcnow()

    @property
    def key(self) -> str:
        return self._key

    @property
    def value(self) -> Dict:
        self._last_updated_at = datetime.utcnow()
        return self._value

    @value.setter
    def value(self, value: Dict):
        self._last_updated_at = datetime.utcnow()
        self._value = value

    @property
    def expires_at(self) -> datetime:
        return self._expires_at

    @expires_at.setter
    def expires_at(self, value: datetime):
        self._last_updated_at = datetime.utcnow()
        self._expires_at = value

    @property
    def last_updated_at(self) -> datetime:
        return self._last_updated_at

    def to_dict(self) -> Dict:
        return {
            'key': self.key,
            'value': self.value,
            'last_updated_at': str(self.last_updated_at)
        }
