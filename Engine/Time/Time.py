from pygame.time import Clock


class Time:

    @property
    def delta_time(self):
        return self.__clock.get_time() / 1000

    @property
    def fps(self):
        return self.__clock.get_fps()

    def tick(self, framerate: int):
        return self.__clock.tick(framerate)

    def __init__(self):
        self.__clock = Clock()
