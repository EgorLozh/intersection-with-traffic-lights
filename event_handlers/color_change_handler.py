from entities.base_trafic_light import TraficLight
from enums import CarTraficLightColor, WalkerTraficLightsColor
from event_handlers.base_trafic_light_handler import BaseTraficlightEventHandler
from events import ColorChangeEvent


class ColorChangeHandler(BaseTraficlightEventHandler):
    def __call__(self, event: ColorChangeEvent):

        tl = event.trafic_light

        print(f"\n{tl.cur_color.value} color change in trafic light {tl.position.value}\n")

        if tl.cur_color == CarTraficLightColor.RED or tl.cur_color == WalkerTraficLightsColor.RED:
            self._red_handle(tl)

        elif tl.cur_color == CarTraficLightColor.YELLOW:
            self._handle_yellow_light(tl)

        elif tl.cur_color == CarTraficLightColor.GREEN or tl.cur_color == WalkerTraficLightsColor.GREEN:
            self._handle_green_light(tl)

    def _red_handle(self, tl: TraficLight) -> None:
        if tl.position in self.horizontal_tl_positions:
            self._change_to_yellow(self.vertical_tls)
        else:
            self._change_to_yellow(self.horizontal_tls)

    def _handle_yellow_light(self, tl: TraficLight) -> None:
        self._change_to_yellow(self.trafic_lights)

    def _handle_green_light(self, tl: TraficLight) -> None:
        if tl.position in self.horizontal_tl_positions:
            self._change_to_yellow(self.vertical_tls)
        else:
            self._change_to_yellow(self.horizontal_tls)
