import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500], 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Resize Butterfly")

butterfly = pygame.image.load("..\\images\\butterfly.png")
butterfly = pygame.transform.scale(butterfly, (50, 50))

game_over = False
butterfly_pos_x = screen.get_width() // 2 - butterfly.get_width() // 2
butterfly_pos_y = screen.get_height() // 2 - butterfly.get_height() // 2

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
    screen.blit(butterfly, (butterfly_pos_x, butterfly_pos_y))
    pygame.display.update()

pygame.quit()
