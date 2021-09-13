from Engine.Time.Time import Time
from typing import Callable
import pygame.event


class Events:

    def on(self, event, callback: Callable):
        if not event in self.on_events:
            self.on_events[event] = set()
        self.on_events[event].add(callback)

    def run(self):
        try:
            self.loop()
        except Exception as e:
            print(f'Error in Events: {e}')

    def loop(self):
        while 1:
            self.Time.tick(31)
            for event in pygame.event.get():
                if event.type in self.on_events:
                    for fn in self.on_events[event.type]:
                        fn(event)

    def __init__(self):
        self.on_events: dict[int, set[Callable]] = dict()
        self.Time = Time()
