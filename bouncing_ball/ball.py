import pygame


class Ball(object):
    def __init__(self):
        self.ball = pygame.image.load("..\\images\\ball.png")
        self.ball = pygame.transform.scale(self.ball, (50, 50))
        # Aligns the picture pixel format with the screen pixel format
        self.ball = self.ball.convert_alpha()
        # Determine football location and grab it
        self.ball_rect = self.ball.get_rect()
        self.ball_start = (0, 0)
        self.ball_speed = (3.0, 3.0)
        self.ball_served = False
        self.sx, self.sy = self.ball_speed
        self.ball_rect.topleft = self.ball_start

    def get_ball(self):
        return self.ball
