from dataclasses import dataclass
import time

from entities.base import BaseEntity


@dataclass
class Car(BaseEntity):
    def drive(self):
        time.sleep(0.5)
