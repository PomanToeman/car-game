
from dataclasses import dataclass

from car_game.Entities import Size
from car_game.Geometry import Box, Coords


@dataclass(frozen=True)
class Settings:
    screen_size: Size = Size(width=800, height=600)
    render_fps: int = 60
    tick_rate: int = 60
    effect_seconds: float = 6.0
    collectable_duration: float = 4.0 
    collectable_cooldown: tuple[float, float] = (5.1, 6.7)
    lane_width: int = 60
    car: Size = Size(50, 90)
    collectable: Size = Size(50, 50)
    obstacle: Size = Size(50, 90)
    lane_width: int = 100
    lane_count: int = 5
    cooldown_time: int = 1000  # in milliseconds
    effect_duration: int = 300  # in milliseconds
    obstacle_count: int = 6
    
    @property
    def effect_ticks(self) -> int:
        return round(self.effect_seconds * self.tick_rate)
    
    @property
    def min_obstacle_speed(self) -> int:
        return round(self.obstacle.height / 10)

    @property
    def max_obstacle_speed(self) -> int:
        return round(self.obstacle.height / 8)
    
    @property
    def screen_Box(self) -> Box:
        return Box(coords=Coords(0, 0), size=self.screen_size)
    
   
    def lane_x_position(self, lane_index: int = 1) -> int:
        if lane_index < 0 or lane_index >= self.lane_count:
            raise ValueError(f"Lane index must be between 0 and {self.lane_count - 1}")
        return (self.screen_size.width - self.lane_width * self.lane_count) // 2 + lane_index * self.lane_width