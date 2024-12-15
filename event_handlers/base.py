from abc import ABC, abstractmethod
from events import BaseEvent


class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, event: BaseEvent):
        ...
