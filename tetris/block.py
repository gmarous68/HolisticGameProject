import pygame
from random import randint

blocks = [
    [[1, 4, 7], [3, 4, 5]],  # straight
    [[1, 3, 4, 5, 7]],  # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]],  # two on two 1
    [[1, 2, 3, 4], [0, 3, 4, 7]],  # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]],  # L 1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]],  # L 2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]]  # one on three
]

colors = [
    (122, 78, 0),
    (15, 15, 80),
    (100, 60, 200),
    (180, 50, 100),
    (50, 100, 200),
    (255, 0, 0),
    (0, 0, 255)
]


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = randint(0, len(blocks) - 1)
        self.rotation = 0
        self.can_drop = False
        self.can_move = False
        self.can_rotate = False
        self.collision = False
        self.color = colors[randint(0, len(colors) - 1)]

    def shape(self):
        return blocks[self.type][self.rotation]

    def rotate(self, rows, cols, game_board):
        last_rotation = self.rotation
        self.rotation = (self.rotation + 1) % len(blocks[self.type])
        self.can_rotate = True
        for x in range(3):
            for y in range(3):
                if y * 3 + x in self.shape():
                    if self.collides(0, 0, rows, cols, game_board):
                        self.can_rotate = False
        if not self.can_rotate:
            self.rotation = last_rotation

    def collides(self, nx, ny, rows, cols, game_board):
        self.collision = False
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape():
                    if x + self.x + nx < 0 or x + self.x + nx > cols - 1:
                        self.collision = True
                        break
                    if y + self.y + nx < 0 or y + self.y + ny > rows - 1:
                        self.collision = True
                        break
                    if game_board[x + self.x + nx][y + self.y + ny] != (0, 0, 0):
                        self.collision = True
                        break
        return self.collision

    def drop_block(self, rows, cols, game_board):
        self.can_drop = True
        for x in range(3):
            for y in range(3):
                if y * 3 + x in self.shape():
                    if self.collides(0, 1, rows, cols, game_board):
                        self.can_drop = False
        if self.can_drop:
            self.y += 1
        else:  # if at the botton - color = green
            for y in range(3):
                for x in range(3):
                    if y * 3 + x in self.shape():
                        game_board[x + self.x][y + self.y] = self.color
        return self.can_drop

    def find_lines(self, rows, cols, game_board):
        lines = 0
        for y in range(rows):
            empty = 0
            for x in range(cols):
                if game_board[x][y] == (0, 0, 0):
                    empty += 1
            if empty == 0:
                lines += 1
                for y2 in range(y, 1, -1):
                    for x2 in range(cols):
                        game_board[x2][y2] = game_board[x2][y2 - 1]
        return lines

    def side_move(self, dx, rows, cols, game_board):
        self.can_move = True
        for y in range(3):
            for x in range(3):
                if y * 3 + x in self.shape():
                    if self.collides(dx, 0, rows, cols, game_board):
                        self.can_move = False
        if self.can_move and self.can_drop:
            self.x += dx

    def draw_block(self, screen, grid_size, x_gap, y_gap):
        for x in range(3):
            for y in range(3):
                if y * 3 + x in self.shape():
                    pygame.draw.rect(screen, self.color,
                                     [(x + self.x) * grid_size + x_gap + 1,
                                      (y + self.y) * grid_size + y_gap + 1,
                                      grid_size - 2, grid_size - 2])
