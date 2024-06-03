#grille.py
import pygame

liste_name_var_case_unique = []

class Grille:
    
    def __init__(self, screen, color, rectangle, cote):
        self.a_screen = screen
        self.a_color = color
        self.a_rectangle = rectangle
        self.a_cote = cote
        
        screen = pygame.Surface
        color = tuple
        rectangle = pygame.Rect(0, 0, cote, cote)
        cote = int()
    
    def toute_les_cases(self, screen, color, rectangle, cote):
        
        casex = 0
        casey = 0
       
        for ligne in range(10):
            for caseunique in range(10) :
                
                rectangle = pygame.Rect(casex, casey, cote, cote)
                Grille.plateau(self, screen, color, rectangle, cote) 
                
                #liste_name_var_case_unique.append()
                
                casex += 20
            casey += 20
            casex = 0
    
    def plateau(self,  screen, color, rectangle, cote):
        
        pygame.draw.rect(screen, color, rectangle, cote)
        
    def zoom_moins(self, screen, color, rectangle, cote):
        
        

        Grille.toute_les_cases(self, screen, color, rectangle, cote)
        print(cote)
        print(rectangle)
            
    def zoom_plus(self, screen, color, rectangle, cote):
        

        Grille.toute_les_cases(self, screen, color, rectangle, cote)
        print(cote)
        print(rectangle)
        
        
        