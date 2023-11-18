# Mars Rover Simulation Game

## Overview
This Mars Rover Simulation Game is a text-based interactive game written in Python. It allows users to control a virtual rover on a grid-based terrain, simulating the movement and navigation on Mars. The rover can move forward, turn left, or turn right and must avoid obstacles.

## Files Description
- `Direction.py`: Contains the `Direction` enum, which represents the cardinal directions and methods for turning the rover.
- `GameInterface.py`: Defines the `GameInterface` class for handling user inputs, displaying the game grid, and running the game loop.
- `Grid.py`: Includes the `Grid` class that represents the grid-based terrain where the rover operates and manages obstacles.
- `Rover.py`: Contains the `Rover` class, which manages the state and movement of the rover within the grid.
- `main.py`: The main executable file that sets up the game environment and starts the game.

## How to Run the Game
To run the Mars Rover Simulation Game, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine or download the files.

2. **Prerequisites**: Ensure you have Python installed on your system. The game is compatible with Python 3.

3. **Run the Game**:
    - Open a terminal or command prompt.
    - Navigate to the directory where the game files are located.
    - Run the game using Python with the command: `python main.py`.
    - Follow the on-screen prompts to enter the grid size, initial rover position, direction, and obstacles.

4. **Playing the Game**:
    - Once the game starts, you will see the rover's position on a grid.
    - Enter commands ('L' for left, 'R' for right, 'M' for move forward) to control the rover.
    - The grid updates with each command showing the rover's new position and direction.
    - Enter 'quit' to end the game.

## Features
- Dynamic grid generation based on user input.
- Obstacle placement and collision detection.
- Real-time grid updating with rover movement and direction change.
- User-friendly command-line interface.
