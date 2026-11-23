from abc import ABC, abstractmethod


class Effect(ABC):
    ticks_left: int
    
    def __init__(self, duration: int):
        self.ticks_left = duration
    
    
    @property
    def ticks_left(self):
        return self._ticks_left

    @ticks_left.setter
    def ticks_left(self, value: int):
        if value < 0:
            raise ValueError("ticks_left cannot be negative")
        self._ticks_left = value

    
    @abstractmethod
    def apply(self, game_object):
        pass
    
    


class score_multiplier(Effect):
    multiplier: float
    
    def __init__(self, duration: int, multiplier: float):
        super().__init__(duration)
        self.multiplier = multiplier
        
    def apply(self, game_object):
        game_object.score *= self.multiplier
        
class Shield(Effect):
    def __init__(self, duration: int):
        super().__init__(duration)

    def apply(self, game_object):
        pass
    
class Shrink(Effect):
    def __init__(self, duration: int):
        super().__init__(duration)

    def apply(self, game_object):
        pass