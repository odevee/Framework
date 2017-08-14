class Sensor():
    def __init__(self, entities, radius = 0, resolution = 0):
        self.radius      = radius
        self.resolution  = resolution
        self.vision = entities

    def setSlice(self):
        print("setSlice executed")
