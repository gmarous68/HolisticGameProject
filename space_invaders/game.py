import pygame
from pygame.constants import K_ESCAPE


class Game(object):
    def __init__(self, name, width, height):
        self.game_name = name
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.game_name)
        self.current_state = None

    def run(self, state):
        game_over = False
        self.current_state = state
        clock = pygame.time.Clock()
        while not game_over:
            clock.tick(20)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True
            pressed = pygame.key.get_pressed()
            if pressed[K_ESCAPE]:
                game_over = True
            self.screen.fill((0, 0, 0))
            self.current_state = self.current_state.update(events)
            self.current_state.draw(self.screen)
            pygame.display.update()
        pygame.quit()
