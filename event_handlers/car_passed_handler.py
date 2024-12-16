from event_handlers.base import BaseEventHandler
from events import CarPassedEvent


class CarPassedHandler(BaseEventHandler):
    def __call__(self, event: CarPassedEvent) -> None:
        print(f"\n /o\_:-)_/o\ ->  /o\_:-)_/o\  Car {event.car} passed {event.trafic_light.position} trafic light \n")
