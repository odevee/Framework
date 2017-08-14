import random
# Actuator eines Agenten. Diese Klasse enthält die spezifische Logik, nach welcher der Agent handeln soll
# und soll über den Agenten mit den Sensorinformationen aufgerufen werden. Die restliche Struktur der Klasse ist
# implementierungsspezifisch.
class Actuator:
    def __init__(self):
        pass


# Erste act-Funktion, die die x und y Koordinate enthält und ein Tupel einer um eine Einheit in eine willkuerliche
# Richtung verschobenen Koordinate returnt.
    def randomwalk(self, x, y):
        r = random.choice(["up", "down", "left", "right"]) # pick where to go
        # go up ...
        if r == "up":
            x = x
            y = y + 1
        # or go down...
        elif r == "down":
            x = x
            y = y - 1
        # or go right ...
        elif r == "right":
            x = x + 1
            y = y
        # or go left
        elif r == "left":
            x = x - 1
            y = y
        return (x, y)
