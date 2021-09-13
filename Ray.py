from Engine import Math
from pygame import Vector2
from math import pi, cos, sin

class Ray:

    def cast():
        pass

    def __init__(self, pos_ref: Vector2, angle: float):
        self.pos = pos_ref
        self.direction = Math.degree_to_vector2(angle)
