from abc import abstractmethod
from typing import Dict

from app.constants import EventType


class EventInterface(object):
    @property
    @abstractmethod
    def type(self) -> EventType: pass

    @property
    @abstractmethod
    def payload(self) -> Dict: pass