from .entity import Entity
class Poi(Entity):
    def __init__(self, x, y, walkable = 1):
        Entity.__init__(self, x, y, walkable)


