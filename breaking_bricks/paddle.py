import pygame


class Paddle:
    def __init__(self, screen):
        self.image = pygame.image.load("..\\images\\paddle.png")
        # aligns image pixel format with screen pixel format - makes rendering a lot quicker
        self.paddle = self.image.convert_alpha()
        self.paddle_rect = self.image.get_rect()
        self.paddle_rect[1] = screen.get_height() - 100

    def get_paddle(self):
        return self.paddle
