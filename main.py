from Direction import Direction
from GameInterface import GameInterface
from Rover import Rover
from Grid import Grid

def get_grid_size():
    width = int(input("Enter grid width: "))
    height = int(input("Enter grid height: "))
    return width, height

def get_initial_position():
    x, y = map(int, input("Enter Rover's starting position (X Y): ").split())
    return x, y

def get_initial_direction():
    direction_input = input("Enter Rover's starting direction (N, E, S, W): ").strip().upper()
    return Direction[direction_input]

def get_obstacles(grid):
    num_obstacles = int(input("Enter the number of obstacles: "))
    for _ in range(num_obstacles):
        x, y = map(int, input("Enter obstacle coordinates (X Y): ").split())
        grid.add_obstacle(x, y)

def main():
    grid_width, grid_height = get_grid_size()
    grid = Grid(grid_width, grid_height)

    get_obstacles(grid)

    rover_x, rover_y = get_initial_position()
    rover_direction = get_initial_direction()

    rover = Rover(rover_x, rover_y, rover_direction, grid)
    game = GameInterface(rover)
    game.run()

if __name__ == "__main__":
    main()
