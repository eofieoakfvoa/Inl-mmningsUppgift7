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

    def ChangeDirection(self, direction):
        if self.IsReverseDirection(direction): return
        self._Direction = direction.value

    def IsReverseDirection(self, direction):
        return self._Direction + direction.value == pygame.Vector2(0,0) #ifall det är motsatta 
    
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

    #sätter alla förutom huvudet på samma position som den framför den 
    #jag tror ätt bättre sätt att göra samma sak är typ att ta bort den längst back sen lägga till en framför, då skulle man slippa en for loop, eftersom alla imellan ser ut som de är på samma plats
    def _BodyTrail(self, previous):
        if self.BodyPartCount == 1: return
        for i in range(self.BodyPartCount, 1, -1):
            self.BodyDictionary[i].Position = pygame.Vector2(self.BodyDictionary[i-1].Position)
        self.BodyDictionary[1].Position = pygame.Vector2(previous)

class BodyPart(Entity):
    def __init__(self, SizeX, SizeY, Color):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.SetColor(Color)

class Food(Entity): # Är ingen skillnad mellan dellan och BodyPart, skulle kunna göra så att färgen är by defualt så att de är annurlundna
    def __init__(self, SizeX, SizeY, Color):
        super().__init__()
        self.SetSize(SizeX, SizeY)
        self.SetColor(Color)
    