from Entity import * 
from enum import Enum
class Player(Entity):
    def __init__(self, SizeX, SizeY, Color, Speed):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.Speed = Speed
        self.SetColor(Color)
        self.BodyDictionary = {1 : self}
        self.BodyPartCount = 1
        self._Direction = pygame.Vector2(0,0)

    class DirectionList(Enum):
        Up = pygame.Vector2(0, -1)
        Down = pygame.Vector2(0, 1)
        Right = pygame.Vector2(1, 0)
        Left = pygame.Vector2(-1, 0)

    def ChangeDirection(self, direction):
        if self.IsReverseDirection(direction): return
        self._Direction = direction.value

    def IsReverseDirection(self, direction):
        return self._Direction + direction.value == pygame.Vector2(0,0)
    
    def MovePlayer(self):

        self._BodyTrail(self.Position)
        x = self.Position.x + (self._Direction.x * self.Speed)
        y = self.Position.y + (self._Direction.y * self.Speed)
        self.SetPosition(x,y)

    def AddBodyPart(self):
        newBodyPart = BodyPart(15,15, self.Color)
        newBodyPart.SetPosition(self.BodyDictionary[self.BodyPartCount].Position.x, self.BodyDictionary[self.BodyPartCount].Position.y)
        self.BodyPartCount = self.BodyPartCount + 1
        self.BodyDictionary[self.BodyPartCount] = newBodyPart

    def _BodyTrail(self, previous):
        if self.BodyPartCount == 0: return
        for i in range(self.BodyPartCount, 1, -1):
            self.BodyDictionary[i].Position = pygame.Vector2(self.BodyDictionary[i-1].Position)
        self.BodyDictionary[1].Position = pygame.Vector2(previous)

class BodyPart(Entity):
    def __init__(self, SizeX, SizeY, Color):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.SetColor(Color)

class Food(Entity):
    def __init__(self, SizeX, SizeY, Color):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.SetColor(Color)
    