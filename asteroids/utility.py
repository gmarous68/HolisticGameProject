from pygame import Vector2
from pygame.transform import rotozoom


# if ship or asteroid going of edge of screen - coming back on the other edge
def wrap_position(pos, screen):
    x, y = pos
    w, h = screen.get_size()
    return Vector2(x % w, y % h)


def blit_rotated(pos, forward, image, screen):
    angle = forward.angle_to(Vector2(0, -1))
    rotated_surface = rotozoom(image, angle, 1.0)
    rotated_surface_size = Vector2(rotated_surface.get_size())
    blit_pos = pos - rotated_surface_size // 2
    screen.blit(rotated_surface, blit_pos)
