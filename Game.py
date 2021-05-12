import pygame
import sys
from pygame.locals import *

def game():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('TronBike')

    # Remplissage de l'arrière-plan
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))


    # Blitter le tout dans la fenêtre
    screen.blit(background, (0, 0))

    # ---- Test for player lightbycicle
    # Initialing Color
    color1 = (255, 0, 0)
    color2 = (0, 0, 255)
    # Drawing rectangle (Marging x, y, Size x, y)
    lb1 = pygame.draw.rect(screen, color1, pygame.Rect(300, 20, 40, 40), 2)
    lb2 = pygame.draw.rect(screen, color2, pygame.Rect(440, 20, 40, 40), 2)

    # Permet de blitter
    pygame.display.flip()

    print("Game Launched")

    # Run the Game Loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return