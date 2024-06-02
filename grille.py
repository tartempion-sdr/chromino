#grille.py
import pygame


blue = (0, 0, 255)
rectangle = pygame.Rect(200, 200, 19, 19)

class Grille:
    
    def __init__():
        pass
    
    def plateau(screen:pygame.Surface, color:tuple, rectangle:tuple):
        
        pygame.draw.rect(screen, blue, rectangle)