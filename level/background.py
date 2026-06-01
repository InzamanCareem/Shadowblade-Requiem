from utils.image_manager import load_image


class Background:
    def __init__(self, background_path, position, size):
        self.position = position
        self.background_image = load_image(background_path, size)

    def draw(self, screen):
        screen.blit(self.background_image, self.position)
