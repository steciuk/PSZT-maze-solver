import time
from maze import Maze
import algorithms

menu = {
    '1': "Create a new maze",
    '2': "Solve maze",
    '3': "Save maze to text file",
    '4': "Exit",
    'h': "Help!"
}


def main():
    maze = None
    choice = True
    while choice:
        print("-----LABYRINTH SOLVER-----")
        for key in sorted(menu.keys()):
            print(key + ") " + menu[key])
        print("--------------------------")
        choice = input("Choose an option: ")

        if choice == "1":
            maze = create_maze()
        elif choice == "2":
            solver(maze)
        elif choice == "3":
            save_to_file(maze)
        elif choice == "4":
            print("Goodbye!\n")
            choice = False
        elif choice == 'h':
            help_message()
        else:
            print("Invalid option, please choose one from the available")


def create_maze():
    print("If you have a .txt file, write it's name down. Otherwise press Enter")
    file = input("Your .txt file: ")

    if file != "":
        maze = Maze.from_file(file)
        print("Successfully created a maze from file!\n")
        return maze
    else:
        try:
            width = input("Specify width (x): ")
            width = int(width)
            height = input("Specify height (y, if you specify nothing it will be the same as x): ")
            if height == "":
                height = width
            else:
                height = int(height)
            seed = input("Seed (Enter to randomize): ")
            if seed == "":
                seed = None
            else:
                seed = int(seed)
            route = input("Should it have only one route? (Y/N): ")
            if route == 'Y' or route == 'y':
                route = True
            else:
                route = False
            maze = Maze(width, height, 0, 0, seed=seed, one_route=route)
            print("Successfully created random maze!\n")
            return maze
        except:
            print("Invalid value was passed to the program.\n")
            return None


def solver(maze):
    if maze is None:
        print("There's no labyrinth to solve right now!\nMaybe it's time to create one?\n")
        return

    start, goal = maze.cell_at(0, 0), maze.cell_at(maze.nx - 1, maze.ny - 1)
    print("Solving...\n")
    print("---DFS---")
    begin = time.time()
    maze.path = algorithms.depth_first(maze, start, goal)
    end = time.time()
    print("Time elapsed [s]: ", end - begin)
    print("{}\n".format(maze.path))
    maze.write_svg("DFS.svg")
    print("---BFS---")
    begin = time.time()
    maze.path = algorithms.breadth_first(maze, start, goal)
    end = time.time()
    print("Time elapsed [s]: ", end - begin)
    print("{}\n".format(maze.path))
    maze.write_svg("BFS.svg")
    if maze.nx > 100 or maze.ny > 100:
        print("IDFS algorithm takes a VERY long for mazes that have x or y > 100. :(")
        return
    else:
        print("---IDFS---")
        begin = time.time()
        maze.path = algorithms.iter_deepening(maze, start, goal)
        end = time.time()
        print("Time elapsed [s]: ", end - begin)
        print("{}\n".format(maze.path))
        maze.write_svg("IDFS.svg")

    print("Pictures will be available after closing the program.\n")


def save_to_file(maze):
    if maze is None:
        print("There's nothing to save right now!\n")
        return

    maze.generate_txt_save('maze.txt')
    print("Your saved maze can be found in files maze.txt!\n")


def help_message():
    print(
    """
    1) Create a new maze
    Creates maze from text file or generates one with properties set by the user.
    txt file should have special formatting:
    
    It only make sense to define 4 states for each cell, remembering state of two of its walls, cause adjacent 
    cells will store information about remaining walls.
     __          __          --          --
    |  | - 0    |    - 1    |  | - 2    |   - 3
     --          --   
     
    Each value should have a space between other value. The numbers should be written in rows and columns.
    
    2) Solve maze
    Solves created maze with 3 different algorithms - DFS, BFS and IDFS.
    Solved mazes are then saved to .svg picture files.
    !!! IDFS is being solved only for mazes with x or y <= 100, because of the time it takes to find the answer.
    
    3)Save maze to text file
    Saves the maze to a text file according to the special formatting.
    """
    )
    input("Press any button to continue...\n")


if __name__ == "__main__":
    main()

