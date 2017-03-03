"""
Author: Fernando Collado
Github: ForFer
"""

"""
Given a graph which consists of several edges connecting the nodes in it.
It is required to find a subgraph of the given graph with the following
properties:

    The subgraph contains all the nodes present in the original graph.
    The subgraph is of minimum overall weight (sum of all edges) among all such
subgraphs.
    It is also required that there is exactly one, exclusive path between any
two nodes of the subgraph.

One specific node S is fixed as the starting point of finding the subgraph.
Find the total weight of such a subgraph (sum of all edges in the subgraph)

Input Format

First line has two integers N, denoting the number of nodes in the graph and
M, denoting the number of edges in the graph.

The next M lines each consist of three space separated integers x y r, where x
and y
denote the two nodes between which the undirected edge exists,r denotes the
length of edge between the corresponding nodes.

The last line has an integer S, denoting the starting node.

If there are edges between the same pair of nodes with different weights, they
are to be considered as is, like multiple edges.

Output Format

Print a single integer denoting the total weight of tree so obtained (sum of
weight of edges).

Sample Input 0

5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1

Sample Output 0

15

"""

    
def findLowest(start, weights, visited):
        
    lowest = 10**6
    node = 0
    for i in range(len(weights[start])):
        if weights[start][i] < lowest and visited[i] != -1 and weights[start][i]!=-1:
            lowest = weights[start][i]
            node = i

    return lowest,node

#Graph implementation using adjacency matrix and weights matrix
n_nodes, n_edges = map(int, input().split())

nodes = [[0 for _ in range(n_nodes)] for _ in range(n_nodes) ]
weights = [[-1 for _ in range(n_nodes)] for _ in range(n_nodes) ]

for i in range(n_edges):
    x,y,weight = map(int,input().split())
    x-=1
    y-=1
    nodes[x][y] = 1
    nodes[y][x] = 1
    if weights[x][y] == -1 :
        weights[x][y] = weight
        weights[y][x] = weight
    elif weights[x][y] != -1 and weight < weights[x][y]:
        weights[x][y] = weight
        weights[y][x] = weight

start = int(input())

visited = [i for i in range(n_nodes)]
cost = 0

current = start-1
visited[current] = -1

while visited.count(-1) < n_nodes:
    low = []
    nodes = []
    fromNode = []
    for i in range(len(visited)):
        if visited[i] == -1:
            temp, newNode = findLowest(i, weights, visited)
            low.append(temp)
            nodes.append(newNode)
            fromNode.append(i)

    minLow = min(low)
    previous = fromNode[low.index(minLow)]
    current = nodes[low.index(minLow)]    
    cost+= minLow
    weights[previous][current] = -1
    weights[current][previous] = -1
    visited[current] = -1
    
    
print(cost)







