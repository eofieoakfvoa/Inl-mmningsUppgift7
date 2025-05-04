from Entity import * 
from enum import Enum
class Player(Entity):
    Direction = pygame.Vector2(0,0)
    Speed = 3
    class DirectionList(Enum):
        Up = pygame.Vector2(0, -1)
        Down = pygame.Vector2(0, 1)
        Right = pygame.Vector2(1, 0)
        Left = pygame.Vector2(-1, 0)

    def ChangeDirection(self, direction):
        self.Direction = direction.value
    def MovePlayer(self):
        x = self.Position.x + (self.Direction.x * self.Speed)
        y = self.Position.y + (self.Direction.y * self.Speed)
        self.SetPosition(x,y)