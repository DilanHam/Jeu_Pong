import pygame

class Joueur:
    def __init__(personnage):

        LARGEUR = 1000
        HAUTEUR = 800
        couleur = (255,255,255)
        fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.draw.rect(fenetre,couleur, pygame.Rect(20,400,15,100))
        pygame.display.flip()