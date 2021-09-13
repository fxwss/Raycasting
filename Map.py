from Engine.Object.Object import Object
import Engine
from pygame import Surface


class Map(Engine.Object):

    def __init__(self, size):
        self.Surface = Surface(size)
        Object.__init__(self)
        self.has_sprite = False
