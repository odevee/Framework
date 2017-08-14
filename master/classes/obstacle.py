from .poi import Poi

class Obstacle(Poi):
    def __init__(self,x,y):
        Poi.__init__(self, x, y, walkable = 0, deleteme = False)
