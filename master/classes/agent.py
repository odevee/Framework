from .entity import Entity
from .actuator import Actuator
from .sensor import Sensor
# agent class
class Agent(Entity):

    #constructs an agent with x,y coordinates and instantiates an Actuator and a Sensor
    def __init__(self, x, y):
        Entity.__init__(self, x, y, 0)
        self.actuator = Actuator()
        self.sensor = Sensor()

    # updates agents
    # future functionality:
    #       * call sensor and get back sensor data
    #       * pass sensor data to actuator
    #       * get back actuator decision on what to do
    #       * update its own state (= desired state) to reflect the decision
    # note: the actual world state is ONLY changed in world.update() inside the
    #       world loop in main.py, NOT by the agent itself
    def update(self):
        tup = self.actuator.randomwalk(self.x, self.y)
        self.x = tup[0]
        self.y = tup[1]
