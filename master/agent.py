from .entity import Entity
from .actuator import Actuator
from .sensor import Sensor
# Agent erbt von Entity und uebernimmt dadurch die Korrdinatenattribute. Der Konstruktor erstellt
# Instanzen einen Actuators und eines Sensors. Die update-Funktion des Agents implementiert die Logik, die mittels Sensor
# und Actuator umgesetzt wird.
class Agent(Entity):

    def __init__(self, x, y):
        Entity.__init__(self, x, y, 0)
        self.actuator = Actuator()
        self.sensor = Sensor()

    def update(self):
        print("Agent Update")
        tup = self.actuator.act(self.x, self.y)
        self.x = tup[0]
        self.y = tup[1]


