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
        x = [randint(0, 11) for p in range(0, 9)]
        #North
        if x[0] <= 2:
            self.x = self.x
            self.y = self.y +1
        #South
        elif x[0] <= 5:
            self.x = self.x
            self.y = self.y - 1
        #East
        elif x[0] <= 8:
            self.x = self.x + 1
            self.y = self.y
        #West
        elif x[0] <= 11:
            self.x = self.x - 1
            self.y = self.y


