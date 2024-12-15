from typing import Dict, List, Type
from event_handlers.base import BaseEventHandler
from events import BaseEvent


class Mediator:
    event_handlers: Dict[Type[BaseEvent], List[BaseEventHandler]] = {}

    def register(self, event_type, handler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def handle(self, event: BaseEvent):
        if event.__class__ in self.event_handlers:
            for handler in self.event_handlers[event.__class__]:
                handler(event)
        else:
            raise ValueError(f"Event type {event.__class__} is not registered")
        