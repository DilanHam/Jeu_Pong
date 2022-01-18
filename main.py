#HAMADOUCHE Dilan
#Le 18/01/2022
#Jeu type 'Pong'
#Version 0.1
#Contact dilan.hamadouche@etu-univ.fr

"Importation Paquet + Initialisation de Pygame"
import pygame
import core
from joueur import Joueur
import Balle
from core import cleanScreen
from core import fps
from Balle import balle

core.fps = 50
LARGEUR = 1000
HAUTEUR = 800
cleanScreen()
pygame.init()

def setup():
    print("C'est parti")
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    print("Fin de partie")

def run():
    position = (500, -200)
    taille = largeur, hauteur = (20, 60)
    position = x, y = (20, 50)
    personnage(1,10,400)
    personnage(2,990,400)
    balle()

core.main(setup,run())