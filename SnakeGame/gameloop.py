import pygame
from game import *
Game = GameSystem()
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption("Snake game")
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()