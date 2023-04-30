import pygame


class MainMenu():
    def __init__(self):
        self.font = pygame.font.Font("..\\fonts\\Alien.ttf", 80)
        self.title = self.font.render("Alien Invasion!", True, (255, 255, 255))
        self.title_pos = (10, 10)

    def update(self, events):
        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_pos)
