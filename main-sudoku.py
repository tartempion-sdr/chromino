#main-chromino.py
#pip install --upgrade pygame
import pygame 
from pygame.locals import *
import sys
import grille

pygame.init()


#type surface
screen = pygame.display.set_mode((400,400))
modifier_screen = pygame.display
pygame.display.set_caption("chromino")
clock = pygame.time.Clock()
white = [255, 255, 255]
blue = (0, 0, 255)
cote = 19
rectangle = pygame.Rect(200, 200, cote, cote)
screen.fill(white)

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEWHEEL:
            rectangle = pygame.Rect(200, 200, cote, cote)
            if event.y == -1 :
                cote -= 1 
                grille.Grille.plateau(screen, blue, rectangle)
                print(cote)
                print(rectangle)

                
            if event.y == 1 :
                cote += 1
                grille.Grille.plateau(screen, blue, rectangle)
                print(cote)
                print(rectangle)
                
            print(type(event.x))
            print(event.x, event.y)
            screen.fill(white)
            pygame.display.flip()
    #gr = grille.Grille.plateau(screen, blue, rectangle)
    pygame.draw.rect(screen, blue, rectangle)
    
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

    
pygame.quit()