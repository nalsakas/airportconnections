airports = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD"
]

routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EWY", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
]

def edge2adjacency(routes):
    nodes = {}
    for route in routes:
        a, b = route
        if a not in nodes: nodes[a] = []
        if b not in nodes: nodes[b] = []
        nodes[a].append(b)
    return nodes

# Explores all posssible travel destinations (connected destinations) of a starting point (start airport).
# List not only contains direct flights but also connected flights.
# Return value is a set
def explore(routes, start, cache = None):
    if cache == None:
        cache = set()
    
    if start in cache:
        return

    cache.add(start)
    
    for a in routes[start]:
        explore(routes, a, cache)

    return cache

def findroutes(airports, routes, start):
    routes_adj = edge2adjacency(routes)
    airports_set = set(airports)

    # Creates a set of all reachable airports for all airports
    # set of start airport is also explored.
    routes_sets = []
    start_set = set()
    for port in airports:
        neighbours = explore(routes_adj, port)
        routes_sets.append(neighbours)
        if port == start: start_set = neighbours
    
    # Starting from start_set airport add other airports to the sum set,
    # Continue until all airports have been reached(collected) in the sum
    # Before addition, sort all airpots based in their difference to the
    # start_set airport. Airport with most difference comes first when sorted
    sum = start_set
    routes_sets.sort(key=lambda x: len(x.difference(sum)), reverse=True)
    i = 0
    res = 0 # required number of connections to the start airport
    while i < len(routes_sets):
        # step over subsets
        if sum.issuperset(routes_sets[i]):
            i += 1
            continue

        # add missing connections from other airports until all airports are added
        sum = sum.union(routes_sets[i])
        i += 1
        res += 1
        if sum == airports_set:
            break
    
    # Result is sum of grand airport + number of added airports to the sum
    return res



if __name__ == "__main__":
    #start = "LGA"
    #start = "SFO"
    start = "BUD"
    print(findroutes(airports, routes, start))