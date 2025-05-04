from Entity import * 
from enum import Enum
class Player(Entity):
    Direction = pygame.Vector2(0,0)
    class DirectionList(Enum):
        Up = pygame.Vector2(0, -10)
        Down = pygame.Vector2(0, 10)
        Right = pygame.Vector2(10, 0)
        Left = pygame.Vector2(-10, 0)

    def ChangeDirection(self, direction):
        self.Direction = direction.value