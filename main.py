from maze import Maze, Cell
import algorithms

# gen seeded 13x11 maze
maze = Maze(13, 11, 0, 0)
start, end = maze.cell_at(0, 0), maze.cell_at(12, 10)
maze.path = algorithms.breadth_first(maze, start, end)

# gen maze savestate
maze.generate_txt_save('maze.txt')

# create maze savestate
maze = Maze.from_file("maze.txt")
maze.path = algorithms.breadth_first(maze, start, end)
maze.write_svg("maze.svg")
