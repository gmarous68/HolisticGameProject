import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480], 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Hello Pygame")

ball = pygame.image.load("..\\images\\football.png")

game_over = False
ball_pos_x = 320 - 16
ball_pos_y = 240 - 16

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
    screen.blit(ball, (ball_pos_x, ball_pos_y))
    pygame.display.update()

pygame.quit()
