from dataclasses import  dataclass
import time

from entities.base import BaseEntity


@dataclass
class Walker(BaseEntity):
    def go(self):
        time.sleep(1)
