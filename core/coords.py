from typing import NamedTuple

class Coords(NamedTuple):
    x: int
    y: int

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def offset(self, dx=0, dy=0):
        return Coords(self.x + dx, self.y + dy)
