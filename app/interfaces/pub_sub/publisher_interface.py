from abc import ABC, abstractmethod

from app.interfaces.models.event_interface import EventInterface


class PublisherInterface(ABC):
    @abstractmethod
    def publish(self, event: EventInterface): pass
