#!/usr/bin/python3

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def dfs(graph, source):
    print(source)

    for neighbour in graph[source]:
        dfs(graph, neighbour)


dfs(graph, 'a')
