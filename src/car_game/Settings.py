
from dataclasses import dataclass

from car_game.Entities import Size
from car_game.Geometry import Box, Coords


@dataclass(frozen=True)
class Settings:
    screen_size: Size = Size(width=800, height=600)
    fps: int = 60
    lanes: int = 4
    car: Size = Size(50, 90)
    collectable: Size = Size(50, 50)
    obstacle: Size = Size(50, 90)
    lane_width: int = 100
    lane_count: int = 4
    cooldown_time: int = 1000  # in milliseconds
    effect_duration: int = 300  # in milliseconds
    obstacle_count: int = 6
    
    @property
    def min_obstacle_speed(self) -> int:
        return round(self.obstacle.height / 10)

    @property
    def max_obstacle_speed(self) -> int:
        return round(self.obstacle.height / 8)
    
    @property
    def screen_Box(self) -> "Box":
        return Box(coords=Coords(0, 0), size=self.screen_size)
    
    @property
    def lane_x_position(self, lane_index: int) -> int:
        if lane_index < 0 or lane_index >= self.lane_count:
            raise ValueError(f"Lane index must be between 0 and {self.lane_count - 1}")
        return (self.screen_size.width - self.lane_width * self.lane_count) // 2 + lane_index * self.lane_width