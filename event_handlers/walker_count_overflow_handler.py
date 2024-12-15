from event_handlers.base_trafic_light_handler import BaseTraficlightEventHandler
from events import WalkerCountOverflowEvent


class WalkerCountOverflowHandler(BaseTraficlightEventHandler):
    def __call__(self, event: WalkerCountOverflowEvent):
        tl = event.trafic_light

        print(f"\n============\nWalker count overflow in {tl.position} trafic light\n============\n")

        self._validate_position(tl)

        if tl.position in self.horizontal_tl_positions:
            self._change_to_yellow(self.horizontal_tls)
        else:
            self._change_to_yellow(self.vertical_tls)
