from pathlib import Path
from utils.image_loader import load_image


class SpriteManager:
    def __init__(self, path):
        self.path = Path(path)

    def load_sprites(self, object_scale) -> dict:
        object_dict = {}
        for cls in self.path.iterdir():
            object_dict[cls.name.lower()] = [load_image(path, object_scale) for path in sorted(cls.iterdir())]

        return object_dict
