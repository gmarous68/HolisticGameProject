import pygame
from random import randint
from ship import Ship
from asteroids import Asteroid

# Screen
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Asteroids")
back_ground = pygame.image.load("..\\images\\space.png")

# Ship
ship = Ship((screen.get_width() // 2, screen.get_height() // 2))

# Asteroids
asteroids = []
for i in range(5):
    asteroids.append(Asteroid((randint(0, screen.get_width()), randint(0, screen.get_height())), 0))

# You lost on screen
font = pygame.font.Font("..\\fonts\\Alien.ttf", 80)
text_loser = font.render("You lost!", True, (255, 255, 255))
text_loser_pos = ((screen.get_width() - text_loser.get_width()) // 2,
                  (screen.get_height() - text_loser.get_height()) // 2)

# You won on screen
text_winner = font.render("You Won!", True, (255, 255, 255))
text_winner_pos = ((screen.get_width() - text_winner.get_width()) // 2,
                (screen.get_height() - text_winner.get_height()) // 2)

clock = pygame.time.Clock()
game_over = False

while not game_over:
    clock.tick(55)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game_over = True
            break

    screen.blit(back_ground, (0, 0))
    if ship is None:
        screen.blit(text_loser, text_loser_pos)
        pygame.display.update()
        continue

    if len(asteroids) == 0:
        screen.blit(text_winner, text_winner_pos)
        pygame.display.update()
        continue

    ship.update(clock, screen)
    ship.draw(screen)

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw(screen)
        if asteroid.hit(ship.pos):
            ship = None
            break
    if ship is None:
        continue

    dead_bullets = []
    dead_asteroids = []

    for bullet in ship.bullets:
        bullet.update()
        bullet.draw(screen)

        if bullet.pos.x < asteroid.out_of_bounds[0] or bullet.pos.x > asteroid.out_of_bounds[2] or \
                bullet.pos.y < asteroid.out_of_bounds[1] or bullet.pos.y > asteroid.out_of_bounds[3]:
            if bullet not in dead_bullets:
                dead_bullets.append(bullet)

        for asteroid in asteroids:
            if asteroid.hit(bullet.pos):
                if bullet not in dead_bullets:
                    dead_bullets.append(bullet)
                if asteroid not in dead_asteroids:
                    dead_asteroids.append(asteroid)

    for bullet in dead_bullets:
        ship.bullets.remove(bullet)
    for asteroid in dead_asteroids:
        if asteroid.size < 2:
            asteroids.append(Asteroid(asteroid.pos, asteroid.size + 1))
            asteroids.append(Asteroid(asteroid.pos, asteroid.size + 1))
        asteroids.remove(asteroid)

    pygame.display.update()

pygame.quit()
