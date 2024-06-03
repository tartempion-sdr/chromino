#main-chromino.py
#pip install --upgrade pygame
import pygame 
from pygame.locals import *
import sys
import grille

pygame.init()


#type surface
screen = pygame.display.set_mode((800,800))
modifier_screen = pygame.display
pygame.display.set_caption("chromino")
clock = pygame.time.Clock()
white = [255, 255, 255]
blue = (0, 0, 255)

casex = 0
casey = 0
cote = 19
rectangle = pygame.Rect(casex, casey, cote, cote)
screen.fill(white)

game_on = True

        

while game_on:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEWHEEL:
            
            rectangle = pygame.Rect(casex, casey, cote, cote)
            if event.y == -1 :
                cote -= 1 
                zoom_moins = grille.Grille(screen, blue, rectangle, cote)
                zoom_moins.zoom_moins(screen, blue, rectangle, cote)
                 
            if event.y == 1 :
                cote += 1 
                zoom_plus = grille.Grille(screen, blue, rectangle, cote)
                zoom_plus.zoom_plus(screen, blue, rectangle, cote)
            
            
            
            print("event", event.y)
            screen.fill(white)
            pygame.display.flip()
    
    
    case1 = grille.Grille(screen, blue, rectangle, cote)
    case1.toute_les_cases(screen, blue, rectangle, cote)
    
    
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

    
pygame.quit()