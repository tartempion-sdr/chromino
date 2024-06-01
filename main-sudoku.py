#main-sudoku.py

import pygame 
import sys
import grille

pygame.init()

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
white = [255, 255, 255]
screen.fill(white)

pygame.display.set_caption("chromino")





game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            pygame.quit()
            sys.exit()
    
    
    #pygame.display.update()
    
    BLUE = (0, 0, 255)
    rectangle = pygame.Rect(100, 100, 200, 150)
    #gr = grille.Jeton
    surface = pygame.Surface((400, 400))
    #carre = gr.jetons(screen, BLUE, rectangle)
    pygame.draw.rect(screen, BLUE, rectangle)
    
    pygame.display.flip()
    
    
    clock.tick(60)  # limits FPS to 60

    
pygame.quit()