from .agent import Agent
from .food import Food
from .obstacle import Obstacle
from .goal import Goal
from .entityType import EntityType
from .entity import Entity
import numpy as np
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Array mit Entities
        #self.entities = [[0 for x in range (w)] for y in range(h)]
        self.entities = np.empty((self.width, self.height), dtype=Entity)
        self.entities_n = self.entities

    # Spawns entities
    def spawn(self, type, x, y):
        if type == EntityType.Agent:
            self.entities[x][y] = Agent(x, y)
        elif type == EntityType.Food:
            self.entities[x][y] = Food(x, y)
        elif type == EntityType.Goal:
            self.entities[x][y] = Goal(x, y)
        elif type == EntityType.Obstacle:
            self.entities[x][y] = Obstacle(x, y)
        else:
            print("ERROR: Entity could not be spawned, type doesn't exist")
    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass
    # Konflikt loesen
    def breakTie(self, entity1, entity2, x, y):
        entity1.x = x
        entity1.y = y
    def moveEntity(self, x, y, xn, yn):
        pass

    def update(self):
        for row in self.entities:
            for entity in row:
                if (type(entity) != type(None)):
                    entity.update()
        self.entities_n = self.entities
        for i in range(self.width):
            for j in range(self.height):
                entity = self.entities_n[i][j]
                if (type(entity) != type(None)):
                    if entity.x != i or entity.y != j:
                        targetPosition = self.entities_n[entity.x][entity.y]
                        if type(targetPosition) != type(None):
                            if targetPosition.walkable:
                                self.entities_n[entity.x][entity.y] = entity
                                self.entities_n[i][j] = None
                            else:
                                self.breakTie(entity, targetPosition, i, j)
                        else:
                            self.entities_n[entity.x][entity.y] = entity
                            self.entities_n[i][j] = None
