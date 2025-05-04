import pygame
from game import *
pygame.init()
Game = GameSystem()
pygame.display.update()
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()