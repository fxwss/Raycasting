from Engine import Math, Object
from pygame import Surface, Vector2, draw
from math import pi, cos, sin


def create_sprite(size: tuple[int]):
    image = Surface(size)
    image.fill((255, 0, 0))
    rect = image.get_rect()
    draw.circle(image, (255, 0, 0), rect.center, 16, 2)
    return image


class Wall(Object):

    def move(self, pos: Vector2):
        self.pos = pos
        self.rect.x = int(pos.x)
        self.rect.y = int(pos.y)

    def __init__(self, pos: Vector2, size=(64, 12)):
        Object.__init__(self, create_sprite(size))
        self.pos = pos
        self.move(self.pos)
