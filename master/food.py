from .poi import Poi
# Food mit Koordinatien x,y aus Integer und kind, das per default 0 ist.
class Food(Poi):
    def __init__(self, x, y, kind = 0):
        Poi.__init__(self, x, y)
        self.kind = kind