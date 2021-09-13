from typing import Callable

from pygame.key import key_code
from Engine.Events.Events import Events

from pygame import KEYDOWN, KEYUP
from pygame.event import Event


class Input:

    def is_pressed(self, key_code: int):
        if key_code in self.pressed:
            return self.pressed[key_code]
        return False

    def on(self, key_code: int, callback: Callable):
        if not key_code in self.on_press:
            self.on_press[key_code] = set()
        self.on_press[key_code].add(callback)

    def on_keydown(self, event: Event):
        self.pressed[event.key] = True

        if event.key in self.on_press:
            for fn in self.on_press[event.key]:
                fn(event)

    def on_keyup(self, event: Event):
        self.pressed[event.key] = False

    def run(self):
        self.Events.on(KEYDOWN, self.on_keydown)
        self.Events.on(KEYUP, self.on_keyup)

    def __init__(self, Events: Events):
        self.Events = Events
        self.pressed = {}
        self.on_press = {}
