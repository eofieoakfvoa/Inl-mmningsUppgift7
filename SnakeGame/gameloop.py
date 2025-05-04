import pygame
from game import *
pygame.init()
Game = GameSystem()
pygame.display.update()
while Game.IsRunning():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Game.Running = False #fixa senare
pygame.quit()
quit()