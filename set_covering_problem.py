#!/usr/bin/python3
# set covering problem is an approximation algorithim that uses greedy methods to find an efficient solution

# make a list of states you want to cover
states_needed = set(
    ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
)

# hashmap of stations and the areas they cover
# keys: stations, values: the states they cover

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# data structure to hold the final set of stations you'll use
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
