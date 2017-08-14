from .entity import Entity
from .actuator import Actuator
from .sensor import Sensor
from random import randint
class Agent(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.actuator = Actuator()
        self.sensor = Sensor()

    def update(self):
        print("Agent Update")

