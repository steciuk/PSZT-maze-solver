import time
from maze import Maze
import algorithms

# gen seeded 13x11 maze
# maze = Maze.from_file("maze.txt")
maze = Maze(100, 100, 0, 0, seed=1, one_route=False, wall_knock=0.25)
# print(maze.graph)
start, end = maze.cell_at(0, 0), maze.cell_at(99, 99)
t_start = time.process_time()
maze.path = algorithms.depth_first(maze, start, end)
t_end = time.process_time()
print(t_end - t_start)

t_start = time.process_time()
maze.path = algorithms.breadth_first(maze, start, end)
t_end = time.process_time()
print(t_end - t_start)

# t_start = time.time()
# maze.path = algorithms.iter_deepening(maze, start, end)
# t_end = time.time()
# print(t_end - t_start)
# print(maze.path)

# gen maze savestate
# maze.generate_txt_save('maze.txt')
maze.write_svg("maze.svg")
