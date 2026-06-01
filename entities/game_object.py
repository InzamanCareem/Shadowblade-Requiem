from systems.sprite_manager import SpriteManager
from systems.physics_manager import PhysicsManager

from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, screen, x, y, object_path, object_scale, frame_rate, move_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.looking = 1

        self.sprite_manager = SpriteManager(object_path)
        self.object_dict = self.sprite_manager.load_sprites(object_scale)

        self.object_frame = 0
        self.frame_rate = frame_rate
        self.move_speed = move_speed

        self.direction = (0, 0)
        self.physics_manager = PhysicsManager()

    def move(self, direction):
        self.direction = direction
        self.x += self.direction[0] * self.move_speed

    @abstractmethod
    def get_state(self):
        pass

    def draw(self):
        state = self.get_state()

        if self.looking == 1:
            state = state.split("-")[0] + "-right"
        else:
            state = state.split("-")[0] + "-left"

        images = self.object_dict.get(state)

        self.object_frame += self.frame_rate
        if self.object_frame >= len(images):
            self.object_frame = 0

        game_object = images[int(self.object_frame)]

        self.screen.blit(game_object, (self.x, self.y))
