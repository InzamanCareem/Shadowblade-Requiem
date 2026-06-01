class PhysicsManager:
    def __init__(self):
        self.gravity = 10

    def apply_gravity(self, velocity_y, delta_time):
        return velocity_y + self.gravity * delta_time

    def detect_collisions(self):
        pass
