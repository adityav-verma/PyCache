from abc import ABC, abstractmethod
from typing import Iterator


class SubscriberInterface(ABC):
    @abstractmethod
    def subscribe(self) -> Iterator: pass
