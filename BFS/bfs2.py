

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'A'],
    'D': ['G', 'C'],
    'G': ['B', 'Z']
}


def bfs(graph, start):

    from collections import deque

    seen = {start}
    visited = []
    queue = deque([start])

    while queue:

        node = queue.popleft()
        visited.append(node)

        for neighbor in graph.get(node, []):

            if neighbor not in seen:

                seen.add(neighbor)
                queue.append(neighbor)

    
    return visited


def dfs(graph, start):

    seen = {start}
    visited = []
    stack = [start]

    while stack:

        node = stack.pop()
        visited.append(node)

        for neighbor in graph.get(node, []):

            if neighbor not in seen:

                seen.add(neighbor)
                stack.append(neighbor)

    
    return visited

items = dfs(graph, 'A')

print(items)