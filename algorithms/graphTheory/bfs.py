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


class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.children = []
        self.data = value

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """
    def __init__(self, node):
        self.root = node

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, parent, node):
        """
        Insert function will insert a node into list of children of node
        """
        parent.children.append(node)
        return None                   

    def search_node(self, root, data):
    
        found = False
        for node in root.children:
            if node.data == data:
                return node

        result = None
        if found == False:
            for node in root.children:
                result = self.search_node(node, data)
        return result
        



def Main():
    q = int(input())

    out = ['' for i in range(q)]

    for _ in range(q):
        n,m = map(int,input().split())
        v1,v2 = map(int,input().split())
    
        node = Node(v1)
        tree = Tree(node)
        root = tree.root
        
        tree.insert(root,Node(v2))
        
        renegades = []

        for i in range(m-1):  
            v1,v2 = map(int,input().split())
            parent = tree.search_node(root, v1)
            child = tree.search_node(root, v2)
            if not child:
                child = Node(v1)
            if parent:
                tree.insert(parent, child)
            else:
                parent=Node(v1)
                renegades.append(parent)
                renegades.append(child)

        while i<len(renegades):
            parent = renegades[i]
            child = renegades[i+1]
            tree.insert(parent,child)
            i+=2

        print("Root data -> " , root.data)
        for i in root.children:
            print("Child " + str(i) +" -> ", i.data)

"""        
2
4 2
1 2
1 3
1
3 1
2 3
2

                
        s = int(input())

        snode = tree.search_node(root,s)
          
   
        distances = [-1 for _ in range(n)]
        for i in range(n): 
            if snode.data != i+1 : 
                print("Finding distance from " + str(i+1))
                queue = []
                queue.append(snode)
                steps = 0
                found = -1
                while(queue):
                    print("Steps so far: " + str(steps))
                    node = queue.pop(0)
                    if node.data == i+1 : 
                        found=node.data
                        break
                    steps+=1
                    if node.left != None :
                        queue.append(node.left)    
                    if node.right != None :
                        queue.append(node.right)
                if found !=-1 :
                    distances[found-1] = steps*6
        
    
        temp = [distances[d] for d in range(n)]# if d!=s-1)]

        out[_] = str(temp)
    print(out)
"""


if __name__=="__main__":
    Main()
