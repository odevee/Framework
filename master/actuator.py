from random import randint
# Actuator eines Agenten. Diese Klasse enthält die spezifische Logik, nach welcher der Agent handeln soll
# und soll über den Agenten mit den Sensorinformationen aufgerufen werden. Die restliche Struktur der Klasse ist
# implementierungsspezifisch.
class Actuator:
    def __init__(self):
        pass


# Erste act-Funktion, die die x und y Koordinate enthält und ein Tupel einer um eine Einheit in eine willkuerliche
# Richtung verschobenen Koordinate returnt.
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