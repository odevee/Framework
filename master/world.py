from .food import Food
from .agent import agent
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Array mit Entities
        self.entities = [[0 for x in range (w)] for y in range(h)]
        self.entities_n = self.entities

    # Spawns entities
    def spawn(self, type):
        if type == "Food" :
            print("spawn food")
        if type == "agent" :
            self.entities[4][4] = agent(4,4)
    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass
    # Konflikt loesen
    def breakTie(self):
        pass


