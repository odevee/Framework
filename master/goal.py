from .poi import Poi

class Goal(Poi):
    def __init__(self, x, y):
        Poi.__init__(self, x, y)