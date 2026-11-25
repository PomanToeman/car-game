from types import MappingProxyType

import pygame

from car_game.Settings import Settings

from car_game.Effects import CollectableType
from car_game.Game import Game
from car_game.Geometry import Box
from car_game.colours import RGB, Palette, Theme
from car_game.assets import PlayerCarAssets, ObstacleCarAssets, CollectableAssets, load_image_assets

collectable_type_to_asset_key = MappingProxyType({
    CollectableType.SCORE_MULTIPLIER:  CollectableAssets.TANK,
    CollectableType.SHIELD: CollectableAssets.SHIELD,
    CollectableType.SHRINK: CollectableAssets.SHRINK,
    CollectableType.SUPER_COIN: CollectableAssets.COIN
})

class Renderer:
    def __init__(self, screen: pygame.Surface, settings: Settings,
                 theme: Theme) -> None:
        self.player_car_assets: dict = load_image_assets(PlayerCarAssets)
        self.obstacle_car_assets: dict = load_image_assets(ObstacleCarAssets)
        self.collectable_assets: dict = load_image_assets(CollectableAssets)
        self.settings: Settings = settings
        self.theme: Theme = theme
        self.screen: pygame.Surface = screen
        
    
        

    def draw(self, game: Game) -> None:
        self.screen.fill(self.theme.background)
        self.draw_road()
        self.draw_collectable(game)
        self.draw_obstacles(game)
        self.draw_player(game)
        
        
    
    def draw_road(self) -> None:
        lane_count: int = self.settings.lane_count
        lane_width: int = self.settings.lane_width
        screen_height = self.screen.get_height()
        for i in range(0, lane_count-1):
            x = self.settings.lane_x_position(i)
            pygame.draw.line(self.screen, self.theme.road, (x, 0),
                             (x, screen_height), lane_width)
            # lines
            pygame.draw.line(self.screen, self.theme.lane_line, (x - (lane_width)//2, 0),
                                         (x - (lane_width)//2, screen_height), lane_width//5)
            pygame.draw.line(self.screen, self.theme.lane_line, (x + (lane_width)//2, 0),
                                         (x + (lane_width)//2, screen_height), lane_width//5)
            
    
    def draw_rectangle(self, box: Box, rect_image: pygame.Surface | None = None, colour: RGB = Palette.GREY) -> None:
        """Draw a coloured rectangle or an image fitted to the rectangle."""
        rectangle = pygame.Rect(box.coords.x, box.coords.y, box.size.width, box.size.height)
        if rect_image is None:
            pygame.draw.rect(self.screen, colour, rectangle)
            return
        resized_image = pygame.transform.smoothscale(rect_image, rectangle.size)
        self.screen.blit(resized_image, rectangle)
        
     
    def draw_player(self, game: Game) -> None:
        rect_image = self.player_car_assets[game.player_car.asset_key.name]
        self.draw_rectangle(game.player_car.box, rect_image)

    def draw_collectable(self, game: Game) -> None:
        if game.collectable is None:
            return
        asset_key = collectable_type_to_asset_key[game.collectable.type]
        rect_image = self.collectable_assets[asset_key.name]
        self.draw_rectangle(game.collectable.box, rect_image)
        
    
    def draw_obstacles(self, game: Game) -> None:
        for obstacle in game.obstacle_car_list:
            rect_image = self.obstacle_car_assets[obstacle.asset_key.name]
            self.draw_rectangle(obstacle.box, rect_image)
    
    
            
    
    
    
        
        
    
    
