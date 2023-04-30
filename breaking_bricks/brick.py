import pygame


class Brick:
    def __init__(self, screen):
        self.image = pygame.image.load("..\\images\\brick.png")
        # aligns image pixel format with screen pixel format - makes rendering a lot quicker
        self.brick = self.image.convert_alpha()
        self.brick_rect = self.image.get_rect()
        # Bricks created across the screen
        self.bricks = []
        self.brick_rows = 5
        self.brick_gap = 5
        self.brick_cols = screen.get_width() // (self.brick_rect[2] + self.brick_gap)
        self.side_gap = (screen.get_width() - (self.brick_rect[2] + self.brick_gap) * \
                         self.brick_cols + self.brick_gap) // 2

    def create_bricks(self):
        # creating table with all brick coordinates
        for y in range(self.brick_rows):
            brick_y = y * (self.brick_rect[3] + self.brick_gap)
            for x in range(self.brick_cols):
                brick_x = x * (self.brick_rect[2] + self.brick_gap) + self.side_gap
                self.bricks.append((brick_x, brick_y))
        return self.bricks

    def get_brick(self):
        return self.brick
