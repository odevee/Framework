from .entity import Entity

class Poi(Entity):
    def __init__(self, x, y, walkable = True, deleteme = False):
        Entity.__init__(self, x, y, walkable, deleteme)
