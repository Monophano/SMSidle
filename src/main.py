#import du modules
from pygame import *

#création d'une fenetre de 360 par 480
game_fen = display.set_mode((360,480))

#définition du titre de la fenetre
display.set_caption("SMSIdle")

#init la fen
init()

#setup du bg
bg = image.load('')
bg = bg.convert()

#condition de continuation du jeu
jouer = True

while jouer == True:
    #si fenetre quitter alors fin du jeux
    for events in event.get():
         if events.type == QUIT:
             jouer=False
             quit()