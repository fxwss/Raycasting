from typing import Callable, Union
from pygame import Rect, transform
from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface


class Object(Sprite):

    def rotate(self, angle: float):
        self.rotation += angle
        if img := transform.rotate(self.original_image, self.rotation):
            self.image = img
            self.rect = self.image.get_rect(center=self.rect.center)
            return True
        return False

    def move(self, v):
        self.pos.x += v.x
        self.pos.y += v.y
        self.rect.x = int(self.pos.x - self.rect.width / 2)
        self.rect.y = int(self.pos.y - self.rect.height / 2)

    def __init__(self, image: Union[Surface, None] = None):

        self.has_sprite = image != None
        if not self.has_sprite:
            image = Surface((32, 32))

        self.pos: Vector2 = Vector2(0.0, 0.0)
        self.original_image = image.copy()
        self.image = image.copy()
        self.rect = self.image.get_rect()
        self.rotation = 0.0
        self.rotation_speed = 180

        Sprite.__init__(self)
        self.move(self.pos)
