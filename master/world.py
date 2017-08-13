from .food import Food
from .agent import agent
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Array mit Entities
        entities = [[0 for x in range (w)] for y in range(h)]
        entities_n = entities
    # Spawns entities
    def spawn(self, type):
        if type == "Food" :
            print("spawn food")
        if type == "agent" :
            print("spawn agent")
    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass
    # Konflikt loesen
    def breakTie(self):
        pass

