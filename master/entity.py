class Entity:

    # x und y geben die Koordinaten des Objekt Entity an (Typ Integer)
    # wenn walkable == 1, kann man das Feld der Entität begangen werden. Wenn 0, dann nicht
    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.walkable = 1

    def update(self):
        pass

