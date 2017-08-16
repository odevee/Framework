class Entity:

    # x und y geben die Koordinaten des Objekts Entity an (Typ Integer)
    # walkable gibt an, ob man das Feld der Entität betreten kann
    # deleteme erlaubt Entitäten sich selbst im nächsten Zeitschritt im world.update()
    # löschen zu lassen
    def __init__(self, x, y, walkable=True, deleteme=False):
            self.x = x
            self.y = y
            self.walkable = walkable
            self.deleteme = deleteme

    # update function
    # should be implemented by each child class of Entity
    def update(self):
        pass
