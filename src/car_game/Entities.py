

from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int
    
    

class Car:
    def __init__(self, size: Size):
        self.size = size
        self.position = (0, 0)  # Initial position of the player car

class Player_Car(Car):
    def __init__(self, size: Size):
        super().__init__(size)
        

class Obstacle(Car):
    def __init__(self, size: Size):
        super().__init__(size)
           
        
        
class Collectable:
    
    def __init__(self, size: Size):
        self.size = size
        self.position = (0, 0)  # Initial position of the collectable
        