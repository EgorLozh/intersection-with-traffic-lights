from abc import ABC
from dataclasses import dataclass, field
from queue import Queue
import time
import uuid
import threading

from entities.base_trafic_light import TraficLight
from entities.car import Car
from enums import CarTraficLightColor, CarTraficLightPosition
from events import CarCountOverflowEvent, CarPassedEvent, ColorChangeEvent, TimeOverEvent, TraficLightStartedEvent

@dataclass
class CarTraficLight(TraficLight):
    position: CarTraficLightPosition
    max_cars_count: int
    green_time: float
    red_time: float
    yellow_time: float
    prev_color: CarTraficLightColor = CarTraficLightColor.YELLOW
    cur_color: CarTraficLightColor = CarTraficLightColor.RED
    car_queue: Queue = field(default_factory=Queue)
    q_size: int = field(init=False)

    def __post_init__(self):
        self.locker = threading.Lock()
        self.color_time = time.time()
        self.q_size = self.car_queue.qsize()

    def add_car(self, car):
        with self.locker:
            self.car_queue.put(car)
            self.q_size += 1
    
    def car_drive(self):
        with self.locker:
            if not self.car_queue.empty():
                car: Car = self.car_queue.get()
                car.drive()
                self.q_size -= 1
                self.mediator.handle(CarPassedEvent(trafic_light=self, car=car))
    
    def change_color(self, color: CarTraficLightColor):
        if self.cur_color == color:
            return
        with self.locker:
            self.prev_color = self.cur_color
            self.cur_color = color
            self.color_time = time.time()
        self.mediator.handle(ColorChangeEvent(trafic_light=self))

    def start(self):
        self.mediator.handle(TraficLightStartedEvent(trafic_light=self))
        while not self._stop:
            if self.cur_color == CarTraficLightColor.RED:
                if time.time() - self.color_time > self.red_time:
                    self.mediator.handle(TimeOverEvent(trafic_light=self))

                if (not self.car_queue.empty()) and self.q_size > self.max_cars_count:
                    self.mediator.handle(CarCountOverflowEvent(trafic_light=self))
            
            if self.cur_color == CarTraficLightColor.YELLOW:
                if time.time() - self.color_time > self.yellow_time:
                    self.mediator.handle(TimeOverEvent(trafic_light=self))

            if self.cur_color == CarTraficLightColor.GREEN:
                self.car_drive()
                if time.time() - self.color_time > self.green_time:
                    self.mediator.handle(TimeOverEvent(trafic_light=self))
            
            time.sleep(0.1)

