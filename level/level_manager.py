from level.background import Background
from level.tile import Tile


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

        self.tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 14, 15, 16, 0, 0, 0, 0, 0, 0, 0],
            [15, 15, 15, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 15, 15, 16, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

        self.tiles = Tile(tile_set_path="Assets/Tileset/Tiles", size=(64, 64))

        self.tile_set_dict = self.tiles.load_tile_set()

    def get_tile_map(self):
        return self.tile_map

    def draw(self, screen):
        self.background.draw(screen)

        self.tiles.draw(screen, self.tile_set_dict, self.get_tile_map())
