from Direction import Direction

class GameInterface:
    def __init__(self, rover):
        self.rover = rover

    def display_grid(self):
        for y in range(self.rover.grid.height - 1, -1, -1):
            print(f"{y:2}", end=" ")
            for x in range(self.rover.grid.width):
                if (x, y) in self.rover.grid.obstacles:
                    print('O', end=' ')
                elif x == self.rover.x and y == self.rover.y:
                    print(self.get_rover_symbol(), end=' ')
                else:
                    print('.', end=' ')
            print()

        print("  ", end=" ")
        for x in range(self.rover.grid.width):
            print(x, end=' ')
        print()

    def get_rover_symbol(self):
        symbols = {
            Direction.N: '^',
            Direction.E: '>',
            Direction.S: 'v',
            Direction.W: '<'
        }
        return symbols[self.rover.direction]

    def run(self):
        while True:
            self.display_grid()
            print(f"Current position: {self.rover.get_position()}")
            command = input("Enter command (L, R, M) or 'quit' to exit: ").strip().upper()

            if command == 'QUIT':
                print("Game Over")
                break
            elif command in ['L', 'R', 'M']:
                self.process_command(command)
            else:
                print("Invalid command. Please enter L, R, M, or 'quit'.")

    def process_command(self, command):
        message = None
        if command == 'L':
            self.rover.rotate(command)
        elif command == 'R':
            self.rover.rotate(command)
        elif command == 'M':
            message = self.rover.move()
        if message:
            print(message)
