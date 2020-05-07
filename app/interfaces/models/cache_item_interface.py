from abc import abstractmethod, ABC
from datetime import datetime
from typing import Dict


class CacheItemInterface(ABC):

    @property
    @abstractmethod
    def key(self) -> str: pass

    @property
    @abstractmethod
    def value(self) -> Dict: pass

    @value.setter
    @abstractmethod
    def value(self, value: Dict): pass

    @property
    @abstractmethod
    def expires_at(self) -> datetime: pass

    @expires_at.setter
    @abstractmethod
    def expires_at(self, value: datetime): pass

    @property
    @abstractmethod
    def last_accessed_at(self) -> datetime: pass

    @abstractmethod
    def to_dict(self) -> Dict: pass
