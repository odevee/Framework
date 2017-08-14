class Entity:

    # x und y geben die Koordinaten des Objekt Entity an (Typ Integer)
    # wenn walkable == 1, kann man das Feld der Entität begangen werden. Wenn 0, dann nicht
    def __init__(self, x, y, walkable = 1):
            self.x = x
            self.y = y
            self.walkable = walkable
    # update function
    # should be implemented by each child class of Entity
    def update(self):
        pass