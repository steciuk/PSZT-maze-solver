from collections import deque


def breadth_first(maze, start, goal):
    """
    BFS algorithm, which keeps track of visited nodes of the graph
    and returns the shortest path from start to goal
    """

    num = 0
    graph = maze.graph
    visited = []
    queue = deque([[start]])

    if start == goal:
        return "Start is the same as goal"

    while queue:
        path = queue.popleft()  # get path from the queue
        node = path[-1]  # get last cell from the path
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                num += 1
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    print(num)
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
