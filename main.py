from Engine.Draw import Line, Rectangle
import Engine
import pygame

from pygame.math import Vector2

from Actor import Actor
from Wall import Wall
from Map import Map

image = pygame.Surface((32, 32))
image.fill((255, 0, 0))


class Colors:
    FLOOR = (82, 82, 82)


world_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def create_draw_fun(Game: Engine.Game):

    width, height = 1024, 1024
    player = Game.get_object_by_type(Actor)
    walls = Game.get_object_by_type(Wall)
    map = Map((width, height))

    Game.add(map)

    def draw(Canvas: Engine.Canvas):
        Canvas.Time.tick(999)

        # Sky
        Canvas.fill((255, 255, 255))

        # Floor
        draw_floor(Game)

        column = 0
        while column < width:
            column += 1

        # Draw map
        map.Surface.fill((0, 0, 0))
        Canvas.Group.draw(map.Surface)
        map_surface = Engine.Transform.scale(map.Surface, 0.2)
        map_size = map_surface.get_size()
        blit_pos = (width - map_size[0] - 5, height - map_size[1] - 5)
        Canvas.Surface.blit(map_surface, blit_pos)

        Canvas.flip()

    return draw


def draw_floor(Game: Engine.Game):
    start = Vector2(Game.Canvas.rect.midleft)
    end = Vector2(Game.Canvas.rect.bottomright)
    rect = Rectangle(start, end, Colors.FLOOR)
    Game.Canvas.Draw.rectangle(rect)


def create_walls(Game: Engine.Game):
    resolution = Vector2(1024, 1024)

    rows = len(world_map)
    columns = len(world_map[0])

    width = resolution.x / columns
    height = resolution.y / rows

    h = 0
    for row in range(rows):
        for column in range(columns):
            if world_map[row][column] == 0:
                continue
            pos = Vector2(width * column, h)
            wall = Wall(pos, (width, height))
            Game.add(wall)
        h += height


def main():
    game = Engine.Game("Raycasting 🐍", (800, 600))

    player = Actor()
    player.move(Vector2(*game.Canvas.rect.center))
    game.add(player)

    create_walls(game)

    game.Canvas.override_draw_logic(create_draw_fun(game))

    game.start()


if __name__ == '__main__':
    main()
