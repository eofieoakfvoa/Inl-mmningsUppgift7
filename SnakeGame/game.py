import pygame
class GameSystem():
        
    def __init__(self):
        GameSystem.Initialize()
    Resolution = pygame.Vector2(400, 300) #använder vector2 eftersom det är lättare att använda .x och .y 
    Title = "Snake Game"
    GameDisplay = None 
    def Initialize():
        GameDisplay = pygame.display.set_mode((GameSystem.Resolution.x, GameSystem.Resolution.y))
        pygame.display.set_caption("Snake game")