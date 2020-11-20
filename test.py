from maze import Maze
import algorithms

maze = Maze.from_file("pusty.txt")
start, goal = maze.cell_at(0, 0), maze.cell_at(maze.nx - 1, maze.ny - 1)
maze.path = algorithms.iter_deepening(maze, start, goal)
maze.write_svg("test.svg")