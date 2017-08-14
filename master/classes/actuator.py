import random
# Actuator eines Agenten. Diese Klasse enthält die spezifische Logik, nach welcher der Agent handeln soll
# und soll über den Agenten mit den Sensorinformationen aufgerufen werden. Die restliche Struktur der Klasse ist
# implementierungsspezifisch.
class Actuator:
    def __init__(self):
        pass

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
