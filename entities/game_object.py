from systems.sprite_manager import SpriteManager
from systems.physics_manager import PhysicsManager


class GameObject:
    def __init__(self, screen, x, y, object_path, object_scale, frame_rate, move_speed, jump_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.on_ground = True
        self.velocity_y = 0
        self.looking = 1

        self.sprite_manager = SpriteManager(object_path)

        self.object_dict = self.sprite_manager.load_sprites(object_scale)

        self.object_frame = 0
        self.frame_rate = frame_rate

        self.move_speed = move_speed

        self.direction = (0, 0)

        self.physics_manager = PhysicsManager()

        self.jump_speed = -jump_speed

    def move(self, direction):
        self.direction = direction
        self.x += self.direction[0] * self.move_speed

        if direction == (0, -1) and self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

        if not self.on_ground:
            self.velocity_y = self.physics_manager.apply_gravity(self.velocity_y, self.frame_rate)
            self.y += self.velocity_y

        # Ground collision
        if self.y >= 400:
            self.y = 400
            self.velocity_y = 0
            self.on_ground = True

    def get_state(self):
        if self.direction == (0, 0):
            return "idle-right"
        elif self.direction == (1, 0):
            self.looking = 1
            return "run-right"
        elif self.direction == (-1, 0):
            self.looking = -1
            return "run-left"
        elif self.direction == (0, -1):
            return "jump-right"
        else:
            return "attack-right"

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
