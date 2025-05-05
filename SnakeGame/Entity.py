import pygame
from game import *
class Entity():
    def __init__(self):
        self.Position = pygame.Vector2(0,0)
        self.Size = pygame.Vector2(0,0)    
        self.Color = None
        self.renderID = None 
    def SetSize(self, x : float,y : float):
        if x < 0 or y < 0:
            print("INVALID NUMBER!!!!!!!!!! >:(")
        else:
            self.Size = pygame.Vector2(x,y)

    def SetPosition(self, x : float,y : float):
        self.Position = pygame.Vector2(x,y)

    def SetColor(self, color):
        if isinstance(color, tuple): # kanske inte den bästa sättet där alla tuples "fungerar" men palla fixa bättre 
            self.Color = color
            return
        if isinstance(color, Color):
            self.Color = color.value
            return
        print("Invalid Color")