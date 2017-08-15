import random
# Aktuator eines Agenten. Diese Klasse enthält die spezifische Logik, nach welcher der Agent handeln soll
# und soll über den Agenten mit den Sensorinformationen aufgerufen werden. Die restliche Struktur der Klasse ist
# implementierungsspezifisch.
class Actuator:
    def __init__(self, steps):
        self.steps = steps

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
        if x < 0 or x > MAP_WIDTH or y < 0 or y > MAP_HEIGHT:
            return True

    def accessibleCoord(x,y):
        pass

    def getAction(self, slice, x, y):
        self.calcEMP(slice, x, y)


    def calcEMP(self, slice, x, y):
        pass

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

