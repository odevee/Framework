import random
import numpy as np

from classes.entity import Entity

# Aktuator eines Agenten. Diese Klasse enthält die spezifische Logik, nach welcher der Agent handeln soll
# und soll über den Agenten mit den Sensorinformationen aufgerufen werden. Die restliche Struktur der Klasse ist
# implementierungsspezifisch.
class Actuator:
    def __init__(self, think_range, range = 1):
        self.range = range
        self.think_range = think_range
        #self. slice =  np.empty(dtype=Entity)


# implementation of random walk: pick where to go (one step increment) or whether
# to stay at random, and return intended future coordinates as tuple
# THIS FUNCTION IS CALLED FROM agent.update()
    def randomwalk(self, x, y):
        r = random.choice(["up", "down", "left", "right", "stay"]) # pick where to go
        if r == "up":           # go up ...
            y += 1
        elif r == "down":       # or go down...
            y -= 1
        elif r == "right":      # or go right ...
            x += 1
        elif r == "left":       # or go left
            x -= 1
        elif r == "stay":       # or stay where you are
            pass
        return (x, y)

# returns True if a set of coordinates lies outside the map
    def outOfWorld(x,y):
        #if x < 0 or x > MAP_WIDTH or y < 0 or y > MAP_HEIGHT:
            return True


# returns all coordinates THEORETICALLY accessible from a given point
    def accessibleCoord(steps, x, y):
         poss_coord=[]
         while steps >= 0:
             for i in range(steps+1):
                 poss_coord.extend( [ (x+i , y+(steps-i)),
                                      (x-i , y-(steps-i)),
                                      (x+i , y-(steps-i)),
                                      (x-i , y+(steps-i))
                                     ] )
             steps -= 1
         return list(set(poss_coord))


# returns all the neighbours, that are reachable within range steps form the current position
    def getNeighbours(self, slice, xa, ya, x, y, range, neighbours):
        n = len(slice)
        m = len(slice[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return
        if range == -1:
            return
        if type(slice[x][y]) == type(None) or slice[x][y].walkable == True or (x, y) == (xa, ya):
            #print(slice[x][y], self)
            neighbours.add((x, y))
            self.getNeighbours(slice, xa, ya, x + 1, y, range - 1, neighbours)
            self.getNeighbours(slice, xa, ya, x - 1, y, range - 1, neighbours)
            self.getNeighbours(slice, xa, ya, x, y + 1, range - 1, neighbours)
            self.getNeighbours(slice, xa, ya, x, y - 1, range - 1, neighbours)

        return neighbours


    def getDirectNeighbours(self, slice, xa, ya, x, y, range, neighbours):
        n = len(slice)
        m = len(slice[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return
        neighbours.add((x, y))
        self.getNeighbours(slice, xa, ya, x + 1, y, range - 1, neighbours)
        self.getNeighbours(slice, xa, ya, x - 1, y, range - 1, neighbours)
        self.getNeighbours(slice, xa, ya, x, y + 1, range - 1, neighbours)
        self.getNeighbours(slice, xa, ya, x, y - 1, range - 1, neighbours)
        return neighbours


# decides where to go based on empowerment
    def getAction(self, slice, x, y):
        n = len(slice)
        m = len(slice)
        # array of all entities in the world ...
        self.slice = np.empty((n, m), dtype=Entity)
        # find direct neighbours
        direct_neighbours = {(x,y)}
        self.getDirectNeighbours(slice, x, y, x, y, self.range, direct_neighbours)
        print('Position:', x, y)
        print('Neighbours: ', direct_neighbours)
        # calculate empowerment
        target = (x, y)
        emp_max = -1
        for n in direct_neighbours:
            emp = self.calcEMP(slice, x, y, n[0], n[1])
            print('Empowerment at ', n[0], n[1], emp)
            if emp > emp_max:
                emp_max = emp
                target = (n[0], n[1])
            elif emp == emp_max:
                pass # find solution later
        #print(target)
        return target


# calculates the empowerment of given position in the world slice
    def calcEMP(self, slice, xa, ya, x, y):
        neighbours = {(x,y)}
        self.getNeighbours(slice, xa, ya, x, y, self.think_range, neighbours)
        print('far neighbours: ', neighbours)
        return len(neighbours)
