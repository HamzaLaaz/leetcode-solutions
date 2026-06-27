from collections import deque


def validPath(
    n: int,
    edges: list[list[int]],
    source: int,
    destination: int
        ) -> bool:
    graph = {}
    for i in range(n):
        graph[i] = []
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    queue = deque()
    queue.append(source)
    visited = {source}
    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            return True
        for d in graph[vertex]:
            if d not in visited:
                visited.add(d)
                queue.append(d)
    return False
