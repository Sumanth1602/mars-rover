from enum import Enum

class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def turn_left(self):
        return Direction((self.value + 3) % 4)

    def turn_right(self):
        return Direction((self.value + 1) % 4)
