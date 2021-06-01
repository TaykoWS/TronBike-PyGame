import pygame
import sys
import time
import os
from menu import Menu
from pygame.locals import *
SETTINGS = {

    'fullscreen': False
}


class Game:
    width = 900
    height = 680

    def __init__(self):
        if SETTINGS["fullscreen"]:
            flags = pygame.FULLSCREEN
        else:
            flags = 0
        # start the program
        pygame.init()
        # set screen
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode(
            [self.width, self.height], flags, 32)
        # set caption of program
        pygame.display.set_caption("TronBike")
        #  set icon
        pygame.display.set_icon(pygame.image.load('image/icon.png'))
        #  set font and size
        self.font = pygame.font.Font("font/retro_font.ttf", 60)
        self.font_small = pygame.font.Font("font/retro_font.ttf", 30)
        #  set music
        pygame.mixer.music.load('sound/menu.mp3')
        pygame.mixer.music.play()
        # call class Menu
        self.menu = Menu(self)
        self.menu.run()
