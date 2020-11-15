from collections import deque

def breadth_first(maze, start, goal):
    """
    BFS algorithm, which keeps track of visited nodes of the graph
    and returns the shortest path from start to goal
    """

    graph = maze.graph
    visited = []
    queue = deque([[start]])

    if start == goal:
        return "Start is the same as goal"

    while queue:
        path = queue.pop()                 # get path from the queue
        node = path[-1]                     # get last cell from the path
        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            visited.append(node)

    return "There's no such path!"