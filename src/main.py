#import de bibliothèques
import pygame, sys
from random import *

#import des modules de jeux

#initiation de pygame
pygame.init()

#paramètres de l'écran
size = width, height = 320, 240

#afficher l'écran
screen = pygame.display.set_mode(size)

#Game running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
