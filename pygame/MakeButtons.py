import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Make Button")
screen.fill((0, 0, 0))

# Colors
button_font = pygame.font.SysFont('Arial', 20)
text_color = (255, 255, 255)
button_text = button_font.render('Quit', True, text_color)
button_color = (0, 0, 170)
button_over_color = (255, 50, 50)
screen.fill((100, 100, 100))

# Button
button_width = 100
button_height = 50
x = screen.get_width() / 2 - button_width / 2
y = screen.get_height() / 2 - button_height / 2
button_rect = [x, y, button_width, button_height]
button_text_x = button_rect[0] + (button_width - button_text.get_width()) / 2
button_text_y = button_rect[1] + (button_height - button_text.get_height()) / 2

game_over = False
x, y = 0, 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if button_rect[0] <= x <= button_rect[0] + button_rect[2] and \
                    button_rect[1] <= y <= button_rect[1] + button_rect[3]:
                game_over = True
                break
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    if button_rect[0] <= x <= button_rect[0] + button_rect[2] and \
            button_rect[1] <= y <= button_rect[1] + button_rect[3]:
        pygame.draw.rect(screen, button_over_color, button_rect)
    else:
        pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_text_x, button_text_y))
    pygame.display.update()

pygame.quit()
