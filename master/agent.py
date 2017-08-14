from entity import Entity
from actuator import Actuator
from sensor import Sensor
# agent class
class Agent(Entity):

    #constructs an agent with x,y coordinates and instantiates an Actuator and a Sensor
    def __init__(self, x, y):
        Entity.__init__(self, x, y, 0)
        self.actuator = Actuator()
        self.sensor = Sensor()
    # updates agents
    # (should later call Sensor and Actuator
    def update(self):
        tup = self.actuator.randomwalk(self.x, self.y)
        self.x = tup[0]
        self.y = tup[1]
