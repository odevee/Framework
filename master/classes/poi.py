from .entity import Entity

class Poi(Entity):
    def __init__(self, x, y, walkable = 1, deleteme = False):
        Entity.__init__(self, x, y, walkable, deleteme)
