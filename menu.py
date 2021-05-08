import pygame


class Menu:
    index = 0
    mode = "menu"

    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('image/background.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (900, 680))
        self.surf_ind = pygame.Surface([game.width, 60])
        self.surf_ind.set_alpha(100)
        self.surf_ind.fill((255, 255, 255))
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

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            time = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            running = False
                        else:
                            self.mode = "menu"
                            self.index = 0
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
                        if self.mode == "menu" and self.index == 3:
                            running = False
                        elif self.mode == "menu" and self.index == 0:
                            pass
                            # self.game.run()
                        elif self.mode == "menu" and self.index == 1:
                            self.mode = "option"
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('sound/option.mp3')
                            pygame.mixer.music.play()
                        elif self.mode == "menu" and self.index == 2:
                            self.mode = "guide"
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('sound/guide.mp3')
                            pygame.mixer.music.play()

            if running:
                self.draw()

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

    def draw(self):
        if self.mode == "menu":
            self.game.screen.blit(self.image, (0, 0))
            self.game.screen.blit(self.name_shadow, (44, 154))
            self.game.screen.blit(self.name, (40, 150))
            self.game.screen.blit(self.surf_ind, (0, self.index * 70 + 350))
            for ind in range(4):
                self.game.screen.blit(
                    self.menu_option_shadow[ind], (354, 350 + ind * 70))
                self.game.screen.blit(
                    self.menu_option[ind], (350, 346 + ind * 70))
        elif self.mode == "guide":
            self.image_guide = pygame.image.load(
                'image/guide.jpg').convert_alpha()
            self.image_guide = pygame.transform.scale(
                self.image_guide, (900, 680))
            self.name_guide = self.game.font.render(
                "GUIDE ", 1, (255, 255, 255))
            self.msg1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vestibulum arcu vitae nisi interdum, pellentesque interdum nunc consectetur. Ut aliquet sit amet ligula vel vehicula. In lacinia nisi vel orci euismod placerat id ac erat."
            self.msg2 = " Escape to return"
            self.game.screen.blit(self.image_guide, (0, 0))
            self.game.screen.blit(self.name_guide, (340, 50))
            self.text_long(self.game.screen, self.msg1,
                           (40, 170), self.game.font_small)
            self.text_long(self.game.screen, self.msg2,
                           (40, 470), self.game.font)
        elif self.mode == "option":
            self.image_option = pygame.image.load(
                'image/option.jpg').convert_alpha()
            self.image_option = pygame.transform.scale(
                self.image_option, (900, 680))
            self.name_option = self.game.font.render(
                "OPTION ", 1, (255, 255, 255))
            self.msg3 = " Change your name: "
            self.msg4 = " Change your color: "
            self.msg5 = " Escape to return"
            self.game.screen.blit(self.image_option, (0, 0))
            self.game.screen.blit(self.name_option, (340, 50))
            self.text_long(self.game.screen, self.msg3,
                           (40, 170), self.game.font_small)
            self.text_long(self.game.screen, self.msg4,
                           (40, 270), self.game.font_small)
            self.text_long(self.game.screen, self.msg5,
                           (40, 370), self.game.font)
        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()
