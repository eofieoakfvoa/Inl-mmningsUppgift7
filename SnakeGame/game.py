import pygame
from enum import Enum
from renderer import *

#Den här delen och renderer.py är har inget med spelet och göra men mer som en engine där man ska kunna skapa spel lättare
#där allt här är general saker som kan behövas, dock eftersom det är gjort för snake spelet så är allt som finns just nu relaterat till snake
#ett sätt att utveckla detta är att ha en bättre entity klass som har metoder som allt kan behöva t.ex att kolla collision.
#hade nog föredragit pånågot sätt ifall gameloopen var här och sen att man hade klasser som var som scener som alla hade en event, draw och logic overrite metoder som den kallar
class Color(Enum):
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0,255,0)
    Blue = (0,0,255)
    Yellow = (255,255,0)

class DirectionList(Enum):
    Up = pygame.Vector2(0, -1)
    Down = pygame.Vector2(0, 1)
    Right = pygame.Vector2(1, 0)
    Left = pygame.Vector2(-1, 0)

class GameSystem():
         
    _Running = False
    Clock = pygame.time.Clock()

    def __init__(self, maxfps : int, screenwidth : int, screenheight : int, gametitle : str):
        self.Resolution = pygame.Vector2(screenwidth, screenheight)  #använder vector2 eftersom det är lättare att använda .x och .y 
        self.Title = gametitle
        self.TickRate = maxfps
        self.GameDisplay = pygame.display.set_mode((self.Resolution.x, self.Resolution.y))
        self._Renderer = Renderer(self.GameDisplay)
        pygame.display.set_caption(gametitle)
        self._Running = True
        pygame.font.init()
        self.DefaultFont = pygame.font.SysFont("bahnschrift", 25)

    #################GENERAL

    def Update(self):
        pygame.display.update()
        self._WaitForTick()      
    def IsRunning(self):
        return self._Running
    def StopRunning(self):
        self._Running = False
    def _WaitForTick(self):
        self.Clock.tick(self.TickRate)

    ###############DRAWING
    
    def DisplayText(self, message : str, xposition : int, yposition : int, color : Color):
        Message = self.DefaultFont.render(message, True, color.value) #true är för anti aliasing som gör så att det blir smoother text
        self.GameDisplay.blit(Message, [xposition, yposition]) 

    #renderer är något som inte användarn ska kunna nå därför finns dessa
    def AddObjectToRenderer(self, object):
        self._Renderer.Add(object)
    def RemoveObjectFromRenderer(self, object):
        self._Renderer.Remove(object)

    def ClearScreen(self, color : Color):
        self.GameDisplay.fill(color.value)
