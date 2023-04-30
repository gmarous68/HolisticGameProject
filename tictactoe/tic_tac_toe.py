import pygame
from pygame.locals import K_ESCAPE
from board import Board

pygame.init()

# Basic Window
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TicTacToe")

board = Board(screen)
x, y = (0, 0)
game_over = False


def key_board_mouse_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global game_over
            game_over = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #x and y within box 1 -> 9 - calculate box size and coordnates

    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        game_over = True


while not game_over:
    screen.fill((0, 0, 0,))
    key_board_mouse_events()
    board.draw_grid_on_screen(screen)
    pygame.display.update()

pygame.quit()
