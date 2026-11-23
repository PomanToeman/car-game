from enum import Enum
from types import MappingProxyType


class CollectableType(Enum):
    """Enum for different types of collectables."""
    SCORE_MULTIPLIER = 1
    SHIELD = 2
    SHRINK = 3
    SUPER_COIN = 4
    

class Effect:
    """Base class for effects. It also acts as the default state where there is no effect active."""
    ticks_left: int
    
    def __init__(self, duration: int):
        self.ticks_left = duration

    def tick(self):
        self.ticks_left = max(0, self.ticks_left - 1)
    
    @property
    def expired(self) -> bool:
        return self.ticks_left <= 0
    
    # ----- HOOKS --------
    
    
    def score_multiplier(self) -> float:
        """Returns the score multiplier for this effect. Default is 1.0 (no multiplier)."""
        return 1.0
    
    def absorb_hit(self) -> bool:
        """Sees whether the player is shielded from obstacles. Default is False (no shield)."""
        return False
    
    def shrink_factor(self) -> float:
        """Returns the shrink factor for the obstacles. Default is 1.0 (no shrink)."""
        return 1.0
    
    def bonus_points(self) -> int:
        """Returns the bonus points for this effect. Default is 0 (no bonus)."""
        return 0
    
    
    def effect_name(self) -> str:
        """Returns the name of the effect. Default is 'No effect'."""
        return "No effect"
  





class score_multiplier(Effect):
    multiplier: float
    
    def __init__(self, duration: int, multiplier: float = 2.0):
        super().__init__(duration)
        self.multiplier = multiplier
        
    def score_multiplier(self) -> float:
        return self.multiplier
    
    def effect_name(self) -> str:
        return f"Score multiplier is active: {self.multiplier}x"
        
   
        
class Shield(Effect):
    def __init__(self, duration: int, shield_capacity: int = 10):
        super().__init__(duration)
        self.shield_strength = shield_capacity
        self.shield_being_used = False

    def absorb_hit(self) -> bool:
        self.ticks_left = self.shield_strength # duration switches to shield capacity when the shield absorbs an initial hit
        self.shield_being_used = True
        return True

    
    def effect_name(self) -> str:
        if self.shield_being_used:
            return "Shield is being used!"
        return "Shield active"

class Shrink(Effect):
    def __init__(self, duration: int, shrink_factor: float = 0.5):
        super().__init__(duration)
        self.shrink_factor = shrink_factor

    def shrink_factor(self) -> float:
        return self.shrink_factor
    
    def effect_name(self) -> str:
        return f"Shrink active: Obstacles are {self.shrink_factor}x smaller"


class SuperCoin(Effect):
    def __init__(self, duration: int, bonus_points: int = 50):
        super().__init__(duration)
        self.bonus_collected = False
        self.bonus_points_value = bonus_points

    def bonus_points(self) -> int:
        points = 0 # would be 0 if the bonus has already been collected
        if not self.bonus_collected:
            self.bonus_collected = True
            points = self.bonus_points_value
        return points
    
    def effect_name(self) -> str:
        return f"Super Coin active: You get {self.bonus_points_value} bonus points!"


# Global mapping of CollectableType to their corresponding Effect classes, avoid accidental modification of the mapping
CollectableTypeMapping = MappingProxyType({
    CollectableType.SCORE_MULTIPLIER: score_multiplier,
    CollectableType.SHIELD: Shield,
    CollectableType.SHRINK: Shrink,
    CollectableType.SUPER_COIN: SuperCoin
})