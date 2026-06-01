from pathlib import Path
from utils.image_manager import load_image, transform_image


class SpriteManager:
    def __init__(self, path):
        self.path = Path(path)

    def load_sprites(self, object_scale) -> dict:
        object_dict = {}
        for cls in self.path.iterdir():
            loaded_image_list = [load_image(path, object_scale) for path in sorted(cls.iterdir())]
            object_dict[cls.name.lower() + "-right"] = loaded_image_list
            object_dict[cls.name.lower() + "-left"] = [transform_image(img) for img in loaded_image_list]

        return object_dict
