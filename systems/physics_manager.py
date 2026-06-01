class PhysicsManager:
    def __init__(self):
        self.gravity = 10

    def apply_gravity(self, velocity_y, delta_time):
        return velocity_y + self.gravity * delta_time

    def detect_collisions(self, entity, tile_map):
        tile_x = int(entity.x / 64)
        tile_y = int(entity.y / 64)

        for y in range(tile_y, tile_y + 2):

            # check the right side
            for x in range(tile_x, tile_x + 1):
                if tile_map[y][x] in [2, 14, 15, 16]:
                    print("Collision")
                    entity.can_move_right = False
                    entity.velocity_x = 0
                else:
                    entity.can_move_right = True
                    entity.can_move_left = True

            # check the left side
            # for x in range(tile_x, tile_x):
            #     if tile_map[y][x] in [2, 14, 15, 16]:
            #         entity.can_move = 1
            #     else:
            #         entity.can_move = 0
