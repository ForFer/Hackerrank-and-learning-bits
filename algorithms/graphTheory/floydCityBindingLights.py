"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Given a directed, weighted graph, consisting of N nodes and there are edges ,of
specified length between some of them in the graph.

Given Q questions, inquring the shortest distance between a queried pair of
nodes in the graph.

Answer all these questions as quickly as possible !

Input Format

First line has two integers N, denoting the number of nodes in the graph and M,
denoting the number of edges in the graph.
The next M lines each consist of three space separated integers x y r, where
x and y denote 
the two nodes between which the directed edge (x->y) exists,r denotes the length of the
edge between the corresponding edges.
The next line contains a single integer Q, denoting number of queries.
The next Q lines each, contain two space separated integers a and b, denoting the
node numbers specified according to the question.

Output Format

Print Q lines, each containing a single integer, specifying the shortest distance
between the nodes specified for that query in the input.

If the distance between a pair of nodes is infinite (not reachable), then print
-1 as the shortest distance.

Sample Input

4 5
1 2 5
1 4 24
2 4 6
3 4 4
3 2 7
3
1 2
3 1
1 4

Sample Output

5
-1
11

"""
import time

n_nodes, n_edges = map(int, input().split())

nodes = [[0 for _ in range(n_nodes)] for _ in range(n_nodes) ]
weights = [[1000 for _ in range(n_nodes)] for _ in range(n_nodes) ]

for i in range(n_edges):
    x,y,weight = map(int,input().split())
    x-=1
    y-=1
    nodes[x][y] = 1 
    weights[x][y] = weight
times = []
start_time = time.time()

for i in range(len(nodes)):
    for j in range(len(nodes)):
        irow = weights[i]
        for k in range(len(nodes)):
            krow = weights[k]
            if weights[i][j] > weights[i][k]+weights[k][j]:
                weights[i][j] = weights[i][k]+weights[k][j]

times.append("--- normal way:  %seconds ---" %(time.time()-start_time))


weights = [[1000 for _ in range(n_nodes)] for _ in range(n_nodes) ]
start_time = time.time()

for i in range(len(nodes)):
    for j in range(len(nodes)):
        irow = weights[i]
        for k in range(len(nodes)):
            krow = weights[k]
            if irow[j] > irow[k]+krow[j]:
                weights[i][j] = irow[k]+krow[j]

times.append("--- irow/krow way:  %seconds ---" %(time.time()-start_time))

weights = [[1000 for _ in range(n_nodes)] for _ in range(n_nodes) ]
start_time = time.time()

for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i==j:
            continue
        irow = weights[i]
        for k in range(len(nodes)):
            krow = weights[k]
            if irow[j] > irow[k]+krow[j]:
                weights[i][j] = irow[k]+krow[j]

times.append("--- i==j way:  %seconds ---" %(time.time()-start_time))

queries = int(input())
res = []
for _ in range(queries):
    i,j = map(int, input().split())
    weight = weights[i-1][j-1] if i!=j else 0
    res.append(weight) if weight!=1000 else res.append(-1)

for r in res:
    print(r) 

for t in times:
    print(t)
