from enum import Enum
import random

from pytest import Class
from types import MappingProxyType
from car_game.Settings import Settings
from car_game.Effects import Effect
from car_game.Entities import Collectable, Obstacle, Player_Car
from car_game.Geometry import Box, Coords
from car_game.Score import HighScore
from car_game.assets import ObstacleCarAssets


class State(Enum):
    """Enum representing the different states of the game."""
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4


class Command(Enum):
    """Enum representing the different commands that can be issued in the game."""
    START = 1
    PAUSE = 2
    RESUME = 3
    RESTART = 4
    QUIT = 5

class Control(Enum):
    """Enum representing the different control inputs for the game."""
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

     
    
    
class Game:
    def __init__(self, settings: Settings, rng: random.Random, state: State = State.MENU, store: HighScore = HighScore()):
        self.settings: Settings = settings
        self.player_car: Player_Car = Player_Car(size=settings.car)
        self.player_car.coords = Coords(settings.lane_x_position(1), 0)
        self.effect: Effect = Effect(settings.effect_duration)
        self.obstacle_car_list: list[Obstacle] = []
        self.collectable: Collectable = None
        self.rng: random.Random = rng
        self.state: State = state
        self.score: int = 0
        self.store: HighScore = store
        
    def change_state(self, new_state: State):
        """Change the current state of the game."""
        self.state = new_state
        
    def handle_command(self, command: Command):
        if command == Command.QUIT and (self.state == State.MENU or self.state == State.PAUSED):
            self.quit_game()
        elif command in command_to_state:
            self.change_state(command_to_state[command])
    
    def handle_control(self, control: Control):
        pass
    
    def update(self, score_increment: int = 0):
        """Update the game state, including score and high score."""
        if self.state == State.PLAYING:
            self.score += max(0, score_increment*self.effect.score_multiplier())  # Ensure score doesn't decrease
            self.store.update_high_score(self.score)
            
            if self.effect is not None and isinstance(self.effect, Effect): # Base effect shouldn't be ticked, only derived classes should be ticked
                self.effect.tick()
                
    
    def inside_border(self, coord_offset: Coords) -> bool:
        provisional_player_box = Box(self.player_car.coords.add_coords_new(coord_offset), self.player_car.size)
        if self.settings.Box.intersects(other=provisional_player_box):
            return True
        return False
            
        
    def reset(self):
        """Reset the game to its initial state."""
        self.state = State.MENU
        self.score = 0
        self.player_car: Player_Car = Player_Car(size=self.settings.Settings.car)
        self.player_car.coords = Coords(self.settings.Settings.lane_x_position(1), 0)
        self.obstacle_car_list = []
        self.store.reset()
        
    
        
    def quit_game(self):
        """Handle quitting the game."""
        self.reset()
        SystemExit("Game has been quit.")



command_to_state = MappingProxyType({
    Command.START: State.PLAYING,
    Command.PAUSE: State.PAUSED,
    Command.RESUME: State.PLAYING,
    Command.RESTART: State.MENU,
    Command.QUIT: State.PAUSED

})