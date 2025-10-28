import curses
from curses import wrapper
import queue
import time

Maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "X", "#", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*3, "X", RED)
            else:
                stdscr.addstr(i, j*3, value, BLUE)


def find_StartPoint(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def GetNew_path(maze, stdscr):
    start = "O"
    end = "X"
    Start_Position = find_StartPoint(maze, start)

    q = queue.Queue()
    q.put((Start_Position, [Start_Position]))

    visited = set()

    while not q.empty():
        Present_Position, path = q.get()
        row, col = Present_Position

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.25)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # UP Searching
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN Searching
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT moment
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT moment
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    GetNew_path(Maze, stdscr)
    stdscr.getch()


wrapper(main)