#main-chromino.py

import pygame 
import sys


pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("chromino")
clock = pygame.time.Clock()
white = [255, 255, 255]
blue = (0, 0, 255)
screen.fill(white)

rectangle = pygame.Rect(10, 10, 20, 20)


game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen, blue, rectangle)
    
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

    
pygame.quit()