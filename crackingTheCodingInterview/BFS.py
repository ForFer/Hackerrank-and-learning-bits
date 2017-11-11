"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
"""

from collections import deque

def bfs(graph, start, distances):
    q = deque([start])

    while q:
        current = q.popleft()
        
        for v in graph[current]:
            if distances[v] == 0:
                distances[v] = distances[current] + 6
                q.append(v)

q = int(input())

for _ in range(q):
    nodes, edges = list(map(int, input().split()))
    
    # Representing graph with a dict
    graph = dict()

    distances = {}
    
    for node in range(nodes):
        graph[node+1] = []
        distances[node+1] = 0
    
    for _ in range(edges):
        a,b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    start = int(input())
    bfs(graph, start, distances)

    del distances[start]

    print(*[x if x>0 else -1 for k,x in distances.items()])
