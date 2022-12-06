#import de bibliothèques
import pygame
from random import *

#import des modules de jeux
from minerais import *

#initiation de pygame
pygame.init()

#paramètres de l'écran
size = width, height = 320, 240

#afficher l'écran
screen = pygame.display.set_mode(size)

#définition de running
running = True

#Game running
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()