from enum import Enum


class CarTraficLightColor(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


class WalkerTraficLightsColor(Enum):
    RED = 'red'
    GREEN = 'green'


class CarTraficLightPosition(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    TOP = 'top'
    BOTTOM = 'bottom'


class WalkerTraficLightPosition(Enum):
    TRT = 'top-right top'
    TRR = 'top-right right'
    TLT = 'top-left top'
    TLL = 'top-left left'
    BRR = 'bottom-right right'
    BRB = 'bottom-right bottom'
    BLL = 'bottom-left left'
    BLB = 'bottom-left bottom'