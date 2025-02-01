## Graphs could be: Adjacency lists, matrices or edge lists
import numpy as np
from collections import deque
from collections import defaultdict

# So BFS first visits ALL NEIGHBORS from a node before moving on.
# Usually used for shortest path, finding closest node which meets a condition or exploring a graph layer by layer


graph_matrix = np.array([
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
])

edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'A'],
    'D': ['G', 'C'],
    'G': ['B', 'Z']
}

def dfs(graph, start):

    # used for finding cycles, solving mazed where you need to explore paths to the end, finding strongly connected components

    seen = {start}
    visited =[]
    stack = [start]

    while stack:

        node = stack.pop()
        visited.append(node)

        for neighbor in graph.get(node, []):

            if neighbor not in seen:

                seen.add(neighbor)
                stack.append(neighbor)

            else:
                print(f"Cycle detected from {node} to {neighbor}")

    return visited


def bfs(graph, start):

    # finding shortest paths, finding nodes closest to start, level-by-level traversal

    seen = {start}
    visited = []

    queue = deque([start]) # because we need an iterable for deque

    while queue:

        node = queue.popleft()
        visited.append(node)

        for neighbor in graph.get(node, []):
            
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


t = dfs(graph, 'A')

print(t)