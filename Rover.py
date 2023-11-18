from Direction import Direction
from Grid import Grid
class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def move(self):
        dx, dy = 0, 0
        if self.direction == Direction.N:
            dy = 1
        elif self.direction == Direction.E:
            dx = 1
        elif self.direction == Direction.S:
            dy = -1
        elif self.direction == Direction.W:
            dx = -1

        new_x, new_y = self.x + dx, self.y + dy
        if self.grid.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y
        else:
            return "Warning: Movement blocked by an obstacle or out of bounds!"
    def rotate(self, rotation):
        if rotation == 'L':
            self.direction = self.direction.turn_left()
        elif rotation == 'R':
            self.direction = self.direction.turn_right()

    def get_position(self):
        return f"{self.x}:{self.y} ({self.direction.name})"

    def check_position_validity(self):
        if not self.grid.is_valid_position(self.x, self.y):
            return "Warning: Rover has encountered an obstacle or is out of bounds!"
        return ""
