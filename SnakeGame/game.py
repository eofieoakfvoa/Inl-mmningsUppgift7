import pygame
from enum import Enum
class GameSystem():
        
    Resolution = pygame.Vector2(400, 300) #använder vector2 eftersom det är lättare att använda .x och .y 
    Title = "Snake Game"
    GameDisplay = None 
    Running = False
    TickRate = 30
    def __init__(self):
        self.GameDisplay = pygame.display.set_mode((self.Resolution.x, self.Resolution.y))
        pygame.display.set_caption("Snake game")
        self.Running = True
        self.GameLoop()
    
    def IsRunning(self):
        return  self.Running

    class Color(Enum):
        White = (255, 255, 255)
        Black = (0, 0, 0)
        Red = (255, 0, 0)
    def DrawRectangle(size : pygame.Vector2, position : pygame.Vector2, color : Color):
        pass

    def GameLoop(self):
        while self.IsRunning():
            self.EventHandler()
            self.Renderer()
            pygame.display.update()            
        pygame.quit()
        quit()
    def EventHandler(self):
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.Running = False #fixa senare
    def Renderer(self):
        
        pygame.draw.rect(self.GameDisplay, self.Color.Red.value, [200,150,10,10])