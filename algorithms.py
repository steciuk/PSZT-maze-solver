from itertools import count
from collections import deque

def print_visited(visited, maze):
    for y in range(maze.ny):
        for x in range(maze.nx):
            if maze.cell_at(x, y) in visited:
                print(visited.index(maze.cell_at(x, y)), end=' ')
            else:
                print("X", end=' ')
        print()
    print()


def breadth_first(maze, start, goal):
    num = 0
    graph = maze.graph
    visited = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()  # get path from the queue
        node = path[-1]         # get last cell from the path
        if node not in visited:
            if node == goal:
                print("BFS Explored nodes: ", num)
                return path

            num += 1
            for neighbour in graph[node]:
                if neighbour in visited:
                    continue

                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

            visited.append(node)
    return "There's no such path!"


def depth_first(maze, start, goal):
    num = 0
    graph = maze.graph
    path = [start]
    stack = deque([(path, start)])
    visited = []
    while stack:
        path, current = stack.pop()
        if current == goal:
            print("DFS Explored nodes:", num)
            return path

        if current in visited:
            continue

        visited.append(current)
        num += 1
        for neighbour in graph[current]:
            if neighbour in visited:
                continue

            append_path = list(path)
            append_path.append(neighbour)
            stack.append((append_path, neighbour))
    return "There's no such path!"


def iter_deepening(maze, start, goal):
    num = 0
    for depth in count(start=0):
        path, traversed = depth_limited(maze, start, goal, depth)
        num += traversed
        if path is None:
            continue
        print("IDFS Resulting depth: " + str(depth) + ", Explored nodes: " + str(num))
        return path

    raise ValueError("There's no such path! (Reached maximum depth value)")


def depth_limited(maze, start, goal, start_depth):
    num = 0
    graph = maze.graph
    stack = deque([([start], start_depth)])
    visited = []
    v = {}

    while stack:
        path, depth = stack.pop()
        node = path[-1]
        if node == goal:
            return path, num
        if depth <= 0:
            continue

        num += 1
        visited.append(node)
        v[node] = depth
        for neighbour in graph[node]:
            if neighbour in v.keys() and depth < v[neighbour]:
                continue

            append_path = list(path)
            append_path.append(neighbour)
            stack.append((append_path, depth - 1))

    return None, num
