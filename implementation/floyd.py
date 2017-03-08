"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

print("Introduce number of nodes, and number of edges")
n_nodes, n_edges = map(int, input().split())

nodes = [[0 for _ in range(n_nodes)] for _ in range(n_nodes) ]
weights = [[1000 for _ in range(n_nodes)] for _ in range(n_nodes) ]

print("Introduce data in the format 'from to weight'")
for i in range(n_edges):
    x,y,weight = map(int,input().split())
    x-=1
    y-=1
    nodes[x][y] = 1 
    weights[x][y] = weight


#Floyd algorithm with a small optimization
for i in range(len(vertices)):
    for j in range(len(vertices)):
        irow = weights[i]
        for k in range(len(vertices)):
            krow = weights[k]
            if irow[j] > irow[k]+krow[j]:
                weights[i][j] = irow[k]+krow[j]



queries = int(input("Number of queries to make"))
res = []
for _ in range(queries):
    i,j = map(int, input("introduce the 2 nodes separated by a space").split())
    weight = weights[i-1][j-1] if i!=j else 0
    res.append(weight) if weight!=1000 else res.append(-1)

for r in res:
    print(r) 

