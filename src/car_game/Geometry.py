
from __future__ import annotations

from dataclasses import dataclass

from car_game.Entities import Size

""" A rectangular area in the game world. has a position (x, y) and a size (width, height). """
@dataclass(frozen=True)
class Box:
    coords: Coords
    size: Size

    @property
    def left(self) -> int:
        return self.coords.x

    @property
    def right(self) -> int:
        return self.coords.x + self.size.width

    @property
    def top(self) -> int:
        return self.coords.y

    @property
    def bottom(self) -> int:
        return self.coords.y + self.size.height
    
    @property
    def center(self) -> Coords:
        return Coords(self.coords.x + self.size.width // 2, self.coords.y + self.size.height // 2)
    

    def intersects(self, other: "Box") -> bool:
        return not (self.right <= other.left or self.left >= other.right or
                    self.bottom <= other.top or self.top >= other.bottom)
        
        
class Coords:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y