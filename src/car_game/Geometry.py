
from dataclasses import dataclass

from car_game.Entities import Size


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    size: Size

    @property
    def left(self) -> int:
        return self.x

    @property
    def right(self) -> int:
        return self.x + self.size.width

    @property
    def top(self) -> int:
        return self.y

    @property
    def bottom(self) -> int:
        return self.y + self.size.height

    def intersects(self, other: "Box") -> bool:
        return not (self.right <= other.left or self.left >= other.right or
                    self.bottom <= other.top or self.top >= other.bottom)