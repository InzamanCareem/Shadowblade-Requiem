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

        self.player = Player(self.screen, 100, 500, "Assets/Ninja", 1 / 4, 0.5)

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

        direction = self.input_manager.get_pressed_keys(keys)
        self.player.move(direction)

        if event_success == -1:
            self.running = False

    def update(self):
        self.level_manager.load_level(1)

    def draw(self):
        self.level_manager.draw(self.screen)

        self.player.draw(state="idle")

        pygame.display.update()
