from event_handlers.base import BaseEventHandler
from events import WalkerPassedEvent


class WalkerPassedHandler(BaseEventHandler):
    def __call__(self, event: WalkerPassedEvent) -> None:
        print(f"\n Walker {event.walker} passed {event.trafic_light.position} trafic light \n")
