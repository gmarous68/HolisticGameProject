import pygame
from pygame.locals import K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE
from ball import Ball
from brick import Brick
from paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

# Ball
ball_obj = Ball()
ball = ball_obj.get_ball()
# Bat
paddle_obj = Paddle(screen)
paddle = paddle_obj.get_paddle()
# Bricks
brick_obj = Brick(screen)
brick = brick_obj.get_brick()
bricks = brick_obj.create_bricks()

clock = pygame.time.Clock()
game_over = False


def key_board_mouse_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global game_over
            game_over = True
            break
    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        game_over = True
    # Move the paddle
    if pressed[K_LEFT]:
        paddle_obj.paddle_rect[0] -= 0.5 * dt
    if pressed[K_RIGHT]:
        paddle_obj.paddle_rect[0] += 0.5 * dt
    # Move the ball
    if pressed[K_SPACE]:
        ball_obj.ball_served = True
    if ball_obj.ball_served:
        ball_obj.ball_rect[0] += ball_obj.sx
        ball_obj.ball_rect[1] += ball_obj.sy

    # Hitting the ball with the bat
    paddle_upper_corner_x = paddle_obj.paddle_rect[0]
    paddle_upper_corner_y = paddle_obj.paddle_rect[1]
    paddle_width = paddle_obj.paddle_rect.width
    ball_upper_corner_x = ball_obj.ball_rect[0]
    ball_upper_corner_y = ball_obj.ball_rect[1]
    ball_height = ball_obj.ball_rect.height
    if paddle_upper_corner_x + paddle_width >= ball_upper_corner_x and \
            ball_upper_corner_x >= paddle_upper_corner_x and \
            (ball_upper_corner_y + ball_height) >= paddle_upper_corner_y and \
            ball_obj.sy > 0:
        # change direction
        ball_obj.sy *= -1
        # increase speed and difficulty
        ball_obj.sx *= 1.02
        ball_obj.sy *= 1.02
        return

    # delete bricks
    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_obj.ball_rect[0] and ball_obj.ball_rect[0] <= (bx + brick_obj.brick_rect.width) and \
            by <= ball_obj.ball_rect[1] and ball_obj.ball_rect[1] <= (by + brick_obj.brick_rect.height):
            delete_brick = b
            # + 2 is a little overlap
            if ball_obj.ball_rect[0] <= bx + 2:
                ball_obj.sx *= -1
            # - 2 is a little overlap
            elif ball_obj.ball_rect[0] >= bx + brick_obj.brick_rect.width - 2:
                ball_obj.sx *= -1
            # + 2 is a little overlap
            if ball_obj.ball_rect[1] <= by + 2:
                ball_obj.sy *= -1
            # - 2 is a little overlap
            elif ball_obj.ball_rect[1] >= by + brick_obj.brick_rect.height - 2:
                ball_obj.sy *= -1
            break
    if delete_brick:
        bricks.remove(delete_brick)

    # ball top limit
    if ball_obj.ball_rect[1] <= 0:
        ball_obj.ball_rect[1] = 0
        ball_obj.sy *= -1
    # ball bottom limit
    if ball_obj.ball_rect[1] >= screen.get_height() - ball_obj.ball_rect.height:
        ball_obj.ball_served = False
        ball_obj.ball_rect.topleft = ball_obj.start_pos
    # ball left limit
    if ball_obj.ball_rect[0] <= 0:
        ball_obj.ball_rect[0] = 0
        ball_obj.sx *= -1
    # ball right limit
    if ball_obj.ball_rect[0] >= screen.get_width() - ball_obj.ball_rect.width:
        ball_obj.ball_rect[0] = screen.get_width() - ball_obj.ball_rect.width
        ball_obj.sx *= -1

    # if paddle outside screen left side
    if paddle_obj.paddle_rect[0] < 0:
        paddle_obj.paddle_rect[0] = 0
    # if paddle outside screen right side
    if paddle_obj.paddle_rect[0] > screen.get_width() - paddle_obj.paddle_rect[2]:
        paddle_obj.paddle_rect[0] = screen.get_width() - paddle_obj.paddle_rect[2]


while not game_over:
    # 50 frames per second
    dt = clock.tick(50)
    screen.fill((0, 0, 0))
    # create bricks on screen
    for b in bricks:
        screen.blit(brick, b)
    # create ball on screen
    screen.blit(ball, ball_obj.ball_rect)
    # create paddle on screen
    screen.blit(paddle, paddle_obj.paddle_rect)
    key_board_mouse_events()
    pygame.display.update()

pygame.quit()
