

from dataclasses import dataclass

from car_game.Effects import CollectableType, Effect
from car_game.Geometry import Box, Coords
from car_game.assets import ObstacleCarAssets, PlayerCarAssets


@dataclass(frozen=True)
class Size:
    width: int
    height: int
    
    

class Car:
    def __init__(self, size: Size):
        self.size = size
        self.coords = Coords(0, 0)  # Initial position of the car
        
        
    @property
    def box(self) -> Box:
        return Box(coords=self.coords, size=self.size)

class Player_Car(Car):
    def __init__(self, size: Size, asset_key: PlayerCarAssets = PlayerCarAssets.CAR_1):
        super().__init__(size)
        self.asset_key: PlayerCarAssets = asset_key
        

class Obstacle(Car):
    def __init__(self, size: Size, asset_key: ObstacleCarAssets = ObstacleCarAssets.OBSTACLE_1):
        super().__init__(size)
        self.asset_key: ObstacleCarAssets = asset_key
           
        
        
class Collectable:
    
    def __init__(self, size: Size, collectable_type: CollectableType, coords: Coords = Coords(0, 0)):
        self.size: Size = size
        self.type: CollectableType = collectable_type
        self.coords: Coords = Coords(0, 0)  # Initial position of the collectable
    
    
    @property
    def box(self) -> Box:
        return Box(coords=self.coords, size=self.size)
    
