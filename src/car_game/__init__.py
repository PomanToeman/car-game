from random import Random
import random
from types import MappingProxyType

import pygame

from car_game.Settings import Settings
from car_game.Game import Game
from car_game.colours import Theme
from car_game.render import Renderer

input_to_command_key = MappingProxyType({
    
    
})


def main() -> None:
    pygame.init()

    settings: Settings = Settings()
    step_ms: float = 1000 / settings.tick_rate           # e.g. 16.67 ms per logic tick
    accumulator: float = 0.0
    running: bool = True
    game: Game = Game(settings, random.Random())
    screen = pygame.display.set_mode((settings.screen_size.width, settings.screen_size.height))
    pygame.display.set_caption("...")
    clock: pygame.Clock = pygame.Clock()
    renderer: Renderer = Renderer(screen=screen, settings=settings, theme=Theme())
    
    while running:
        frame_ms = clock.tick(settings.render_fps)   # returns ms since the last call
        accumulator += min(frame_ms, 250)            # cap, so a stall can't cause a huge catch-up

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        while accumulator >= step_ms:
            game.update()                            # exactly one logic tick
            accumulator -= step_ms

        renderer.draw(game)
        pygame.display.flip()

if __name__ == "__main__":
    main()


