import pygame
from pygame.locals import *
from ball import Ball

pygame.init()

# Basic Window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Bouncing Ball")

ball_obj = Ball()
ball = ball_obj.get_ball()  

clock = pygame.time.Clock()
x, y = 0, 0
game_over = False


def key_board_mouse_events():
    global x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global game_over
            game_over = True
            break

    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        game_over = True
    if pressed[K_SPACE]:
        ball_obj.ball_served = True

    # ball top limit
    if ball_obj.ball_rect[1] <= 0:
        ball_obj.ball_rect[1] = 0
        ball_obj.sy *= -1
    # ball bottom limit
    if ball_obj.ball_rect[1] >= screen.get_height() - ball_obj.ball_rect.height:
        ball_obj.ball_rect[1] = screen.get_height() - ball_obj.ball_rect.height
        ball_obj.sy *= -1
    # ball left limit
    if ball_obj.ball_rect[0] <= 0:
        ball_obj.ball_rect[0] = 0
        ball_obj.sx *= -1
    # ball right limit
    if ball_obj.ball_rect[0] >= screen.get_width() - ball_obj.ball_rect.width:
        ball_obj.ball_rect[0] = screen.get_width() - ball_obj.ball_rect.width
        ball_obj.sx *= -1

    if ball_obj.ball_served:
        ball_obj.ball_rect[0] += ball_obj.sx
        ball_obj.ball_rect[1] += ball_obj.sy


while not game_over:
    # update 150 frames per second
    dt = clock.tick(150)
    # Update screen to black
    screen.fill((0, 0, 0,))
    key_board_mouse_events()
    screen.blit(ball, ball_obj.ball_rect)
    pygame.display.update()
pygame.quit()
