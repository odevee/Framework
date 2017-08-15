class Sensor():
    def __init__(self, entities, radius = float('Inf'), resolution = 0):
        self.radius      = radius
        self.resolution  = resolution
        self.vision      = entities

    def setSlice(self):
        print("setSlice executed")
    def getSlice(self):
        if self.radius == float('Inf'):
            return self.vision
