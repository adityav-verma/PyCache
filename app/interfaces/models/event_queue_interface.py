from abc import abstractmethod, ABC
from typing import Callable

from app.interfaces.models.event_interface import EventInterface


class EventQueueInterface(ABC):
    @abstractmethod
    def subscribe(self, handler: Callable): pass

    @abstractmethod
    def publish(self, event: EventInterface): pass
