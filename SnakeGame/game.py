import pygame
from enum import Enum
from renderer import *

class GameSystem():
        
    Resolution = pygame.Vector2(400, 300) #använder vector2 eftersom det är lättare att använda .x och .y 
    Title = "Snake Game"
    GameDisplay = None 
    Running = False
    TickRate = 30
    Renderer = None
    Clock = pygame.time.Clock()
    def __init__(self):
        self.GameDisplay = pygame.display.set_mode((self.Resolution.x, self.Resolution.y))
        self.Renderer = Renderer(self.GameDisplay)
        pygame.display.set_caption("Snake game")
        self.Running = True

    class Color(Enum):
        White = (255, 255, 255)
        Black = (0, 0, 0)
        Red = (255, 0, 0)
    
    def IsRunning(self):
        return  self.Running
    def StopRunning(self):
        self.Running = False
    def DrawRectangle(size : pygame.Vector2, position : pygame.Vector2, color : Color):
        pass
    def AddObjectToRenderer(self, object):
        return self.Renderer.Add(object)
    def WaitForTick(self):
        self.Clock.tick(self.TickRate)
