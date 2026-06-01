from entities.game_object import GameObject

from typing import override


class Player(GameObject):
    def __init__(self, screen, x, y, object_path, object_scale, frame_rate, move_speed, jump_speed):
        super().__init__(screen, x, y, object_path, object_scale, frame_rate, move_speed)
        self.on_ground = False
        self.velocity_y = 0
        self.jump_speed = -jump_speed

    @override
    def move(self, direction):
        self.direction = direction

        if self.can_move_right and self.looking == 1:
            self.velocity_x = self.direction[0] * self.move_speed
            self.x += self.velocity_x

        if self.can_move_left and self.looking == -1:
            self.velocity_x = self.direction[0] * self.move_speed
            self.x += self.velocity_x

        if direction == (0, -1) and self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

        if not self.on_ground:
            self.velocity_y = self.physics_manager.apply_gravity(self.velocity_y, self.frame_rate)
            self.y += self.velocity_y

        # Ground collision
        if self.y >= 400:
            self.y = 400
            self.velocity_y = 0
            self.on_ground = True

    def get_state(self):
        if self.direction == (0, 0):
            return "idle-right"
        elif self.direction == (1, 0):
            self.looking = 1
            return "run-right"
        elif self.direction == (-1, 0):
            self.looking = -1
            return "run-left"
        elif self.direction == (0, -1):
            return "jump-right"
        else:
            return "idle-right"
