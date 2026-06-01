from systems.sprite_manager import SpriteManager


class GameObject:
    def __init__(self, screen, x, y, object_path, object_scale, frame_rate, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.is_falling = False

        self.sprite_manager = SpriteManager(object_path)

        self.object_dict = self.sprite_manager.load_sprites(object_scale)

        self.object_frame = 0
        self.frame_rate = frame_rate

        self.speed = speed

        self.direction = (0, 0)

    def move(self, direction):
        self.direction = direction
        self.x += direction[0] * self.speed
        self.y += direction[1] * self.speed

    def get_state(self):
        if self.direction == (0, 0):
            return "idle-right"
        elif self.direction == (1, 0):
            return "run-right"
        elif self.direction == (-1, 0):
            return "run-left"

    def draw(self):
        state = self.get_state()

        images = self.object_dict.get(state)

        self.object_frame += self.frame_rate
        if self.object_frame >= len(images):
            self.object_frame = 0

        player = images[int(self.object_frame)]

        self.screen.blit(player, (self.x, self.y))
