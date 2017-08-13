from .food import Food
from .agent import Agent
from .entityType import EntityType
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Array mit Entities
        self.entities = [[0 for x in range (w)] for y in range(h)]
        self.entities_n = self.entities

    # Spawns entities
    def spawn(self, type, x, y):
        if type == EntityType.Food :
            print("spawn food")
        if type == EntityType.Agent :
            self.entities[x][y] = Agent(x,y)
    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass
    # Konflikt loesen
    def breakTie(self):
        pass


