from utils.image_manager import load_image

import re
from pathlib import Path


class Tile:
    def __init__(self, tile_set_path, size):
        self.tile_set_path = Path(tile_set_path)
        self.size = size

    def load_tile_set(self) -> dict:
        tile_set_dict = {}
        for tile in sorted(self.tile_set_path.iterdir()):
            tile_number = int(re.search(r"\((\d+)\)", tile.name).group(1))
            tile_set_dict[tile_number] = load_image(tile, self.size)

        return tile_set_dict

    def draw(self, screen, tile_set_dict, tile_map):
        for row_index, row in enumerate(tile_map):
            for col_index, tile_id in enumerate(row):
                if tile_id != 0:
                    tile_image = tile_set_dict.get(tile_id)

                    x = col_index * self.size[0]
                    y = row_index * self.size[0]

                    screen.blit(tile_image, (x, y))
