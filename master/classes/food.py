from .poi import Poi
class Food(Poi):

    # constructs Food with:
    def __init__(self,
                 x,                     # coordinates x ...
                 y,                     # ... and y
                 kind = 0,              # a kind (with a default value)
                 perishable = False,            # whether it's perishables
                 lifetime = 5,              # a lifetime (relevant if perishable)
                 existence = 0        ):   # duration of existence so far
        Poi.__init__(self, x, y)
        self.kind       = kind
        self.perishable = perishable
        self.lifetime   = lifetime
        self.existence  = existence

    # food can perish after a certain while
    def update(self):
        if not self.perishable:
            pass                    # if food never goes bad, do nothing
        elif (self.perishable and self.existence < self.lifetime):
            self.existence += 1     # if it's not bad yet, increment its existence time
        else:
            self.deleteme = True    # if it's gone bad, set it to be deleted
