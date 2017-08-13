from .poi import Poi

class Food(self):
    def __init__(self,x,y,kind):
        Poi.__init__(self, x, y)
        self.kind = kind
