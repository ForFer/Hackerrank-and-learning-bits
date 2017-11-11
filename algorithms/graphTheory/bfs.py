"""
Author: Fernando Collado
Github: ForFer
"""

"""
Consider an undirected graph consisting of nodes where each node is labeled from
to and the edge between any two nodes is always of length . We define node to be
the starting position for a BFS.

Given queries in the form of a graph and some starting node, , perform each
query by calculating the shortest distance from starting node to all the other
nodes in the graph. Then print a single line of n-1 space-separated integers listing
node 's shortest distance to each of the n-1 other nodes (ordered sequentially by
node number); if is disconnected from a node, print n-1 as the distance to that
node.

Input Format

The first line contains an integer, q, denoting the number of queries. The
subsequent lines describe each query in the following format:

    The first line contains two space-separated integers describing the
respective values of n (the number of nodes) and m (the number of edges) in the
graph.
    Each line i of the m subsequent lines contains two space-separated
integers, u and v , describing an edge connecting node u to node v. 
    The last line contains a single integer, s, denoting the index of the
starting node.

Output Format

For each of the q queries, print a single line n-1 of space-separated integers
denoting the shortest distances to each of the n-1 other nodes from starting
position s. These distances should be listed sequentially by node number,
but should not include node . If some node is unreachable from s, print
-1 as the distance to that node.

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2

Sample Output

6 6 -1
-1 6

"""

"""
2
4 2
1 2
1 3
1
3 1
2 3
2
"""

from collections import deque

class Graph():
    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = {}
        self.graph_dict = graph_dict

    def insert(self, parent, child):
        if parent not in self.graph_dict:
            self.graph_dict[parent] = [child]
        else:
            self.graph_dict[parent].append(child)

    def __str__(self):
        res = ''
        for k in self.graph_dict:
            res+= str(k) + ": {"
            for n in self.graph_dict[k]:
                res+= str(n) + ", "
            res += "} \n"
        return res

    def distances(self, start, distance):

        q = deque([start])

        while q:
            current = q.popleft()
            for v in self.graph_dict[current]:
                if distance[v] == 0:
                    distance[v] = distance[current] + 6
                    q.append(v)

        del distance[start]
        return distance

    def __getitem__(self, index):
        return self.graph_dict[index]


q = int(input())

res = []

for _ in range(q):
    
    nodes,edges = map(int, input().split())
    myDict = {}
    distances = {}
    for i in range(1, nodes+1):
        myDict[i] = []
        distances[i] = 0
    myGraph = Graph(myDict)
    

    for _ in range(edges):
        p,c = map(int,input().split())
        myGraph.insert(p,c)
        myGraph.insert(c,p)

    start = int(input())

    d = myGraph.distances(start, distances) 
    distances = [x if x > 0 else -1 for k,x in d.items()]

    print(*distances)
