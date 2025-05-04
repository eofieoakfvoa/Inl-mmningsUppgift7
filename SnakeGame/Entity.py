import pygame
class Entity():
    def __init__(self):
        self.Position = pygame.Vector2(0,0)
        self.Size = pygame.Vector2(0,0)    
        self.Color = None
    def SetSize(self, x,y):
        if x < 0 or y < 0:
            print("INVALID NUMBER!!!!!!!!!! >:(")
        else:
            self.Size = pygame.Vector2(x,y)
    def SetColor(self, color):
        self.Color = color