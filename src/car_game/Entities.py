

from dataclasses import dataclass

from car_game.Effects import CollectableType, Effect
from car_game.Geometry import Box, Coords


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
    def __init__(self, size: Size):
        super().__init__(size)
        

class Obstacle(Car):
    def __init__(self, size: Size):
        super().__init__(size)
           
        
        
class Collectable:
    
    def __init__(self, size: Size, CollectableType: CollectableType):
        self.size = size
        self.type = CollectableType
        self.coords = Coords(0, 0)  # Initial position of the collectable
    
    
    @property
    def box(self) -> Box:
        return Box(coords=self.coords, size=self.size)
    
