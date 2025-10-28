# Maze Runner

Maze Runner is a Python-based terminal application that visualizes a pathfinding algorithm to navigate through a maze. The program uses the `curses` library to display the maze and highlights the path from the start point to the end point.

## Features

- **Maze Visualization**: Displays the maze in the terminal with color-coded elements.
- **Pathfinding Algorithm**: Implements a breadth-first search (BFS) algorithm to find the shortest path from the start (`O`) to the end (`X`).
- **Real-Time Updates**: Animates the pathfinding process step by step.

## How It Works

1. The maze is represented as a 2D grid where:
   - `#` represents walls.
   - `O` represents the starting point.
   - `X` represents the endpoint.
   - Spaces (` `) represent walkable paths.
2. The program uses BFS to explore the maze and find the shortest path.
3. The pathfinding process is visualized in real-time in the terminal.

## Prerequisites

- Python 3.6 or higher
- A terminal that supports the `curses` library (Linux, macOS, or Windows with a compatible terminal emulator).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/maze-runner.git
   cd maze-runner
   ```

2. Ensure you have Python installed. You can check by running:
   ```bash
   python --version
   ```

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Watch as the program visualizes the pathfinding process.

## File Structure

- `main.py`: The main script containing the maze and the pathfinding logic.
- `.idea/`: IDE-specific configuration files (can be ignored).
- `.gitignore`: Specifies files and directories to be excluded from version control.

## Example Output

The terminal will display the maze with the pathfinding process. The path will be highlighted in red as the algorithm progresses.

```
# O # # # # # # #
#   X           #
#   # #   # #   #
#   # #   # #   #
#   #     #     #
#   #   # #     #
#   #   # #     #
#   #   # # # # #
#               #
# # # # # # #   #
# # # # # # X # #
```

## Customization

- You can modify the maze by editing the `Maze` variable in `main.py`.
- Adjust the animation speed by changing the `time.sleep()` value in the `GetNew_path` function.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by classic maze-solving algorithms.
- Built using Python's `curses` library for terminal-based UI.

Enjoy solving mazes!