from enum import Enum
import random

from pytest import Class

from car_game.Score import HighScore

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
    def __init__(self, Settings, rng: random.Random, state: State = State.MENU, store: HighScore = HighScore()):
        self.settings = Settings
        self.rng = rng
        self.state = state
        self.store = store
        
    def change_state(self, new_state: State):
        """Change the current state of the game."""
        self.state = new_state
        
    def handle_command(self, command: Command):
        pass
    
    def handle_control(self, control: Control):
        pass
    
    def update(self):
        pass
    
    