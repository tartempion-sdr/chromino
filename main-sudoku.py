#main-sudoku.py

import pygame 
import sys

pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
pygame.display.set_caption("chromino")






game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
    screen.fill((128,0,128))
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()