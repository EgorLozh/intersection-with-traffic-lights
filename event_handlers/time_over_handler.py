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
            self._change_to_yellow([tl])

        elif tl.cur_color == CarTraficLightColor.YELLOW:
            if tl.prev_color == CarTraficLightColor.RED:
                self._change_to_green([tl])

            else:
                self._change_to_red([tl])

        else:
            self._change_to_yellow([tl])
