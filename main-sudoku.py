#main-sudoku.py

import pygame 
import sys

pygame.init()
pygame.display.set_mode((400,400))
pygame.display.set_caption("chromino")


game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()