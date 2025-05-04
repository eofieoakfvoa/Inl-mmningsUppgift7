from Entity import * 
from enum import Enum
class Player(Entity):
    def __init__(self, SizeX, SizeY, Color, Speed):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.Speed = Speed
        self.SetColor(Color)
    Direction = pygame.Vector2(0,0)
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

class Food(Entity):
    def __init__(self, SizeX, SizeY, Color):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.SetColor(Color)
    