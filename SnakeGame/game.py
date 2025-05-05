import pygame
from enum import Enum
from renderer import *

class GameSystem():
        
    Resolution = pygame.Vector2(400, 300) #använder vector2 eftersom det är lättare att använda .x och .y 
    Title = "Snake Game"
    GameDisplay = None 
    Running = False
    TickRate = 15
    Renderer = None
    Clock = pygame.time.Clock()

    def __init__(self):
        self.GameDisplay = pygame.display.set_mode((self.Resolution.x, self.Resolution.y))
        self.Renderer = Renderer(self.GameDisplay)
        pygame.display.set_caption("Snake game")
        self.Running = True
        pygame.font.init()
        self.DefaultFont = pygame.font.SysFont("bahnschrift", 25)

    class Color(Enum):
        White = (255, 255, 255)
        Black = (0, 0, 0)
        Red = (255, 0, 0)

    def Update(self):
        pygame.display.update()
        self._WaitForTick()      

    def IsRunning(self):
        return self.Running
    def StopRunning(self):
        self.Running = False

    def DisplayText(self,message, xposition, yposition, color):
        Message = self.DefaultFont.render(message, True, color.value)
        self.GameDisplay.blit(Message, [xposition, yposition])
    def AddObjectToRenderer(self, object):
        self.Renderer.Add(object)
    def RemoveObjectFromRenderer(self, object):
        self.Renderer.Remove(object)

    def _WaitForTick(self):
        self.Clock.tick(self.TickRate)
