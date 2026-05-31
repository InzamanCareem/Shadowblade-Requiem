from level.background import Background


class LevelManager:
    def __init__(self):
        self.current_level = None

    def load_level(self, level_number):
        if level_number == 1:
            self.current_level = Level1()

    def draw(self, screen):
        self.current_level.draw(screen)


class Level1:
    def __init__(self):
        self.background = Background(background_path="Assets/Tileset/background.png", position=(0, 0), size=(1024, 640))

    def draw(self, screen):
        self.background.draw(screen)
