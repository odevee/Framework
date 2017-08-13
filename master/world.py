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
    def spawn(self, type, x, y):
        if type == EntityType.Agent:
            self.entities[x][y] = agent(x,y)
        elif type == EntityType.Food:
            print("spawn food")
        elif type == EntityType.Goal:
            print("spawn goal")
        elif type == EntityType.Obstacle:
            print("spawn obstacle")
        else:
            print("ERROR: Entity could not be spawned, type doesn't exist")
    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass
    # Konflikt loesen
    def breakTie(self):
        pass