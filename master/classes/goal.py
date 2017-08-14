from .poi import Poi
# Goal as child class of Poi
class Goal(Poi):
    # construct a Goal instance. x,y are the coords
    def __init__(self, x, y):
        Poi.__init__(self, x, y, walkable = 1, deleteme = False)
