import pygame


class InputManager:
    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return -1
