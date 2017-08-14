from .poi import Poi
# Goal als Erbe von Point of Interest. x und y geben die Koordinaten an.
class Goal(Poi):
    def __init__(self, x, y):
        Poi.__init__(self, x, y)