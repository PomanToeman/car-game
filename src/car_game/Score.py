
from pytest import Class


class HighScore:
    """Class to manage the high score of the game. Saves the high score to a file and loads it when the game starts."""
    def __init__(self, score: int = 0, store_path: str = "highscore.txt"):
        self.load_high_score()
        self.update_high_score(score)
        self.store_path = store_path
        
        
    def load_high_score(self):
        try:
            with open(self.store_path, "r") as file:
                self.score = int(file.read().strip())
        except FileNotFoundError:
            self.score = 0
            self.save_high_score()
        except ValueError:
            self.score = 0
            self.save_high_score()
            
    def save_high_score(self):
        with open(self.store_path, "w") as file:
            file.write(str(self.score))
            
    def update_high_score(self, new_score: int):
        if new_score > self.score:
            self.score = new_score
            self.save_high_score()
    
    @score.setter
    def score(self, value: int):
        if value < 0:
            raise ValueError("Score cannot be negative")
        self.update_high_score(value)
            
    