import pygame
import time
import random
import os
import sys
from pygame.locals import *


class Menu:
    index = 0
    mode = "menu"
    # set init for class Menu

    def __init__(self, game):
        self.game = game
        # set background
        self.image = pygame.image.load('image/background.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (900, 680))
        self.surf_ind = pygame.Surface([game.width, 60])
        self.surf_ind.set_alpha(100)
        self.surf_ind.fill((255, 255, 255))
        # set content in the homepage
        self.name = game.font.render(
            "WELCOME TO TRON BIKE ", 1, (255, 255, 255))
        self.name_shadow = game.font.render(
            "WELCOME TO TRON BIKE ", 1, (0, 0, 0))
        self.menu_option = [
            game.font.render("PLAY", 1, (255, 255, 255)),
            game.font.render("OPTION", 1, (255, 255, 255)),
            game.font.render("GUIDE", 1, (255, 255, 255)),
            game.font.render("QUIT", 1, (255, 255, 255)),
        ]
        self.menu_option_shadow = [
            game.font.render("PLAY", 1, (0, 0, 0)),
            game.font.render("OPTION", 1, (0, 0, 0)),
            game.font.render("GUIDE", 1, (0, 0, 0)),
            game.font.render("QUIT", 1, (0, 0, 0)),
        ]
    # set main menu function

    def run(self):
        # set a loop for the program to work stably
        clock = pygame.time.Clock()
        running = True
        while running:
            time = clock.tick(30)
            for event in pygame.event.get():
                #  if not quit, program run
                if event.type == pygame.QUIT:
                    running = False
                #  use keyboard to control, check if button is pressed
                if event.type == pygame.KEYDOWN:
                    # use button escape to return
                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            running = False
                        else:
                            self.mode = "menu"
                            self.index = 0
                    # set arrows
                    elif event.key == pygame.K_UP:
                        if self.index > 0:
                            self.index -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.index < 3:
                            self.index += 1
                    elif event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        # if choice= quit -> exit program
                        if self.mode == "menu" and self.index == 3:
                            running = False
                        # set a mode depend on your choice
                        elif self.mode == "menu" and self.index == 0:
                            self.mode = "play"
                        elif self.mode == "menu" and self.index == 1:
                            self.mode = "option"
                            # set music
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('sound/option.mp3')
                            pygame.mixer.music.play()
                        elif self.mode == "menu" and self.index == 2:
                            self.mode = "guide"
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('sound/guide.mp3')
                            pygame.mixer.music.play()
            # not quit, so the program call function draw
            if running:
                self.draw()
    # function to set a text but so long, if the length of the text is longer than the length of the screen then a line break

    def text_long(self, surface, text, pos, font, color=pygame.Color('white')):
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height
    # this function is to draw and set the position

    def draw(self):
        if self.mode == "menu":
            # to display something tin the screen
            self.game.screen.blit(self.image, (0, 0))
            self.game.screen.blit(self.name_shadow, (44, 64))
            self.game.screen.blit(self.name, (40, 60))
            self.game.screen.blit(self.surf_ind, (0, self.index * 70 + 350))
            for ind in range(4):
                self.game.screen.blit(
                    self.menu_option_shadow[ind], (354, 350 + ind * 70))
                self.game.screen.blit(
                    self.menu_option[ind], (350, 346 + ind * 70))
        # your option before will be moved here
        # if your option is GUIDE
        elif self.mode == "guide":
            #  set image
            self.image_guide = pygame.image.load(
                'image/guide.jpg').convert_alpha()
            # and size
            self.image_guide = pygame.transform.scale(
                self.image_guide, (900, 680))
            # set content of page GUIDE
            self.name_guide = self.game.font.render(
                "GUIDE ", 1, (255, 255, 255))
            self.msg1 = "The objective is to force the enemy light cycles into walls and jet trails, while simultaneously avoiding them. "
            self.msg2 = "Humain vs Computer Mode : use arrows to run "
            self.msg3 = "Humain vs Humain Mode : use arrows and button :  q z d s"
            self.msg4 = " Escape to return"
            self.game.screen.blit(self.image_guide, (0, 0))
            self.game.screen.blit(self.name_guide, (340, 50))
            # call function text_long to display a long text
            self.text_long(self.game.screen, self.msg1,
                           (40, 170), self.game.font_small)
            self.text_long(self.game.screen, self.msg2,
                           (40, 330), self.game.font_small)
            self.text_long(self.game.screen, self.msg3,
                           (40, 400), self.game.font_small)
            self.text_long(self.game.screen, self.msg4,
                           (40, 500), self.game.font)
        # if your option is OPTION
        elif self.mode == "option":
            self.image_option = pygame.image.load(
                'image/option.jpg').convert_alpha()
            self.image_option = pygame.transform.scale(
                self.image_option, (900, 680))
            self.name_option = self.game.font.render(
                "OPTION ", 1, (255, 255, 255))
            self.msg5 = " Change your name: Yaya"
            self.msg6 = " Escape to return"
            self.game.screen.blit(self.image_option, (0, 0))
            self.game.screen.blit(self.name_option, (340, 50))
            self.text_long(self.game.screen, self.msg5,
                           (40, 170), self.game.font_small)
            self.text_long(self.game.screen, self.msg6,
                           (40, 270), self.game.font_small)
        #  if your option is PLAY
        elif self.mode == "play":
            # call a fonction PLAY
            self.play()
        self.game.real_screen.blit(self.game.screen, (0, 0))
        # update the entire display surface to the screen
        pygame.display.flip()
    # function PLAY to start game

    def play(self):
        # set color
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        LIGHTBLUE = (4, 229, 225)
        ORANGE = (249, 141, 0)
        BLUE = (0, 73, 209)

        size = (500, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("TronBike")
        done = False
        clock = pygame.time.Clock()

        # setup
        trailX = [46]
        trailY = [50]
        robotrailX = [250]
        robotrailY = [254]
        animationtrailX = [434]
        animationtrailY = [450]
        animationcolor = [ORANGE]
        playerX = 50
        playerY = 50
        roboY = 250
        roboX = 250
        animationX = 430
        animationY = 450
        playerX_speed = 1
        playerY_speed = 0
        roboX_speed = 0
        roboY_speed = -1
        animationX_speed = -1
        animationY_speed = 0
        death = False
        win = False
        speed = 2
        Continue = False
        end = False
        turning = False

        # game setup loop
        while not Continue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mode = "human"
                    done = True
                    end = True
                    Continue = True

            # logic
            pos = pygame.mouse.get_pos()
            mouseX = pos[0]
            mouseY = pos[1]
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if pressed1 and (mouseX >= 160) and (mouseX <= 340) and (mouseY >= 360) and (mouseY <= 400):
                mode = "human"
                done = True
                end = True
                Continue = True
            elif pressed1 and (mouseX <= 250):
                mode = "human"
                Continue = True
            elif pressed1 and (mouseX > 250):
                mode = "computer"
                Continue = True

            """animation"""
            if (animationX >= 470) and (animationX_speed == 1):
                animationX_speed = 0
                animationY_speed = 1
            elif (animationX <= 30) and (animationX_speed == -1):
                animationX_speed = 0
                animationY_speed = -1
            elif (animationY >= 470) and (animationY_speed == 1):
                animationX_speed = -1
                animationY_speed = 0
            elif (animationY <= 30) and (animationY_speed == -1):
                animationX_speed = 1
                animationY_speed = 0

            if len(animationtrailX) > 200:
                del animationtrailX[0]
                del animationtrailY[0]
                del animationcolor[0]
            animationtrailX.append(animationX)
            animationtrailY.append(animationY)
            if (animationX >= 250):
                animationcolor.append(LIGHTBLUE)
            elif (animationX < 250):
                animationcolor.append(ORANGE)

            animationX += animationX_speed*speed
            animationY += animationY_speed*speed

            # display
            screen.fill(BLACK)
            pygame.draw.rect(screen, LIGHTBLUE, [0, 0, 500, 500], 10)
            for i in range(len(animationtrailX)):
                pygame.draw.rect(screen, animationcolor[i], [
                                 animationtrailX[i], animationtrailY[i], 4, 4])
            pygame.draw.rect(screen, WHITE, [animationX, animationY, 4, 4])
            pygame.draw.line(screen, BLUE, [70, 170], [430, 170], 5)

            pygame.draw.line(screen, ORANGE, [250, 497], [500, 497], 5)
            pygame.draw.line(screen, ORANGE, [497, 0], [497, 500], 5)
            pygame.draw.line(screen, ORANGE, [250, 2], [500, 2], 6)
            pygame.draw.line(screen, ORANGE, [250, 0], [250, 80], 5)
            pygame.draw.line(screen, ORANGE, [248, 78], [440, 78], 5)
            pygame.draw.line(screen, ORANGE, [440, 76], [440, 215], 5)
            pygame.draw.line(screen, ORANGE, [442, 218], [250, 218], 5)
            pygame.draw.line(screen, ORANGE, [252, 218], [252, 500], 5)

            pygame.draw.line(screen, LIGHTBLUE, [245, 0], [245, 80], 5)
            pygame.draw.line(screen, LIGHTBLUE, [247, 78], [60, 78], 5)
            pygame.draw.line(screen, LIGHTBLUE, [60, 76], [60, 215], 5)
            pygame.draw.line(screen, LIGHTBLUE, [58, 218], [249, 218], 5)
            pygame.draw.line(screen, LIGHTBLUE, [247, 218], [247, 500], 5)

            pygame.draw.line(screen, ORANGE, [250, 357], [330, 357], 5)
            pygame.draw.line(screen, ORANGE, [329, 355], [329, 404], 5)
            pygame.draw.line(screen, ORANGE, [329, 402], [250, 402], 5)

            pygame.draw.line(screen, LIGHTBLUE, [245, 357], [170, 357], 5)
            pygame.draw.line(screen, LIGHTBLUE, [171, 355], [171, 404], 5)
            pygame.draw.line(screen, LIGHTBLUE, [171, 402], [245, 402], 5)

            startfont = pygame.font.SysFont('Calibri', 25, True, False)
            humantext = startfont.render("Human v.s. Human", True, WHITE)
            screen.blit(humantext, [25, 240])
            robotext = startfont.render("Human v.s. Computer", True, WHITE)
            screen.blit(robotext, [260, 240])
            pygame.draw.rect(screen, BLACK, [190, 360, 120, 40])
            robotext = startfont.render("Click a side to begin", True, BLUE)
            screen.blit(robotext, [140, 185])
            robotext = startfont.render("Close Program", True, WHITE)
            screen.blit(robotext, [175, 370])

            Titlefont = pygame.font.SysFont(
                'Times New Roman', 100, True, False)
            Titletext = Titlefont.render("T R O N", True, BLUE)
            screen.blit(Titletext, [70, 70])

            pygame.display.flip()

        pygame.mouse.set_visible(False)

        while not done:
            # --- Main loop / input detec
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    end = True

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        if (playerX_speed == 0):
                            playerX_speed = -1
                            playerY_speed = 0
                    elif event.key == pygame.K_RIGHT:
                        if (playerX_speed == 0):
                            playerX_speed = 1
                            playerY_speed = 0
                    elif event.key == pygame.K_UP:
                        if (playerY_speed == 0):
                            playerY_speed = -1
                            playerX_speed = 0
                    elif event.key == pygame.K_DOWN:
                        if (playerY_speed == 0):
                            playerY_speed = 1
                            playerX_speed = 0

                    if (mode == "human"):
                        if event.key == pygame.K_z:
                            if (roboY_speed == 0):
                                roboY_speed = -1
                                roboX_speed = 0
                        elif event.key == pygame.K_s:
                            if (roboY_speed == 0):
                                roboY_speed = 1
                                roboX_speed = 0
                        elif event.key == pygame.K_d:
                            if (roboX_speed == 0):
                                roboX_speed = 1
                                roboY_speed = 0
                        elif event.key == pygame.K_q:
                            if (roboX_speed == 0):
                                roboX_speed = -1
                                roboY_speed = 0

            # --- Game detection collision
            for i in range(len(trailX)):
                if (abs(playerX-trailX[i]) < speed) and (abs(playerY-trailY[i]) < speed):
                    death = True
                elif (abs(playerX-robotrailX[i]) < speed) and (abs(playerY-robotrailY[i]) < speed):
                    death = True
                if (turning == False):
                    if (abs(roboX-robotrailX[i]) < 2) and (abs(roboY-robotrailY[i]) < 2):
                        win = True
                    elif (abs(roboX-trailX[i]) < 2) and (abs(roboY-trailY[i]) < 2):
                        win = True

            turning = False

            trailX.append(playerX)
            trailY.append(playerY)
            robotrailX.append(roboX)
            robotrailY.append(roboY)

            """robot decision"""
            if (mode == "computer"):
                if (roboX < 440) and (roboX > 60) and (roboY > 60) and (roboY < 440):
                    roboaction = random.randint(1, 180)
                    if (roboaction == 1):
                        if (roboX_speed == 1) or (roboX_speed == -1):
                            roboY_speed = 1
                            roboX_speed = 0
                        elif (roboY_speed == 1) or (roboY_speed == -1):
                            roboX_speed = 1
                            roboY_speed = 0
                    if (roboaction == 2):
                        if (roboX_speed == 1) or (roboX_speed == -1):
                            roboY_speed = -1
                            roboX_speed = 0
                        elif (roboY_speed == 1) or (roboY_speed == -1):
                            roboX_speed = -1
                            roboY_speed = 0

                if (roboX > 480) or (roboX < 10) or (roboY > 480) or (roboY < 10):
                    move = random.randint(1, 2)
                    if (roboX > 470) or (roboX < 20):
                        turning = True
                        roboX_speed = 0
                        if (roboY > 450):
                            roboY_speed = -1
                        elif (roboY < 50):
                            roboY_speed = 1
                        else:
                            if (move == 1):
                                roboY_speed = -1
                            if (move == 2):
                                roboY_speed = 1
                    if (roboY > 470) or (roboY < 20):
                        roboY_speed = 0
                        turning = True
                        if (roboX > 450):
                            roboX_speed = -1
                        elif (roboX < 50):
                            roboX_speed = 1
                        else:
                            if (move == 1):
                                roboX_speed = -1

                            if (move == 2):
                                roboX_speed = 1

                roboaction = random.randint(1, 2)
                for i in range(len(trailX)):
                    if (abs((roboX+(roboX_speed*7))-trailX[i]) < 6) and (abs((roboY+(roboY_speed*7))-trailY[i]) < 6):
                        if (roboX_speed != 0):
                            roboX_speed = 0
                            if (roboaction == 1):
                                roboY_speed = 1
                                for i in range(len(trailX)):
                                    if (abs((roboX)-trailX[i]) < 4) and (abs((roboY+(roboY_speed*7))-trailY[i]) < 6):
                                        roboY_speed = -1
                                    if ((roboY + 5) >= 480):
                                        roboY_speed = -1
                            if (roboaction == 2):
                                roboY_speed = -1
                                for i in range(len(trailX)):
                                    if (abs((roboX)-trailX[i]) < 4) and (abs((roboY+(roboY_speed*7))-trailY[i]) < 6):
                                        roboY_speed = 1
                                    if ((roboY - 5) <= 10):
                                        roboY_speed = 1
                        elif (roboY_speed != 0):
                            roboY_speed = 0
                            if (roboaction == 1):
                                roboX_speed = 1
                                for i in range(len(robotrailX)):
                                    if (abs((roboX+(roboX_speed*7))-trailX[i]) < 6) and (abs((roboY)-trailY[i]) < 4):
                                        roboX_speed = -1
                                    if ((roboX + 5) >= 480):
                                        roboX_speed = -1
                            if (roboaction == 2):
                                roboX_speed = -1
                                for i in range(len(robotrailX)):
                                    if (abs((roboX+(roboX_speed*7))-trailX[i]) < 6) and (abs((roboY)-trailY[i]) < 4):
                                        roboX_speed = 1
                                    if ((roboX - 5) <= 10):
                                        roboX_speed = 1
                for i in range(len(robotrailX)):
                    if (abs((roboX+(roboX_speed*7))-robotrailX[i]) < 6) and (abs((roboY+(roboY_speed*7))-robotrailY[i]) < 6):
                        if (roboX_speed != 0):
                            roboX_speed = 0
                            if (roboaction == 1):
                                roboY_speed = 1
                                for i in range(len(robotrailX)):
                                    if (abs((roboX)-robotrailX[i]) < 4) and (abs((roboY+(roboY_speed*7))-robotrailY[i]) < 6):
                                        roboY_speed = -1
                                    if ((roboY + 5) >= 480):
                                        roboY_speed = -1
                            if (roboaction == 2):
                                roboY_speed = -1
                                for i in range(len(robotrailX)):
                                    if (abs((roboX)-robotrailX[i]) < 4) and (abs((roboY+(roboY_speed*7))-robotrailY[i]) < 6):
                                        roboY_speed = 1
                                    if ((roboY - 5) <= 10):
                                        roboY_speed = 1
                        elif (roboY_speed != 0):
                            roboY_speed = 0
                            if (roboaction == 1):
                                roboX_speed = 1
                                for i in range(len(robotrailX)):
                                    if (abs((roboX+(roboX_speed*7))-robotrailX[i]) < 6) and (abs((roboY)-robotrailY[i]) < 4):
                                        roboX_speed = -1
                                    if ((roboX + 5) >= 480):
                                        roboX_speed = -1
                            if (roboaction == 2):
                                roboX_speed = -1
                                for i in range(len(robotrailX)):
                                    if (abs((roboX+(roboX_speed*7))-robotrailX[i]) < 6) and (abs((roboY)-robotrailY[i]) < 4):
                                        roboX_speed = 1
                                    if ((roboX - 5) <= 10):
                                        roboX_speed = 1

            """general movement"""
            playerX += playerX_speed*speed
            playerY += playerY_speed*speed
            roboX += roboX_speed*speed
            roboY += roboY_speed*speed

            if (playerX > 490) or (playerX < 5) or (playerY > 490) or (playerY < 5):
                death = True
            if (roboX > 490) or (roboX < 5) or (roboY > 490) or (roboY < 5):
                win = True

            screen.fill(BLACK)

            # --- display color player
            for i in range(len(trailX)):
                pygame.draw.rect(screen, LIGHTBLUE, [
                                 trailX[i], trailY[i], 4, 4])
            for i in range(len(robotrailX)):
                pygame.draw.rect(screen, ORANGE, [
                                 robotrailX[i], robotrailY[i], 4, 4])
            pygame.draw.rect(screen, WHITE, [playerX, playerY, 4, 4])
            pygame.draw.rect(screen, WHITE, [roboX, roboY, 4, 4])
            pygame.draw.rect(screen, ORANGE, [0, 0, 500, 500], 5)
            font = pygame.font.SysFont('Calibri', 25, True, False)

            if (death == True):
                text = font.render("ORANGE has WON!", True, WHITE)
                screen.blit(text, [165, 220])
            if (win == True):
                text = font.render("BLUE has WON!", True, WHITE)
                screen.blit(text, [180, 220])

            pygame.display.flip()

            # check death
            if (death == True) or (win == True):
                time.sleep(0.5)
                done = True
            clock.tick(144)

        # ALT F4 ?
        if end == False:
            done = True

        pygame.quit()
