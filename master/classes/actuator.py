import random
import numpy as np

from classes.entity     import Entity

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
            x = x
            y = y + 1
        elif r == "down":       # or go down...
            x = x
            y = y - 1
        elif r == "right":      # or go right ...
            x = x + 1
            y = y
        elif r == "left":       # or go left
            x = x - 1
            y = y
        elif r == "stay":       # or stay where you are
            x = x
            y = y
        return (x, y)

# returns True if a set of coordinates lies outside the map
    def outofWorld(x,y):
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

    def getNeighbours(self, slice, x, y, range, neighbours):
        n = len(slice)
        m = len(slice[0])
        if x < 0 or x >=n or y < 0 or y >= m:
            return
        if range == -1:
            return
        if (type(slice[x][y]) == type(None) or slice[x][y].walkable == True):
            neighbours.add((x,y))
        #else:
         #   return
        self.getNeighbours(slice, x + 1, y, range - 1, neighbours)
        self.getNeighbours(slice, x - 1, y, range - 1, neighbours)
        self.getNeighbours(slice, x, y + 1, range - 1, neighbours)
        self.getNeighbours(slice, x, y - 1, range - 1, neighbours)

        return neighbours


    def getAction(self, slice, x, y):
        n = len(slice)
        m = len(slice)
        self.slice = np.empty((n, m), dtype=Entity)     # array of all entities in the world ...
        # find direct neighbours
        direct_neighbours = {(x,y)}
        self.getNeighbours(slice, x, y, self.range, direct_neighbours)
        # calculate empowerment
        target = (x, y)
        emp_max = -1
        for n in direct_neighbours:
            emp = self.calcEMP(slice, n[0], n[1])
            if emp > emp_max:
                emp_max = emp
                target = (n[0], n[1])
            elif emp == emp_max:
                pass # find solution later
        return target



    def calcEMP(self, slice, x, y):
        neighbours = {(x,y)}
        self.getNeighbours(slice, x, y, self.think_range, neighbours)
        return len(neighbours)





""""
# Funktion noch UNGETESTET: sollte die Anzahl Zugmöglichkeiten in n Zügen iterativ bestimmen
    def EMP_optionCounter(steps, x, y, sensorinfo):
        stepnum = steps
        accessible_coord = [(x,y)]
        checked = []
        mov_equivs = {"up"    :(x,y+1),
                      "down"  :(x,y-1),
                      "left"  :(x-1,y),
                      "right" :(x+1,y)  }
        while stepnum > 0:
            for field in accessible_coord:
                if field not in checked:
                    for name, coord in mov_equivs:
                        if not outofWorld(coord[0], coord[1])
                           and ( sensorinfo[coord[0]][coord[1]].walkable
                           or    type(sensorinfo[coord[0]][coord[1]]) == None ):
                            accessible_coord.append(coord)
                checked.append(field)
            stepnum -= 1
        return len(set(accessible_coord))

"""

