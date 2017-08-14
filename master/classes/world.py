import numpy as np

from .entityType import EntityType
from .agent import Agent
from .entity import Entity
from .food import Food
from .goal import Goal
from .obstacle import Obstacle


# represents the world grid with all entities
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        # world array which contains the entities and its copy
        self.entities = np.empty((self.width, self.height), dtype=Entity)
        self.entities_n = self.entities

    # spawns entities
    def spawn(self, entityType, x, y, kind = 0, perishable = False, lifetime = 5, existence = 0):
        if entityType == EntityType.Agent:
            self.entities[x][y] = Agent(x, y)
        elif entityType == EntityType.Food:
            self.entities[x][y] = Food(x, y, kind, perishable, lifetime, existence)
        elif entityType == EntityType.Goal:
            self.entities[x][y] = Goal(x, y)
        elif entityType == EntityType.Obstacle:
            self.entities[x][y] = Obstacle(x, y)
        else:
            print("ERROR: Entity could not be spawned, type doesn't exist")

    # get SubArray for vision
    def getSlice(self, x, y, radius):
        pass

    # if two entities want to move to the same position or if an agent wants to walk into a wall,
    # this function is called and can break the tie
    def breakTie(self, entity1, entity2, x, y):
        #entity 2 always wins
        entity1.x = x
        entity1.y = y

    # moves entities through the world
    def moveEntity(self, entity, x, y, xn, yn):
        # copy entity to new position
        self.entities_n[xn][yn] = entity
        # delete entity at old position
        self.entities_n[x][y] = None

    # deletes entities from world
    def delEntity(self, entity, x, y):
        self.entities_n[x][y] = None

    # updates all entities and the world grid
    def update(self):
        # call the update method of all entities in the world
        for row in self.entities:
            for entity in row:
                if (type(entity) != type(None)):
                    entity.update()
        # copy the world grid
        self.entities_n = self.entities
        # modify all entities in the grid copy
        for x in range(self.width):
            for y in range(self.height):
                # entity which wants to be modified
                entity = self.entities_n[x][y]
                # delete entities that want to be deleted
                if (type(entity) != type(None) and entity.deleteme):
                    self.delEntity(entity, x, y)
                # other modifications
                if (type(entity) != type(None)):
                    # coordinates, which the entity wants to move to
                    xn = entity.x
                    yn = entity.y
                    # if wanted position differs from current position
                    if xn != x or yn != y:
                        # get entity at target position
                        entityAtTarget = self.entities_n[xn][yn]
                        # if there isn't one ...
                        if type(entityAtTarget) == type(None):
                            # move entity
                            self.moveEntity(entity, x, y, xn, yn)
                        else:
                            # if there is food/goal ...
                            if entityAtTarget.walkable:
                                # move entity
                                self.moveEntity(entity, x, y, xn, yn)
                            # if it's an agent/obstacle
                            else:
                                # use the tie breaker
                                self.breakTie(entity, entityAtTarget, x, y)
