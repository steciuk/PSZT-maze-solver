from maze import Maze, Cell
import algorithms

# gen seeded 13x11 maze

maze = Maze.from_file("maze.txt")
print(maze.graph)
# maze = Maze(10, 10, 0, 0, 2)
start, end = maze.cell_at(0, 0), maze.cell_at(9, 9)
# maze.path = algorithms.depth_first(maze, start, end)
maze.path = algorithms.breadth_first(maze, start, end)
print(maze.path)

# gen maze savestate
# maze.generate_txt_save('maze.txt')

# create maze savestate
# maze = Maze.from_file("maze.txt")
# maze.path = algorithms.breadth_first(maze, start, end)
maze.write_svg("maze.svg")
