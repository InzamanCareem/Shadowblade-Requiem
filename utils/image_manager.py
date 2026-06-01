from typing import overload
import pygame


@overload
def load_image(path: str, size: tuple[int, int]) -> pygame.Surface:
    ...


@overload
def load_image(path: str, scale: float) -> pygame.Surface:
    ...


def load_image(path: str, size_or_scale):
    image = pygame.image.load(path).convert_alpha()

    if isinstance(size_or_scale, tuple):
        return pygame.transform.scale(image, size_or_scale)
    else:
        return pygame.transform.rotozoom(image, 0, size_or_scale)


def transform_image(image: pygame.Surface) -> pygame.Surface:
    return pygame.transform.flip(image, 1, 0)
