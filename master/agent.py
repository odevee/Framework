from .entity import Entity
from .actuator import Actuator
from .sensor import Sensor

class Agent:
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.actuator = Actuator()
        self.sensor = Sensor()