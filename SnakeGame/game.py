import pygame
from enum import Enum
from renderer import *
from Entity import * # används för att skriva typen borde nog göra en bättre entity klass

class Color(Enum):
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
class DirectionList(Enum):
        Up = pygame.Vector2(0, -1)
        Down = pygame.Vector2(0, 1)
        Right = pygame.Vector2(1, 0)
        Left = pygame.Vector2(-1, 0)

class GameSystem():
         
    _Running = False
    Clock = pygame.time.Clock()

    def __init__(self, maxfps, screenwidth, screenheight, gametitle):
        self.Resolution = pygame.Vector2(screenwidth, screenheight)  #använder vector2 eftersom det är lättare att använda .x och .y 
        self.Title = gametitle
        self.TickRate = maxfps
        self.GameDisplay = pygame.display.set_mode((self.Resolution.x, self.Resolution.y))
        self.Renderer = Renderer(self.GameDisplay)
        pygame.display.set_caption("Snake game")
        self._Running = True
        pygame.font.init()
        self.DefaultFont = pygame.font.SysFont("bahnschrift", 25)


    def Update(self):
        pygame.display.update()
        self._WaitForTick()      
    def IsRunning(self):
        return self._Running
    def StopRunning(self):
        self._Running = False
    def _WaitForTick(self):
        self.Clock.tick(self.TickRate)

    def DisplayText(self, message : str, xposition : int, yposition : int, color : Color):
        Message = self.DefaultFont.render(message, True, color.value)
        self.GameDisplay.blit(Message, [xposition, yposition])

    def AddObjectToRenderer(self, object : Entity):
        self.Renderer.Add(object)
    def RemoveObjectFromRenderer(self, object : Entity):
        self.Renderer.Remove(object)
    def ClearScreen(self, color : Color):
        self.GameDisplay.fill(color.value)
