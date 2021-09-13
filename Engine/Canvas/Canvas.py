from Engine.Time.Time import Time
from Engine.Draw.Draw import Tool as DrawTool
from pygame.sprite import RenderUpdates as Group
from pygame import Surface

import pygame.display


class Canvas(Surface):

    def __logic(self):
        self.Time.tick(301)
        self.Surface.fill((0, 0, 0))
        pygame.display.update(self.Group.draw(self.Surface))

    def flip(self):
        pygame.display.flip()

    def update(self, x):
        pygame.display.update(x)

    def loop(self):
        while 1:
            self.__logic()

    def run(self):
        try:
            self.loop()
        except Exception as e:
            print(f'Error in canvas: {e}')

    def override_draw_logic(self, fn):
        self.__logic = lambda: fn(self)

    def __init__(self, draw_group: Group, resolution=(0, 0)):
        # Private
        self.Surface = pygame.display.set_mode(resolution)

        # Public
        self.rect = self.Surface.get_rect()
        self.Group = draw_group
        self.Time = Time()
        self.Draw = DrawTool(self.Surface)

        Surface.__init__(self, self.Surface.get_size())
