import pygame


class Balle:
    def __init__(balle):

        LARGEUR = 1000
        HAUTEUR = 800
        couleur = (255,255,255)
        fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
        corps = pygame.draw.rect(fenetre,couleur,pygame.Rect(500,400,8,8))
        pygame.display.flip()