# import modules
import numpy as np
# import classes and types
from .entityType import EntityType
from .agent      import Agent
from .entity     import Entity
from .food       import Food
from .goal       import Goal
from .obstacle   import Obstacle

# define the class "World": represents the world grid with all entities
class World:
    # constructor
    def __init__(self, width, height):
        (self.width, self.height) = width, height                   # define width and height
        self.entities = np.empty((width, height), dtype=Entity)     # array of all entities in the world ...
        self.entities_n = self.entities                             # ... and a copy of the array
        # note: entities_n is used as a way to specify entitiy-modification intent
        #       during world updates, to do conflict management

    # spawns entities by creating and putting them into the entities-array;
    # can be passed any kwd-argument of any type of entity
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

    # get subarray of world (to be used by sensors)
    def getSlice(self, x, y, radius):
        pass

    # resolves conflict, given two entities that want to occupy the same spot
    # (two agents, and agent and an obstacle etc.)
    def breakTie(self, entity1, entity2, x, y):
        # entity 2 always wins
        entity1.x = x
        entity1.y = y

    # moves entities through the world
    def moveEntity(self, entity, x, y, xn, yn):
        self.entities_n[xn][yn] = entity        # copy entity to new position
        self.entities_n[x][y] = None            # delete entity at old position

    # deletes entities from world
    def delEntity(self, entity, x, y):
        self.entities_n[x][y] = None

    # updates all entities and the world grid
    def update(self):

        # call update method of all entities in the world
        for row in self.entities:
            for entity in row:
                if (type(entity) != type(None)):
                    entity.update()
        self.entities_n = self.entities # copy the world grid

        # modify all entities in the grid copy
        for x in range(self.width):
            for y in range(self.height):
                # entity currently considered for modification
                entity = self.entities_n[x][y]

                # delete entities that want to be deleted
                if type(entity) != type(None) and entity.deleteme:
                    self.delEntity(entity, x, y)

                # movement of entities
                # if current coordinates differ from wanted ones (entity.x, entity.y)
                elif (type(entity) != type(None) and (x,y) != (entity.x, entity.y)):
                    # get entity at target position
                    entityAtTarget = self.entities_n[entity.x][entity.y]
                    # if desired position walkable, move the entity there
                    if type(entityAtTarget) == type(None) or entityAtTarget.walkable:
                        self.moveEntity(entity, x, y, entity.x, entity.y)
                    # otherwise resolve the conflict
                    else:
                        self.breakTie(entity, entityAtTarget, x, y)
