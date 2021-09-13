from pygame import Surface, transform


class Transform:

    def scale(surface: Surface, percentage: float):
        sizes = surface.get_size()
        w = int(sizes[0] * percentage)
        h = int(sizes[1] * percentage)

        return transform.scale(surface, (w, h))
