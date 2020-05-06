from datetime import datetime
from typing import Dict, Optional

from app.interfaces.models.cache_item_interface import CacheItemInterface


def add_audit_info(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        result._last_updated_at = datetime.utcnow()
        return result
    return wrapper


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
        return self._value

    @value.setter
    @add_audit_info
    def value(self, value: Dict):
        self._value = value

    @property
    def expires_at(self) -> datetime:
        return self._expires_at

    @expires_at.setter
    @add_audit_info
    def expires_at(self, value: datetime):
        self._expires_at = value

    @property
    def last_updated_at(self) -> datetime:
        return self._last_updated_at
