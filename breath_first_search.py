#!/usr/bin/python3
from collections import deque

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def bfs(graph, source):
    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        # breakpoint()
        for neighbour in graph[current]:
            queue.append(neighbour)


bfs(graph, 'a')
