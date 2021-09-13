from math import pi, cos, sin
from pygame import Vector2


class Math:

    def degree_to_radian(angle: float):
        return angle * (pi / 180)

    def degree_to_vector2(angle: float):
        rad = Math.degree_to_radian(angle)

        return Vector2(
            cos(rad),
            sin(rad)
        )
