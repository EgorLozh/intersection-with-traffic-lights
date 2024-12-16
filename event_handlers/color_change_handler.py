from entities.base_trafic_light import TraficLight
from enums import CarTraficLightColor, WalkerTraficLightsColor
from event_handlers.base_trafic_light_handler import BaseTraficlightEventHandler
from events import ColorChangeEvent


class ColorChangeHandler(BaseTraficlightEventHandler):
    def __call__(self, event: ColorChangeEvent):

        tl = event.trafic_light

        print(f"\n{tl.cur_color.value} color change in trafic light {tl.position.value}\n")

        if tl.cur_color == CarTraficLightColor.YELLOW:
            self._change_to_yellow(self.trafic_lights)

        elif tl.cur_color == CarTraficLightColor.GREEN:
            if tl in self.horizontal_tls:
                self._change_to_green(self.horizontal_tls)

            elif tl in self.vertical_tls:
                self._change_to_green(self.vertical_tls)
