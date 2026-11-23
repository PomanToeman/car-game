
from enum import Enum
import pygame

def MissingAssetError(message: str):
    """Custom exception for missing assets."""
    return Exception(message)

def load_image(path: str) -> pygame.Surface:
    """Load an image from the given path and return a Pygame Surface."""
    try:
        image = pygame.image.load(path)
        return image.convert_alpha()  # Convert for better performance with transparency
    except pygame.error as e:
        print(f"Unable to load image at {path}: {e}")
        raise SystemExit(e)
    
def load_image_assets(asset_enum: Enum) -> dict:
    """Load images for all assets defined in the given Enum and return a dictionary mapping asset names to Pygame Surfaces."""
    assets = {}
    assets_missing = [] # this list will hold the names of any assets that fail to load
    for asset in asset_enum:
        try:
            assets[asset.name] = load_image(asset.value)
        except SystemExit:
            print(f"Failed to load image for asset: {asset.name}")
            assets_missing.append(asset.name)
    if assets_missing:
        raise MissingAssetError(f"Missing assets for {asset_enum.__name__}: {', '.join(assets_missing)}")
    return assets      

class PlayerCarAssets(Enum):
    """Enum for player car assets."""
    CAR_1 = "assets/car_1.png"
    CAR_2 = "assets/car_2.png"
    CAR_3 = "assets/car_3.png"
    CAR_4 = "assets/car_4.png"
    CAR_5 = "assets/car_5.png"
    CAR_6 = "assets/car_6.png"
    
class ObstacleCarAssets(Enum):
    """Enum for obstacle assets."""
    OBSTACLE_1 = "assets/car_ob1.png"
    OBSTACLE_2 = "assets/car_ob2.png"
    OBSTACLE_3 = "assets/car_ob3.png"
    OBSTACLE_4 = "assets/car_ob4.png"
    OBSTACLE_5 = "assets/car_ob5.png"
    OBSTACLE_6 = "assets/car_ob6.png"
    
class CollectableAssets(Enum):
    """Enum for collectable assets."""
    SHIELD = "assets/shield.png"
    SHRINK = "assets/shrink.png"
    TANK = "assets/tank.png"
    COIN = "assets/coin.png"