from event_handlers.base import BaseEventHandler
from events import TraficLightStartedEvent


class TraficLightStartedHandler(BaseEventHandler):
    def __call__(self, event: TraficLightStartedEvent):
        print(f"\n{event.trafic_light.position.value} trafic light started with {event.trafic_light.cur_color.value} color\n")