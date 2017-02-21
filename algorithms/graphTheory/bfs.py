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

class Graph():
    def __init__(self, g_dict=None):
        if not g_dict:
            g_dict = {}
        self.g_dict = g_dict

    def insert(self, parent, node):
        if parent not in self.g_dict:
            self.g_dict[parent] = [node]
        else:
            self.g_dict[parent].append(node)

    def __str__(self):
        res = ''
        for k in self.g_dict:
            res+= str(k) + ": {"
            for n in self.g_dict[k]:
                res+= str(n) + ", "
            res += "} \n"
        return res

    def distances(self, start):

        q = [start]
        d = {start:0}

        while q:
            u = q.pop()
            for v in self.g_dict[u]:
                if v not in d:
                    d[v] = d[u]+6
                    q.append(v)
        return d

    def __getitem__(self, index):
        return self.g_dict[index]


q = int(input())

res = []

for _ in range(q):
    
    nodes,edges = map(int, input().split())
    myDict = {}
    for i in range(1, nodes+1):
        myDict[i] = []
    myGraph = Graph(myDict)
    

    for _ in range(edges):
        p,c = map(int,input().split())
        if c not in myGraph[p]:
            myGraph.insert(p,c)
            myGraph.insert(c,p)

    start = int(input())

    if start > nodes or start < 0:
        dis = [-1 for _ in range(nodes)]
        res.append(dis)
        continue

    d = myGraph.distances(start)
    dis = []
    for i in range(1,nodes+1):
        if i!=start:
            if i in d:
                dis.append(d[i])    
            else:
                dis.append(-1)
    res.append(dis)

for r in res:
    print(*r)
