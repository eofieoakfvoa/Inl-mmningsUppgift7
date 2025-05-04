import pygame
class GameSystem():
        
    Resolution = pygame.Vector2(400, 300) #använder vector2 eftersom det är lättare att använda .x och .y 
    Title = "Snake Game"
    GameDisplay = None 
    Running = False
    
    def __init__(self):
        self.Initialize()
    
    
    def IsRunning(self):
        return  self.Running
    def Initialize(self):
        self.GameDisplay = pygame.display.set_mode((self.Resolution.x, self.Resolution.y))
        pygame.display.set_caption("Snake game")
        self.Running = True