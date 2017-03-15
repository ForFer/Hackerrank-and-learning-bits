"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Dijkstra implementation using dicts, and getting a graph in a dict
"""

#TODO: add tests

def dijkstra(graph, start):
    q = [v for v in graph]

    dist = {}
    prev = {}
    
    for v in graph:
        dist[v] = float('Inf')
        prev[v] = None

    dist[start] = 0

    while q:
        u = min(dist)
        
        q.pop(u)

        for neigh in graph[u]:
            temp = dist[u] + graph[u][neigh]

            if temp<dist[neigh]:
                dist[neigh] =  alt
                prev[v] = neigh

    return dist, prev


