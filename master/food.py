from .poi import Poi

class Food(Poi):
    def __init__(self, x, y, kind = 0):
        Poi.__init__(self, x, y)
        self.kind = kind