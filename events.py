from dataclasses import dataclass

from base_event import BaseEvent
from entities.car import Car
from entities.base_trafic_light import TraficLight
from entities.walker import Walker



@dataclass
class TimeOverEvent(BaseEvent):
    trafic_light: TraficLight


@dataclass
class CarPassedEvent(BaseEvent):
    trafic_light: TraficLight
    car: Car


@dataclass
class WalkerPassedEvent(BaseEvent):
    trafic_light: TraficLight
    walker: Walker


@dataclass
class WalkerCountOverflowEvent(BaseEvent):
    trafic_light: TraficLight


@dataclass
class CarCountOverflowEvent(BaseEvent):
    trafic_light: TraficLight


@dataclass
class ColorChangeEvent(BaseEvent):
    trafic_light: TraficLight

@dataclass
class TraficLightStartedEvent(BaseEvent):
    trafic_light: TraficLight
