import pygame
from block import Block
from random import randint

pygame.init()

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Tetris")
screen_fill = (0, 0, 0)

# grid
grid_size = 30
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

block = Block((cols - 1) // 2, 0)

clock = pygame.time.Clock()
fps = 5

game_board = []
score = 0
font = pygame.font.SysFont("Arial", 25, True, False)
font2 = pygame.font.SysFont("Arial", 50, True, False)
finished_text = font2.render("Game Over", True, (255, 255, 255))
ft_pos = ((screen.get_width() - finished_text.get_width()) // 2,
          (screen.get_height() - finished_text.get_height()) // 2)
game_finished = False
game_over = False


def draw_grid_on_screen():
    rect_fill = (100, 100, 100)
    for y in range(rows):  # rows
        for x in range(cols):  # cols
            pygame.draw.rect(screen, rect_fill, \
                             [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)
            if game_board[x][y] != (0, 0, 0):
                pygame.draw.rect(screen, game_board[x][y], \
                                 [x * grid_size + x_gap + 1, y * grid_size + y_gap + 1, \
                                  grid_size - 1, grid_size - 1])


def populate_game_board(game_board):
    # initialize game board
    for i in range(cols):
        new_col = []
        for k in range(rows):
            new_col.append((0, 0, 0))
        game_board.append(new_col)


while not game_over:
    # frames pr second
    clock.tick(fps)

    populate_game_board(game_board)

    # keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                block.rotate(rows, cols, game_board)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game_over = True
            break
        if event.key == pygame.K_LEFT:
            block.side_move(-1, rows, cols, game_board)
        if event.key == pygame.K_RIGHT:
            block.side_move(1, rows, cols, game_board)

    screen.fill(screen_fill)
    draw_grid_on_screen()
    if block:
        block.draw_block(screen, grid_size, x_gap, y_gap)
        if event.type != pygame.KEYDOWN:
            if not block.drop_block(rows, cols, game_board) and not game_finished:
                score += block.find_lines(rows, cols, game_board)
                block = Block(randint(5, cols - 5), 0)
                if block.collides(0, 0, rows, cols, game_board):
                    game_finished = True
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, [0, 0])
    if game_finished:
        screen.blit(finished_text, ft_pos)
    pygame.display.update()

pygame.quit()
