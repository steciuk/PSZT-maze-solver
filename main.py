from maze import Maze

# gen seeded 13x11 maze
maze = Maze(13, 11, 0, 0)
maze.make_maze()

# gen maze savestate
maze.generate_txt_save('maze.txt')

# create maze savestate
maze = Maze.from_file("maze.txt")
maze.write_svg("maze.svg")
