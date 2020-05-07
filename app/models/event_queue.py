from typing import Callable, List

from app.interfaces.models.event_interface import EventInterface
from app.interfaces.models.event_queue_interface import EventQueueInterface
from app.utilities.singleton import singleton


@singleton
class EventQueue(EventQueueInterface):
    def __init__(self):
        self._handlers: List[Callable] = []

    def subscribe(self, handler: Callable):
        self._handlers.append(handler)

    def publish(self, event: EventInterface):
        for handler in self._handlers:
            handler(event)
