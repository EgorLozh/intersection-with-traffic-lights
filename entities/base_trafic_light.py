from abc import ABC
from dataclasses import dataclass, field
from queue import Queue
import time
import uuid
import threading

from entities.base import BaseEntity
from entities.car import Car
from entities.walker import Walker
from enums import CarTraficLightColor, CarTraficLightPosition, WalkerTraficLightPosition, WalkerTraficLightsColor


@dataclass(kw_only=True)
class TraficLight(BaseEntity, ABC):
    mediator: "Mediator"
    oid: str = field(default_factory=uuid.uuid4)
    
    _stop: bool = field(default=False, init=False)

    def stop(self):
        self._stop = True

from mediator import Mediator