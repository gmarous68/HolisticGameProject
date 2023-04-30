import pygame
from pygame import Vector2
from pygame.mixer import Sound
import utility


class Bullet:
    def __init__(self, pos, velocity):
        self.pos = pos
        self.velocity = velocity

    def update(self):
        self.pos += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.pos.x, self.pos.y, 5, 5])


class Ship(object):
    def __init__(self, pos):
        self.pos = Vector2(pos)
        self.image = pygame.image.load("..\\images\\ship.png")
        self.forward = Vector2(0, -1)
        self.rotated_image = 0
        self.bullets = []
        self.can_shoot = 0
        self.drift = (0, 0)
        self.shoot = Sound("..\\sounds\\shoot.wav")

    def update(self, clock, screen):
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_UP]:
            self.pos += self.forward
            self.drift = (self.drift + self.forward) / 1.5
        if is_key_pressed[pygame.K_LEFT]:
            self.forward = self.forward.rotate(-1)
        if is_key_pressed[pygame.K_RIGHT]:
            self.forward = self.forward.rotate(1)
        if is_key_pressed[pygame.K_SPACE] and self.can_shoot == 0:
            self.bullets.append(Bullet(Vector2(self.pos), self.forward * 10))
            #self.shoot.play()
            self.can_shoot = 500
        self.pos += self.drift
        if self.can_shoot > 0:
            self.can_shoot -= clock.get_time()
        else:
            self.can_shoot = 0

    def draw(self, screen):
        self.pos = utility.wrap_position(self.pos, screen)
        utility.blit_rotated(self.pos, self.forward, self.image, screen)

