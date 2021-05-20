import pygame
import os

# Initialisation de la fenêtre d'affichage
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tron Bike')

# Couleurs
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

# Permet de faire tourner le programme à un certains taux d'images par secondes "avec la variable clock"
FPS = 60

# Images pour les motos
LIGHTBIKE_WIDTH, LIGHTBIKE_HEIGHT = 26, 29
LIGHTBIKE1_IMAGE = pygame.image.load(os.path.join('Assets', 'lb1.png'))
LIGHTBIKE2_IMAGE = pygame.image.load(os.path.join('Assets', 'lb2.png'))
LIGHTBIKE2 = pygame.transform.rotate(LIGHTBIKE2_IMAGE, 180)

# Données pour le jeu
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
DIRECTION = 1

def draw_screen(lightbike1, lightbike2):
    # Dessine le fond d'écran de la fenêtre
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, BORDER, 1)
    SCREEN.blit(LIGHTBIKE1_IMAGE, (lightbike1.x, lightbike1.y))
    SCREEN.blit(LIGHTBIKE2, (lightbike2.x, lightbike2.y))
    pygame.display.update()

def lightbike1_movement(keys_pressed, lb1):
    # Test des inputs
    if keys_pressed[pygame.K_q]:  # Left for lb1
        lb1.x -= DIRECTION
    if keys_pressed[pygame.K_d]:  # Right for lb1
        lb1.x += DIRECTION
    if keys_pressed[pygame.K_z]:  # Up for lb1
        lb1.y -= DIRECTION
    if keys_pressed[pygame.K_s]:  # Down for lb1
        lb1.y += DIRECTION

def lightbike2_movement(keys_pressed, lb2):
    # Test des inputs
    if keys_pressed[pygame.K_LEFT]:  # Left for lb1
        lb2.x -= DIRECTION
    if keys_pressed[pygame.K_RIGHT]:  # Right for lb1
        lb2.x += DIRECTION
    if keys_pressed[pygame.K_UP]:  # Up for lb1
        lb2.y -= DIRECTION
    if keys_pressed[pygame.K_DOWN]:  # Down for lb1
        lb2.y += DIRECTION

def lightbike1_collision(lb1):
    # Test des limites du terrain pour prévoir collision
    if lb1.x + DIRECTION < -6:
        lb1.x = -6
    if lb1.x + DIRECTION > WIDTH - 20:
        lb1.x = WIDTH - 20
    if lb1.y + DIRECTION < -6:
        lb1.y = -6
    if lb1.y + DIRECTION > HEIGHT - 25:
        lb1.y = HEIGHT - 25

def lightbike2_collision(lb2):
    # Test des limites du terrain pour prévoir collision
    if lb2.x + DIRECTION < 0:
        lb2.x = 0
    if lb2.x + DIRECTION > WIDTH - 15:
        lb2.x = WIDTH - 15
    if lb2.y + DIRECTION < -2:
        lb2.y = -2
    if lb2.y + DIRECTION > HEIGHT - 25:
        lb2.y = HEIGHT - 25

def run():
    lb1 = pygame.Rect(350, 300, LIGHTBIKE_WIDTH, LIGHTBIKE_HEIGHT)
    lb2 = pygame.Rect(400, 300, LIGHTBIKE_WIDTH, LIGHTBIKE_HEIGHT)

    # Fait tourner la boucle de jeu
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Déplacement automatique des motos
        lb1.y -= 1
        lb2.y += 1

        # Test des collision
        lightbike1_collision(lb1)
        lightbike2_collision(lb2)

        keys_pressed = pygame.key.get_pressed()
        lightbike1_movement(keys_pressed, lb1)
        lightbike2_movement(keys_pressed, lb2)

        draw_screen(lb1, lb2)

    pygame.quit()