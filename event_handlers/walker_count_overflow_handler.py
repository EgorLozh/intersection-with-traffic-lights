from entities.walker_trafic_light import WalkerTraficLight
from enums import WalkerTraficLightsColor
from event_handlers.base_trafic_light_handler import BaseTraficlightEventHandler
from events import WalkerCountOverflowEvent


class WalkerCountOverflowHandler(BaseTraficlightEventHandler):
    def __call__(self, event: WalkerCountOverflowEvent):
        tl: WalkerTraficLight = event.trafic_light

        print(f"\n============\nWalker count overflow in {tl.position} trafic light\n============\n")

        self._validate_position(tl)

        self._change_to_yellow(self.trafic_lights)
