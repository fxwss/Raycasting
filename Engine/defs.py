from dataclasses import dataclass

from Engine import Game, Canvas, Input, Events, Time


class ToolCollection:
    def __init__(self, Game: Game, Canvas: Canvas, Input: Input, Events: Events, Time: Time):
        self.Game = Game
        self.Canvas = Canvas
        self.Input = Input
        self.Events = Events
        self.Time = Time
