from collections import deque
from itertools import count

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
        node = path[-1]         # get last cell from the path
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
                    return new_path

            visited.append(node)

    return "There's no such path!"


def depth_first(maze, start, goal):
    num = 0
    graph = maze.graph
    path = [start]
    stack = deque([(path, start)])
    visited = set()
    while stack:
        path, current = stack.pop()
        if current == goal:
            print("checked nodes:", num)
            return path

        if current in visited:
            continue

        visited.add(current)
        for neighbour in graph[current]:
            if neighbour in visited:
                continue

            num += 1
            append_path = list(path)
            append_path.append(neighbour)
            stack.append((append_path, neighbour))
    return "NO WAY!"

def iter_deepening(maze, start, goal):
    for depth in count(start=0):
        result, path = depth_limited(maze.graph, ([start], []), goal, depth)
        if result is False:
            continue
        print("Found a path to " + repr(goal) + ". Resulting depth: " + str(depth))
        return path

    raise ValueError("There's no such path! (Reached maximum depth value)")

def depth_limited(graph, nodes, goal, depth):
    path, visited = nodes
    node = path[-1]
    if node == goal:
        print(path)
        return True, path
    if depth <= 0:
        return False, []

    visited.append(node)
    for neighbour in graph[node]:
        if neighbour in visited:
            continue

        append_path = list(path)
        append_path.append(neighbour)
        result, new_path = depth_limited(graph, (append_path, visited), goal, depth - 1)
        if result:
            return True, new_path

    return False, []

"""
def depth_limited(graph, start, goal, depth):
    visited = set()
    stack = deque([[start]])

    while stack:
        path = stack.popleft()
        node = path[-1]
        if node == goal:
            print(path)
            return True, path
        if depth <= 0:
            return False, []

        visited.add(node)
        for neighbour in graph[node]:
            if neighbour in visited:
                continue

            append_path = list(path)
            append_path.append(neighbour)
            stack.append(append_path)
        depth -= 1

    return False, []
"""