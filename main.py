import random
import threading
import time

from entities.car import Car
from entities.walker import Walker
from enums import CarTraficLightColor, CarTraficLightPosition, WalkerTraficLightPosition
from events import CarPassedEvent, TraficLightStartedEvent, WalkerPassedEvent, TimeOverEvent, ColorChangeEvent, CarCountOverflowEvent, WalkerCountOverflowEvent
from mediator import Mediator
from entities.car_trafic_light import CarTraficLight
from entities.walker_trafic_light import WalkerTraficLight
from event_handlers.car_passed_handler import CarPassedHandler
from event_handlers.walker_passed_handler import WalkerPassedHandler
from event_handlers.time_over_handler import TimeOverHandler
from event_handlers.color_change_handler import ColorChangeHandler
from event_handlers.car_count_overflow_handler import CarCountOverflowHandler
from event_handlers.walker_count_overflow_handler import WalkerCountOverflowHandler
from event_handlers.trafic_light_started import TraficLightStartedHandler

mediator = Mediator()
RED_TIME = 5
YELLOW_TIME = 2
GREEN_TIME = 5
MAX_CARS_COUNT = 10
MAX_WALKERS_COUNT = 10


car_trafic_lights = []
for position in CarTraficLightPosition:
    if position == CarTraficLightPosition.RIGHT or position == CarTraficLightPosition.LEFT:
        car_trafic_light = CarTraficLight(position=position, 
                       max_cars_count=MAX_CARS_COUNT,
                       green_time=GREEN_TIME,
                       red_time=RED_TIME,
                       yellow_time=YELLOW_TIME,
                       cur_color=CarTraficLightColor.GREEN,
                       mediator=mediator)
    else:
        car_trafic_light = CarTraficLight(position=position, 
                        max_cars_count=MAX_CARS_COUNT,
                        green_time=GREEN_TIME,
                        red_time=RED_TIME,
                        yellow_time=YELLOW_TIME,
                        mediator=mediator)
        
    car_trafic_lights.append(car_trafic_light)


walker_trafic_lights = []
for position in WalkerTraficLightPosition:
    walker_trafic_lights.append(
        WalkerTraficLight(position=position, 
                         max_walkers_count=MAX_WALKERS_COUNT,
                         mediator=mediator)
    )

trafic_lights = car_trafic_lights + walker_trafic_lights

mediator.register(CarPassedEvent, CarPassedHandler())
mediator.register(WalkerPassedEvent, WalkerPassedHandler())
mediator.register(TimeOverEvent, TimeOverHandler(trafic_lights=trafic_lights))
mediator.register(ColorChangeEvent, ColorChangeHandler(trafic_lights=trafic_lights))
mediator.register(CarCountOverflowEvent, CarCountOverflowHandler(trafic_lights=car_trafic_lights))
mediator.register(WalkerCountOverflowEvent, WalkerCountOverflowHandler(trafic_lights=walker_trafic_lights))
mediator.register(TraficLightStartedEvent, TraficLightStartedHandler())


def random_car_arrived(trafic_light: CarTraficLight):
    if random.randint(0, 1) == 1:
        trafic_light.add_car(Car())

def random_walker_arrived(trafic_light: WalkerTraficLight):
    if random.randint(0, 1) == 1:
        trafic_light.add_walker(Walker())


start_time = time.time()
for trafic_light in trafic_lights:
    thread = threading.Thread(target=trafic_light.start)
    thread.start()

while True:
    for trafic_light in trafic_lights:
        if isinstance(trafic_light, CarTraficLight):
            random_car_arrived(trafic_light)
        else:
            random_walker_arrived(trafic_light)

    time.sleep(1)

    if time.time() - start_time > 20:
        for trafic_light in trafic_lights:
            trafic_light.stop()

            

