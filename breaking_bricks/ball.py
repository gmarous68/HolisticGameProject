import pygame


class Ball:
    def __init__(self):
        self.image = pygame.image.load("..\\images\\football.png")
        # aligns image pixel format with screen pixel format - makes rendering a lot quicker
        self.ball = self.image.convert_alpha()
        self.ball_rect = self.image.get_rect()
        self.start_pos = (200, 200)
        self.ball_speed = (3.0, 3.0)
        self.ball_served = False
        # speed in the x and y direction
        self.sx, self.sy = self.ball_speed
        self.ball_rect.topleft = self.start_pos

    def get_ball(self):
        return self.ball
