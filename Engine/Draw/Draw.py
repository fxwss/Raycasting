from pygame import Surface, Vector2, draw, Rect


class Line:
    def __init__(self, start: Vector2, end: Vector2, color=(255, 0, 0)):
        self.start = start
        self.end = end
        self.color = color


class Rectangle:

    def to_pg_rect(self):
        w = self.end.x - self.start.x
        h = self.end.y - self.start.y
        return Rect(int(self.start.x), int(self.start.y), int(w), int(h))

    def __init__(self, start: Vector2, end: Vector2, color=(255, 0, 0)):
        self.start = start
        self.end = end
        self.color = color


class Tool:

    def rectangle(self, rect: Rectangle):
        return draw.rect(self.canvas, rect.color, rect.to_pg_rect())

    def line(start, end, color):
        pass

    def __init__(self, canvas: Surface):
        self.canvas = canvas
