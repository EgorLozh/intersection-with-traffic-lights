
from entities.car_trafic_light import CarTraficLight
from enums import CarTraficLightColor
from event_handlers.base_trafic_light_handler import BaseTraficlightEventHandler
from events import CarCountOverflowEvent


class CarCountOverflowHandler(BaseTraficlightEventHandler):
    def __call__(self, event: CarCountOverflowEvent):
        tl: CarTraficLight = event.trafic_light

        print(f"\n============\n "
              f"Car count overflow in {tl.position} trafic light "
              f"\n============\n")

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

