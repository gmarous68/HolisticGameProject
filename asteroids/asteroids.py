import pygame
from random import randint
from pygame import Vector2
from pygame.mixer import Sound
import utility


class Asteroid(object):
    def __init__(self, pos, size):
        self.asteroids = ["..\\images\\asteroid1.png", "..\\images\\asteroid2.png", "..\\images\\asteroid3.png"]
        self.image = pygame.image.load(self.asteroids[size])
        self.pos = Vector2(pos)
        self.velocity = Vector2(randint(-3, 3), randint(-3, 3))
        self.out_of_bounds = [-150, -150, 900, 900]
        self.radius = self.image.get_width() // 2
        self.explode = Sound("..\\sounds\\explode.mp3")
        self.size = size

    def update(self):
        self.pos += self.velocity

        # replaced by self.pos = utility.wrap_position(screen) in draw method
        # # top, bottom and side limits
        # if self.pos.x < self.out_of_bounds[0] or self.pos.y > self.out_of_bounds[2]:
        #     self.velocity.x *= -1
        # if self.pos.y < self.out_of_bounds[1] or self.pos.y > self.out_of_bounds[3]:
        #     self.velocity.y *= -1

    def draw(self, screen):
        # if asteroids are going of egde of screen - coming back on the other edge
        self.pos = utility.wrap_position(self.pos, screen)
        utility.blit_rotated(self.pos, self.velocity, self.image, screen)

    def hit(self, bullet_pos):
        if self.pos.distance_to(bullet_pos) <= self.radius:
            # self.explode.play()
            return True
        return False
