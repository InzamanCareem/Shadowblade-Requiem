import pygame

from game.input_manager import InputManager
from level.level_manager import LevelManager
from entities.player import Player


class GameManager:
    FRAME_RATE = 60

    def __init__(self, title, width, height):
        pygame.init()

        self.input_manager = InputManager()
        self.level_manager = LevelManager()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(self.screen, 100, 350, "Assets/Ninja", 1 / 4, 0.5, 10, 50)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(GameManager.FRAME_RATE)

        pygame.quit()

    def handle_events(self):
        events = pygame.event.get()

        event_success = self.input_manager.update(events)

        keys = pygame.key.get_pressed()

        player_direction = self.input_manager.get_pressed_keys(keys)
        self.player.move(player_direction)

        if event_success == -1:
            self.running = False

    def update(self):
        self.level_manager.load_level(1)

        tile_map = self.level_manager.current_level.get_tile_map()

        self.player.update(tile_map)

    def draw(self):
        self.level_manager.draw(self.screen)

        self.player.draw()

        pygame.display.update()
