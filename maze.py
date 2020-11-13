# df_maze.py
import random
from collections import defaultdict


class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.

    """

    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        """Does this cell still have all its walls?"""

        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""

        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False


class Maze:
    """A Maze, represented as a grid of cells."""

    num_map = []
    graph = defaultdict(set)

    def __init__(self, nx, ny, ix=0, iy=0, seed=None):
        """Initialize the not seeded maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy

        self.maze_map = [[Cell(x, y) for x in range(nx)] for y in range(ny)]
        """It only make sense to define 4 states for each cell, remembering state of two of its walls, cause adjacent 
        cells will store information about remaining walls.
         __          __          --          --
        |  | - 0    |    - 1    |  | - 2    |   - 3
         --          --                  
        """
        if seed is not None:
            random.seed(seed)

        self.generate_graph()

    @classmethod
    def from_file(cls, filename):
        """Initialize maze from a file"""

        with open(filename, 'r') as f:
            lines = f.read().splitlines()
            num_map = [[x for x in line] for line in lines]

        maze = cls(len(num_map[0]), len(num_map))
        maze.num_map = num_map
        maze.maze_from_num_map()
        maze.generate_graph()
        return maze

    def print_cords(self):
        for row in self.maze_map:
            for cell in row:
                print(str(cell.x) + ',' + str(cell.y), ' ', end='')
            print()

    def find_neighbours(self, cell):
        """Returns a list of neighbours you can move to"""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                neighbours.append((direction, neighbour))
        return neighbours

    def generate_graph(self):
        for row in self.maze_map:
            for cell in row:
                for neighbour in self.find_neighbours(cell):
                    if not cell.walls[neighbour[0]]:
                        self.graph[cell].add(neighbour[1])

    def maze_from_num_map(self):
        """Generate cellular maze structure from a number map"""

        for row in self.maze_map:
            for cell in row:
                state = self.num_map[cell.y][cell.x]
                if state == '1':
                    cell.knock_down_wall(self.cell_at(cell.x + 1, cell.y), 'E')
                elif state == '2':
                    cell.knock_down_wall(self.cell_at(cell.x, cell.y + 1), 'S')
                elif state == '3':
                    cell.knock_down_wall(self.cell_at(cell.x + 1, cell.y), 'E')
                    cell.knock_down_wall(self.cell_at(cell.x, cell.y + 1), 'S')

    def generate_num_map(self):
        """Generate number map from the cellular maze structure"""

        for row in self.maze_map:
            rowlist = []
            for cell in row:
                if not cell.walls['E'] and not cell.walls['S']:
                    rowlist.append('3')
                elif not cell.walls['S']:
                    rowlist.append('2')
                elif not cell.walls['E']:
                    rowlist.append('1')
                else:
                    rowlist.append('0')
            self.num_map.append(rowlist)

    def generate_txt_save(self, filename):
        """Write nummap to a file"""

        if not self.num_map:
            self.generate_num_map()

        with open(filename, 'w') as f:
            f.write('\n'.join(map(''.join, self.num_map)))

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""

        return self.maze_map[y][x]

    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.nx * 2]
        for y in range(self.ny):
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[y][x].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[y][x].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def write_svg(self, filename):
        """Write an SVG image of the maze to filename."""

        aspect_ratio = self.nx / self.ny
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / self.ny, width / self.nx

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Write a single wall to the SVG image file handle f."""

            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
                  .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width + 2 * padding, height + 2 * padding,
                          -padding, -padding, width + 2 * padding, height + 2 * padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).
            for x in range(self.nx):
                for y in range(self.ny):
                    if self.cell_at(x, y).walls['S']:
                        x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                    if self.cell_at(x, y).walls['E']:
                        x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)

    def find_unvisited_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze(self):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_unvisited_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1
