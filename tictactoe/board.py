import pygame


class Board:
    def __init__(self, screen):
        self.game_board = []
        self.rows_and_cols = 3
        self.grid_size = screen.get_width() // self.rows_and_cols

    def draw_grid_on_screen(self, screen):
        rect_fill = (255, 255, 255)
        for y in range(self.rows_and_cols):  # rows
            for x in range(self.rows_and_cols):  # cols
                pygame.draw.rect(screen, rect_fill, [x * self.grid_size, y * self.grid_size, \
                                                     self.grid_size, self.grid_size], 1)
