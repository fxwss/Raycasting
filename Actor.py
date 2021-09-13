from Ray import Ray
from Engine import Object, ToolCollection
from pygame import Surface, K_d, K_a, K_s, K_w, K_LSHIFT, Vector2, draw


def create_sprite():
    image = Surface((32, 32))
    rect = image.get_rect()
    draw.circle(image, (255, 0, 0), rect.center, 16, 2)
    draw.line(image, (0, 255, 0), rect.center, rect.midtop, 2)
    return image


class Actor(Object):

    def update(self, Tools: ToolCollection):

        self.speed = 100
        move = Vector2(0.0, 0.0)

        if Tools.Input.is_pressed(K_LSHIFT):
            self.speed *= 1.5

        if Tools.Input.is_pressed(K_d):
            self.rotate(-self.rotation_speed * Tools.Time.delta_time)

        if Tools.Input.is_pressed(K_a):
            self.rotate(self.rotation_speed * Tools.Time.delta_time)

        if Tools.Input.is_pressed(K_w):
            move.y = -1

        if Tools.Input.is_pressed(K_s):
            move.y = 1

        if move.length() > 0:
            move = move.rotate(-self.rotation).normalize()
            self.move(move * self.speed * Tools.Time.delta_time)

    def __init__(self):
        Object.__init__(self, create_sprite())
        self.speed = 100.0
        self.rotation_speed = 270
        self.rays = set(Ray(self.pos, -angle) for angle in range(45, 135))
