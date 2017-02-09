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

def Main():
    q = int(input())
    res = [] 
    for _ in range(q):
        nodes, edges = map(int,input().split())

        graph = {}
        for i in range(nodes+1):
            graph[i] = []
        for i in range(edges):
            v1,v2 = map(int,input().split())
            if v1 in graph and v2 in graph[v1]:
                graph[v2].append(v1)
            else:
                graph[v1].append(v2)

        start = int(input())
    
        edges = generate_edges(graph)
        distances = [ -1 for _ in range(nodes) ]
        
        direct = []
        for edge in edges:
            if edge[0] == start:
                distances[edge[1]-1] = 6
                direct.append(edge[1])
        for v in direct:
            calculateDistance(distances, v, edges, 2, 6*nodes)            

        s = ''
        for i in range(len(distances)):
            if i != start-1:
                s += str(distances[i]) + ' '
        res.append(s)
    for r in res:
        print(r)

def calculateDistance(distances, v, edges, dist, maxDis):
    direct = []
    if(dist*6 < maxDis):
        for edge in edges:
            if edge[0] == v:
                if distances[edge[1]-1] > dist*6 or distances[edge[1]-1] < 0:
                    distances[edge[1]-1] = dist * 6
                    direct.append(edge[1])
        for v in direct:
            calculateDistance(distances, v, edges, dist+1, maxDis)

    


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges


if __name__=="__main__":
    Main()
