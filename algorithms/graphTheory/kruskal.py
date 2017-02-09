"""
Since most, if not all, the algorithm has been copied from github, there is the
author and where I got it from:
https://github.com/israelst/Algorithms-Book--Python/blob/master/5-Greedy-algorithms/kruskal.py
"""

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

n,m= map(int, input().split())
vertices = [i+1 for i in range(n)]
edges = []

for i in range(m):
    v1,v2,w = map(int, input().split())
    edges.append((w,v1,v2))

graph = {
        'vertices': vertices,
        'edges': set(edges) 
}

parent = dict()
rank = dict()

values = kruskal(graph)

suma = 0
for conection in values:
    suma += conection[0]

print(suma)

