from abc import ABC
from typing import List, Tuple

from entities.base_trafic_light import TraficLight
from entities.car_trafic_light import CarTraficLight
from entities.walker_trafic_light import WalkerTraficLight
from enums import CarTraficLightColor, CarTraficLightPosition, WalkerTraficLightPosition, WalkerTraficLightsColor
from event_handlers.base import BaseEventHandler


class BaseTraficlightEventHandler(BaseEventHandler, ABC):
    trafic_lights: List[TraficLight]
    horizontal_tls: List[TraficLight]
    vertical_tls: List[TraficLight]
    horizontal_tl_positions: Tuple[CarTraficLightPosition, WalkerTraficLightPosition]
    vertical_tl_positions: Tuple[CarTraficLightPosition, WalkerTraficLightPosition]
    car_trafic_lights: List[CarTraficLight]
    walker_trafic_lights: List[WalkerTraficLight]

    def __init__(self, trafic_lights: List[TraficLight]):
        self.trafic_lights = trafic_lights

        self.horizontal_tl_positions = (
            CarTraficLightPosition.LEFT,
            CarTraficLightPosition.RIGHT,
            WalkerTraficLightPosition.TLT,
            WalkerTraficLightPosition.TRT,
            WalkerTraficLightPosition.BLB,
            WalkerTraficLightPosition.BRB
        )
        self.vertical_tl_positions = (
            CarTraficLightPosition.TOP,
            CarTraficLightPosition.BOTTOM,
            WalkerTraficLightPosition.TLL,
            WalkerTraficLightPosition.BLL,
            WalkerTraficLightPosition.TRR,
            WalkerTraficLightPosition.BRR
        )

        self.horizontal_tls = []
        self.vertical_tls = []
        self.car_trafic_lights = []
        self.walker_trafic_lights = []

        for trafic_light in self.trafic_lights:
            if trafic_light.position in self.horizontal_tl_positions:
                self.horizontal_tls.append(trafic_light)
            elif trafic_light.position in self.vertical_tl_positions:
                self.vertical_tls.append(trafic_light)
            
            if isinstance(trafic_light, CarTraficLight):
                self.car_trafic_lights.append(trafic_light)
            elif isinstance(trafic_light, WalkerTraficLight):
                self.walker_trafic_lights.append(trafic_light)


    def _validate_position(self, tl: CarTraficLight):
        if (tl.position not in self.horizontal_tl_positions 
            and tl.position not in self.vertical_tl_positions):
            raise ValueError(f"Trafic light position {tl.position} is not supported")

    def _change_to_yellow(self, trafic_lights: List[TraficLight]):
        for trafic_light in trafic_lights:
            if trafic_light in self.car_trafic_lights:
                trafic_light.change_color(CarTraficLightColor.YELLOW)
            elif trafic_light in self.walker_trafic_lights:
                trafic_light.change_color(WalkerTraficLightsColor.RED)

    def _change_to_red(self, trafic_lights: List[TraficLight]):
        for trafic_light in trafic_lights:
            if trafic_light in self.car_trafic_lights:
                trafic_light.change_color(CarTraficLightColor.RED)
            elif trafic_light in self.walker_trafic_lights:
                trafic_light.change_color(WalkerTraficLightsColor.RED)
    
    def _change_to_green(self, trafic_lights: List[TraficLight]):
        for trafic_light in trafic_lights:
            if trafic_light in self.car_trafic_lights:
                trafic_light.change_color(CarTraficLightColor.GREEN)
            elif trafic_light in self.walker_trafic_lights:
                trafic_light.change_color(WalkerTraficLightsColor.GREEN)

    