class Entity:

    # x und y geben die Koordinaten des Objekt Entity an (Typ Integer)
    # wenn walkable == 1, kann man das Feld der Entität betreten. Wenn 0, dann nicht.
    # deleteme erlaubt Entitäten sich selbst im nächsten Zeitschritt im world.update()
    # löschen zu lassen
    def __init__(self, x, y, walkable = 1, deleteme = False):
            self.x = x
            self.y = y
            self.walkable = walkable
            self.deleteme = deleteme

    # update function
    # should be implemented by each child class of Entity
    def update(self):
        pass
