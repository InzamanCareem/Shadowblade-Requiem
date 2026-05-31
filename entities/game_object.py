from systems.sprite_manager import SpriteManager


class GameObject:
    def __init__(self, screen, x, y, object_path, object_scale, frame_rate):
        self.screen = screen
        self.x = x
        self.y = y
        self.can_move = (0, 0)
        self.is_falling = False

        self.sprite_manager = SpriteManager(object_path)

        self.object_dict = self.sprite_manager.load_sprites(object_scale)

        self.object_frame = 0
        self.frame_rate = frame_rate

    def move(self, keys):
        pass

    def draw(self, state):
        images = self.object_dict.get(state)

        self.object_frame += self.frame_rate
        if self.object_frame >= len(images):
            self.object_frame = 0

        player = images[int(self.object_frame)]

        self.screen.blit(player, (self.x, self.y))
