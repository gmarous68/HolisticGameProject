import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([500, 500], 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Hello Keyboard")

butterfly = pygame.image.load("..\\images\\butterfly.png")
butterfly = pygame.transform.scale(butterfly, (50, 50))

game_over = False
butterfly_pos_x = screen.get_width() // 2 - butterfly.get_width() // 2
butterfly_pos_y = screen.get_height() // 2 - butterfly.get_height() // 2

x, y = 0, 0
clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            x -= butterfly.get_width() / 2
            y -= butterfly.get_height() / 2
    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        game_over = True
        break
    if pressed[K_SPACE]:
        x, y = 0, 0
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if x < 0:
        x = 0
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if x > (screen.get_width() - butterfly.get_width()):
        x = screen.get_width() - butterfly.get_width()
    if pressed[K_UP]:
        y -= 0.5 * dt
    if y < 0:
        y = 0
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if y > (screen.get_height() - butterfly.get_height()):
        y = screen.get_height() - butterfly.get_height()

    screen.fill((0, 0, 0))
    screen.blit(butterfly, (x, y))
    pygame.display.update()

pygame.quit()
