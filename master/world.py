from .food import Food
from .agent import agent
from .entityType import EntityType
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Array mit Entities
        self.entities = [[0 for x in range (w)] for y in range(h)]
        self.entities_n = self.entities

    # Spawns entities
    def spawn(self, type):
        if type == EntityType.Food :
            print("spawn food")
        if type == EntityType.Agent :
            self.entities[4][4] = agent(4,4)
    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass
    # Konflikt loesen
    def breakTie(self):
        pass


