from abc import abstractmethod
from datetime import datetime
from typing import Dict

from app.constants import EventType


class EventInterface(object):
    @property
    @abstractmethod
    def source(self) -> str: pass

    @property
    @abstractmethod
    def type(self) -> EventType: pass

    @property
    @abstractmethod
    def payload(self) -> Dict: pass

    @property
    @abstractmethod
    def created_at(self) -> datetime: pass
