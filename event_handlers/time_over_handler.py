from enums import CarTraficLightColor
from events import TimeOverEvent
from event_handlers.base_trafic_light_handler import BaseTraficlightEventHandler
from entities.car_trafic_light import CarTraficLight


class TimeOverHandler(BaseTraficlightEventHandler):

    def __call__(self, event: TimeOverEvent):
        tl = event.trafic_light

        print(f"\n---------- {tl.cur_color.value} time is over in trafic light {tl.position.value}----------\n")

        self._validate_position(tl)

        if tl.cur_color == CarTraficLightColor.RED:
            self._handle_red_light(tl)

        elif tl.cur_color == CarTraficLightColor.YELLOW:
            self._handle_yellow_light(tl)

        else:
            self._handle_green_light(tl)

    def _handle_red_light(self, tl: CarTraficLight):
        if tl.position in self.horizontal_tl_positions:
            self._change_to_yellow(self.horizontal_tls)
        else:
            self._change_to_yellow(self.vertical_tls)

    def _handle_yellow_light(self, tl: CarTraficLight):
        if tl.prev_color == CarTraficLightColor.RED:
            if tl.position in self.horizontal_tl_positions:
                self._change_to_red(self.horizontal_tls)
            else:
                self._change_to_red(self.vertical_tls)
        else:
            if tl.position in self.horizontal_tl_positions:
                self._change_to_green(self.horizontal_tls)
            else:
                self._change_to_green(self.vertical_tls)

    def _handle_green_light(self, tl: CarTraficLight):
        if tl.position in self.horizontal_tl_positions:
            self._change_to_yellow(self.horizontal_tls)
        else:
            self._change_to_yellow(self.vertical_tls)