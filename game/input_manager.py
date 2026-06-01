import pygame


class InputManager:
    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return -1

    def get_pressed_keys(self, keys):
        direction = (0, 0)

        if keys[pygame.K_RIGHT]:
            direction = (1, 0)
        if keys[pygame.K_LEFT]:
            direction = (-1, 0)
        if keys[pygame.K_SPACE]:
            direction = (0, -1)

        return direction
