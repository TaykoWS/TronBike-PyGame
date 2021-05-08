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
        pygame.init()
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode(
            [self.width, self.height], flags, 32)
        pygame.display.set_caption("TronBike")
        pygame.display.set_icon(pygame.image.load('image/icon.png'))
        self.font = pygame.font.Font("font/retro_font.ttf", 60)
        self.font_small = pygame.font.Font("font/retro_font.ttf", 30)
        pygame.mixer.music.load('sound/menu.mp3')
        pygame.mixer.music.play()
        self.menu = Menu(self)
        self.menu.run()
