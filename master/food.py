from .poi import Poi
class Food(Poi):
    # constructs Food with coords x,y and kind, which is 0 by default
    def __init__(self, x, y, kind = 0):
        Poi.__init__(self, x, y)
        self.kind = kind