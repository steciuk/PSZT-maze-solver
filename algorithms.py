from collections import deque
from itertools import count


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
    """
    BFS algorithm, which keeps track of visited nodes of the graph
    and returns the shortest path from start to goal
    """

    num = 0
    graph = maze.graph
    visited = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()  # get path from the queue
        node = path[-1]  # get last cell from the path
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour in visited:
                    continue

                num += 1
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    print("Explored nodes: ", num)
                    print_visited(visited, maze)
                    return new_path

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
            print("Checked nodes:", num)
            print_visited(visited, maze)
            return path

        if current in visited:
            continue

        visited.append(current)
        for neighbour in graph[current]:
            if neighbour in visited:
                continue

            num += 1
            append_path = list(path)
            append_path.append(neighbour)
            stack.append((append_path, neighbour))
    return "NO WAY!"


def iter_deepening(maze, start, goal):
    for depth in range(maze.nx * maze.ny):
        result, path = depth_limited(maze, start, goal, depth)
        if result is False:
            continue
        print("Found a path to " + repr(goal) + ". Resulting depth: " + str(depth))
        return path

    raise ValueError("There's no such path! (Reached maximum depth value)")


def depth_limited(maze, start, goal, depth):
    graph = maze.graph
    visited = []
    stack = deque([[start]])

    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            print_visited(visited, maze)
            return True, path
        if depth <= 0:
            print_visited(visited, maze)
            return False, []

        visited.append(node)
        for neighbour in graph[node]:
            if neighbour in visited:
                continue

            append_path = list(path)
            append_path.append(neighbour)
            stack.append(append_path)
        depth -= 1

    return False, []
