from maze import Maze, Cell
import algorithms

# gen seeded 13x11 maze

# maze = Maze.from_file("maze.txt")
maze = Maze(50, 50, 0, 0, seed=2, one_route=False, wall_knock=0.25)
print(maze.graph)
start, end = maze.cell_at(0, 0), maze.cell_at(49, 49)
# maze.path = algorithms.depth_first(maze, start, end)
maze.path = algorithms.breadth_first(maze, start, end)
# print(maze.path)

# gen maze savestate
# maze.generate_txt_save('maze.txt')

maze.write_svg("maze.svg")
