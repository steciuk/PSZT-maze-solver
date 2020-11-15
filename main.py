from maze import Maze, Cell
import algorithms

# gen seeded 13x11 maze
maze = Maze(13, 11, 0, 0, 1)
print(algorithms.breadth_first(maze, maze.cell_at(0, 0), maze.cell_at(5, 3)))

# gen maze savestate
# maze.generate_txt_save('maze.txt')

# create maze savestate
# maze = Maze.from_file("maze.txt")
# maze.write_svg("maze.svg")
