from .entity import Entity
from .actuator import Actuator
from .sensor import Sensor
from .behaviour import Behaviour

class agent:
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.actuator = Actuator()
        self.sensor = Sensor()
        self.behaviour = Behaviour()