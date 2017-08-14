from random import randint
# Actuator eines Agents (unvollständiger Konstruktor)
class Actuator:
    def __init__(self):
        pass


# act function. Randomly moves agent in one direction.
# receives x,y, the current coordinates of the agent
# returns new coordinates
    def act(self, x, y):
        r = [randint(0, 11) for p in range(0, 9)]
        # North
        if r[0] <= 2:
            x = x
            y = y + 1
        # South
        elif r[0] <= 5:
            x = x
            y = y - 1
        # East
        elif r[0] <= 8:
            x = x + 1
            y = y
        # West
        elif r[0] <= 11:
            x = x - 1
            y = y
        return (x, y)