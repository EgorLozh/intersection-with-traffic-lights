from abc import ABC
from dataclasses import dataclass, field
from queue import Queue
import threading


from entities.base_trafic_light import TraficLight
from entities.walker import Walker
from enums import WalkerTraficLightPosition, WalkerTraficLightsColor
from events import ColorChangeEvent, TraficLightStartedEvent, WalkerCountOverflowEvent, WalkerPassedEvent
from mediator import Mediator



@dataclass
class WalkerTraficLight(TraficLight):
    position: WalkerTraficLightPosition
    max_walkers_count: int
    cur_color: WalkerTraficLightsColor = WalkerTraficLightsColor.RED
    walker_queue: Queue = field(default_factory=Queue)

    def __post_init__(self):
        self.locker = threading.Lock()
        self.q_size = self.walker_queue.qsize()

    def add_walker(self, walker):
        with self.locker:
            self.walker_queue.put(walker)
            self.q_size += 1
    
    def walker_go(self):
        with self.locker:
            if not self.walker_queue.empty():
                walker: Walker = self.walker_queue.get()
                walker.go()
                self.q_size -= 1
                self.mediator.handle(WalkerPassedEvent(trafic_light=self, walker=walker))
            
    def change_color(self, color: WalkerTraficLightsColor):
        if self.cur_color == color:
            return
        with self.locker:
            self.cur_color = color
        self.mediator.handle(ColorChangeEvent(trafic_light=self))

    def start(self):
        self.mediator.handle(TraficLightStartedEvent(trafic_light=self))
        while not self._stop:
            if self.cur_color == WalkerTraficLightsColor.RED:
                if (not self.walker_queue.empty()) and self.q_size > self.max_walkers_count:
                    self.mediator.handle(WalkerCountOverflowEvent(trafic_light=self))
            
            if self.cur_color == WalkerTraficLightsColor.GREEN:
                self.walker_go()

