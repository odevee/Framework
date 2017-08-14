from .agent import Agent
from .food import Food
from .obstacle import Obstacle
from .goal import Goal
from .entityType import EntityType
from .entity import Entity
import numpy as np
#represents the world grid with all entities
class World:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        #world array which contains the entities and its copy
        self.entities = np.empty((self.width, self.height), dtype = Entity)
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

    #if two entities want to move to the same position or if an agent wants to walk into a wall,
    #this function is called and can break the tie
    def breakTie(self, entity1, entity2, x, y):
        #entity 2 always wins
        entity1.x = x
        entity1.y = y

    #moves entity through the world
    def moveEntity(self, entity, x, y, xn, yn):
        #copy entity to new position
        self.entities_n[xn][yn] = entity
        #delete entity at old position
        self.entities_n[x][y] = None

    #updates all entities and the world grid
    def update(self):
        #call the update method of all entities in the world
        for row in self.entities:
            for entity in row:
                if (type(entity) != type(None)):
                    entity.update()
        #copy the world grid
        self.entities_n = self.entities
        #move all entities in the grid copy
        for x in range(self.width):
            for y in range(self.height):
                #entity which wants to move
                entity = self.entities_n[x][y]
                if (type(entity) != type(None)):
                    # coordinates, which the entity wants to move to
                    xn = entity.x
                    yn = entity.y
                    #if wanted position differs from current position
                    if xn != x or yn != y:
                        #get entity at target position
                        entityAtTarget = self.entities_n[xn][yn]
                        #if there isn't one ...
                        if type(entityAtTarget) == type(None):
                            #move entity
                            self.moveEntity(entity, x, y, xn, yn)
                        else:
                            #if there is food/goal ...
                            if entityAtTarget.walkable:
                                #move entity
                                self.moveEntity(entity, x, y, xn, yn)
                            #if it's an agent/obstacle
                            else:
                                #use the tie breaker
                                self.breakTie(entity, entityAtTarget, x, y)