from app.models.event import Event
from app.models.event_queue import EventQueue
from app.utilities.singleton import singleton


@singleton
class CacheEventObserver:
    def __init__(self):
        EventQueue().subscribe(self.handle)

    def handle(self, event: Event):
        # Push event to broker for syncing across
        print('inside observer')
        print(event.__dict__)
