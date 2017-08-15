from enum import Enum
# EnumerationType, um zwischen den unterschiedlichen Entity-Erben zu unterscheiden.
#EntityType = Enum('EntityType', 'Agent Food Goal Obstacle')
class EntityType(Enum):
    Agent = 0
    Food = 1
    Goal = 2
    Obstacle = 3