#!/usr/bin/python3

infinity = float("inf")

graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "fin": 1
    },
    "b": {
        "a": 3,
        "fin": 5
    },
    "fin": {}
}

costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node] # get the cost of getting to the current node
        neighbors = graph[node] # get all the neighbours of the current node

        for n in neighbors.keys():
            new_cost = cost + neighbors[n] # cost of getting to current node + cost of getting to that node via this node
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


dijkstra(graph, costs, parents, processed)

# Print parents
print("Parents of each node:")
for node, parent in parents.items():
    print(f"Node: {node}, Parent: {parent}")

# Parents final costs
print("\nCosts of each node from the start:")
for node, cost in costs.items():
    print(f"Node: {node}, Cost: {cost}")

# reconstruct the path
def reconstruct_path(parents, start, end):
    path = []
    current = end

    while current != start:
        path.append(current)
        current = parents[current]
    
    path.append(start)
    path.reverse()
    return "->".join(path)

path = reconstruct_path(parents, "start", "fin")
print("\nShortest path:")
print(path)
